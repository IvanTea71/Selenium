# Импортируем Selenium WebDriver — он позволяет управлять браузером
from selenium import webdriver
# Импортируем Service для запуска ChromeDriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
