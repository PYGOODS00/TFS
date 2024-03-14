import streamlit
import pyttsx3
text = streamlit.text_input("EYT:")
bot = pyttsx3.init()
bot.say(text)
bot.runAndWait()
