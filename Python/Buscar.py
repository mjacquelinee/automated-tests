import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestBusquedaGoogle(unittest.TestCase):

    def setUp(self):
        # Puedes especificar el path a tu chromedriver aquí si no lo tienes en PATH
        self.driver = webdriver.Chrome()

    def test_busqueda_sol(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(2)  # Espera a que cargue la página, en un test real usar WebDriverWait

        # Acepta cookies si aparece el popup (opcional, depende de tu región)
        try:
            aceptar_boton = driver.find_element(By.XPATH, "//button/div[text()='Aceptar todo']")
            aceptar_boton.click()
            time.sleep(1)
        except:
            pass  # Si no aparece el boton, sigue adelante

        # Encuentra el campo de búsqueda, escribe "sol" y presiona Enter
        caja_busqueda = driver.find_element(By.NAME, "q")
        caja_busqueda.send_keys("sol")
        caja_busqueda.send_keys(Keys.RETURN)

        time.sleep(2)  # Espera resultados

        # Comprueba que hay resultados relacionados con "sol"
        self.assertIn("sol", driver.title.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


        
