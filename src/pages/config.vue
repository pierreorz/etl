<template>
  <div style="display: flex">
    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >MySQL</template
      >
      <img src="/img/mysql.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('mysql')"
      />
    </el-card>

    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >Postgres</template
      >
      <img src="/img/pg.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('postgres')"
      />
    </el-card>

    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >Oracle</template
      >
      <img src="/img/oracle.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('oracle')"
      />
    </el-card>

    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >Kafka</template
      >
      <img src="/img/kafka.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('kafka')"
      />
    </el-card>

    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >Redis</template
      >
      <img src="/img/redis.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('redis')"
      />
    </el-card>

    <el-card style="max-width: 150px; margin: 10px">
      <template #header style="font-weight: bold; margin: auto; width: 100px"
        >MariaDB</template
      >
      <img src="/img/mariadb.png" style="max-height: 100px; max-width: 200px" />
      <el-button
        type="primary"
        :icon="DocumentAdd"
        style="width: 100px"
        @click="AddBtn('mariadb')"
      />
    </el-card>
  </div>

  <!-- POPUP弹窗 -->

  <el-dialog v-model="dialogFormVisible" title="连接配置">
    <el-form :model="tableForm">
      <el-form-item
        label="ID"
        :label-width="250"
        v-if="dialogType === 'add' ? false : true"
      >
        <el-input v-model="tableForm.id" autocomplete="off" disabled />
      </el-form-item>
      <el-form-item label="连接名称" :label-width="250">
        <el-input v-model="tableForm.name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="连接类型" :label-width="250">
        <el-checkbox v-model="tableForm.source" :checked="tableForm.source==='true'?true:false" label="源头端" size="large" />
        <el-checkbox v-model="tableForm.sink"  :checked="tableForm.sink==='true'?true:false" label="目标端" size="large" />
      </el-form-item>
   
      <el-form-item label="HOST" :label-width="250">
        <el-input v-model="tableForm.host" autocomplete="off" />
      </el-form-item>
      <el-form-item label="PORT" :label-width="250">
        <el-input v-model="tableForm.port" autocomplete="off" />
      </el-form-item>
      <el-form-item label="数据库名(ServiceName)" :label-width="250">
        <el-input v-model="tableForm.database" autocomplete="off" />
      </el-form-item>
      <el-form-item label="用户名" :label-width="250">
        <el-input v-model="tableForm.username" autocomplete="off" />
      </el-form-item>
      <el-form-item label="密码" :label-width="250">
        <el-input v-model="tableForm.password" autocomplete="off" />
      </el-form-item>
      <el-form-item label="模式名" :label-width="250">
        <el-input v-model="tableForm.schema" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="dialogConfirm"> 确认 </el-button>
      </span>
    </template>
  </el-dialog>

  <!-- 查询表格-->
  <div class="m-10 flex justify-between w-100">
    <el-input v-model="search" placeholder="输入关键字查询 " />
  </div>

  <el-table
    :data="
      tData?.filter(
        (data) =>
          !search || data.id.toLowerCase().includes(search.toLowerCase())
      )
    "
  >
    <el-table-column prop="id" label="ID" width="100" />
    <el-table-column prop="dbtype" label="数据库类型" width="200" >
      <template #default="scope">
         
         <el-tag :type="scope.row.dbtype==='RUNNING'?'success':''">{{ scope.row.dbtype }}</el-tag>

         </template>
      </el-table-column>
      <el-table-column   label="连接类型" width="200" >
        <template #default="scope">
         
         <el-tag :type="scope.row.source==='true'?'success':''" v-if="scope.row.source==='true'?true:false">源头端</el-tag>
         <el-tag :type="scope.row.sink==='true'?'success':''" v-if="scope.row.sink==='true'?true:false">目标端</el-tag>
         </template>
      </el-table-column>

    <el-table-column prop="name" label="连接名称" width="200" />
    <el-table-column prop="host" label="HOST" width="200" />
    <el-table-column prop="port" label="PORT" width="200" />
    <el-table-column prop="database" label="数据库名" width="200" />
    <el-table-column prop="username" label="用户名" width="200" />
    <el-table-column prop="password" label="密码" width="200" />
    <el-table-column prop="schema" label="模式" width="200" />
    <el-table-column fixed="right" label="操作" width="120">
      <template #default="scope">
        <el-button
            :icon="Edit"
            size="large"
            @click="editBtn(scope.$index, scope.row)"
            link
          />
          <el-button
            :icon="Delete" 
            size="large"
            @click="deleteBtn(scope.$index, scope.row)"
            link
          />
      </template></el-table-column
    >
  </el-table>
</template>

<script lang="ts" setup>
import { DocumentAdd,Edit,Delete } from "@element-plus/icons-vue";
import { AddDBConfig, DeleteDBConfig, ListAllDBConfig,UpdateDBConfig } from "~/api/test";

const reload: any = inject('reload');

const search = ref("");
const dialogFormVisible = ref(false);
const dialogType = ref("");

interface DBConfig {
  id: string,
  name: string,
  host: string,
  port: string,
  database: string,
  username: string,
  password: string,
  schema: string,
  dbtype:string,
  source:string,
  sink:string
}

const tableForm = reactive({
  id: "",
  name: "",
  host: "",
  port: "",
  database: "",
  username: "",
  password: "",
  schema: "",
  dbtype:"",
  source:"",
  sink:""
});
function setValues(newValues: any) {
  Object.assign(tableForm, newValues);
}



const AddBtn = (type: any) => {
  setValues({
    id: "",
    name: "",
    host: "",
    port: "",
    database: "",
    username: "",
    password: "",
    schema: "",
    dbtype:type,
    source:"",
    sink:""
  });
  dialogFormVisible.value = true;
  dialogType.value = "add";
};

const editBtn = (index: number, row: DBConfig) => {
  dialogType.value = 'edit';
  dialogFormVisible.value = true;

  tableForm.id = row.id;
  tableForm.name = row.name;
  tableForm.host = row.host;
  tableForm.port = row.port;
  tableForm.database = row.database;
  tableForm.username = row.username;
  tableForm.password = row.password;
  tableForm.schema = row.schema;
  tableForm.dbtype= row.dbtype;
  tableForm.source = row.source;
  tableForm.sink = row.sink;
};

const deleteBtn = (index:number,row:DBConfig) => {
  const {data} = DeleteDBConfig({id:row.id});
  watch(data, () => {
      reload();
    });
};

const dialogConfirm = (type: any) => {
  dialogFormVisible.value = false;
  if (dialogType.value==='add'){
    const { data } = AddDBConfig({
      name: tableForm.name,
      host: tableForm.host,
      port: tableForm.port,
      database: tableForm.database,
      username: tableForm.username,
      password: tableForm.password,
      schema: tableForm.schema,
      dbtype:tableForm.dbtype,
      source:tableForm.source,
      sink:tableForm.sink
    });
    watch(data, () => {
      reload();
    });
  }

  if (dialogType.value==='edit'){
    const { data } = UpdateDBConfig({
      id:tableForm.id,
      name: tableForm.name,
      host: tableForm.host,
      port: tableForm.port,
      database: tableForm.database,
      username: tableForm.username,
      password: tableForm.password,
      schema: tableForm.schema,
      dbtype:tableForm.dbtype,
      source:tableForm.source,
      sink:tableForm.sink
    });
    watch(data, () => {
      reload();
    });
  }


};

// 查询表格

const tData = ListAllDBConfig().data;
watch(tData, () => {
});
</script>
