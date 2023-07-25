from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    search_element = (By.XPATH, "//input[@placeholder='Найти в Halyk Market']")
    favorites_folder = (By.XPATH, "//a[@title= 'Перейти в раздел избранное']")

    def open(self, url):
        self.driver.get(url)

    def is_title_present(self, title):
        return title in self.driver.title

    def search_product(self, product_name):
        search_input = self.element_is_visible(self.search_element)
        search_input.send_keys(product_name)
        search_input.submit()

    def go_to_favorites(self):
        favorites_btn = self.element_is_visible(self.favorites_folder)
        favorites_btn.click()
