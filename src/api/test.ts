import { useRequest } from 'vue-request';
import { ElNotification } from 'element-plus';
const reload: any = inject('reload');

//获取flink运行的所有任务列表
export const getAllTask = () => {
  const { data, loading, error,run } = useRequest({
    url: '/api/task/getall',
    method: 'get'
  });
  run();
  return { data, loading, error };
};

//更新flink服务器配置
export const updateFlinkConfig = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/flinkconfig',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};
 
//获取flink服务器配置
export const getFlinkConfig = () => {
  const { data,run} = useRequest({
    url: '/api/flinkconfig',
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  });
  run();
  return { data};
};

//添加数据库连接信息
export const AddDBConfig = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/dbconfig/create',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};

//查询数据库连接信息列表
export const ListAllDBConfig = () => {
  const { data,run} = useRequest({
    url: '/api/dbconfig/listall',
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  });
  run();
  return { data};
};


//更新数据库连接信息
export const UpdateDBConfig = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/dbconfig/update',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};

//删除数据库连接信息
export const DeleteDBConfig = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/dbconfig/delete',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};



//查询源头端DB连接列表
export const GetDBConfigList = (key:string) => {
  const { data,run} = useRequest({
    url: '/api/dbconfig/query?key='+key,
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  });
  run();
  return { data};
};

//查询表名列表
export const GetTableNameList = (id:string) => {
  const { data,run} = useRequest({
    url: '/api/dbconfig/tables?id='+id,
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  });
  run();
  return { data};
};

//flink job submit
export const SubmitFlinkJob = () => {
  const { data, run } = useRequest(() => ({
    url: '/api/flink/job/submit',
    method: 'post',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run();
  return { data };
};


//job 


//添加Job
export const AddJob = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/job/create',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};

//查询所有Jobs
export const ListAllJobs = () => {
  const { data,run} = useRequest({
    url: '/api/job/listall',
    method: 'get',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  });
  run();
  return { data};
};


//更新Job信息
export const UpdateJob = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/job/update',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};

//删除Job
export const DeleteJob = (x: any) => {
  const { data, run } = useRequest((data) => ({
    url: '/api/job/delete',
    method: 'post',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    }
  }));
  run(x);
  return { data };
};

//获取flink运行的所有任务列表
export const getAllInstance = () => {
  const { data, loading, error,run } = useRequest({
    url: '/api/task/getall',
    method: 'get'
  });
  run();
  return { data, loading, error };
};