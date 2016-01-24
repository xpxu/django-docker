DATABASE
========

数据表更改
----------
    change models.py
    python manage.py makemigrations
    python manage.py migrate

数据库导入
----------
eg.

    Blog.objects.create(title=title,content=content)
    Blog.objects.get_or_create(title=title,content=content) # 避免导入重复数据
