import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SearchResultPage(BasePage):
    search_results = (By.XPATH, "//span[@class='category-page-amount']")
    product_name_element = (By.XPATH, "//div[@class='product-card-title']")

    def are_results_present(self):
        return self.element_is_visible(self.search_results)

    def select_product(self):
        product_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@title = 'Смартфон Apple iPhone 14 Pro 128Gb Deep Purple']"))
        )
        product_link.click()
        time.sleep(10)

    def get_search_result_product_price(self):
        product_price_element = self.driver.find_element(By.XPATH,
                                                         "//div[@title = 'Смартфон Apple iPhone 14 Pro 128Gb Deep Purple']//span[@class = 'product-card-value-value']")
        return product_price_element.text.strip()

    def get_product_name(self):
        product_name_element = self.element_is_visible(self.product_name_element)
        return product_name_element.text.strip()
