Who Wants to Be a Millionaire – Quiz Generator (Streamlit Web App)

This project automatically generates multiple-choice quiz questions for a “Who Wants to Be a Millionaire”-style game using movie data from IMDb. It is implemented as an interactive Streamlit web application and demonstrates key skills from the course, including a clean project structure, modular code, data loading from APIs or local files, and a difficulty-weighted scoring system.

The project loads IMDb movie data, generates a quiz question with four possible answers, selects distractors based on the chosen difficulty level, and calculates a performance score for the player based on the difficulty of each question.

Repository: https://github.com/Jafarova1/python-project

Project Structure

project_root/
├── data/
│   ├── cached_movies.json       # Local cache of fetched movie data (ignored by Git)
│   └── sample_movie_ids.csv     # List of movie IDs used for the quiz
├── src/
│   ├── data_fetch.py            # API access, data caching, and cache clearing logic
│   ├── question_generator.py    # Logic for assembling questions and options
│   ├── difficulty.py            # Logic for selecting difficulty-based distractors
│   └── visualization.py         # Matplotlib logic for the histogram
├── app.py                       # Main Streamlit application file
├── venv/
├── .gitignore
├── requirements.txt
└── README.md

Data Sources

IMDb — Movies and metadata: Data is obtained through the Cinemagoer API, which provides movie titles, release years, genres, and other metadata used to create quiz questions. Data is saved locally in data/cached_movies.json to speed up loading.
Sample movie IDs: Local file data/sample_movie_ids.csv contains IMDb title IDs.

Installation

Clone the repository:

git clone [https://github.com/Jafarova1/python-project.git](https://github.com/Jafarova1/python-project.git)
cd python-project


Create and activate the virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Running the Project

To run the Streamlit web application:

streamlit run app.py


This will load movie data, generate the quiz interface in your browser, allow the player to answer, and compute a difficulty-weighted score.

Dependencies

The following key dependencies are required (listed in requirements.txt):

streamlit

cinemagoer

pandas

matplotlib

Git Usage

This project follows recommended Git practices: .gitignore excludes unnecessary files such as venv/, __pycache__/, and cached JSON files; commits are frequent, small, and have clear messages; and the README documents project purpose, installation, and usage.

Example commit messages:

feat: add IMDb data loader
feat: implement quiz question generator
fix: handle missing movie metadata
docs: update README with run instructions
