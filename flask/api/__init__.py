
from flask import Blueprint
from flask_restful import Api


from .index import Index,FlinkConfig, UpdateDBConfig,DeleteDBConfig,CreateDBConfig,ListAllDBConfig,GetAllTask,QueryDBConfig,QueryTablesByConfig,SubmitFlinkJob,CreateJob,UpdateJob,DeleteJob,ListAllJobs,SignIn
from .account import Account
api_blueprint = Blueprint('api', __name__,url_prefix='/api')
api = Api(api_blueprint)

api.add_resource(Index, '/')
api.add_resource(GetAllTask,'/task/getall')
api.add_resource(FlinkConfig,'/flinkconfig')
api.add_resource(CreateDBConfig,'/dbconfig/create')
api.add_resource(UpdateDBConfig,'/dbconfig/update')
api.add_resource(DeleteDBConfig,'/dbconfig/delete')
api.add_resource(ListAllDBConfig,'/dbconfig/listall')
api.add_resource(QueryDBConfig,'/dbconfig/query')
api.add_resource(QueryTablesByConfig,'/dbconfig/tables')
api.add_resource(SubmitFlinkJob,'/flink/job/submit')

api.add_resource(CreateJob,'/job/create')
api.add_resource(UpdateJob,'/job/update')
api.add_resource(DeleteJob,'/job/delete')
api.add_resource(ListAllJobs,'/job/listall')

api.add_resource(SignIn, '/signin')
api.add_resource(Account, '/get-account')


