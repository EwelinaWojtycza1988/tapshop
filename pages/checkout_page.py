from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    _header = (By.XPATH, "//h1[text()='Zamówienie']")
    _header_1 = (By.XPATH, "//h1[text()='Zamówienie otrzymane']")
    _name = (By.CSS_SELECTOR, "input[name='billing_first_name']")
    _last_name = (By.CSS_SELECTOR, "input[name='billing_last_name']")
    _country_label = (By.XPATH, "//label[@for='billing_country']/../span[contains(@class,'woocommerce-input-wrapper')]")
    _search_country = (By.CSS_SELECTOR, "input[aria-activedescendant*='billing_country']")
    _address = (By.CSS_SELECTOR, "input[name='billing_address_1']")
    _postcode = (By.CSS_SELECTOR, "input[name='billing_postcode']")
    _city = (By.CSS_SELECTOR, "input[name='billing_city']")
    _phone_number = (By.CSS_SELECTOR, "input[name='billing_phone']")
    _email = (By.CSS_SELECTOR, "input[name='billing_email']")
    _buy_and_pay_button = (By.CSS_SELECTOR, "button[data-value='Kupuję i płacę']")

    @property
    def loaded(self):
        return self.is_element_displayed(*self._header) or self.is_element_displayed(*self._header_1)

    def fill_the_form(self, name, last_name, country, address, postcode, city, phone_number, email):
        self.find_element(*self._name).send_keys(name)
        self.find_element(*self._last_name).send_keys(last_name)
        self.select_country(country)
        self.find_element(*self._address).send_keys(address)
        self.find_element(*self._postcode).send_keys(postcode)
        self.find_element(*self._city).send_keys(city)
        self.find_element(*self._phone_number).send_keys(phone_number)
        self.find_element(*self._email).send_keys(email)
        return self

    def select_country(self, country):
        self.find_element(*self._country_label).click()
        self.find_element(*self._search_country).send_keys(country)
        return self

    def buy_and_pay(self):
        sleep(1)
        self.find_element(*self._buy_and_pay_button).click()

    def verify_success_message(self, message):
        success_message = (By.XPATH, f"//p[contains(text(),'{message}')]")
        assert self.is_element_displayed(*success_message)








