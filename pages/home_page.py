from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    _background_image = (By.CSS_SELECTOR, "span[class*='has-background-dim']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._background_image)







