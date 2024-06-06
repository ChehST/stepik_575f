from .base_page import BasePage
from .locators import MainPageLocators

# links to other page's objects
from .login_page import LoginPage

class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)