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

<img width="1058" alt="Снимок экрана 2024-11-13 в 16 16 41" src="https://github.com/user-attachments/assets/56e272dd-2545-43a2-a668-2dac8e936c0e">

