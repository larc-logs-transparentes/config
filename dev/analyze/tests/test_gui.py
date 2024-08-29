from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from enum import Enum
import selenium.webdriver.support.ui as ui
import time


driver = None
tempo_usuario:float = 0.2 # Tempo de resposta do usuário
tempo_final:float = 1.0


def test_gui_navigation():
    global driver
    driver = webdriver.Chrome()
    ui.WebDriverWait(driver, 2.0) # Wait 2 secondas for all elements

    driver.get('http://localhost:3000')
    time.sleep(tempo_usuario)
    
    # Click - Election comboBox
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/ul/li[7]").click()
    time.sleep(tempo_usuario)

    # Select specific election (2022 - 1st Federal)
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/ul/li[7]/ul/li[1]").click()
    time.sleep(tempo_usuario)

    navigateToSection(driver, 'RS', 'PORTO ALEGRE', '1', '2')

    # Click - Election comboBox
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/ul/li[7]").click()
    time.sleep(tempo_usuario)

    # Select specific election (2022 - 2nd Federal)
    driver.find_element(By.XPATH, "//html/body/div/div/div[1]/div[5]/ul/li[7]/ul/li[2]").click()
    time.sleep(tempo_usuario)

    navigateToSection(driver, 'AM', 'MANAUS', '1', '616')
    
    # Click - Election comboBox
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/ul/li[7]").click()
    time.sleep(tempo_usuario)

    # Select specific election - 1° Turno 2022 (Estadual Ordinária)
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="1° Turno 2022 (Estadual Ordinária)"]'))
    bt.click()
    time.sleep(tempo_usuario)

    navigateToSection(driver, 'GO', 'CALDAS NOVAS', '7', '9')

    # Click - Election comboBox
    driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[5]/ul/li[7]").click()
    time.sleep(tempo_usuario)

    # Select specific election - 2° Turno 2022 (Estadual Ordinária)
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="2° Turno 2022 (Estadual Ordinária)"]'))
    bt.click()
    time.sleep(tempo_usuario)

    navigateToSection(driver, 'SC', 'JOINVILLE', '95', '30')

    time.sleep(tempo_final)


def navigateToSection(driver, state, city, zone, section):
    # Select State
    # Click State ComboBox
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/div/ul/div[1]/li").click()
    time.sleep(tempo_usuario)
    # Select: RS
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="{state}"]'))
    bt.click()
    time.sleep(tempo_usuario)
    # Select: Porto Alegre
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="{city}"]'))
    bt.click()
    time.sleep(tempo_usuario)
    # Select: Zona 1
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="{zone}"]'))
    bt.click()
    time.sleep(tempo_usuario)
    # Select: Seção 2
    quick_wait = ui.WebDriverWait(driver, 5.0)
    bt:WebElement = quick_wait.until(lambda driver: driver.find_element(By.XPATH, f'//li[text()="{section}"]'))
    bt.click()
    time.sleep(tempo_usuario)
    
    # Click Pesquisar
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/div/ul/button").click()
    time.sleep(tempo_usuario)
    
    # Wait for Img "Verificação correta" to show
    try:
        bu_img=driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/p/img")
        long_wait = ui.WebDriverWait(driver, 15.0)
        long_wait.until(EC.text_to_be_present_in_element_attribute(locator = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/p/img'), attribute_ = 'alt', text_ = 'Verificação Correta'))
        bu_img.click()
        time.sleep(tempo_usuario)
        
        # Close detail window
        bt_close:WebElement = long_wait.until(lambda driver: driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[1]"))
        bt_close.click()
    except TimeoutException as ex:
        print(f'Exception: {ex}')


    time.sleep(tempo_usuario)


if __name__ == '__main__':    
    test_gui_navigation()