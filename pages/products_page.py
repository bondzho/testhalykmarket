from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    product_name_element = (By.XPATH, "//h1[@class='desc-name']")
    favorite_button_element = (By.XPATH, "//button[@class='btn product-buttons-favorite filled giant']")
    favorite_button_active_element = (By.XPATH, "//button[contains(@class, 'btn product-buttons-favorite filled giant isFavorite')]")
    product_price_element = (By.XPATH, "(//div[@class = 'desc-price-value'])[1]")

    def get_product_name(self):
        product_name_element = self.element_is_visible(self.product_name_element)
        return product_name_element.text.strip()

    def is_favorite_button_available(self):
        favorite_button_element = self.element_is_visible(self.favorite_button_element)
        return favorite_button_element.is_enabled()

    def is_favorite_button_active(self):
        favorite_button = self.element_is_visible(self.favorite_button_active_element)
        return favorite_button.is_enabled()

    def click_favorite_button(self):
        favorite_button = self.element_is_visible(self.favorite_button_element)
        favorite_button.click()

    def get_product_price(self):
        product_price_element = self.element_is_visible(self.product_price_element)
        return product_price_element.text.strip()
