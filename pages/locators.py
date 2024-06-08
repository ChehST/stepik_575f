from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKT_BTN = (By.XPATH,"//a[contains(text(),'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"#register_form")
    REGISTRATIOM_MAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATIOM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATIOM_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.XPATH, "//button[text()='Register']")
    REG_OK_SIGN = (By.CSS_SELECTOR,".alertinner.wicon .icon-ok-sign")


class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    PRODUCT__TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MSG_PRD = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    MSG_BUSKET_VOLUME = (By.CSS_SELECTOR, "#messages div:nth-child(3)")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner p")
