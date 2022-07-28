## How to Use the TOML configuration:

> 1. Your project setup should look like this :point_down:
```
_qr_gen_project/
    |
    |----config/
    |       |
    |       |----__init__.py
    |       |
    |       |----conf.toml
    |       |
    |       |----README.md

```
> 2. Edit it appropriately
```
    SECRET_KEY = "django-insecure-o80n6aftui53q1^mbo*lbm1cpmjfmoy=gvda1^z(l27@zwo$r5"
    DEBUG = true

    [DB]
        NAME = 'your_db_name'
        USER = '_your_db_user'  
        PASSWORD = '_your_password'  
        HOST = '_your_host_'  
        PORT = _your_port_(*integer, usually 3306*)

    [EMAIL]
        EMAIL_USE_TLS = true
        EMAIL_HOST_USER = "_your_sandbox_user"
        EMAIL_HOST_PASSWORD = "your_sandbox_password"

```


> 3. Go to project settings file (settings.py)

### *if you are using the default sqlite Database, ignore this step*
### *Otherwise*
### Go to settings

### *replace this*

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```
### *With this*

        ```python
        DATABASES = {
            'default': {
                'ENGINE': conf["DB']['ENGINE'],
                'NAME': conf['DB']['NAME'],  
                'USER': conf['DB']['USER'],  
                'PASSWORD': conf['DB']['PASSWORD'],  
                'HOST': conf['DB']['HOST'],
                'PORT': conf['DB']['PORT'],  
                'OPTIONS': {  
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
                }  
            }
        }
        ```
> 4. 
    