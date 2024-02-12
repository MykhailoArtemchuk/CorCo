from selenium.webdriver.common.by import By


# form fields

class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, '#userName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    #created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class LinksPageLocators:
    HOME = (By.ID, 'simpleLink')
    HOME_SRS0W = (By.ID, 'dynamicLink')
    CREATED = (By.ID, 'created')
    NO_CONTENT = (By.ID, 'no-content')
    MOVED = (By.ID, 'moved')
    BAD_REQUEST = (By.ID, 'bad-request')
    UNAUTHORIZED = (By.ID, 'unauthorized')
    FORBIDDEN = (By.ID, 'forbidden')
    NOT_FOUND = (By.ID, 'invalid-url')
