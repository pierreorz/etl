
from flask_sqlalchemy import SQLAlchemy
from flask_serialize import FlaskSerialize
from sqlalchemy.sql import func
from datetime import datetime

db = SQLAlchemy()


# 数据库连接配置表
class DBConfig(db.Model):
    __tablename__ = 'db_config_t'
    id = db.Column("ID",db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("NAME",db.String(250))    #名称
    host = db.Column("HOST",db.String(250))    #HOST
    port    =db.Column("PORT",db.String(250))   #PORT
    database=db.Column("DATABASE",db.String(250))   #目标数据库名
    username=db.Column("USERNAME",db.String(250))    #用户名
    password=db.Column("PASSWORD",db.String(250))     #密码
    schema=db.Column("SCHEMA",db.String(250))    #模式
    dbtype=db.Column("DBTYPE",db.String(250))    #类型
    source=db.Column("SOURCE",db.String(250))    #类型
    sink=db.Column("SINK",db.String(250))    #类型

   
class Jobs(db.Model):
    __tablename__='jobs_t'
    id = db.Column("id",db.Integer, primary_key=True, autoincrement=True)
    jobname = db.Column("job_name",db.String(255))    #任务名称
    jobid = db.Column("job_id",db.String(255))    #任务编号/flink返回的JOBID
    sourceconfigid=db.Column("source_config_id",db.Integer)   #源头端信息
    sinkconfigid=db.Column("sink_config_id",db.Integer)   #目标端信息
    source=db.Column("source",db.String(4000))    #source的flinksql
    sink=db.Column("sink",db.String(4000))     #sink的finksql
    connect=db.Column("connect",db.String(4000))    #组合flinksql
    isdeploy=db.Column("is_deploy",db.Boolean)    #是否提交到flink
    msg=db.Column("msg",db.String(4000))            #flink返回的错误信息
    createtime=db.Column("create_time",db.DateTime(timezone=True),default=datetime.now)    #创建时间 
    updatetime=db.Column("update_time",db.DateTime(timezone=True),default=datetime.now,onupdate=datetime.now)    #更新时间 


