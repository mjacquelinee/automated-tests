"""
# Por ID
driver.find_element(By.ID, "elemento")

# Por NAME
driver.find_element(By.NAME, "elemento")

# Por XPATH
driver.find_element(By.XPATH, "//input[@name='username']")

# Por CSS Selector
driver.find_element(By.CSS_SELECTOR, "input[name='username']")

# Por Clase
driver.find_element(By.CLASS_NAME, "clase-del-elemento")

"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

try:
    # Configurar el driver con ruta directa
    service = Service(r"C:\chromedriver\chromedriver.exe")
    
    # Opciones adicionales para Chrome
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")  # Maximizar ventana
    # chrome_options.add_argument("--disable-extensions")  # Deshabilitar extensiones
    
    # Crear driver con opciones
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Navegar a la página de inicio de sesión
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Aumentar tiempo de espera
    driver.implicitly_wait(10)
    
    # Métodos múltiples para encontrar el campo de usuario
    metodos_usuario = [
        #(By.ID, "identifierId"),
        #(By.NAME, "username"),
        (By.XPATH, "//input[@placeholder='Username']"),
        #(By.CSS_SELECTOR, "input[type='email']")
    ]
    
    usuario_encontrado = False
    for metodo in metodos_usuario:
        try:
            # Buscar elemento con diferentes estrategias
            usuario = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(metodo)
            )
            
            # Verificar si el elemento está visible y habilitado
            if usuario.is_displayed() and usuario.is_enabled():
                # Ingresar usuario
                usuario.clear()
                usuario.send_keys("Admin")
                
                # Buscar botón siguiente
                boton_siguiente = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
                )
                boton_siguiente.click()
                
                usuario_encontrado = True
                break
        
        except (TimeoutException, NoSuchElementException):
            continue
    
    # Si no se encuentra el campo de usuario
    if not usuario_encontrado:
        print("No se pudo encontrar el campo de usuario")
        raise Exception("Campo de usuario no encontrado")
    
    # Esperar y manejar campo de contraseña
    metodos_contrasena = [
        #(By.NAME, "password"),
        (By.XPATH, "//input[@name='password']"),
        #(By.CSS_SELECTOR, "input[type='password']")
    ]
    
    contrasena_encontrada = False
    for metodo in metodos_contrasena:
        try:
            # Esperar a que aparezca el campo de contraseña
            contrasena = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(metodo)
            )
            
            # Verificar si el elemento está visible y habilitado
            if contrasena.is_displayed() and contrasena.is_enabled():
                # Ingresar contraseña
                contrasena.clear()
                contrasena.send_keys("admin123")
                
                # Buscar botón de inicio de sesión
                boton_login = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Login')]"))
                )
                boton_login.click()
                
                contrasena_encontrada = True
                break
        
        except (TimeoutException, NoSuchElementException):
            continue
    
    # Si no se encuentra el campo de contraseña
    if not contrasena_encontrada:
        print("No se pudo encontrar el campo de contraseña")
        raise Exception("Campo de contraseña no encontrado")
    
    # Tiempo para verificar el inicio de sesión
    time.sleep(5)

except Exception as e:
    print(f"Ocurrió un error: {e}")
    
    # Capturar screenshot en caso de error
    driver.save_screenshot("error_screenshot.png")

finally:
    # Cerrar el navegador
    driver.quit()