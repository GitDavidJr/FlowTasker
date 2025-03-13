import pyautogui as pa
import time

# Obtém a posição atual do mouse
x, y = pa.position()

time.sleep(2)
print(f'Posição do mouse: X = {x}, Y = {y}')
