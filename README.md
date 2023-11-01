# SOAR
Скрипт для сбора данных с коммутатора cisco7200

## Необходимые библиотеки
netmiko==4.2.0<br>

## Настройка 
Перед запуском программы необходимо изменить данные для подключения к cisco в main файле

Пример подключения:
```
device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.253.2',
        'username': 'administrator',
        'password': 'admin',
        'port': 22,         
        'secret': '',        
        'verbose': False,    
    }
```
## Запуск программы
Для запуска необходимо прописать команды:<br>

```
docker-compose build
docker-compose up
```

Для рестарта необходимо прописать команды:<br>
```
docker-compose down
docker-compose build
docker-compose up
```
Для рестарта необходимо прописать команды:<br>
```
docker-compose down
docker-compose build
docker-compose up
```
