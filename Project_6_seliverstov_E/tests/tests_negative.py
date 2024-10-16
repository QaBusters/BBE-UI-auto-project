import time
import pytest
from cart_page import CartPage
from confirm_page import ConfirmPage
from start_page import StartPage
from order_page import OrderStatusPage

@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidPromo:
    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Id продукта, который хотим добавить в корзину
        product_id = '253354942'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)

        # Проверка, что товар добавлен в корзину
        assert start_page.is_product_added_to_cart(), "Product was not added to cart"
        time.sleep(5)
        # Клик по кнопке "Корзина"
        start_page.clic_to_icon_cart()

        # Введение промокода
        cart_page.input_promo()

        # Клик на "Применить промокод"
        cart_page.clic_to_button_promo()

        # Проверка, что появилось сообщение "Указан несуществующий купон..."
        assert cart_page.text_promo().count('Указан несуществующий купон, убедитесь, что он введен верно') == 1


@pytest.mark.usefixtures("init_driver", "base_url")
class TestInvalidClient:

    def test_add_product_to_cart(self, base_url):
        # Инициализация страницы
        start_page = StartPage(self.driver)
        cart_page = CartPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        # Открытие стартовой страницы
        start_page.open_start_page()

        # Id продукта, который хотим добавить в корзину
        product_id = '253354771'

        # Добавление продукта в корзину
        start_page.add_product_to_cart(product_id)
        time.sleep(10)
        # Клик по кнопке "Корзина"
        start_page.clic_to_icon_cart()

        # Клик по  кнопке "Оформить заказ"
        cart_page.clic_to_button_confirm()
        time.sleep(10)

        # Клик по кнопке "Подтвердить заказ" (все поля для заполнения - пустые)
        confirm_page.clic_to_button_confirm()
        time.sleep(10)

        # Проверка сообщени "Поле не заполнено"
        assert confirm_page.is_text_error().count("Поле не заполнено") == 1
        time.sleep(10)

