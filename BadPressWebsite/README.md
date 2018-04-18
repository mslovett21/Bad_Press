
## To get it running
### Required Resources
* Django
* mysql
* mysqlclient

Make migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create superuser
```
python3 manage.py createsuperuser

```

Run Server
```python
python manage.py runserver
```

Add your credentials in my.cnf file
```
[client]
database = badpress
user = <YOURUSERNAME>
password = <YOURPASSWORD>
default-character-set = utf8
```

Update the location of my.cnf file in BPW/BPW/settings.py in 'read_default_file': '/usr/local/opt/mysql/my.cnf'
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
    'OPTIONS': {
            'read_default_file': '/usr/local/opt/mysql/my.cnf',
        },
    }
}
```
