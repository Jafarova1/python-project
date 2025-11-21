import streamlit as st
import pandas as pd
import random
from src.data_fetch import load_cache, save_cache, fetch_movie
from src.question_generator import generate_question
from src.visualization import plot_movie_years

# ----------------------------------------------------
# 1. INITIAL SESSION STATE SETUP
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0
if 'max_possible_score' not in st.session_state:
    st.session_state.max_possible_score = 0
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
# ----------------------------------------------------

# Load movie IDs
try:
    movie_ids = pd.read_csv("data/sample_movie_ids.csv", header=None).iloc[:, 0].tolist()
except Exception:
    st.error("Error: The file 'sample_movie_ids.csv' could not be loaded. Please check its path and format.")
    movie_ids = []

cache = load_cache()

# Sidebar
st.sidebar.header("Quiz Settings")
num_questions = st.sidebar.slider("Number of Questions", 1, 10, 3)
difficulty_level = st.sidebar.selectbox("Quiz Difficulty", ["Easy", "Medium", "Hard"], index=1)

st.title("Who Wants to Be a Millionaire - Movie Quiz")
st.write("---")

# ----------------------------------------------------
# 2. START / RESTART QUIZ
if st.button("Start / Restart Quiz"):
    st.session_state.total_score = 0
    st.session_state.max_possible_score = 0
    st.session_state.answers = {}
    st.session_state.quiz_started = True
    st.session_state.quiz_finished = False
    st.session_state.questions = []

    st.toast("Creating a new quiz...", icon='🎬')
    
    with st.spinner(f"Fetching data for {num_questions} questions..."):
        for i in range(num_questions):
            if movie_ids:
                movie_id = random.choice(movie_ids)
                info = fetch_movie(movie_id, cache)
                
                question, options, answer, score_weight = generate_question(info, difficulty_level)

                if question:
                    st.session_state.questions.append({
                        'question': question,
                        'options': options,
                        'answer': answer,
                        'score_weight': score_weight
                    })
                    st.session_state.max_possible_score += score_weight
            else:
                st.warning("The movie ID list is empty. Please check the 'sample_movie_ids.csv' file.")
                break
    
    st.rerun()
# ----------------------------------------------------


# ----------------------------------------------------
# 3. QUIZ QUESTIONS DISPLAY
if st.session_state.quiz_started and st.session_state.questions and not st.session_state.quiz_finished:
    st.header("Quiz Questions")

    for i, q_data in enumerate(st.session_state.questions):
        st.subheader(f"Question {i + 1} ({q_data['score_weight']} points)")
        st.write(q_data['question'])

        radio_key = f"answer_{i}"

        default_index = None
        if st.session_state.answers.get(i) in q_data['options']:
            default_index = q_data['options'].index(st.session_state.answers.get(i))

        user_answer = st.radio(
            "Choose your answer:",
            q_data['options'],
            key=radio_key,
            index=default_index
        )

        st.session_state.answers[i] = user_answer

    st.write("---")

    # ----------------------------------------------------
    # 4. CALCULATE SCORE
    if st.button("Calculate Score"):
        final_score = 0
        
        for i, q_data in enumerate(st.session_state.questions):
            correct_answer = q_data['answer']
            user_choice = st.session_state.answers.get(i)
            score_weight = q_data['score_weight']

            if str(user_choice) == str(correct_answer):
                final_score += score_weight 

        st.session_state.total_score = final_score
        st.session_state.quiz_finished = True
        st.session_state.quiz_started = False
        st.rerun()
# ----------------------------------------------------


# ----------------------------------------------------
# 5. QUIZ RESULTS
if st.session_state.quiz_finished:
    st.header("Quiz Results 🏆")
    
    max_score = st.session_state.max_possible_score
    current_score = st.session_state.total_score
    
    percentage = (current_score / max_score) * 100 if max_score > 0 else 0
    
    st.success(f"Your Total Score: **{current_score}** / **{max_score}**")
    st.info(f"Percentage: **{percentage:.1f}%**")
    
    # Show answers
    with st.expander("Review Your Answers"):
        for i, q_data in enumerate(st.session_state.questions):
            user_choice = st.session_state.answers.get(i)
            is_correct = str(user_choice) == str(q_data['answer'])
            
            status = "✅ Correct" if is_correct else "❌ Incorrect"
            gained_score = q_data['score_weight'] if is_correct else 0
            
            st.markdown(f"**Question {i+1} ({gained_score}/{q_data['score_weight']} points):** {q_data['question']}")
            st.write(f"Your Answer: **{user_choice}**")
            st.write(f"Correct Answer: **{q_data['answer']}**")
            st.markdown(f"**Result:** {status}")
            st.write("---")

# ----------------------------------------------------


# 6. VISUALIZATION (Histogram)
st.write("---")
st.subheader("Histogram of Movie Release Years")

movies_for_plot = [fetch_movie(mid, cache) for mid in movie_ids[:10] if movie_ids]

if movies_for_plot:
    try:
        fig = plot_movie_years(movies_for_plot)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error displaying histogram: {e}")
else:
    st.info("No movie data available to display the histogram.")

# Save cache
save_cache(cache)
