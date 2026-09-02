import pytest
from playwright.sync_api import expect


class TestUIWithoutQuestionnaire:
    
    def test_without_questionnaire(self, page, base_url, new_user_data):
        
        # 1. Открываем главную страницу
        page.goto(base_url)
        expect(page).to_have_url(base_url + "/")
        
        # 2. Вводим email и получаем код
        page.get_by_label("Email").fill(new_user_data.email)
        page.get_by_role("button", name="Получить код").click()
        expect(page).to_have_url(base_url + "/verify")
        
        # 3. Вводим код
        code = page.get_by_test_id("demo-code").inner_text()
        page.get_by_label("Код").fill(code)
        page.get_by_role("button", name="Войти").click()
        
        # 4. Проверяем, что мы на странице анкеты
        expect(page).to_have_url(base_url + "/questionnaire")
        expect(page.get_by_role("heading", name="Анкета")).to_be_visible()
        
        # 5. Пытаемся перейти в профиль напрямую
        page.goto(f"{base_url}/profile")
        
        # 6. Должны быть перенаправлены на анкету
        expect(page).to_have_url(base_url + "/questionnaire")