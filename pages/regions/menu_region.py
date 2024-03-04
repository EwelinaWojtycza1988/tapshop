from selenium.webdriver.common.by import By

from pages.regions.base_region import BaseRegion
from pages.regions.popup_region import PopupRegion


class MenuRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "header[role='banner']")
    _shop_locator = (By.XPATH, ".//li[@id='menu-item-102']//a[contains(text(), 'Sklep')]")
    _amount_locator = (By.CSS_SELECTOR, "a[class='cart-contents'] span[class*='Price-amount amount']")

    def click_store_button(self):
        self.find_element(*self._shop_locator).click()
        return self

    @property
    def amount(self):
        value = self.find_element(*self._amount_locator).text
        return value[1:]

    def menu_popup(self):
        amount_element = self.find_element(*self._amount_locator)
        self.actions.move_to_element(amount_element).perform()
        return PopupRegion(self)
