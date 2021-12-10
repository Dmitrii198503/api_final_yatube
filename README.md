#### **Описание:**
API для проекта сообщества Yatube. Позволяет создавать посты, комментарии к постам, а также подписываться на пользователей. Имеет полноценную авторизацию и аутентификацию.
#### **Установка:**
<u>Клонировать репозиторий и перейти в него в командной строке:</u>

<font color="#24292f" face="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">git clone https://github.com/Dmitrii198503/api_final_yatube</span></font>
- - -
<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;"><u>Cоздать и активировать виртуальное окружение:</u></span>

<font color="#24292f" face="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">python -m venv venv</span></font>

<font color="#24292f" face="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">source venv/Scripts/activate</span></font>

python -m pip install --upgrade pip
- - -
<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;"><u>Установить зависимости из файла requirements.txt:</u></span>

<font color="#24292f" face="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji"><span style="font-size: 16px;">pip install -r requirements.txt</span></font>
- - -
<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;"><u>Выполнить миграции:</u></span>

<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;">cd yatube_api</span>

<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;">python manage.py migrate</span>
- - -
<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;"><u>Запустить проект:</u></span>

<span style="color: rgb(36, 41, 47); font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px;">python manage.py runserver</span>
#### <b>Примеры:</b>
<b>GET <u>api/v1/posts/</u></b>

Получение списка всех публикаций
- - -
<b>POST <u>api/v1/jwt/refresh/</u></b>

Обновить JWT токен
- - -
<b>POST <u>api/v1/posts/&lt;post_id&gt;/comments/</u></b>

Добавление нового комментария к публикации. Анонимные комментарии запрещены.
