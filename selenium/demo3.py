from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Edge()
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