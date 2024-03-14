import streamlit as st
import pyttsx3

# Set up Streamlit app title and text input
text = st.text_input("Enter your text:")

# Function to convert text to speech
def convert_to_speech(text):
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties before adding text
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)   # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Run and wait for the speech to finish
    engine.runAndWait()

# Check if the "Submit" button is clicked
if st.button("Submit"):
    if text:  # Check if text input is not empty
        convert_to_speech(text)
    else:
        st.warning("Please enter some text.")
else:
    st.write("Type something and press 'Submit' to hear it.")
