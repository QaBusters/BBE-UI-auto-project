from selenium.webdriver.common.by import By
from base_page import BasePage


class ConfirmPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для кнопки "Подтвердить заказ"
    def confirm_button_locator(self):
        return By.XPATH, f'//button[@id="create_order"]'

    # Локатор для поля ввода контактного телефона
    def phone_input_locator(self):
        return By.XPATH, f'//input[@id="client_phone"]'

    # Локатор для ввода населенного пункта
    def locality_input_locator(self):
        return By.XPATH, f'//input[@id="shipping_address_full_locality_name"]'

    # Локатор для водда  Ф.И.О. покупателя (контактного лица)
    def customer_input_locator(self):
        return By.XPATH, f'//input[@id="client_name"]'

    # Локатор для чекбокса доставки курьерером
    def select_selfdelivery_locator(self):
        return By.XPATH, f'//label[@for="order_delivery_variant_id_2922417""]//span[@class="radio co-delivery_method-input co-toggable_field-input co-toggable_field-input--radio"]'

    # Локатор для чекбокса оплаты через Sberpay
    def select_sberpay_locator(self):
        return By.XPATH, f'//label[@for="order_payment_gateway_id_2646307]//span[@class="co-payment_method-input co-toggable_field-input  co-toggable_field-input--radio"]'


    # Локатор для текста "Поле не заполнено"
    def message_error_locator(self):
        return By.XPATH, f'//*[@id="tabs-person"]/div[1]/div'


    # Метод для клика по "Подтвердить заказ"
    def clic_to_button_confirm(self):
        self.find_element(self.confirm_button_locator())
        self.click(self.confirm_button_locator())

    # Метод для получения текста из поля адреса
    def get_address_value(self):
        return self.find_element(self.locality_input_locator()).get_attribute('value')

    #Метод для заполнения всех обяазтельных полей
    def enter_required_data(self):
        self.send_keys(self.phone_input_locator(), "89853676865")
        self.send_keys(self.locality_input_locator(), "Москва")
        self.send_keys(self.customer_input_locator(), "Евгений Селиверстов")

    # Метод для выбора доставки самовывозом
    def clic_to_checkbox_selfdelivery(self):
        self.find_element(self.select_selfdelivery_locator())
        self.click(self.select_selfdelivery_locator())

    #Метод для выбора оплаты через Sberpay
    def clic_to_checkbox_sberpay(self):
        self.find_element(self.select_sberpay_locator())
        self.click(self.select_sberpay_locator())

    # Метод для проверки появления сообщения "Поле не заполнено"
    def is_text_error(self):
        error_message = self.find_element(self.message_error_locator())
        text = error_message.text
        return text
