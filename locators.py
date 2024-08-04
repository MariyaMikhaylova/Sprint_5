# Для тестирования использовались следующие локаторы:
# страница регистрации
name = ".//label[text() = 'Имя']/following-sibling::input" # Имя
login = ".//label[text() = 'Email']/following-sibling::input" # Почта
password = ".//label[text() = 'Пароль']/following-sibling::input" # Пароль
button_register = ".//button[text() = 'Зарегистрироваться']" # Кнопка "Зарегистрироваться"
password_error = "input__error" # ошибка "Некорректный пароль"
a_in = ".//a[@href = '/login']" # гиперссылка "Войти"

# страница авторизации
login_aut = ".//label[text() = 'Email']/following-sibling::input" # Почта
password_aut = ".//label[text() = 'Пароль']/following-sibling::input" # Пароль
button_enter = ".//button[text() = 'Войти']" # Кнопка "Войти"
a_forgot_password = ".//a[@href = '/forgot-password']" # Гиперссылка "Восстановить пароль"

# главная страница
a_account = ".//a[@href = '/account']" # гиперссылка «Личный кабинет»
button_enter_acc = ".//button[text() = 'Войти в аккаунт']" # кнопка «Войти в аккаунт»
title = ".//h1[text() = 'Соберите бургер']" # заголовок "Соберите бургер"
chapter_buns = ".//span[text() = 'Булки']/parent::div" # раздел «Булки»
chapter_sauces = ".//span[text() = 'Соусы']/parent::div" # раздел «Соусы»
chapter_fillings = ".//span[text() = 'Начинки']/parent::div" # раздел «Начинки»
button_constructor = ".//p[text() = 'Конструктор']/parent::a" # кнопка «Конструктор»
button_logo = ".//div[@class = 'AppHeader_header__logo__2D0X2']/child::a" # Логотип

# страница профиля
a_profile = ".//a[@href = '/account/profile']" # гиперссылка «Профиль»
button_exit = ".//button[text() = 'Выход']"  # кнопка «Выйти»

# # страница восстановления пароля .../forgot-password
login_forgot = ".//label[text() = 'Email']/following-sibling::input" # Почта
button_restore = ".//button[text() = 'Восстановить']"  #  кнопка «Восстановить»

# страница восстановления пароля .../reset-password
letter_code = ".//label[text() = 'Введите код из письма']" # плейсхолдер "Введите код из письма"
