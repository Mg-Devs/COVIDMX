# import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
  
# create webdriver object
driver = webdriver.Firefox()
  
# get geeksforgeeks.org
driver.get("https://covid19.sinave.gob.mx/graficasestimados.aspx")

# get element 
element = "/html/body/table/tbody/tr/td/table/tbody/tr/td/div/div/ul/li/ul/li[2]/ul/li[3]/a"
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element))).click()