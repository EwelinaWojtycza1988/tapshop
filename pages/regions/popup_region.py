from selenium.webdriver.common.by import By

from pages.regions.base_region import BaseRegion


class PopupRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "div[class='widget woocommerce widget_shopping_cart']")
    _cart_button = (By.XPATH, ".//a[text()='Zobacz koszyk']")

    def go_to_the_cart(self):
        self.find_element(*self._cart_button).click()
        return self
