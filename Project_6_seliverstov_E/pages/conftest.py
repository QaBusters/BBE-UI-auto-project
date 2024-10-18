import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    # Инициализация драйвера
    chrome_options = Options() 
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def base_url():
    return 'https://demo.yookassa.ru/'
