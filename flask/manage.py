from mimetypes import init
from flask_script import Manager, Server
from app import app
from flask_migrate import Migrate
from db.exts import db
from models import Task,Instance # 模型文件必须导入进来，否则运行报错

manager = Manager(app)
Migrate(app=app, db=db)



if __name__ == '__main__':
    manager.run()