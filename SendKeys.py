# Импортируем Selenium WebDriver — он позволяет управлять браузером
from selenium import webdriver
# Импортируем Service для запуска ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# Импортируем ChromeDriverManager — он автоматически скачивает и устанавливает подходящую версию ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# Создаём настройки для браузера Chrome
options = webdriver.ChromeOptions()
# Указываем не закрывать браузер после завершения работы скрипта
options.add_experimental_option("detach", True)
# Создаём объект driver — через него Selenium будет управлять браузером
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
# Сохраняем адрес тестируемого сайта в переменную
base_url = "https://www.saucedemo.com/"
# Открываем сайт в браузере
driver.get(base_url)
# Устанавливаем размер окна браузера:
driver.set_window_size(3200, 2000)
user_name = driver.find_element(By.ID,"user-name")
user_name.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
input("Нажмите Enter для завершения...")
