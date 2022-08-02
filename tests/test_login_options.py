def test_authorize_using_login_button_on_homepage(app):
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


def test_authorize_using_user_profile_button_on_homepage(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Кликаем по кнопке "Личный кабинет" на главной странице сайта
    app.login_actions.click_user_profile_button()
    # Проверяем, что юзер перешел на страницу авторизации
    app.login_actions.check_user_is_redirected_to_the_login_screen()
    # Заполняем форму входа в аккаунт
    app.login_actions.login_in_system(email='rutko_test@testya.com', password='qwerTEST123!')
    # Заходим в личный кабинет
    app.login_actions.open_user_profile_on_homepage()
    # Проверяем, что авторизован необходимый пользователь
    app.login_actions.check_correct_user_is_authorized_in_system(email='rutko_test@testya.com')


def test_authorize_from_registration_form(app):
    # Открываем страницу регистрации
    app.session.open_page("/register")
    # Кликаем по кнопке "Войти" на странице регистрации
    app.login_actions.click_login_button_on_registration_form()
    # Проверяем, что юзер перешел на страницу авторизации
    app.login_actions.check_user_is_redirected_to_the_login_screen()
    # Заполняем форму входа в аккаунт
    app.login_actions.login_in_system(email='rutko_test@testya.com', password='qwerTEST123!')
    # Заходим в личный кабинет
    app.login_actions.open_user_profile_on_homepage()
    # Проверяем, что авторизован необходимый пользователь
    app.login_actions.check_correct_user_is_authorized_in_system(email='rutko_test@testya.com')


def test_authorize_using_forgot_password_button_on_login_screen(app):
    # Открываем страницу "Восстановить пароль"
    app.session.open_page("/forgot-password")
    # Кликаем по кнопке "Войти" на странице "Восстановить пароль"
    app.login_actions.click_login_button_on_forgot_password_form()
    # Проверяем, что юзер перешел на страницу авторизации
    app.login_actions.check_user_is_redirected_to_the_login_screen()
    # Заполняем форму входа в аккаунт
    app.login_actions.login_in_system(email='rutko_test@testya.com', password='qwerTEST123!')
    # Заходим в личный кабинет
    app.login_actions.open_user_profile_on_homepage()
    # Проверяем, что авторизован необходимый пользователь
    app.login_actions.check_correct_user_is_authorized_in_system(email='rutko_test@testya.com')
