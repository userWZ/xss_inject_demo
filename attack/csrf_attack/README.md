# 攻撃方法

First, run ``python manage.py runserver`` to run the target website on localhost port 8000.
Then run the command below.

```
$ cd csrf_attack/
$ python -m http.server 8080
```

http://localhost:8080 The attack is complete when you access .