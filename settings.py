import os
from dotenv import load_dotenv
load_dotenv()

# Базовая страница Ростелекома
base_url = "https://b2c.passport.rt.ru"

# Личная информация зарегистрированного в системе пользователя
valid_name = 'Сергей'
valid_lastname = 'Новиков'
valid_login = os.getenv('valid_login')
valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')
# Лицевой счет зарегистрированного в системе пользователя
valid_account = os.getenv('valid_account')

# Информация незарегистрированного в системе пользователя
other_name1 = 'Ася' # 3 символа
other_name2 = 'Ян' # 2 символа
other_name3 = 'Абдурахмангадживильгельминаия' # 29 символов
other_name4 = 'Варфоломейкаллистратиннокентий' # 30 символов

other_phone = '+79117021753'
other_email = 'vsaga67@mail.ru'

other_password1 = '8wb7gIb8qL@BvSpzSlN' # 19 символов
other_password2 = '8wb7gIb8qL@BvSp23FhN' # 20 символов

# Невалидные значения для проверки полей ввода
invalid_name1 = 'К' # 1 символ
invalid_name2 = 'Варфоломейкаллистратиннокентиий' # 31 символ
invalid_name3 = 'Альбертинабраниславакапитолинамарисабельантуанетта' # 50 символов
invalid_name4 = 'Helen' # латиница
invalid_name5 = '6754' # числа
invalid_name6 = '@%($' # спецсимволы

invalid_phone1 = '99817111222' # номер без +7
invalid_phone2 = 'номертелефона'  # строка

invalid_email1 = 'volobmail.ru' # email без @
invalid_email2 = 'volobmail@' # email без домена

invalid_password1 = '56ghTlo' # 7 символов
invalid_password2 = 'Qa@TVpr%ke7kfZm5oqaio' # 21 символ
invalid_password3 = 'Zy5xFHQ8G6OOIXoafJ8lSHWGjQ1q57nTnkl' # 35 символов
invalid_password4 = 'nzyqy%ein' # 9 символов, без заглавной буквы
invalid_password5 = 'A@WPBFULX' # 9 символов, без строчной буквы
invalid_password6 = 'zedPlblJ' # 8 символов, без цифры/без спецсимвола
invalid_password7 = 'Г7р1н9ом7' # 9 символов, кириллица






