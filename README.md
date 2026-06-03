# movies-you-could-hate

# How to Compile the Web-App from Source
# (1) Clone the repository by running the following command in Terminal:
#           git clone https://github.com/almaguichardd-alt/movies-you-could-hate.git
# Then, move to the backend folder: cd movies-you-could-hate/backend


# (2) Install Python Dependencies by running:
#           pip install -r requirements.txt


# (3) Create the database with the name project_bd by running:
#           CREATE DATABASE project_db; 
# Note: This can be done using pgAdmin, Psql terminal, or any PostgreSQL client


# (4) Initialize the database schema, creating the tables, by running: 
#           psql -d project_db -f schema.sql


# (5) Populate the database with the seed_data data by running: 
#           psql -d project_db -f seed_data.sql


# (6) Open the file database.py (located in movies-you-could-hate\backend\database.py) and change the password by replacing ‘CHANGEME!’ with your local PostgreSQL password 


# (7) Run the Flask app by running:
#           python app.py
