# Тестовое задание на вакансию "Python Backend Developer" 

## ТЗ

Необходимо разработать скрипт на языке Python 3, который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).


2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»

    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).


3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).


Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:
4. a. Упаковка решения в docker контейнер

    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    
    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.


## Запуск проекта

### Необходимо склонировать репозиторий и установить переменные окружения в .env файле
```shell
git clone https://github.com/novoseltcev/backend-test-task.git
cd backend-test-task
cp .env.example .env
```

1. Для обращения к API Google Spreadsheets необходимо создать API-ключ и добавить его в .env: https://console.cloud.google.com/apis/credentials
```shell
GOOGLE_API_KEY={VALUE}
```

2. Для отправки уведомлений в Telegram - добавить токен доступа к Боту и ID целевого чата, в котором Бот состоит
```shell
TG_TOKEN={VALUE}
TG_CHAT_ID=-{VALUE}
```

3. Для работы сервера - добавить рандомные строковые последовательности в качестве ключей шифрации сессии и JWT-токенов
```shell
SECRET_KEY={VALUE}
JWT_SECRET_KEY={VALUE}
```

### Запуск контейнеров
```shell
docker-compose up --build -d
```

### Проверка логов контейнеров
```shell
docker logs backend-test-task-db-1
docker logs backend-test-task-cron-1
docker logs backend-test-task-backend-1
```
### Конфигурация планировщика выполнения скриптов
```shell
*/2 * * * * update_orders           # Каждые две минуты обновляет БД
0 */12 * * * update_exchange_rate   # Дважды в сутки (в 12:00 и 00:00) обновляет курс доллара
0 10 * * * check_delivery_delays    # Каждый день в 10:00 по МСК уведомляет в Telegram о задерживании поставки
```
После обновления конфигурации перезапустить контейнеры

Проверка логов crond
```shell
sudo docker exec backend-test-task-cron-1 cat crontab.log
```

### Подключение к БД и проверка данных
```shell
docker exec -it backend-test-task-db-1 psql -U postgres -h db -d test
# Ввод пароля от БД
\d+
select * from orders;
select * from currency;
```