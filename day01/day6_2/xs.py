from selenium.webdriver.common.by import By
driver = None
sport = By.CSS_SELECTOR, '.telA'
print(type(sport))
print('1:', sport)
print('2:', *sport)