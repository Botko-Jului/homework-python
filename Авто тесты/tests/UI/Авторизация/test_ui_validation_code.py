import pytest
from playwright.sync_api import expect


class TestUIValidationCode:

    # пустой код
    def test_login_empty_code(self, page, base_url, new_user_data):
        page.goto(base_url)
        page.get_by_label("Email").fill(new_user_data.email)
        page.get_by_role("button", name="Получить код").click()
        
        expect(page).to_have_url(base_url + "/verify")
        
        page.get_by_role("button", name="Войти").click()
        
        expect(page).to_have_url(base_url + "/verify")
        code_input = page.get_by_label("Код")
        expect(code_input).to_have_js_property("validity.valid", False)

    # неправильный код
    def test_login_wrong_code(self, page, base_url, new_user_data):
        page.goto(base_url)
        page.get_by_label("Email").fill(new_user_data.email)
        page.get_by_role("button", name="Получить код").click()
        
        page.get_by_label("Код").fill("000000")
        page.get_by_role("button", name="Войти").click()
        
        expect(page.get_by_text("Неверный код или email")).to_be_visible()