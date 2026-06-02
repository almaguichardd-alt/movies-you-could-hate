from flask import Flask, jsonify
from db import get_connection
from hate_score import compute_hate_score

app = Flask(__name__)


# helper to find a film
def get_movie(movie_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT movie_id, title, violence_level, pacing, tone
        FROM Movie
        WHERE movie_id = %s
    """, (movie_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "movie_id": row[0],
        "title": row[1],
        "violence_level": row[2],
        "pacing": row[3],
        "tone": row[4]
    }


# helper to find the genres of a film
def get_genres(movie_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT g.name
        FROM Genre g
        JOIN MovieGenre mg ON g.genre_id = mg.genre_id
        WHERE mg.movie_id = %s
    """, (movie_id,))
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

# helper to find the people in a film
def get_people(movie_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.name, p.role
        FROM Person p
        JOIN MoviePerson mp ON p.person_id = mp.person_id
        WHERE mp.movie_id = %s
    """, (movie_id,))
    rows = cur.fetchall()
    conn.close()
    return [{"name": r[0], "role": r[1]} for r in rows]


# endpoint: return the 3 most different movies
@app.get("/movies/<int:movie_id>/hated")
def hated_movies(movie_id):
    movie_a = get_movie(movie_id)
    if not movie_a:
        return jsonify({"error": "Movie not found"}), 404

    genres_a = get_genres(movie_id)
    people_a = get_people(movie_id)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT movie_id FROM Movie WHERE movie_id != %s", (movie_id,))
    all_ids = [row[0] for row in cur.fetchall()]
    conn.close()

    scores = []
    for mid in all_ids:
        movie_b = get_movie(mid)
        genres_b = get_genres(mid)
        people_b = get_people(mid)
        score = compute_hate_score(movie_a, movie_b, genres_a, genres_b, people_a, people_b)
        scores.append((score, movie_b))

    # sort by descending score
    scores.sort(reverse=True, key=lambda x: x[0])
    # take the 3 worst
    top3 = [m for _, m in scores[:3]]
    return jsonify(top3)

# launch the server
if __name__ == "__main__":
    app.run(debug=True)
