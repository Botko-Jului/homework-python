import pytest
from playwright.sync_api import expect


class TestUIValidationLogin:

    # пустой email
    def test_login_empty_email(self, page, base_url):
        page.goto(base_url)
        page.get_by_role("button", name="Получить код").click()
        
        expect(page).to_have_url(base_url + "/")
        
        email_input = page.get_by_label("Email")
        expect(email_input).to_have_js_property("validity.valid", False)

    # email без @
    def test_login_email_without_at(self, page, base_url):
        page.goto(base_url)
        page.get_by_label("Email").fill("testexample.com")
        page.get_by_role("button", name="Получить код").click()
        
        expect(page).to_have_url(base_url + "/")
        
        email_input = page.get_by_label("Email")
        expect(email_input).to_have_js_property("validity.valid", False)

    # невалидный email 
    def test_login_invalid_email(self, page, base_url, invalid_email):
        page.goto(base_url)
        
        if invalid_email.strip() == "":
            return
        
        page.get_by_label("Email").fill(invalid_email)
        page.get_by_role("button", name="Получить код").click()
        
        expect(page).to_have_url(base_url + "/")
        expect(page.get_by_text("Некорректный email")).to_be_visible()
