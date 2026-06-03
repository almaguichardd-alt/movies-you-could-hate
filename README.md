# movies-you-could-hate
#
# How to Compile the Web-App from Source:
# (1) Clone the repository by running the following command in Terminal: git clone https://github.com/almaguichardd-alt/movies-you-could-hate.git
# Then, move to the backend folder: cd movies-you-could-hate\backend
#
# (2) Install Python Dependencies by running: pip install -r requirements.txt
#
# (3) Create the database with the name project_bd by running: CREATE DATABASE project_db; 
# Note: This can be done using pgAdmin, Psql terminal, or any PostgreSQL client
#
# (4) Initialize the database schema, creating the tables, by running: psql -d project_db -f schema.sql
#
# (5) Populate the database with the seed_data data by running: psql -d project_db -f seed_data.sql
#
# (6) Open the file database.py (located in movies-you-could-hate\backend\database.py) and change the password by replacing ‘CHANGEME!’ with your local PostgreSQL password 
#
# (7) Run the Flask app by running: python app.py
#
#
#
#
# How to Run and Interact with the Web-App:
# (1) Start the Flask server by running in Terminal: python app.py (it should run at http://127.0.0.1:5000)
#
# (2) Test the Homepage by visiting on a browser: http://127.0.0.1:5000/ 
# This should give a message that Movies You Could Hate API is running!
#
# (3) Test Endpoints
# Endpoint 1: /movies/’MOVIE_ID’/hated 
# Replace ‘MOVIE_ID’ with the movie_id of a movie you like from the database.This returns 3 movies that you might hate from the database based on the hate score calculated. These 3 movies have the highest hate score when compared to the inputted movie, based on the difference in violence-level, pace, and tone. 
# eg. http://127.0.0.1:5000/movies/1/hated will return the 3 movies with the highest hate score compared to the movie "The Notebook", which has movie_id=1
# 
# Endpoint 2: /search?title=‘REGEX’
# Replace ‘REGEX’ with a regular expression to get all movies whose titles match the regular expression.
# Examples of Usage:
# --- Titles starting with “The”: http://127.0.0.1:5000/search?title=^The
# --- Titles containing a number: http://127.0.0.1:5000/search?title=[0-9]
# --- Titles ending with “land”: http://127.0.0.1:5000/search?title=land$
# --- Titles containing the word “dark” or “black”: http://127.0.0.1:5000/search?title=dark|black



