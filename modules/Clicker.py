# clicker_module.py
import pyautogui as pg
import time
import asyncio

class Clicker:
    def __init__(self, delay=0.01):
        self.delay = delay
        self.request_click = False
        self.turn_on = True

    def click(self):
        pg.click()
        time.sleep(self.delay)

    def click_range_clicks(self, num_clicks):
        print(f"Iniciando clicker. Simulando {num_clicks} clics.")
        for i in range(num_clicks):
            pg.click()
            time.sleep(self.delay)
        print("Clicker completado.")

    def start_clicker(self):
        print("Iniciando clicker. Presiona ['End' - 'Shift' - 'C'] para detener.")
        self.request_click = True

    def stop_clicker(self):
        print("Pausando clicker.")
        self.request_click = False

    def end_clicker(self):
        print("Finalizado clicker.")
        self.turn_on = False

    async def clicker(self):
        while self.turn_on:
            print('intento')
            while self.request_click:
                pg.click()
                pg.click()
                await asyncio.sleep(self.delay)
            await asyncio.sleep(5)


    async def main(self):
        # Iniciar las tareas como objetos asyncio.Task
        _clicker_ = asyncio.create_task(self.clicker())
        
        return _clicker_
        # Esperar que ambas tareas se completen
        #await asyncio.gather(task_start_clicker, task_stop_clicker)