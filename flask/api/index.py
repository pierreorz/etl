
from flask_restful import Resource,request,reqparse
from flask import jsonify,session,current_app
from services import DBConfigService,JobService
from configparser import ConfigParser
import requests
from flask_restful import Resource, fields, marshal
import json

from casdoor import CasdoorSDK
 
class CreateJob(Resource):
    
    def post(self):
        try:
            params=request.get_json()
            # jobname=params.get("jobname")
            # jobid=params.get("jobid") 
            # sourceconfigid=params.get("sourceconfigid")
            # sinkconfigid=params.get("sinkconfigid") 
            # source=params.get("source") 
            # sink=params.get("sink") 
            # connect=params.get("connect") 
            # isdeploy=params.get("isdeploy") 
            # msg=params.get("msg") 
            ts=JobService()       
            result=ts.create(params)
            return jsonify(msg="ok",id=result.id)
        except Exception as e:
            print(e)
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)

##更新数据库连接配置
class UpdateJob(Resource):
    def post(self):
        try:
            params=request.get_json()
            ts=JobService()       
            result=ts.update(params)
            return jsonify(msg="ok",id=result.id)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)

#删除任务
class DeleteJob(Resource):
    def post(self):
        try:
            params=request.get_json()
            id=params.get("id")
            if id==None or id<0:
                return jsonify(msg="id is null")
            ts=JobService()       
            result=ts.delete({"id":id})    
            return result
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)


Job_fields = {
    'id': fields.Integer,
    'jobname': fields.String,
    'jobid': fields.String,
    'sourceconfigid': fields.Integer,
    'sinkconfigid':fields.Integer,
    'source':fields.String,
    'sink':fields.String,
    'connect':fields.String,
    'isdeploy':fields.Boolean,
    'msg':fields.String,
    'createtime':fields.DateTime,
    'updatetime':fields.DateTime
}
        
class ListAllJobs(Resource):
    def get(self):
        try:
            ts=JobService()       
            result=ts.listAll()
            return marshal(result,Job_fields)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)
        
        

##健康检查
class Index(Resource):
    def get(self):
        return jsonify({"msg": "ok"}) 

##获取flink运行的task状态
class GetAllTask(Resource):
    def get(self):
        config = ConfigParser()
        config.read('flinkconfig.ini')
        host=config.get('flink','host')   
        port=config.get('flink','Port')   
        try:
            resp=requests.get("http://"+host+":"+port+"/jobs")
            return resp.json()
        except Exception as e:
            pass    
            
##修改或者查询flink配置信息
class FlinkConfig(Resource):
    def post(self):
        params=request.get_json()
        host=str(params.get("host"))
        port=str(params.get("port"))
        config = ConfigParser()
        config.read('flinkconfig.ini')
        config.set("flink","host", host)   
        config.set("flink","port",  port)   
        status="未知"
        try:
            resp=requests.get("http://"+host+":"+port+"/jobs")
            if resp.status_code==200:
                status="正常"
        except Exception as e:
            status="异常"
            print(e)
        with open('flinkconfig.ini','w') as configfile:            
            config.write(configfile)
        return jsonify({"host": host,"port":port,"status":status})         

    def get(self):
        config = ConfigParser()
        config.read('flinkconfig.ini')
        status="未知"
        host=config.get('flink','host')   
        port=config.get('flink','Port')   
        try:
            resp=requests.get("http://"+host+":"+port+"/jobs")
            if resp.status_code==200:
                status="正常"
        except Exception as e:
            status="异常"        
        return jsonify({"host": host,"port":port,"status":status}) 
        
##创建数据库连接配置
class CreateDBConfig(Resource):
    def post(self):
        try:
            params=request.get_json()
            # name=params.get("name")
            # host=params.get("host") 
            # port=params.get("port")
            # database=params.get("database") 
            # username=params.get("username") 
            # password=params.get("username") 
            # schema=params.get("username") 
            ts=DBConfigService()       
            result=ts.create(params)
            return jsonify(msg="ok",id=result.id)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)

##更新数据库连接配置
class UpdateDBConfig(Resource):
    def post(self):
        try:
            params=request.get_json()
            ts=DBConfigService()       
            result=ts.update(params)
            return jsonify(msg="ok",id=result.id)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)

#删除任务
class DeleteDBConfig(Resource):
    def post(self):
        try:
            params=request.get_json()
            id=params.get("id")
            if id==None or id<0:
                return jsonify(msg="id is null")
            ts=DBConfigService()       
            result=ts.delete({"id":id})    
            return result
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)


DBConfig_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'host': fields.String,
    'port': fields.String,
    'database':fields.String,
    'username':fields.String,
    'password':fields.String,
    'schema':fields.String,
    'dbtype':fields.String,
    'source':fields.String,
    'sink':fields.String
}
        
class ListAllDBConfig(Resource):
    def get(self):
        try:
            ts=DBConfigService()       
            result=ts.listAll()
            return marshal(result,DBConfig_fields)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)


##根据参数查询
class QueryDBConfig(Resource):
    def get(self):
        try:
            key=request.args.get("key")
            ts=DBConfigService()       
            result=ts.queryByKey(key)
            return marshal(result,DBConfig_fields)
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return jsonify(msg=errmsg)
        
##查询表名
class QueryTablesByConfig(Resource):
    def get(self):
        try:
            key=request.args.get("id")
            ts=DBConfigService()       
            result=ts.getTablesByConfig(key)
            return [{"id":index,"name":i[0]} for index,i in enumerate(result)]
        except Exception as e:
            errmsg=f"Error,e:{e}"
            return {}

##提交任务到flink
class SubmitFlinkJob(Resource):
    def post(self):
        try:
            ##todo 可通过配置参数拼出来URL
            url="http://172.16.7.170:8081/jars/d6796b75-e7ef-4a97-8b3f-3ff00a043402_flinkjob-0.0.1-SNAPSHOT.jar/run?entry-class=org.springframework.boot.loader.JarLauncher"
            resp=requests.post(url)
            return {"result":"ok"}
        except Exception as e:
            return {"result":str(e)}
        
def parse_error(json_string):
    if 'error_description' not in json_string:
        return None, None

    try:
        data = json.loads(json_string)
        error = data.get('error', None)
        error_description = data.get('error_description', None)
        return error, error_description
    except json.JSONDecodeError:
        return "JSONDecodeError", f"the input is not valid JSON:{json_string}"
            
class SignIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('code', required=True, location='args')
        parser.add_argument('state', required=True, location='args')
        args = parser.parse_args()
        code = args['code']
        state = args['state']

        sdk: CasdoorSDK = current_app.config.get('CASDOOR_SDK')
        token = sdk.get_oauth_token(code)
        err, error_description = parse_error(str(token))
        if err is not None:
            return jsonify({'status': 'error', 'msg': f"{err}: {error_description}"})

        user = sdk.parse_jwt_token(token['access_token'])
        session['casdoorUser'] = user
        

        return jsonify({'status': 'ok','user':user})