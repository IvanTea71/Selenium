# Импортируем Selenium WebDriver — он позволяет управлять браузером
from selenium import webdriver

# Адрес сайта, который будем открывать в браузерах
base_url = "https://www.saucedemo.com/"

# Запускаем браузер Chrome
driver_сhrome = webdriver.Chrome()
# Открываем сайт в Chrome
driver_сhrome.get(base_url)
# Устанавливаем размер окна Chrome(такое разрешение у меня на ноуте):
driver_сhrome.set_window_size(3200, 2000)
# Останавливаем выполнение программы и ждём
input("Нажмите Enter для завершения")
# Закрываем бруезер
driver_сhrome.close()
# Запускаем браузер Firefox
driver_firefox = webdriver.Firefox()
# Открываем сайт в Firefox
driver_firefox.get(base_url)
# Устанавливаем размер окна Firefox
driver_firefox.set_window_size(3220, 2000)
# Останавливаем выполнение программы и ждём
input("Нажмите Enter для завершения")
# Закрываем бруезер
driver_firefox.close()
# Запускаем браузер Edge
driver_edge = webdriver.Edge()
# Открываем сайт в Edge
driver_edge.get(base_url)
# Устанавливаем размер окна Edge
driver_edge.set_window_size(3200, 2000)
# Останавливаем выполнение программы и ждём
input("Нажмите Enter для завершения")
# Закрываем бруезер
driver_edge.close()