"""
Homework:    Module 6: WEB UI
Author:      Hayden Hargreaves with some basic help from Gemini
Date:        3/11/2025
Description: This is a game that tests your knowledge of HTTP codes. Using cats!
"""

from typing import Dict, List
import streamlit as st
from codes import random_code, random_choices, get_code_from_msg

# Global value
# * Size of the quiz
quiz_size: int = 5


@st.cache_data
def get_cat(ans: str):
    """Get the image of the cat. It was abstracted to allow for caching."""
    st.image(f"https://http.cat/{get_code_from_msg(ans)}.jpg")


# Initialize session state with the generated data
if "quiz_data" not in st.session_state:
    # Stores a list of the correct answers, so that way we dont
    codes: List[int] = []
    quiz_data: List[Dict[str, any]] = []
    for _ in range(quiz_size):
        code: tuple[int, str] = random_code(codes)
        quiz_data.append(
            {
                "question": f"What is the message for HTTP code: {code[0]}",
                "options": random_choices(code[0], 4),
                "correct_answer": code[1],
            }
        )
        codes.append(code[0])
    st.session_state.quiz_data = quiz_data

# Set a blank state for the users answers
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# Set a blank state for the users score
if "score" not in st.session_state:
    st.session_state.score = 0

# Set a blank state for the submission state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Display the quiz
st.title("How well do you know your HTTP response codes?")
for i, question_data in enumerate(st.session_state.quiz_data):
    question = question_data["question"]
    options = question_data["options"]

    st.session_state.user_answers[i] = st.radio(
        question,
        options,
        key=f"question_{i}",
        # Gemini helped me with this part, the state modal is a bit off
        index=(
            options.index(st.session_state.user_answers.get(i))
            if st.session_state.user_answers.get(i) in options
            else 0 if st.session_state.user_answers.get(i) is not None else None
        ),
    )


# Handle submission
if st.button("Submit Answers"):
    st.session_state.score = 0
    for i, question_data in enumerate(st.session_state.quiz_data):
        correct_answer = question_data["correct_answer"]
        user_answer = st.session_state.user_answers.get(i)

        if user_answer == correct_answer:
            st.session_state.score += 1
            st.success(f"Question {i + 1}: Correct!")
        else:
            st.error(
                f"Question {i + 1}: Incorrect. The correct answer was: {correct_answer}"
            )
        get_cat(correct_answer)
    st.session_state.submitted = True

if st.session_state.submitted:
    st.write(
        f"Your score: {st.session_state.score} / {len(st.session_state.quiz_data)}"
    )
