# Importa el módulo unittest incorporado de Python para definir pruebas unitarias
import unittest
# Importa el módulo selenium webdriver para controlar el navegador web
from selenium import webdriver
# Importa la clase By para buscar elementos utilizando diferentes criterios (ID, XPATH, etc.)
from selenium.webdriver.common.by import By
# Importa Keys para simular la pulsación de teclas (como ENTER)
from selenium.webdriver.common.keys import Keys
# Importa Service para inicializar el servicio del ChromeDriver
from selenium.webdriver.chrome.service import Service
# Importa ChromeDriverManager para gestionar automáticamente la descarga y selección del ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager
# Importa time para pausar la ejecución (utilizado en este ejemplo)
import time

# Define una clase de prueba que hereda de unittest.TestCase
class PaginaSigiente(unittest.TestCase):

    # Método que se ejecuta antes de cada test (preparación)
    def setUp(self):
        # Inicializa el navegador Chrome usando ChromeDriverManager para el driver correcto automáticamente
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def test_pagina_siguiente(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        driver.get("https://gporcm.com.mx/")
        time.sleep(3)
        driver.get("https://www.rcmsegurosyfianzas.com.mx/fianzas.html")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)

if __name__=='__main__':
    unittest.main()

    