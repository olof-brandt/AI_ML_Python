
#20250116_colabPrompt_speechGenerator01

# prompt: set up a text to audio generator please!

#!pip install gTTS


from gtts import gTTS
from IPython.display import Audio

def text_to_speech(text, language='en', slow=False):
  """
  Generates an audio file from the given text using gTTS.

  Args:
    text: The text to convert to speech.
    language: The language of the text (default: 'en').
    slow: Whether to speak slowly (default: False).

  Returns:
    An IPython.display.Audio object representing the generated audio.
  """
  tts = gTTS(text=text, lang=language, slow=slow)
  tts.save("output.mp3")
  return Audio("output.mp3", autoplay=True)



import pygame
import time
import threading
def play_music(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

"""
# Engelska
my_text = "Hello, this is a text-to-speech demo."
audio = text_to_speech(my_text)
#display(audio)
"""


# Example usage with different language and speed
my_text = "♪Storstadens puls! Jag ser piketbussen den stannar står rakt framför mig. Storstadens puls! Åtta snutar i en ring säger vad har du för dig?♪"
audio = text_to_speech(my_text, language='sv')
#display(audio)



"""
# Spanska
my_text = "Hola, esta es una demostración de texto a voz."
audio = text_to_speech(my_text, language='es', slow=True)
#display(audio)
"""

play_music("../output.mp3")

