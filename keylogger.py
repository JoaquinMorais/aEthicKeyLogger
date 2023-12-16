from pynput.keyboard import Listener as KeyboardListener, Key
from pynput.mouse import Listener as MouseListener
import asyncio
from secuence_keys import secuence_keys
#modules
from modules.Clicker import Clicker


class Keylogger:
    def __init__(self):
        self.clicker = Clicker()

        self.log = ""
        self.exit_event = asyncio.Event()  
        self.lastEventIsClick = False

        self.keys_pressed = []



    def clean_key(self,key):
        special_keys = {
            Key.enter: 'Enter',
            Key.esc: 'Esc',
            Key.space: 'Space',
            Key.tab: 'Tab',
            Key.backspace: 'Backspace',
            Key.shift: 'Shift',
            Key.shift_r: 'Shift',
            Key.ctrl: 'Ctrl',
            Key.ctrl_l: 'Ctrl',
            Key.ctrl_r: 'Ctrl',
            Key.alt: 'Alt',
            Key.alt_l: 'Alt',
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
            Key.print_screen : 'Print Screen',
            Key.scroll_lock : 'Scroll_Lock',
            Key.pause : 'Pause',
            Key.insert : 'Insert',
            Key.home : 'Home',
            Key.page_up : 'Page Up',
            Key.delete : 'Delete',
            Key.end : 'End',
            Key.page_down : 'Page Down',
            Key.menu : 'Menu',
            Key.alt_gr : 'Alt Gr',
            
        }
        if key in special_keys:
            return special_keys[key]
        else:
            char = getattr(key, 'char', None)
            if char is not None:
                return char
            return key

    def special_functions(self):
        if any(all(element in self.keys_pressed for element in combination) for combination in secuence_keys['Start Clicker']):
            #asyncio.run(self.clicker.start_clicker())
            self.clicker.start_clicker()
        elif any(all(element in self.keys_pressed for element in combination) for combination in secuence_keys['Stop Clicker']):
            self.clicker.stop_clicker()
        elif any(all(element in self.keys_pressed for element in combination) for combination in secuence_keys['End Clicker']):
            self.clicker.end_clicker()



    def on_press(self,key):
        key = self.clean_key(key)
        if key not in self.keys_pressed:
            self.keys_pressed.append(key)
        print(self.keys_pressed)

        
        self.special_functions()


        """if key in special_keys:
            if special_keys[key] == 'Space':
                self.log+=' '

            elif special_keys[key] == 'Backspace' and not self.lastEventIsClick:
                self.log = self.log[0:-1]

            elif special_keys[key] == 'Enter':
                self.log += '\n'
            
            elif special_keys[key] == 'F6':
                if self.log == '':
                    self.exit_event.set()
                print(self.log)
                self.log=''
            
            else:
                self.log+= f'\n[{special_keys[key].upper()}] '
            
        else:
            try:
                char = key.char
                if char:
                    self.log+=char
                
            except AttributeError:
                print(f'on_press {key} type: {type(key)}')

        self.lastEventIsClick = False"""


    def on_release(self, key):
        try:
            self.keys_pressed.remove(self.clean_key(key))
        except Exception as e:
            print(f"Error en on_release: {e}")


    def on_click(self,x, y, button, pressed):
        # Tu lógica aquí para manejar el evento de clic
        print(f'Click en ({x}, {y}) con el botón {button}, Presionado: {pressed}')
        self.lastEventIsClick = True

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
        
        # Esperar que todas las tareas se completen
        await asyncio.gather(
            task_keyboard, 
            task_mouse,
            self.clicker.main()
        )

# Ejecutar el bucle de eventos de asyncio
if __name__ == '__main__':
    keylogger = Keylogger()
    asyncio.run(keylogger.main())
