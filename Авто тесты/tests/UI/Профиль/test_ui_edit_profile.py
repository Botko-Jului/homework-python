import pytest
from playwright.sync_api import expect


class TestUIEditProfile:
    
    def test_edit_profile(self, page, base_url, new_user_data):
        
        # 1. Полный вход + анкета
        page.goto(base_url)
        expect(page).to_have_url(base_url + "/")
        
        page.get_by_label("Email").fill(new_user_data.email)
        page.get_by_role("button", name="Получить код").click()
        expect(page).to_have_url(base_url + "/verify")
        
        code = page.get_by_test_id("demo-code").inner_text()
        page.get_by_label("Код").fill(code)
        page.get_by_role("button", name="Войти").click()
        expect(page).to_have_url(base_url + "/questionnaire")
        
        page.get_by_label("Имя").fill(new_user_data.first_name)
        page.get_by_label("Фамилия").fill(new_user_data.last_name)
        page.get_by_label("Возраст").fill(str(new_user_data.age))
        page.get_by_label("Город").fill(new_user_data.city)
        page.get_by_label("О себе").fill(new_user_data.bio or "Тест")
        page.get_by_role("button", name="Сохранить анкету").click()
        expect(page).to_have_url(base_url + "/profile")
        
        # 2. Проверяем начальный город
        expect(page.get_by_test_id("profile-city")).to_have_text(new_user_data.city)
        
        # 3. Редактируем город
        new_city = "Казань"
        page.get_by_label("Город").fill(new_city)
        page.get_by_role("button", name="Сохранить изменения").click()
        
        # 4. Проверяем, что город изменился
        expect(page.get_by_test_id("profile-city")).to_have_text(new_city)
        
        # 5. Проверяем, что остальные поля не изменились
        expect(page.get_by_test_id("profile-first_name")).to_have_text(new_user_data.first_name)
        expect(page.get_by_test_id("profile-last_name")).to_have_text(new_user_data.last_name)
        expect(page.get_by_test_id("profile-age")).to_have_text(str(new_user_data.age))