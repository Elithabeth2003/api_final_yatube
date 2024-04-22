# Проект «API для Yatube»
api final
## Описание
API для Yatube представляет собой проект социальной сети в которой реализованы следующие возможности, публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
## Запуск проекта
+ Клонируйте репозидорий и перейдите в него с помощью командной строки:
```
git clone git@github.com:Elithabeth2003/api_final_yatube.git
cd api_final_yatube
```
+ Установите и активируйте виртуальное окружение c учетом версии Python 3.9:

```
python3 -m venv env
либо
python -m venv venv
```
* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```
```
python -m pip install --upgrade pip
```

+ Затем установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

+ Выполняем миграции:

```
python3 manage.py migrate
либо
python manage.py migrate
```

+ Запускаем проект:

```
python3 manage.py runserver
либо
python manage.py runserver
```
Теперь в браузере или в программе для взаимодействия с API (например, Postman), можете перейти по адресу http://127.0.0.1:8000/api/v1/ для запросов к API проекта

## Примеры работы с API для всех пользователей

Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.

+ Получение публикаций

```
GET api/v1/posts/
При указании параметров limit и offset выдача должна работать с пагинацией
```

Пример ответа:

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
+ Получение публикации по id

```
GET api/v1/posts/{id}/
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
+ Получение списка доступных сообществ

```
GET api/v1/groups/
```
Пример ответа:

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

+ Получение информации о сообществе по id

```
GET api/v1/groups/{id}/
```
Пример ответа:

```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
+ Получение всех комментариев к публикации

```
GET api/v1/{post_id}/comments/
```
Пример ответа:

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
+ Получение комментария к публикации по id

```
GET api/v1/{post_id}/comments/{id}/
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
## Примеры работы с API для авторизованных пользователей

+ Создание публикации

```
POST /api/v1/posts/
```

Пример запроса:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

+ Обновление публикации

```
PUT /api/v1/posts/{id}/
```

Пример запроса:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

+ Частичное обновление публикации

```
PATCH /api/v1/posts/{id}/
```
Пример запроса:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

+ Удаление публикации

```
DELETE /api/v1/posts/{id}/
```
Пример ответа:

```
{
  "detail": "Учетные данные не были предоставлены."
}
```

+ Создание комментария

```
POST /api/v1/posts/{post_id}/comments/
```

Пример запроса:

```
{
  "text": "string"
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

+ Обновление комментария

```
PUT /api/v1/posts/{post_id}/comments/{id}/
```
Пример запроса:

```
{
  "text": "string"
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

+ Частичное обновление комментария

```
PATCH /api/v1/posts/{post_id}/comments/{id}/
```

Пример запроса:

```
{
  "text": "string"
}
```
Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

+ Удаление комментария

```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```
Пример ответа:

```
{
  "detail": "Учетные данные не были предоставлены."
}
```

+ Подписки

Возвращает все подписки пользователя, сделавшего запрос:

```
GET api/v1/follow/
```
Пример ответа:

```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса:

```
POST api/v1/follow/
```

Пример запроса:

```
{
  "following": "string"
}
```
Пример ответа:

```
{
  "user": "string",
  "following": "string"
}
```
+ Получить JWT-токен

```
POST /api/v1/jwt/create/
```
Пример запроса:

```
{
  "username": "string",
  "password": "string"
}
```
Пример ответа:

```
{
  "refresh": "string",
  "access": "string"
}
```

+ Обновить JWT-токен

```
POST api/v1/jwt/refresh/
```

Пример запроса:

```
{
  "refresh": "string"
}
```
Пример ответа:

```
{
  "access": "string"
}
```

+ Проверить JWT-токен

```
POST /api/v1/jwt/verify/
```

Пример запроса:

```
{
  "token": "string"
}
```
Пример ответа:

```
{
  "token": [
    "Обязательное поле."
  ]
}
```

+ В проекте API реализована пагинация (LimitOffsetPagination):

```
GET /api/v1/posts/?limit=5&offset=0
```
