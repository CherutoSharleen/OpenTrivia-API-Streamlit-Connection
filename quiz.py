import streamlit as st
import requests
import random
import time

def get_questions(amount, category, difficulty):
    parameters = {
        "amount": amount,
        "type": "multiple",
        "category": category,
        "difficulty": difficulty
    }
    response = requests.get(url='https://opentdb.com/api.php', params=parameters)
    question_data = response.json()["results"]
    return question_data

def main():
    st.set_page_config(initial_sidebar_state="auto")
    st.title("Quiz App")
    category_dict = {
        "General Knowledge": 9,
        "Computers": 18,
        "Science": 17,
        # Add more categories and their corresponding numbers here
    }

    # Sidebar for category and difficulty selection
    selected_category = st.sidebar.selectbox("Select Category:", list(category_dict.keys()))
    selected_difficulty = st.sidebar.selectbox("Select Difficulty:", ["easy", "medium", "hard"])

    category = category_dict[selected_category]
    difficulty = selected_difficulty

    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0

    question_data = get_questions(10, category, difficulty)

    if st.session_state.question_index < len(question_data):
        question = question_data[st.session_state.question_index]
        st.subheader(f"Question {st.session_state.question_index + 1}: {question['question']}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)
        selected_option = st.radio('Select the correct option:', options)

        submit_button = st.button("Submit")
        if submit_button:
            if selected_option == question['correct_answer']:
                st.success('CORRECT!!')
                st.session_state.score += 1
            else:
                st.error('Wrong Answer')

            st.write("---")
            st.session_state.question_index += 1

    else:
        st.subheader("Quiz Completed!")
        st.balloons()
        st.header(f"Your final score is: {st.session_state.score}/{len(question_data)}")

if __name__ == "__main__":
    main()
