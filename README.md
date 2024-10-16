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

```bash
# сборка image
docker build -t swagger_server .

# запуск контейнера
docker run -p 8080:8080 swagger_server
```
