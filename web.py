"""from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import webbrowser,asyncio

def on_press(key):
    print('onepress')

def on_release(key):
    print('onrelaese')

def on_click(x, y, button, pressed):
    # Tu lógica aquí para manejar el evento de clic
    print(f'Click en ({x}, {y}) con el botón {button}, Presionado: {pressed}')


async def listenKeyboard():
	with KeyboardListener(on_press=on_press,on_release=on_release) as keyboard_listener:
	   keyboard_listener.join()
    
async def listenMouse():
    with MouseListener(on_click=on_click) as mouse_listener:
        mouse_listener.join()


async def main():
    # Schedule two calls *concurrently*:
    await asyncio.gather(listenMouse(),listenKeyboard())

asyncio.run(main())



"""


from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import webbrowser
import asyncio

def on_press(key):
    print(f'on_press {key}')

def on_release(key):
    print('on_release')

def on_click(x, y, button, pressed):
    # Tu lógica aquí para manejar el evento de clic
    print(f'Click en ({x}, {y}) con el botón {button}, Presionado: {pressed}')

async def listenKeyboard():
    with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
        await asyncio.Future()  # Espera indefinida para que la tarea no se complete automáticamente

async def listenMouse():
    with MouseListener(on_click=on_click) as mouse_listener:
        await asyncio.Future()  # Espera indefinida para que la tarea no se complete automáticamente

async def main():
    # Iniciar las tareas como objetos asyncio.Task
    task_keyboard = asyncio.create_task(listenKeyboard())
    task_mouse = asyncio.create_task(listenMouse())

    # Esperar que ambas tareas se completen
    await asyncio.gather(task_keyboard, task_mouse)

# Ejecutar el bucle de eventos de asyncio
asyncio.run(main())
