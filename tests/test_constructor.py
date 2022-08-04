def test_bun_tab_is_active(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Проверяем, что вкладка "Булки" активна
    app.constructor_actions.check_bun_tab_is_active()
    # Кликаем на вкладку "Соусы"
    app.constructor_actions.click_sauce_button()
    # Проверяем, что вкладка "Соусы" активна
    app.constructor_actions.check_sauce_tab_is_active()
    # Кликаем на вкладку "Булки"
    app.constructor_actions.click_bun_button()
    # Проверяем, что вкладка "Булки" активна
    app.constructor_actions.check_bun_tab_is_active()


def test_sause_tab_is_active(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Проверяем, что вкладка "Булки" активна
    app.constructor_actions.check_bun_tab_is_active()
    # Кликаем на вкладку "Соусы"
    app.constructor_actions.click_sauce_button()
    # Проверяем, что вкладка "Соусы" активна
    app.constructor_actions.check_sauce_tab_is_active()


def test_stuffing_tab_is_active(app):
    # Открываем домашнюю страницу сайта
    app.session.open_page("/")
    # Проверяем, что вкладка "Булки" активна
    app.constructor_actions.check_bun_tab_is_active()
    # Кликаем на вкладка "Начинки"
    app.constructor_actions.click_stuffing_button()
    # Проверяем, что вкладка "Начинки" активна
    app.constructor_actions.check_stuffing_tab_is_active()
