

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r"C:\Users\Venkat\PycharmProjects\pythonseleniumProject\Driver\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("u_0_2").click()
driver.find_element(By.XPATH,"//label[text()='Female']").click()
# d=driver.find_element_by_id("day")
# s=Select(d)
# s.select_by_value('2')
# # s.select_by_index(3)
# s.select_by_visible_text("Rajasthan")

