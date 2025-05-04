import unittest  # Framework de pruebas integrado en Python
from selenium import webdriver  # Controlar navegador web con Selenium
from selenium.webdriver.common.keys import Keys  # Simular pulsación de teclas
from selenium.webdriver.chrome.service import Service  # Dar ruta a ChromeDriver
import time  # Manejar pausas

class UsandoUnittest(unittest.TestCase):  # Clase de pruebas que hereda de unittest

    def setUp(self):
        # Se ejecuta antes de cada test: prepara el entorno
        service = Service(executable_path=r"C:\chromedriver\chromedriver.exe")  # Ruta a ChromeDriver
        self.driver = webdriver.Chrome(service=service)  # Abre Chrome controlado por Selenium
        
    def test_buscar(self):
        # Prueba a buscar una palabra en Google
        driver = self.driver  # Referencia corta
        driver.get("http://www.google.com")  # Abre Google
        self.assertIn("Google", driver.title)  # Verifica que el título contiene "Google"
        elemento = driver.find_element("name", "q")  # Busca la barra de búsqueda (name="q")
        elemento.send_keys("Selenium")  # Escribe "Selenium"
        elemento.send_keys(Keys.RETURN)  # Simula pulsar Enter
        time.sleep(5)  # Espera 5 segundos para el resultado
        self.assertNotIn("No se encontro el elemento", driver.page_source)  # Verifica que salió algún resultado
        
    def tearDown(self):
        # Limpia después de cada test
        self.driver.quit()  # Cierra el navegador

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas si el script es principal