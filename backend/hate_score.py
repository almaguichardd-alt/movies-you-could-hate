def compute_hate_score(movie_a, movie_b, genres_a, genres_b, people_a, people_b):

    # 1 base score: violence, pacing, tone
    diff_violence = abs(movie_a["violence_level"] - movie_b["violence_level"])
    diff_pacing = abs(movie_a["pacing"] - movie_b["pacing"])
    diff_tone = abs(movie_a["tone"] - movie_b["tone"])

    score = diff_violence + diff_pacing + diff_tone

    # 2 genre penalty: +1 if no genre in commun
    if not (set(genres_a) & set(genres_b)):
        score += 1

    # 3. extract actors and directors
    actors_a = {p["name"] for p in people_a if p["role"] == "actor"}
    actors_b = {p["name"] for p in people_b if p["role"] == "actor"}

    directors_a = {p["name"] for p in people_a if p["role"] == "director"}
    directors_b = {p["name"] for p in people_b if p["role"] == "director"}

    # 4. Bonus / malus humains
    # same director = too close = penalty
    if directors_a & directors_b:
        score -= 2

    # actors in common = films more similar = penalty
    if actors_a & actors_b:
        score -= 1
        
    # no human overlap = very different films = bonus
    if not (actors_a & actors_b) and not (directors_a & directors_b):
        score += 1

    return score
