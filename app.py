import streamlit as st

from langchain.llms import HuggingFaceHub

# Create function to return response from model
def load_answer(x):
    try:
        llm = HuggingFaceHub(repo_id="google/flan-t5-large")
        return llm(x)
    except ValueError as e:
        error_message = str(e)
        if "args[0]" in error_message and "have the wrong format" in error_message:
            return "Invalid input format. Please provide a valid input."
        else:
            return f"Error occurred: {e}"

# Create app UI using Streamlit
st.set_page_config(page_title="Q&A Bot", page_icon=":robot:")
st.header("Q&A Bot")

# Get user input
def get_text():
    return st.text_input("You: ", key="input")

# Connecting the user's qwuestion as an input to the load_answer function
question = get_text()
response = load_answer(question)

#Creating a Generate button for the user
submit = st.button("Generate")

# When Generate Button is clicked, generate answer
if submit:
    st.subheader("Answer: ")
    st.write(response)
