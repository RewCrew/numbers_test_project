# TEST-PROJECT
##Выполнил Шайдуллин К.Р.

### Запуск проекта в:
`Docker`, команда для запуска:
   
`docker-compose up --build -d --remove-orphans`

### Описание проекта:

1) Получение данных с документа при помощи Google API
`ссылка на гугл документ` - https://docs.google.com/spreadsheets/d/1mu6ZVdOLoFdC1KV2JliilzsrR4j82cxDSuVcDNOBdKE/edit#gid=0


2) Для получения актуальнык котировок по курсу ЦБ РФ используется библиотека `pycbrf`


Заполнение БД `PostgreSQL` через cli команду в контейнере order_service:
    `order_api get-orders`


3) Проксирование происходит через веб-сервер `Nginx`.

4) Для развертывания приложения используется `Docker`. 

5) Список ордеров отправляется в очередь `RabbitMQ`.

6) Ордеры из очереди обрабатывает `consumer` в микросервисе `order_service`.
