from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FavoritesPage(BasePage):
    product_name_element = (By.XPATH, "//div[@class='product-card-title']")
    product_price_element = (By.XPATH, "//div[@title = 'Смартфон Apple iPhone 14 Pro 128Gb Deep Purple']//span[@class = 'product-card-value-value']")

    def get_favorites_product_name(self):
        product_name_element = self.element_is_visible(self.product_name_element)
        return product_name_element.text.strip()

    def get_favorites_product_price(self):
        product_price_element = self.element_is_visible(self.product_price_element)
        return product_price_element.text.strip()
