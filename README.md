# Who Wants to Be a Millionaire – Quiz Generator (Python Project) This project automatically generates multiple-choice quiz questions for a “Who Wants to Be a Millionaire”-style game using movie data from IMDb. It demonstrates key skills from the course, including a clean project structure, modular code, data loading from APIs or local files, and reproducible environments using virtual environments. The project loads IMDb movie data using the Cinemagoer API (or an optional local cache), generates a quiz question with four possible answers, selects distractors based on the chosen difficulty level, and calculates a performance score for the player based on the difficulty of each question.

**Repository:** [https://github.com/Jafarova1/python-project](https://github.com/Jafarova1/python-project)

## Project Structure project_root/ ├── data/ │ ├── cached_movies.json │ └── sample_movie_ids.csv ├── src/ │ ├── data_fetch.py │ ├── question_generator.py │ ├── difficulty.py │ ├── gameplay.py │ └── main.py ├── venv/ ├── .gitignore ├── requirements.txt └── README.md


## Data Sources
**IMDb — Movies and metadata**: Data is obtained through the Cinemagoer API, which provides movie titles, release years, genres, and other metadata used to create quiz questions. Data can optionally be saved locally in `data/cached_movies.json` to speed up loading.  
**Sample movie IDs**: Local file `data/sample_movie_ids.csv` contains IMDb title IDs used when running the quiz without live API calls.

## Installation
Clone the repository:
```bash
git clone https://github.com/Jafarova1/python-project.git
cd python-project

Create and activate the virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt


Running the Project

Run the quiz game:

python -m src.main


This will load movie data, generate a quiz question with four options, apply difficulty-based distractor selection, allow the player to answer, and compute a difficulty-weighted score.


Dependencies

Listed in requirements.txt:

cinemagoer

pandas

numpy

Git Usage

This project follows recommended Git practices: .gitignore excludes unnecessary files such as venv/, __pycache__/ and cached JSON files, commits are frequent, small, and have clear messages, and the README documents project purpose, installation, and usage.



Example commit messages:

feat: add IMDb data loader
feat: implement quiz question generator
fix: handle missing movie metadata
docs: update README with run instructions
