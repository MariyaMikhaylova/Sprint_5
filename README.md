# В проекте автоматизиронные проверки сайта Stellar burgers https://stellarburgers.nomoreparties.site/

# Для запуска тестирования необходимо установить библиотеку selenium

# Для тестирования использовались следующие локаторы (XPATH):
# страница регистрации
html/body/div/div/main/div/form/fieldset[1]/div/div/input # Имя 
html/body/div/div/main/div/form/fieldset[2]/div/div/input # Почта 
html/body/div/div/main/div/form/fieldset[3]/div/div/input # Пароль 
html/body/div/div/main/div/form/button # Кнопка "Зарегистрироваться" 
html/body/div/div/main/div/form/fieldset[3]/div/p # Ошибка "Некорректный пароль" 

# страница авторизации
html/body/div/div/main/div/form/fieldset[1]/div/div/input # Почта 
html/body/div/div/main/div/form/fieldset[2]/div/div/input # Пароль 
html/body/div/div/main/div/form/button # Кнопка "Войти" 
html/body/div/div/main/div/form/fieldset/div/div/input  # Пароль на странице восстановления пароля 

# главная страница
html/body/div/div/header/nav/a # кнопка «Личный кабинет» 
html/body/div/div/main/section[2]/div/button # кнопка «Войти в аккаунт» 
html/body/div/div/main/section/div/div[1] # раздел «Булки» 
html/body/div/div/main/section/div/div[2] # раздел «Соусы» 
html/body/div/div/main/section/div/div[3] # раздел «Начинки» 
html/body/div/div/header/nav/ul/li[1]/a # кнопка «Конструктор» 
html/body/div/div/header/nav/div/a # Логотип 

# страница профиля
html/body/div/div/main/div/nav/ul/li[3]/button  # кнопка «Выйти»