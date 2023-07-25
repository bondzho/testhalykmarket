import time

from pages.home_page import HomePage
from pages.search_result_page import SearchResultPage
from pages.products_page import ProductPage
from pages.favorites_page import FavoritesPage
from conftest import driver


def test_search_and_favorite_product(driver):
    url = "https://www.halykmarket.kz/"
    product_name = "iPhone 14 Pro 128Gb Deep Purple"

    # Pages init
    home_page = HomePage(driver)
    search_result_page = SearchResultPage(driver)
    product_page = ProductPage(driver)
    favorites_page = FavoritesPage(driver)

    home_page.open(url)

    # 2. Проверить, что заголовок страницы содержит "Halyk Market - Выгодные покупки в рассрочку".
    assert home_page.is_title_present("Halyk Market - Выгодные покупки в рассрочку")

    # 3. Найти поле поиска на сайте.
    # 4. Ввести "iPhone 14 Pro 128 Deep Purple" в поле поиска.
    # 5. Нажать клавишу Enter или выполнить поиск, чтобы получить результаты.
    home_page.search_product(product_name)

    # 6. Подождать, пока результаты поиска загрузятся.
    # 7. Проверить, что есть результаты поиска.
    assert search_result_page.are_results_present()
    search_product_price = search_result_page.get_search_result_product_price()

    # 8. Найти продукт "iPhone 14 Pro 128 Deep Purple" среди результатов поиска.
    # 9. Проверить, что название продукта соответствует "iPhone 14 Pro 128 Deep Purple".
    # 10. Кликнуть на продукт "iPhone 14 Pro 128 Deep Purple", чтобы открыть его страницу.
    assert product_name in search_result_page.get_product_name()
    search_result_page.select_product()
    time.sleep(1)

    # 11. Подождать, пока страница продукта загрузится.
    # 12. Проверить, что название продукта на странице соответствует "iPhone 14 Pro 128 Deep Purple".

    assert product_name in product_page.get_product_name()
    product_page_product_price = product_page.get_product_price()
    time.sleep(1)

    # 13. Найти кнопку "Избранное" на странице продукта.
    # 14. Проверить, что кнопка "Избранное" доступна для нажатия.
    assert product_page.is_favorite_button_available()
    time.sleep(1)

    # 15. Кликнуть на кнопку "Избранное", чтобы добавить продукт в избранное.
    # 16. Подождать, пока продукт будет добавлен в избранное.
    product_page.click_favorite_button()
    time.sleep(1)

    # 17. Проверить, что продукт успешно добавлен в избранное.
    assert product_page.is_favorite_button_active()
    time.sleep(1)

    # 18. Перейти на страницу карточки товара.
    home_page.go_to_favorites()
    time.sleep(2)
    favorites_product_price = favorites_page.get_favorites_product_price()

    # 19. Убедиться, что название товара в избранном совпадает с названием товара на странице карточки товара.
    assert product_name in favorites_page.get_favorites_product_name()
    time.sleep(1)

    # 20. Убедиться, что цена товара в поиске, избранном, и карточке товара одинакова.
    assert search_product_price == product_page_product_price[3:] == favorites_product_price

    # 21. Завершить сеанс браузера.
    driver.close()
