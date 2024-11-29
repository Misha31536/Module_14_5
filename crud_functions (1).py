import sqlite3

file_name = './Products.db'
fill_table = ''
user_table = ''
base_names = 'Products'
base_users = 'User'
connection = sqlite3.connect(file_name)
cursor = connection.cursor()


# Создание файла базы SQL по заданным параметрам
def initiate_db(catalog_id, title_name, description, price, image, username, email, age, balance):
    global fill_table
    global user_table
    global connection
    global cursor
    print(f'\033[32mСоздаем базу данных, если она существует, то открываем: {file_name}\033[0m')
    fill_table = catalog_id, title_name, description, price, image
    print(fill_table)
    print(f'\033[34mСоздаем список таблиц - Пользователь: {base_names}, поля: {catalog_id}, {title_name}, '
          f'{description}, {price}, {image}\033[0m')
    print(f'\033[32mСоздаем базу данных, если она существует, то открываем: {file_name}\033[0m')
    user_table = username, email, age, balance
    print(user_table)
    print(f'\033[34mСоздаем список таблиц - Пользователь: {base_users}, поля: {username}, {email}, '
          f'{age}, {balance}\033[0m')
    set_file_name = (f'''CREATE TABLE IF NOT EXISTS {base_names}(
            id INTEGER PRIMARY KEY,
            {catalog_id} TEXT NOT NULL,
            {title_name} TEXT,
            {description} TEXT,
            {price} INT NOT NULL,
            {image} TEXT
        )
    ''')
    cursor.execute(set_file_name)
    set_file_name = (f'''CREATE TABLE IF NOT EXISTS {base_users}(
                id INTEGER PRIMARY KEY,
                {username} TEXT NOT NULL,
                {email} TEXT,
                {age} INT NOT NULL,
                {balance} INT NOT NULL
            )
        ''')
    cursor.execute(set_file_name)


# Очистка таблицы SQL
def delete_table(table_del):
    global connection
    global cursor
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    print('Очистка списка')
    cursor.execute(f'DELETE FROM {table_del};')


# Заполнение таблицы SQL Products по заданным параметрам
def fill_in_the_table(set_catalog, set_title, set_description, set_price, set_photo):
    global fill_table
    global connection
    global cursor
    sql = str(f'INSERT INTO {base_names} ({fill_table[0]}, {fill_table[1]}, {fill_table[2]}, '
              f'{fill_table[3]}, {fill_table[4]}) VALUES (?, ?, ?, ?, ?)')
    cursor.execute(f'{sql}', (f'{set_catalog}', f'{set_title}', f'{set_description}',
                              set_price, f'{set_photo}'))


# Отображение содержимого таблицы по определенным параметрам
def screen(screen_elements):
    cursor.execute(f'SELECT * FROM {screen_elements}')
    products = cursor.fetchall()
    for product in products:
        # print('fill_table', fill_table)
        print(f'id: {product[0]} | {fill_table[2]}: {product[2]} | {fill_table[3]}: {product[3]} | '
              f'{fill_table[4]}: {product[4]}')
    commit()


# Проверяем наличие пользователя в таблице
def is_included(user_name):
    print(f'Проверяем, есть ли пользователь в базе:')
    count = cursor.execute(f"SELECT COUNT(*) FROM {base_users} WHERE {user_table[0]} = '{user_name}'").fetchone()
    commit()
    return count[0] > 0


# Наполнение таблицы пользователей
def add_user(username, email, age, balance=1000):
    sql = str(f'INSERT INTO {base_users} ({user_table[0]}, {user_table[1]}, {user_table[2]}, '
              f'{user_table[3]}) VALUES (?, ?, ?, ?)')
    cursor.execute(f'{sql}', (f'{username}', f'{email}', age, balance))
    commit()
    display(base_users)


# Отображение содержимого таблицы
def display(base):
    # global base_names
    cursor.execute(f'SELECT * FROM {base}')
    products = cursor.fetchall()
    for product in products:
        print(product)
    commit()


# Закрытие таблицы
def commit():
    global connection
    global cursor
    connection.commit()


# Завершение работы с таблицей
def finish():
    global connection
    global cursor
    connection.close()
