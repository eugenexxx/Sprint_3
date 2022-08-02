def test_registration(app):
    # Открываем страницу с формой регистрации
    app.session.open_page("/register")
    # Заполняем поле "Имя"
    app.registration_actions.fill_name_field()
    # Заполняем поле "Email"
    app.registration_actions.fill_email_field()
    # Заполняем поле "Пароль"
    app.registration_actions.fill_password_field()
    # Нажимаем кнопку "Зарегистрироваться" и проверяем, что открылась форма авторизации (форма "Вход")
    app.registration_actions.tap_registration_button_and_check_register_successfully()
