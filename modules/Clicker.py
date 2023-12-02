# clicker_module.py
import pyautogui as pg
import time
import asyncio

class Clicker:
    def __init__(self, delay=1):
        self.delay = delay
        self.stop_requested = False

    def click(self):
        pg.click()
        time.sleep(self.delay)

    def click_range_clicks(self, num_clicks):
        print(f"Iniciando clicker. Simulando {num_clicks} clics.")
        for i in range(num_clicks):
            pg.click()
            time.sleep(self.delay)
        print("Clicker completado.")

    async def start_clicker(self):
        print("Iniciando clicker. Presiona ['End' - 'Shift' - 'C'] para detener.")
        while not self.stop_requested:
            pg.click()
            await asyncio.sleep(self.delay)

    def stop_clicker(self):
        print("Terminando clicker.")
        self.stop_requested = True

    async def main(self):
        # Iniciar las tareas como objetos asyncio.Task
        task_start_clicker = asyncio.create_task(self.start_clicker())
        task_stop_clicker = asyncio.create_task(self.stop_clicker())
        
        # Esperar que ambas tareas se completen
        await asyncio.gather(task_start_clicker, task_stop_clicker)