from typing import FrozenSet
import requests
import random

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)

if font == "random":
  data = requests.get('http://artii.herokuapp.com/fonts_list')
  fontsArray = data.text.split('\n')

  # for i in range(3):
  #   font = random.choice(fontsArray)
  #   r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  #   print("Font:", font)
  #   print(r.text)
  
  for i in range(3):
      font = random.choice(fontsArray)
      getAsciiArt(text, font)


elif font == "":
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}')
  print("Font:", font)
  print(r.text)

elif font:
  font = font
  r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
  print("Font:", font)
  print(r.text)

      
