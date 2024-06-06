import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # Add to card method
    def should_add_product_to_cart_from_its_promo_page(self):
        # check url
        self.should_be_promo_url()
        # add to cart
        self.find(*ProductPageLocators.ADD_TO_CART_BTN).click()
        self.solve_quiz_and_get_code()
        self.should_be_succes_message_on_the_product_add()
        self.should_basket_increased_on_the_products_price_values
    
    def should_be_promo_url(self):
        assert "?promo" in self.browser.current_url , "It isn't promo!"

    def should_be_succes_message_on_the_product_add(self):
        product_name = self.get_text(*ProductPageLocators.PRODUCT__TITLE)
        msg=(product_name + " has been added to your basket.")
        assert msg in self.get_text(*ProductPageLocators.MSG_PRD), "Ordered product doesn't matc"

    def should_basket_increased_on_the_products_price_values(self):
        product_price = self.get_text(*ProductPageLocators.PRODUCT_PRICE)
        msg = ("Your basket total is now" + product_price)
        assert msg in self.get_text(*ProductPageLocator.MSG_BUSKET_VOLUME), f'{msg}'


    