import random

# Main function for generating multiple-choice options
def determine_options(q_type, correct_answer, difficulty_level, **kwargs):
    """
    Generates the correct answer along with 3 distractors based on question type and difficulty level.

    Args:
        q_type (str): Type of the question ("Year", "Director", "Genre").
        correct_answer: The correct answer to the question.
        difficulty_level (str): "Easy", "Medium", or "Hard".
        kwargs: Optional extra data (e.g., 'all_movie_genres' for genre questions).

    Returns:
        List[str]: Shuffled list of options including the correct answer.
    """
    options = [correct_answer]
    num_distractors = 3

    if q_type == "Year":
        # Set the spread based on difficulty
        if difficulty_level == "Easy":
            spread = 5
        elif difficulty_level == "Medium":
            spread = 2
        else:  # Hard
            spread = 1

        # Generate possible distractor years
        possible_distractors = set()
        for i in range(1, spread + 6):  # slightly increased spread
            possible_distractors.add(correct_answer - i)
            possible_distractors.add(correct_answer + i)

        # Limit years to >= 1800
        possible_distractors = {y for y in possible_distractors if y >= 1800}

        possible_distractors.discard(correct_answer)

        num_to_add = min(num_distractors, len(possible_distractors))
        if num_to_add > 0:
            distractors_to_add = random.sample(list(possible_distractors), num_to_add)
            options.extend(distractors_to_add)

    elif q_type == "Director":
        # Simulate distractors for director names
        all_directors = [
            "Steven Spielberg", "Quentin Tarantino", "Greta Gerwig",
            "Denis Villeneuve", "David Fincher", "Christopher Nolan",
            "Alfred Hitchcock", "James Cameron", "Tim Burton", "George Miller",
            "Martin Scorsese", "Stanley Kubrick", "Hayao Miyazaki", "Sofia Coppola"
        ]

        # Remove correct answer and any "Unknown" entries
        candidates = [d for d in all_directors if d != correct_answer and d != "Unknown"]

        if len(candidates) >= num_distractors:
            distractors = random.sample(candidates, num_distractors)
            options.extend(distractors)
        else:
            options.extend(candidates)

    elif q_type == "Genre":
        # Genre distractor logic
        all_movie_genres = kwargs.get('all_movie_genres', [])
        all_possible_genres = [
            "Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance",
            "Thriller", "Documentary", "Animation", "Family", "Crime", "Mystery",
            "Adventure", "Fantasy", "Biography", "War", "Musical"
        ]

        # Distractor candidates: genres not in the movie's genres
        distractor_candidates = [g for g in all_possible_genres if g not in all_movie_genres]

        if len(distractor_candidates) >= num_distractors:
            distractors = random.sample(distractor_candidates, num_distractors)
            options.extend(distractors)
        else:
            options.extend(distractor_candidates)

    # Convert all options to strings and shuffle
    options = [str(opt) for opt in options]
    random.shuffle(options)

    return options
