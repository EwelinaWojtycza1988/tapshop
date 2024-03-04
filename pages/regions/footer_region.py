from selenium.webdriver.common.by import By

from pages.regions.base_region import BaseRegion


class FooterRegion(BaseRegion):
    _root_locator = (By.CSS_SELECTOR, "p[class*='woocommerce-store-notice demo_store']")
    _reject_button = (By.CSS_SELECTOR, "a[class*='dismiss-link']")

    def click_on_reject_button(self):
        self.find_element(*self._reject_button).click()


