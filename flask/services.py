from models import db,DBConfig,Jobs
from sqlalchemy import  text
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class JobService:
    def create(self,config):
        new=Jobs()
        new.id=config.get("id")
        new.jobname=config.get("jobname")
        new.jobid=config.get("jobid")
        new.sourceconfigid=config.get("sourceconfigid")
        new.sinkconfigid=config.get("sinkconfigid")
        new.source=config.get("source")
        new.sink=config.get("sink")
        new.connect=config.get("connect")
        new.isdeploy=config.get("isdeploy")
        new.msg=config.get("msg")
        db.session.add(new)
        db.session.commit()
        return new
    
    def update(self,config):
        modified=Jobs.query.get(config.get("id"))
        modified.jobname=config.get("jobname")
        modified.jobid=config.get("jobid")
        modified.sourceconfigid=config.get("sourceconfigid")
        modified.sinkconfigid=config.get("sinkconfigid")
        modified.source=config.get("source")
        modified.sink=config.get("sink")
        modified.connect=config.get("connect")
        modified.isdeploy=config.get("isdeploy")
        modified.msg=config.get("msg")
        db.session.commit()
        return modified

    def delete(self,config):
        deleted=Jobs.query.get(config.get("id"))
        db.session.delete(deleted)
        db.session.commit()
        return True
    
    def listAll(self):
        sql=text("select * from jobs_v")
        result=db.session.execute(sql).fetchall()
        return result
    
    def getOne(self,id):
        return Jobs.query.get(id)



class DBConfigService:
    def create(self,config):
        newConfig=DBConfig()
        newConfig.id=config.get("id")
        newConfig.name=config.get("name")
        newConfig.host=config.get("host")
        newConfig.port=config.get("port")
        newConfig.database=config.get("database")
        newConfig.username=config.get("username")
        newConfig.password=config.get("password")
        newConfig.schema=config.get("schema")
        newConfig.dbtype=config.get("dbtype")
        newConfig.source=config.get("source")
        newConfig.sink=config.get("sink")
        db.session.add(newConfig)
        db.session.commit()
        return newConfig
    
    def update(self,config):
        modified=DBConfig.query.get(config.get("id"))
        modified.name=config.get("name")
        modified.host=config.get("host")
        modified.port=config.get("port")
        modified.database=config.get("database")
        modified.username=config.get("username")
        modified.password=config.get("password")
        modified.schema=config.get("schema")
        modified.dbtype=config.get("dbtype")
        modified.source=config.get("source")
        modified.sink=config.get("sink")
        db.session.commit()
        return modified

    def delete(self,config):
        deleted=DBConfig.query.get(config.get("id"))
        db.session.delete(deleted)
        db.session.commit()
        return True
    
    def listAll(self):
        return DBConfig.query.order_by(DBConfig.id).all()
    
    def queryByKey(self,key):
        if key=="source":
            return DBConfig.query.filter(DBConfig.source=='true').order_by(DBConfig.id).all()
        if key=="sink":
            return DBConfig.query.filter(DBConfig.sink=='true').order_by(DBConfig.id).all()

    def getOne(self,id):
        return DBConfig.query.get(id)
    
    ##根据连接信息查询所有表名
    def getTablesByConfig(self,id):
        config:DBConfig=DBConfig.query.get(id)
        if config.dbtype=="mysql":
            return self.getMysqlTable(config)
        if config.dbtype=="postgres":
            return self.getPostgresTable(config)
        if config.dbtype=="oracle":
            return self.getOracleTable(config)


    def getMysqlTable(self,config:DBConfig):
        engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(config.username, config.password,config.host, config.database)) 
        with engine.connect() as conn:
            stmt = text("select concat(table_schema,'.',table_name) as table_name from information_schema.tables where table_schema = :table_schema")
            stmt=stmt.bindparams(table_schema=config.database)
            return conn.execute(stmt).fetchall()
    
    def getPostgresTable(self,config:DBConfig):
        engine = create_engine("postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}".format(username=config.username, password=config.password,hostname=config.host,port=config.port,db= config.database)) 
        with engine.connect() as conn:
            if len(config.schema)>0:
                stmt = text("select concat(table_schema,'.',table_name) as table_name from information_schema.tables where table_catalog=:table_catalog and table_schema = :table_schema")
                
                stmt=stmt.bindparams(table_catalog=config.database,table_schema=config.schema)
                return conn.execute(stmt).fetchall()
            else:
                stmt = text("select concat(table_schema,'.',table_name) as table_name from information_schema.tables where table_catalog=:table_catalog ")
                stmt=stmt.bindparams(table_catalog=config.database)
                return conn.execute(stmt).fetchall()
    
    def getOracleTable(self,config:DBConfig):
        engine = create_engine('oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{service_name}'.format(username=config.username, password=config.password, host=config.host,port=config.port,service_name=config.database)) 
        with engine.connect() as conn:
            stmt = text("SELECT table_name FROM user_tables")
            return conn.execute(stmt).fetchall()
    
    



    