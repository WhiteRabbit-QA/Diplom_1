import allure

from data import Data
from praktikum.bun import Bun


class TestBun:
    @allure.title("Проверка верного присваивания названия булки")
    def test_name_of_bun_correct(self):
        bun = Bun(Data.buns[0].get("name"), Data.buns[0].get("price"))

        assert bun.name == "black bun"

    @allure.title("Проверка верного присваивания цены булки")
    def test_price_of_bun_correct(self):
        bun = Bun(Data.buns[1].get("name"), Data.buns[1].get("price"))

        assert bun.price == 200.0

    @allure.title("Проверка, что метод возвращает верное название булки")
    def test_get_name_return_true_name(self):
        bun = Bun(Data.buns[2].get("name"), Data.buns[2].get("price"))
        name = bun.get_name()

        assert name == "red bun"

    @allure.title("Проверка, что метод возвращает верную цену булки")
    def test_get_price_return_true_price(self):
        bun = Bun(Data.buns[2].get("name"), Data.buns[2].get("price"))
        price = bun.get_price()

        assert price == 300.0
