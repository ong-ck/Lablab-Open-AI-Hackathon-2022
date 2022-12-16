import replicate
import streamlit as st
from PIL import Image
from audiorecorder import audiorecorder
import string
import updateScore as uS
import updatePointer as uP

print("")
print("Start of code")

st.title("Logo Guessing Game")

# Logo list
logos = [
  'assets/Adidas.jpg',
  'assets/Amazon.jpg',
  'assets/Apple.jpg',
  'assets/Chanel.jpg',
  'assets/Facebook.jpg',
  'assets/Google.jpg',
  'assets/Pepsi.jpg',
  'assets/Starbucks.jpg',
  'assets/Tommy.jpg'
]

x = uP.getPointer()
uP.updatePointer()
logo = logos[x]
logoAns = logos[x - 1]
start = logoAns.index('/')
end = logoAns.index('.', start + 1)
answer = logoAns[start + 1:end]  # Correct answer to compare with useranswer

image = Image.open(logo)
st.image(image, caption='guess the logo', width=100)

st.text("Score: " + uS.printScore()) # Display score

# Audio Record Button
audio = audiorecorder("Click to record", "Recording...")
print("Record")

# Check if audio has been recorded and save as file locally
if len(audio) > 0:
  print("Recording")
  # To save audio to a file:
  wav_file = open("audio.mp3", "wb")
  wav_file.write(audio.tobytes())
  
  # Uses replicate API to run whisper (cause Replit RAM too little to be able to run whisper locally, keeps crashing)
  # Passes locally saved audio into API and retrieves transcription to be printed/used
  # Comment out to prevent wasting free API uses
  model = replicate.models.get("openai/whisper")
  version =       model.versions.get("30414ee7c4fffc37e260fcab7842b5be470b9b840f2b608f5baa9bbef9a259ed")
  output = version.predict(audio=open("audio.mp3", "rb"))
  reply = output["transcription"]
  # Removes additional space at the front of the word whisper records
  reply = reply[1:]
  reply = reply.translate(str.maketrans('', '', string.punctuation))
  
  st.text(reply)
  st.text(answer)
  print("x: ", x)
  print("Recorded: ", reply)
  print("Answer: ", answer)
  if (reply.lower() == answer.lower()):
    image = Image.open(logos[x])
    uS.updateScore()
    st.success('Correct!')
  else:
    st.error("Please try again!")
  
if st.button("Reset Score"):
  uS.resetScore()
  st.experimental_rerun()