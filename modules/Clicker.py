import pyautogui as pg
import time
import asyncio

class Clicker:
    def __init__(self, delay=0.1):
        self.delay = delay
        self.stop_requested = False

    def click(self):
        pg.click()
        time.sleep(self.delay)

    def click_range_clicks(self, num_clicks):
        print(f"Iniciando clicker. Simulando {num_clicks} clics.")

        for i in range(num_clicks):
            self.click()

        print("Clicker completado.")

    async def start_click(self):
        print("Iniciando clicker. Presiona ['End' - 'Shift' - 'C'] para detener.")
        while not self.stop_requested:
            self.click()

    def stop_click(self):
        print("Terminando clicker.")
        self.stop_requested = True
        

