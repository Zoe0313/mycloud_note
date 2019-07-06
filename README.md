# 我的云笔记
### 一对多案例, 实现网络云笔记
- 功能:
  - 应用 user 实现如下功能:
    1. 注册
    2. 登陆
    3. 退出登陆
  - 应用 note 实现如下功能:
    1. 发表笔记
    2. 显示笔记列表
    3. 修改笔记
    4. 删除笔记
    
- 项目名称:  **mycloud_notebook**
```shell
  django-admin startproject mycloud_notebook
```

- 创建两个app:
```shell
  python3 manage.py startapp note
  python3 manage.py startapp user
```

- 在settings.py 中注册两个应用
  - 添加子路由
    - 添在 user/urls.py 写入子路由的内容
      ```python   
       from django.conf.urls import url
       urlpatterns = []
      ```
    - 添加 note/urls.py 写入子路由的内容(同上)          
    - 将子路由添加到主路由mycloud_notebook/urls.py中
    - 在主路由中加入主页，对应视图函数views.index
      ```python   
         # 在主包文件内添加一个views.py 写入
            def index(request):
      ```
      
- 添加模板文件夹
    - mycloud_notebook/templates
    - mycloud_notebook/templates/note
    - mycloud_notebook/templates/user
      
- 在 settings.py 添加模板文件夹
- 在 mycloud_notebook/templates创建 index.html
  写入主页的模板文件
    
- 添加模型类
    - user/models.py 里创建User:
        ```python   
        class User(models.Model)
        ```
    - note/models.py 里创建Note:
        ```python  
        class Note(models.Model)
        ```
    - 数据库名：　mynote
        ```mysql
        create database mynote default charset utf8 collate utf8_general_ci;
        ```
    - 修改settings.py 加入数据库支持
        ```python  
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'mynote',  # 数据库名称
                'USER': 'root',
                'PASSWORD': '123456',  # 管理员密码
                'HOST': '127.0.0.1',
                'PORT': 3306,
            }
        }
        ```
    - 修改 __init__.py 加入:
         ```python  
         import pymysql
         pymysql.install_as_MySQLdb()
         ```

- 迁移操作
    ```shell
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

- 创建后台管理员账号
    ```shell
    python3 manage.py createsuperuser
    ```
    用 后台管理员 直接操作User表和Note表添加一些假数据做测试用
    
  
  在note/admin.py 加入Note模型的支持
    ```python
    from . import models
    admin.site.register(models.Note)
    ```
  在user/admin.py 加入User模型的支持
    ```python
    from . import models
    admin.site.register(models.User)
    ```