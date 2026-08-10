import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#para docker
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions




def ejecutar_test(browser):


    #driver para chrome y firefox en paralelo con selenium grid 
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()

    driver = webdriver.Remote(
            command_executor="http://localhost:4444",
            options=options
    )

    #driver para edge
    #driver = webdriver.Edge()

    driver.maximize_window()
    wait = WebDriverWait(driver, 10)


    try:

        driver.get("https://www.saucedemo.com/")
        time.sleep(5)

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("usuario_incorrecto")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("clave_incorrecta")

        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)


        error = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "error-message-container")
            )
        )

        assert "Username and password do not match" in error.text

        print("Login incorrecto validado correctamente")


        driver.refresh()
        time.sleep(5)


        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        time.sleep(3)

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        time.sleep(5)


        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        print("Login correcto realizado correctamente")


        driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

        time.sleep(5)


        driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()

        time.sleep(5)

        producto = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert producto.text == "Sauce Labs Backpack"


        print("Test E2E ejecutado correctamente")

        time.sleep(5)

    finally:

        driver.quit() 

#Test en "edge"
#ejecutar_test("edge")

#Test en "chrome" y "firefox" en paralelo con selenium grid

hilo_chrome = threading.Thread(
    target=ejecutar_test,
    args=("chrome",)
)

hilo_firefox = threading.Thread(
    target=ejecutar_test,
    args=("firefox",)
)

hilo_chrome.start()
hilo_firefox.start()

hilo_chrome.join()
hilo_firefox.join()

print("Todos los tests terminaron")