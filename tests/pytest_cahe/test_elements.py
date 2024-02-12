import time

from pages.elements_page import TextBoxPage, LinksPage




def test_text_box(driver):
    test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
    test_box_page.open()
    test_box_page.fill_all_fields()

def test_links_page(driver):
    test_links = LinksPage(driver, 'https://demoqa.com/links')
    test_links.open()

