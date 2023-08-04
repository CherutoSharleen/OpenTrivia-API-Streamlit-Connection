import time
import streamlit as st

#Page set Up
st.set_page_config(
    page_title='BigBrainTime',
    page_icon=':brain:'
)


st.header(":brain: Big Brain Time ")
answer = st.radio("Who is the most famous Actor?", ['Joy', 'Jewel', 'Apartment'])
submit_btn = st.button('Submit')

#If a person finishes the quiz and wins
st.balloons()

#If a person gets a question wrong
def questionResult(answer):
    if(answer == Answer):
        right_msg =st.success('CORRECT!!')
        time.sleep(2) 
        right_msg.empty()
    else:
        wrong_msg =st.error('Wrong Answer')
        time.sleep(3) 
        wrong_msg.empty()



