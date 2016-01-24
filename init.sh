# 初始化数据库，并启动django server

rm db/blog.db
python manage.py makemigrations
python manage.py migrate --database=essaydb
python manage.py migrate --database=userdb
python userApp.data2db.py
python publicationApp.data2db.py
python essayApp.data2db.py
python manage.py runserver 0.0.0.0:8080
