from time import sleep

import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.store_page import StorePage


@pytest.mark.usefixtures("driver")
class TestOrderProcessing:

    def test_order_product(self):
        home_page = HomePage(self.driver).open()
        home_page.footer.click_on_reject_button()
        home_page.menu.click_store_button()
        # store_page = StorePage(self.driver).open()
        store_page = StorePage(self.driver).wait_for_page_to_load()
        store_page.add_item("Belt", "65,00")
        store_page.menu.menu_popup().go_to_the_cart()
        cart_page = CartPage(self.driver).wait_for_page_to_load()
        cart_page.assert_item_data("Belt", "65,00", "1", "65,00")
        cart_page.assert_data_are_correct("5,00", "16,10", "86,10")
        cart_page.go_to_checkout()
        checkout_page = CheckoutPage(self.driver).wait_for_page_to_load()
        checkout_page.fill_the_form("Ewelina", "wojtycza", "Polska", "ul. Dobra 12", "32-447", "Krakow", "512123345", "pl@interia.pl")
        checkout_page.buy_and_pay()
        checkout_page.verify_success_message("Dziękujemy. Otrzymaliśmy Twoje zamówienie.")




