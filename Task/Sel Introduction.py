from selenium import webdriver
#congigure browser
driver=webdriver.Chrome(r'C:\Users\Venkat\PycharmProjects\selenium\Driver\chromedriver.exe')

print(type(driver))

#browser launch
driver.get("https://www.amazon.in/")

#title
p=driver.title
print(p)

#current Url
c=driver.current_url
print(c)

#close browser
driver.quit()


