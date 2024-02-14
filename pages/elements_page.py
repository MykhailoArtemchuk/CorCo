import time
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, LinksPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME)
        email = self.element_is_present(self.locators.EMAIL)
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS)
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS)
        return full_name.text, email.text, current_address.text, permanent_address.text


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
