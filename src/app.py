import streamlit as st
from question_bank import get_question
from evaluator import evaluate

st.title("AI Mock Interview Bot")

if "question" not in st.session_state:
    st.session_state.question = get_question()

st.subheader("Interview Question")
st.write(st.session_state.question)

answer = st.text_area("Your Answer")

if st.button("Submit"):
    feedback = evaluate(st.session_state.question, answer)

    st.subheader("Evaluation")
    st.write(feedback)

if st.button("Next Question"):
    st.session_state.question = get_question()