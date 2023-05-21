# stu_helper
毕设-校园助手微信小程序项目后端
基于 ```python3.8``` 和 ```Django4.0```的校园助手微信小程序
## 主要功能
部分功能前端实现
- 成绩查询
- 课表查询
- 选课查询
- 空教室查询
- 考试信息查询
- 图书借阅信息查询
- 校历
- 校园地图
- 校园通讯
## 项目配置
### 配置python运行环境
- 在windows终端中运行以下命令
```
pip install -r requirements.txt
```
- 修改stu_helper/stu_helper/settings.py, 修改数据库配置
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "stu_helper",
        "USER": "数据库用户名",
        "PASSWORD": "连接密码",
        "HOST": "127.0.0.1",
        "PORT": "端口号",
    }
}
```
### 创建数据库
- 连接Mysql数据库，执行如下命令创建数据库
```shell
CREATE DATABASE `stu_helper` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
```
- 在项目根目录下打开终端，执行如下命令，执行数据库迁移命令
```shell
python manage.py makemigrations
python manage.py migrate
```
### 创建超级用户
- 终端下执行:
```shell
python manage.py createsuperuser
```