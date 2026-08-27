import pytest
from playwright.sync_api import expect


class TestUIHappyPath:
    
    def test_happy_path(self, page, base_url, new_user_data):
        
        # 1. Открываем главную страницу
        page.goto(base_url)
        expect(page).to_have_url(base_url + "/")
        
        # 2. Вводим email и получаем код
        page.get_by_label("Email").fill(new_user_data.email)
        page.get_by_role("button", name="Получить код").click()
        
        # 3. Проверяем, что перешли на страницу верификации
        expect(page).to_have_url(base_url + "/verify")
        
        # 4. Код показан на странице — вводим его
        code = page.get_by_test_id("demo-code").inner_text()
        page.get_by_label("Код").fill(code)
        page.get_by_role("button", name="Войти").click()
        
        # 5. Проверяем, что перешли на страницу анкеты
        expect(page).to_have_url(base_url + "/questionnaire")
        
        # 6. Заполняем анкету
        page.get_by_label("Имя").fill(new_user_data.first_name)
        page.get_by_label("Фамилия").fill(new_user_data.last_name)
        page.get_by_label("Возраст").fill(str(new_user_data.age))
        page.get_by_label("Город").fill(new_user_data.city)
        page.get_by_label("О себе").fill(new_user_data.bio or "Тест")
        page.get_by_role("button", name="Сохранить анкету").click()
        
        # 7. Проверяем, что перешли на страницу профиля
        expect(page).to_have_url(base_url + "/profile")
        
        # 8. Проверяем данные в профиле
        expect(page.get_by_test_id("profile-first_name")).to_have_text(new_user_data.first_name)
        expect(page.get_by_test_id("profile-last_name")).to_have_text(new_user_data.last_name)
        expect(page.get_by_test_id("profile-age")).to_have_text(str(new_user_data.age))
        expect(page.get_by_test_id("profile-city")).to_have_text(new_user_data.city)