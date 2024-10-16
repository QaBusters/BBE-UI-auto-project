from xmlrpc.client import Boolean

from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локатор для поиска товара по data-product-id
    def product_form_cartpage_locator(self, product_id):
        return By.XPATH, f'//form[@data-product-id="{product_id}"]//div[@class="product-preview__content"]'

    # Локатор для кнопки "В корзину" в миниатюре продукта
    def add_to_cart_button_cartpage_locator(self, product_id):
        return (
            By.XPATH,
            f'//form[@data-product-id="{product_id}"]//div[@class="product-preview__content"]//button[@class="button add-cart-counter__btn"]')

    # Локатор для кнопки "Оформить заказ"
    def make_an_order_button_locator(self):
        return By.XPATH, f'//button[@class= "button button_size-l button_wide"]'

    # Локатор для кнопки "удалить"
    def delete_button_locator(self, product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]//button[@class="button js-item-delete icon icon-trash"]'

    # Локатор для формы товара
    def cart_item_locator(self, product_id):
        return By.XPATH, f'//div[@data-product-id="{product_id}"]'

    # Локатор для формы деталей заказа (промокод и пр.)
    def form_order_locator1(self):
        return By.XPATH, f'//div[@class="cart__area-controls-sticky"]'

    # Локатор для поля ввода промокода
    def promocode_input_locator(self):
        return By.XPATH, f'//input[@name="cart[coupon]"]'

    # Локатор для кнопки применения промокода
    def promocode_button_locator(self):
        return By.XPATH, f"//button[@class='coupon-button button button-link_size-m']"

    # Локатор для сообщения "Указан несуществующий купон..."
    def invalid_promocode_locator(self):
        return By.XPATH, "//div[@class='cart__area-coupon']//div[@class='insales-ui-discount-error']"


    # Метод для проверки видимости текста
    def form_order_locator(self):
        return self.find_element(self.form_order_locator1())

    # Метод для проверки видимости сообщения "Указан несуществующий купон..."
    def text_promo(self):
        error_message = self.find_element(self.invalid_promocode_locator())
        text = error_message.text
        return text

    # Метод для клика по кнопке применения  промокода
    def clic_to_button_promo(self):
        self.find_element(self.promocode_button_locator())
        self.click(self.promocode_button_locator())

    # Метод для ввода значения в поле промокода
    def input_promo(self):
        self.send_keys(self.promocode_input_locator(),"Happypromo")

    # Метод для клика по кнопке "Удалить"
    def clic_to_icon_trash(self,product_id):
        # Найти кнопку урны
        self.find_element(self.delete_button_locator(product_id))
        # Кликнуть на кнопку
        self.click(self.delete_button_locator(product_id))

    # Метод для клика по кнопке "Оформить заказ"
    def clic_to_button_confirm(self):
        # Найти кнопку
        self.find_element(self.make_an_order_button_locator())
        # Кликнуть по кнопке
        self.click(self.make_an_order_button_locator())



