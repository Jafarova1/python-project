import random
from src.difficulty import determine_options

def get_score_weight(difficulty_level):
    """Returns the score weight based on difficulty level."""
    if difficulty_level == "Easy":
        return 1
    elif difficulty_level == "Medium":
        return 3
    elif difficulty_level == "Hard":
        return 5
    return 1  # Default weight


def generate_question(movie_info, difficulty_level):
    """
    Generates a question, answer options, correct answer, and score weight
    based on the given movie info.

    Returns: 
        question (str)
        options (list)
        correct_answer (str)
        score_weight (int)
    """

    # 1. Score weight based on difficulty
    score_weight = get_score_weight(difficulty_level)

    # 2. Determine which type of question can be asked
    available_data = []
    if movie_info.get('year'):
        available_data.append("Year")
    if movie_info.get('director'):
        available_data.append("Director")
    
    # If no usable info exists, return empty set
    if not available_data:
        return None, [], None, 0

    q_type = random.choice(available_data)
    
    question = ""
    correct_answer = None
    
    if q_type == "Year":
        correct_answer = movie_info['year']
        question = f"In what year was the movie '{movie_info['title']}' released?"
        
    elif q_type == "Director":
        correct_answer = movie_info['director']
        question = f"Who directed the movie '{movie_info['title']}'?"

    # 3. Generate answer options (using helper from difficulty.py)
    options = determine_options(
        q_type,
        correct_answer,
        difficulty_level,
        movie_info=movie_info
    )

    # Convert to string for consistent comparison
    correct_answer_str = str(correct_answer)

    # Shuffle answer choices
    random.shuffle(options)
    
    return question, options, correct_answer_str, score_weight
