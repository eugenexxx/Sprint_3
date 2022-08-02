# Проверяем переход в личный кабинет
def test_redirect_to_user_profile(app):
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


# Проверяем переход из личного кабинета в конструктор
def test_redirect_from_user_profile_to_constructor(app):
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
    # Кликаем по кнопке "Конструктор" в личном кабинете
    app.profile_actions.click_constructor_button()
    # Проверяем, что открылась главная страница и активна вкладка "Конструктор"
    app.profile_actions.check_constructor_is_active()


def test_redirect_to_homepage_by_clicking_logo(app):
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
    # Кликаем по логотипу в хедере
    app.profile_actions.click_header_logo()
    # Проверяем, что открылась главная страница и активна вкладка "Конструктор"
    app.profile_actions.check_constructor_is_active()
