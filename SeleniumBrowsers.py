# Импортируем Selenium WebDriver — он позволяет управлять браузером
from selenium import webdriver

# Адрес сайта, который будем открывать в браузерах
base_url = "https://www.saucedemo.com/"

# Запускаем браузер Chrome
driverChrome = webdriver.Chrome()

# Открываем сайт в Chrome
driverChrome.get(base_url)
# Устанавливаем размер окна Chrome(такое разрешение у меня на ноуте):
driverChrome.set_window_size(3200, 2000)

# Запускаем браузер Firefox
driverFirefox = webdriver.Firefox()
# Открываем сайт в Firefox
driverFirefox.get(base_url)
# Устанавливаем размер окна Firefox
driverFirefox.set_window_size(3220, 2000)

# Запускаем браузер Edge
driverEdge = webdriver.Edge()
# Открываем сайт в Edge
driverEdge.get(base_url)
# Устанавливаем размер окна Edge
driverEdge.set_window_size(3200, 2000)

# Останавливаем выполнение программы и ждём
input("Нажмите Enter для завершения")