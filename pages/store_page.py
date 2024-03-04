

from selenium.webdriver.common.by import By

from helpers.helpers import find_region_by_name
from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion


class StorePage(BasePage):
    _page_title = (By.XPATH, "//h1[text()='Sklep']")
    _product = (By.CSS_SELECTOR, "li[class*='product type-product']")
    # URL_TEMPLATE = "/sklep/"

    @property
    def loaded(self):
        return self.is_element_displayed(*self._page_title)

    @property
    def items(self):
        return [Item(self, product) for product in self.find_elements(*self._product)]

    def add_item(self, item_name, price):
        find_region_by_name(self.items, item_name).click_on_add_to_cart_button()
        self.wait.until(lambda page: self.menu.amount == price, f"Expected price should be {price} but it was {self.menu.amount}")   # dodanie lambdy zrobilo mi funkcje bo wait.until przyjmuje funkcje


class Item(BaseRegion):
    _name = (By.CLASS_NAME, "woocommerce-loop-product__title")
    _add_to_cart_button = (By.XPATH, ".//a[text()='Dodaj do koszyka']")

    @property
    def name(self):
        return self.find_element(*self._name).text

    def click_on_add_to_cart_button(self):
        self.find_element(*self._add_to_cart_button).click()
        return self





