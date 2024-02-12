import time

from locators.elements_page_locators import TextBoxPageLocators, LinksPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self, ):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sdasds')

        self.element_is_visible(self.locators.EMAIL).send_keys('jfjjkhiik.com')

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('kd5ttttvh')

        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('sukbl')

        self.element_is_visible(self.locators.SUBMIT).click()


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_home_link(self, ):
        self.element_is_visible(self.locators.HOME)

    def check_home_random_link(self, ):
        self.element_is_visible(self.locators.HOME_SRS0W)

    def check_created_link(self, ):
        self.element_is_visible(self.locators.CREATED)

    def check_moved_link(self, ):
        self.element_is_visible(self.locators.MOVED)

    def check_bad_request_link(self, ):
        self.element_is_visible(self.locators.BAD_REQUEST)

    def check_unauthorized_link(self, ):
        self.element_is_visible(self.locators.UNAUTHORIZED)

    def check_forbidden_link(self, ):
        self.element_is_visible(self.locators.FORBIDDEN)

    def check_not_found_link(self, ):
        self.element_is_visible(self.locators.NOT_FOUND)
