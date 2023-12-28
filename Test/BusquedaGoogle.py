import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait





textos = []


@pytest.fixture
def driver():
    service_obj = Service()
    driver = webdriver.Firefox(service=service_obj)
    driver.implicitly_wait(10)  # Reducido el tiempo de espera implícita
    driver.maximize_window()
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()  # Cierra el navegador al finalizar la prueba

def test_buquedaGoogle(driver):
    # Mejora la selección del elemento de búsqueda de Google
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("panda")
    search_box.send_keys(Keys.ENTER)

    # Espera explícita para asegurar que la página de resultados se haya cargado
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='srKDX cvP2Ce']")))

    textoPagina = driver.find_elements(By.XPATH, "//div[@class='srKDX cvP2Ce']")

    for indice, valor in enumerate(textoPagina):
        if indice == 6:
            try:
                # Espera explícita para asegurar que el enlace esté presente y sea clickeable
                #wait.until(EC.element_to_be_clickable((By.XPATH, "div[1]/div/div/span/a/h3")))
                valor.find_element(By.XPATH, "div[1]/div/div/span/a/h3").click()
                break
            except Exception as e:
                print("No se encuentra:", e)

    # Espera explícita para asegurar que la nueva página se haya cargado completamente
    #wait.until(EC.title_contains("panda"))

    titulo = driver.title
    print("Titulo de la página después de la búsqueda:", titulo)

