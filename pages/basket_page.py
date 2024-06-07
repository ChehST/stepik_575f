from .base_page import BasePage

from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "basket isn't empty!"

    def should_be_message_about_empty(self):
        assert 'is empty' in self.get_text(*BasketPageLocators.BASKET_EMPTY_MSG), \
            "basket isn't empty!"