import random
from src.data_fetch import load_cache, save_cache, fetch_movie
# generate_question now returns 4 values: question, options, answer, score_weight
from src.question_generator import generate_question 
from src.visualization import plot_movie_years
import pandas as pd

# --- Initial Configuration ---
movie_ids = pd.read_csv("data/sample_movie_ids.csv")["tconst"].tolist()
cache = load_cache()
movies = [fetch_movie(mid, cache) for mid in movie_ids[:10]]  # First 10 movies

# --- Game Settings ---
total_score = 0
total_questions = len(movies)
difficulty_levels = ["Easy", "Medium", "Hard"]  # Additional difficulty levels

print("--- Welcome to the IMDb Movie Quiz! ---")

# --- Quiz Loop ---
for i, movie in enumerate(movies):
    # For each question, select a random difficulty level (or set a fixed one)
    current_difficulty = random.choice(difficulty_levels) 
    
    # Pass difficulty level to generate_question function
    question, options, correct_answer, score_weight = generate_question(movie, current_difficulty)
    
    # Skip question if it cannot be generated (missing data)
    if question is None:
        continue
        
    print(f"\n## Question {i + 1} ({current_difficulty} level, Weight: {score_weight} points)")
    print(question)
    
    # Map options to letters for display
    option_map = {chr(65 + j): option for j, option in enumerate(options)}  # A, B, C, D
    for key, value in option_map.items():
        print(f" {key}. {value}")
        
    # Get user input
    user_input = input("\nSelect your answer (A, B, C, or D): ").upper()
    
    # Map selected letter to actual answer
    selected_answer = option_map.get(user_input)
    
    # --- Score Calculation ---
    if selected_answer is not None and str(selected_answer) == str(correct_answer):
        total_score += score_weight  # Correct answer gives score based on weight
        print(f"✅ CORRECT! You earned {score_weight} points.")
    else:
        print(f"❌ WRONG. The correct answer was: {correct_answer}.")
    
    print("-------------------------")

# --- Display Results ---
print("\n--- Results ---")
print(f"Total Score (weighted by difficulty): **{total_score}**")
# To calculate the maximum possible score, sum the weights of all questions
# (Here we just display the total points earned)

# --- Visualization and Cache Saving ---
print("\n--- Data Visualization ---")
fig = plot_movie_years(movies)
fig.show()

# Save cache
save_cache(cache)
print("Cache updated.")
