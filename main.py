import streamlit
import pyttsx3
text = streamlit.text_input("EYT:")
if streamlit.button("SUBMIT>"):
  bot = pyttsx3.init()
  bot.say(text)
  bot.runAndWait()
else:
  streamlit.write("HI")
