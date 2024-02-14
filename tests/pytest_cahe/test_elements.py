import time

from pages.elements_page import TextBoxPage, LinksPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            test_box_page.open()
            input_data = test_box_page.fill_all_fields()
            output_data = test_box_page.check_filled_form()
            assert input_data == output_data


def test_links_page(driver):
    test_links = LinksPage(driver, 'https://demoqa.com/links')
    test_links.open()
