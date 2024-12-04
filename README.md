# OpenAPI спецификация предметов в вузе

## Требования
Python 3.5.2+

## Использование
Чтобы запустить сервер, выполните следующие команды из директории проекта:

```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pip install 'connexion[swagger-ui]<3.0'

python3 -m swagger_server
```

и откройте в браузере URL:

```
http://localhost:8080/ui/
```

## Запуск в Docker контейнере

Чтобы запустить сервер в контейнере, выполните следующие команды из директории проекта::

```
# сборка image
docker build -t swagger_server .

# запуск контейнера
docker run -p 8080:8080 swagger_server
```

## Внешний вид

<img width="657" alt="Снимок экрана 2024-10-17 в 01 31 30" src="https://github.com/user-attachments/assets/c0eb8f14-8f28-4313-a338-4ee6f6923141">

<img width="643" alt="Снимок экрана 2024-10-17 в 01 31 49" src="https://github.com/user-attachments/assets/fc2649ae-f083-47e8-ab45-ba66e9db239d">

<img width="723" alt="Снимок экрана 2024-12-01 в 21 40 42" src="https://github.com/user-attachments/assets/01e091f3-b34e-4917-96f1-2bed0fbb65fb">

<img width="803" alt="Снимок экрана 2024-11-20 в 23 43 53" src="https://github.com/user-attachments/assets/e33275a8-c296-481c-b807-73a89bfa4776">

<img width="794" alt="Снимок экрана 2024-11-20 в 23 44 05" src="https://github.com/user-attachments/assets/fb91ff7e-48f2-435f-b565-8e7c319c7cd5">

<img width="682" alt="Снимок экрана 2024-12-04 в 20 57 24" src="https://github.com/user-attachments/assets/8cdba6ad-8fd9-49fe-b556-25c6a22bbaac">
