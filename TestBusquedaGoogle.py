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
class TestBusquedaGoogle(unittest.TestCase):

    # Método que se ejecuta antes de cada test (preparación)
    def setUp(self):
        # Inicializa el navegador Chrome usando ChromeDriverManager para el driver correcto automáticamente
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Método de prueba que verifica la búsqueda de "sol" en Google
    def test_busqueda_sol(self):
        driver = self.driver  # Obtiene la instancia del navegador

        # Abre la página principal de Google
        driver.get("https://www.google.com")
        time.sleep(2)  # Espera unos segundos para que la página cargue completamente

        # Opcional: trata de hacer clic en el botón "Aceptar todo" de cookies si aparece
        try:
            aceptar_boton = driver.find_element(By.XPATH, "//button/div[normalize-space()='Aceptar todo']")
            aceptar_boton.click()
            time.sleep(1)  # Espera un segundo después de hacer clic
        except:
            pass  # Si no aparece el botón, continúa sin interrumpir el test

        # Busca el campo de texto donde se escribe la búsqueda usando el atributo "name"
        caja_busqueda = driver.find_element(By.NAME, "q")

        # Escribe la palabra 'sol' en el campo de búsqueda
        caja_busqueda.send_keys("sol")

        # Simula pulsar la tecla ENTER para enviar la búsqueda
        caja_busqueda.send_keys(Keys.RETURN)

        time.sleep(2)  # Espera a que se carguen los resultados

        # Verifica que la palabra "sol" aparezca en el título de la página de resultados
        self.assertIn("sol", driver.title.lower())

    # Método que se ejecuta después de cada test (limpieza)
    def tearDown(self):
        # Cierra el navegador
        self.driver.quit()

# Ejecuta el test si el archivo es ejecutado directamente
if __name__ == "__main__":
    unittest.main()


        