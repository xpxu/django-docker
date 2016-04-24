启动Django
----------
    python manage.py runserver 0.0.0.0:8080 # 使得外部浏览器可以通过8080端口访问django server
    
    
Django REST Framework
---------------------
    REST Framework有两种view： Class Based Views 和 Function Based Views。
    当使用Class Based Views时，是用url指定该class时要注意：
    For class-based view, you need to use the as_view method in your URL pattern:
        url(r'^$', home.as_view()),
