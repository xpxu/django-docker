DATABASE
========

数据表更改
----------
    change models.py
    python manage.py makemigrations # migrate前的准备
    python manage.py migrate # migrate default 数据库
    python manage.py migrate --database=users # migrate名字为user数据库

数据库导入
----------
eg.

    Blog.objects.create(title=title,content=content)
    Blog.objects.get_or_create(title=title,content=content) # 避免导入重复数据

创建管理员
----------
python manage.py createsuperuser
