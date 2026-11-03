from gtts import gTTS

text = input("Enter the text you want to convert to speech: ")

tts = gTTS(text=text, lang='en')

tts.save("voice-output.mp3")

print("Text-to-speech conversion completed. The audio has been saved as 'voice-output.mp3'.")