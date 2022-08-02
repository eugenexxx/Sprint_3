class RegistrationForm:

    name_field = "//div[label[contains(., 'Имя')]]/input"
    email_field = "//div[label[contains(., 'Email')]]/input"
    password_field = "//input[@name='Пароль']"
    password_validation_error = "//p[text()='Некорректный пароль']"
    registration_failed_error = "//p[text()='Такой пользователь уже существует']"
    registration_button = "//button[text()='Зарегистрироваться']"
    enter_button = "//button[text()='Войти']"
