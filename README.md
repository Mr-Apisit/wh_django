# homework_django

    กิจกรรมหลังเรียน
        |_ แบ่งเป็น Day by home_work

## กิจกรรมหลังเรียน

ใช้ประกอบเป็นแบบทดสอบของตนเอง

## Pre-Installation ก่อนเริ่มทำกิจกรรม

```bash
pip install --upgrade pip #upgrade version ของ pip
pip install virtualenv  #ติดตั้ง package environment
```

package manager [pip](https://pip.pypa.io/en/stable/) เพื่อติดตั้ง package.

## Usually when create new project

สร้าง Folder ก่อนจากนั้น.....เข้าไป

```bash
virtualenv env
# จากนั้นได้ Folder ชื่อ env ซึ่งเป็น environments package

```

## After activate env ทำครั้งเดียว (env) สังเกตหัว terminal

```bash
    pip install django
    # และ
    pip freeze > requirments.txt # เพื่อเก็บ version package ไว้ที่ไฟล์ requirments.txt
```

## Usually when open project

```bash
.\env\Scripts\activate #เปิดใช้งาน env

```

## start your project

```bash
django-admin startproject your_project . # . เพื่อไม่ต้องการให้ django สร้าง directory ซ้ำตามชื่อ project
```

## make your app in folder apps

สร้าง Folder apps และจากนั้น.......เข้าไป

```bash
# Django-admin startapp your_app
```

## แก้ไข file apps.py

```python
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.your_app'


```

## เพิ่ม your_app ใน project settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.your_app'#----------
]
```

## run django server

```bash
python manage.py runserver
```

```python
from django.shortcuts import render

def knowledge_is_power(self,request):
    context = dict(brain="let it work")
    return render(request,context,"your_brain.html")

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
