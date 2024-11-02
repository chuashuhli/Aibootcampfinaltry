import streamlit as st
from logics.customer_query_handler import process_user_message
from utility import check_password

#check if password is correct
if not check_password():
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="The Social Assistance Care App",
    page_icon="🐻"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Social Assistance Com Care Bear🐻")
st.write("You can use our Com Care Bear to find out more about the available social assistance available in Singapore:")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = process_user_message(user_prompt) #<--- This calls the `process_user_message` function that we have created 🆕
    st.write(response)
    print(f"User Input is {user_prompt}")

st.markdown("""
**Disclaimer**

IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

Always consult with qualified professionals for accurate and personalized advice.
""")