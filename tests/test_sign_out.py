def test_authorize_in_user_profile_and_sign_out(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Кликаем по кнопке "Войти в аккаунт" на главной странице сайта
    app.login_actions.click_login_button()
    # Проверяем, что юзер перешел на страницу авторизации
    app.login_actions.check_user_is_redirected_to_the_login_screen()
    # Заполняем форму входа в аккаунт
    app.login_actions.login_in_system(email='rutko_test@testya.com', password='qwerTEST123!')
    # Заходим в личный кабинет
    app.login_actions.open_user_profile_on_homepage()
    # Проверяем, что авторизован необходимый пользователь
    app.login_actions.check_correct_user_is_authorized_in_system(email='rutko_test@testya.com')
    # Нажимаем кнопку "Выход"
    app.profile_actions.click_sign_out()
    # Проверяем, что пользователь вышел
    app.login_actions.check_user_is_redirected_to_the_login_screen()
