from selenium.webdriver.common.by import By

from helpers.helpers import find_region_by_name
from pages.base_page import BasePage
from pages.regions.base_region import BaseRegion


class CartPage(BasePage):
    _cart_title = (By.XPATH, "//h1[text()='Koszyk']")
    _cart_item = (By.CSS_SELECTOR, "tr[class*='cart_item']")
    _sub_total = (By.CSS_SELECTOR, "tr[class='cart-subtotal']")
    _shipping_fee = (By.XPATH, ".//label[text()='Płaska Stawka: ']//span")
    _tax = (By.CSS_SELECTOR, "td[data-title='VAT'] span")
    _order_total = (By.CSS_SELECTOR, "td[data-title='Łącznie'] span")
    _checkout_button = (By.CSS_SELECTOR, "a[class*='checkout-button']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._cart_title)

    @property
    def products(self):
        return [ProductRegion(self, product) for product in self.find_elements(*self._cart_item)]

    @property
    def shipping_fee(self):
        return self.find_element(*self._shipping_fee).text[1:]

    @property
    def tax(self):
        return self.find_element(*self._tax).text[1:]

    @property
    def order_total(self):
        return self.find_element(*self._order_total).text[1:]

    def assert_item_data(self, name, price, quantity, total):
        product = find_region_by_name(self.products, name)
        assert product.price == price
        assert product.quantity == quantity
        assert product.total == total

    def assert_data_are_correct(self, expected_shipping_fee, expected_tax, expected_order_total):
        assert self.shipping_fee == expected_shipping_fee, f"Expected shipping fee should be:{expected_shipping_fee}, but is {self.tax}!"
        assert self.tax == expected_tax, f"Expected tax should be:{expected_tax}, but is {self.tax}!"
        assert self.order_total == expected_order_total, f"Expected order total should be:{expected_order_total}, but is {self.order_total}!"

    def go_to_checkout(self):
        self.find_element(*self._checkout_button).click()


class ProductRegion(BaseRegion):
    _name = (By.CSS_SELECTOR, "td[class='product-name']")
    _price = (By.CSS_SELECTOR, "td[class='product-price']")
    _quantity = (By.CSS_SELECTOR, "td[class*='product-quantity'] input[aria-label='Ilość produktu']")
    _total = (By.CSS_SELECTOR, "td[class='product-subtotal']")

    @property
    def name(self):
        return self.find_element(*self._name).text

    @property
    def price(self):
        return self.find_element(*self._price).text[1:]

    @property
    def quantity(self):
        item_quantity = self.find_element(*self._quantity)
        return item_quantity.get_attribute("value")

    @property
    def total(self):
        return self.find_element(*self._total).text[1:]
