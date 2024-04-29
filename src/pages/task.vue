<template>
  <el-row>
    <el-col :span="24" style="margin: 20px;">

    
    </el-col>
    
    </el-row>
  <el-row >
    <el-col :span="5" >
      <div class="m-4">
        <el-select
          @change="sourceDBchange"
          v-model="s_selected"
          value-key="id"
          placeholder="Select"
          style="width: 240px"
        >
          <el-option
            v-for="item in s_items"
            :key="item.id"
            :label="item.name"
            :value="item"
          />
        </el-select>
        <p>
          源头端数据库连接信息:
          <b style="color: red"> {{ s_selected.name }} </b>
        </p>
      </div>
 
    </el-col>
    <el-col :span="5" >
      <div class="m-4">
        <el-select
          v-model="st_selected"
          value-key="id"
          placeholder="Select"
          style="width: 240px"
        >
          <el-option
            v-for="item in st_items"
            :key="item.id"
            :label="item.name"
            :value="item"
          />
        </el-select>
        <p>
          源头端数据表名:
          <b style="color: red"> {{ st_selected.name }} </b>
        </p>
      </div>
    </el-col>
    <el-col :span="2">  <span>Source:</span></el-col>
      <el-col :span="12" >
      <el-input
        v-model="s_fsql"
        style="height:200px;width: 800px;margin:5px;"
        type="textarea"
        placeholder="select * from table"
      />
    </el-col>
</el-row>

 

  <el-row>
    <el-col :span="5" >
    
  <div class="m-4">
    <el-select
      v-model="k_selected"
      @change="sinkDBchange"
      value-key="id"
      placeholder="Select"
      style="width: 240px"
    >
      <el-option
        v-for="item in k_items"
        :key="item.id"
        :label="item.name"
        :value="item"
      />
    </el-select>
    <p>
      目标端数据库连接信息:
      <b style="color: red"> {{ k_selected.name }} </b>
    </p>
  </div>
  </el-col>
  <el-col :span="5" >
  <div class="m-4">
    <el-select
      v-model="kt_selected"
      value-key="id"
      placeholder="Select"
      style="width: 240px"
    >
      <el-option
        v-for="item in kt_items"
        :key="item.id"
        :label="item.name"
        :value="item"
      />
    </el-select>
    <p>
      目标端数据表名:
      <b style="color: red"> {{ kt_selected.name }} </b>
    </p>
  </div>
</el-col>
<el-col :span="2">  <span>Sink:</span></el-col>
<el-col :span="12" >
  <!--目标端flink sql-->
  <el-input
    v-model="k_fsql"
    style="height: 200px;width: 800px;margin:5px;"
    type="textarea"
    placeholder="select * from table"
  />
  </el-col>
</el-row>
<el-row>
  <el-col :span="10">
    <div> 
    <span>任务名称:</span>
      <el-input
        v-model="jobname"
        style="width: 500px;"
        type="input" 
        placeholder="任务名称"
      /></div>
  </el-col>
  <el-col :span="2">  <span>Connect:</span></el-col>
<el-col :span="12" >
  <el-input
    v-model="c_fsql"
    style="height: 200px;width: 800px;margin:5px;"
    type="textarea"
    placeholder="select * from table"
  />
</el-col>
</el-row>
<el-row style="margin:10px;">
  <!-- 查询表格-->

   
    <el-col :span="6" >
    <el-input v-model="search" placeholder="输入关键字查询 " />
  </el-col>
  <el-col :span="12" >
    <el-button type="primary" @click="submitFlinkJob">
      保存并提交任务到flink<el-icon class="el-icon--right"><Upload /></el-icon>
    </el-button>
    </el-col>
    <el-col :span="6" >
    <el-link style="text-wrap: nowrap;color:red;">{{ processMsg }}</el-link>
     </el-col>
 
</el-row>
  <el-table
    :data="
      tData?.filter(
        (tData) =>
          !search || tData.jobname.toLowerCase().includes(search.toLowerCase())
      )
    "
  >
    <el-table-column prop="id" label="ID" width="100" />
    <el-table-column prop="jobname" label="任务名称" width="200" />
    <el-table-column prop="jobid" label="任务编号" width="200" />
    <el-table-column
      prop="source"
      label="Source"
      width="200"
      style="white-space: nowrap; text-wrap: nowrap"
    />
    <el-table-column
      prop="sink"
      label="Sink"
      width="200"
      style="white-space: nowrap; text-wrap: nowrap"
    />
    <el-table-column
      prop="connect"
      label="Connect"
      width="200"
      style="white-space: nowrap; text-wrap: nowrap"
    />
    <el-table-column prop="sourceconfig" label="源头端名称" width="200" />
    <el-table-column prop="sinkconfig" label="目标端名称" width="200" />
    <el-table-column prop="isdeploy" label="是否提交flink" width="200" />
    <el-table-column
      prop="msg"
      label="flink返回错误信息"
      width="200"
      style="white-space: nowrap; text-wrap: nowrap"
    />
    <el-table-column prop="createtime" label="创建时间" width="200" />
    <el-table-column prop="updatetime" label="更新时间" width="200" />

    <el-table-column fixed="right" label="操作" width="120">
      <template #default="scope">
        <el-button
          :icon="Edit"
          size="large"
          @click="editBtn(scope.$index)"
          link
        />
        <el-button
          :icon="Delete"
          disabled
          size="large"
          @click="deleteBtn(scope.$index)"
          link
        /> </template
    ></el-table-column>
  </el-table>

  <!--todo5end -->
</template>

<script lang="ts" setup>
import { Upload, Delete, Edit } from "@element-plus/icons-vue";
import {
  GetDBConfigList,
  GetTableNameList,
  SubmitFlinkJob,
  ListAllJobs,
  AddJob,
} from "~/api/test";

const reload: any = inject("reload");

const jobname = ref("同步任务");
const handleChange = (val: string[]) => {
  console.log(val);
};

const s_selected = ref("");
const st_selected = ref("");
const k_selected = ref("");
const kt_selected = ref("");
const s_fsql = ref("create table if not exists test (\n        `id` int,\n        primary key(`id`) not enforced\n        ) with(\n         \'connector\' = \'mysql-cdc\',\n \'hostname\' = \'172.16.7.170\',\n \'port\' = \'3306\',\n \'username\' = \'root\',\n \'password\' = \'root\',\n \'database-name\' = \'opsli-boot\',\n \'table-name\' = \'test\',\n \'scan.incremental.snapshot.enabled\' = \'false\'\n)");
const k_fsql = ref("create table if not exists test1 (\n   `id` int,\n   primary key(`id`) not enforced\n) with(\n \'connector\' = \'jdbc\',\n \'url\' = \'jdbc:mysql://172.16.7.170:3306/opsli-boot\',\n \'username\' = \'root\',\n \'password\' = \'root\',\n \'table-name\' = \'test1\'\n)");
const c_fsql = ref("insert into test1 select * from test ");
const st_items = ref([]);
const s_items = ref([]);
const kt_items = ref([]);
const k_items = ref([]);
const search = ref("");
const processMsg = ref("");

const sourceDBchange = () => {
  st_items.value = [];
  //获取表名列表,并监听接口返回后赋值给下拉框
  const tablelist = GetTableNameList(s_selected.value.id).data;
  watch(tablelist, () => {
    st_items.value = tablelist.value;
  });
};

const sinkDBchange = () => {
  st_items.value = [];
  //获取表名列表,并监听接口返回后赋值给下拉框
  const tablelist = GetTableNameList(k_selected.value.id).data;
  watch(tablelist, () => {
    kt_items.value = tablelist.value;
  });
};

//请求DB连接信息,并监听接口返回给下拉框
onMounted(() => {
  const result = GetDBConfigList("source").data;
  const sinkResult = GetDBConfigList("sink").data;

  watch(result, () => {
    s_items.value = result.value;
  });

  watch(sinkResult, () => {
    k_items.value = sinkResult.value;
  });
});
//保存任务内容,并提交到flink
const submitFlinkJob = () => {
  processMsg.value = "已提交,处理中......";
  //保存到DB
  const { data } = AddJob({
    jobname:jobname.value,
    sourceconfigid:s_selected.value.id,
    sinkconfigid:k_selected.value.id,
    source:s_fsql.value,
    sink:k_fsql.value,
    connect:c_fsql.value
  });
  watch(data,()=>{
    processMsg.value = "保存任务成功,开始提交flink......";
  })
 
  //调用flink提交job接口
  const result = SubmitFlinkJob().data;
  processMsg.value = "已提交flink,等待返回结果中......";
  //刷新主表数据
  watch(result, () => {
    console.log(result.value.result);
    reload();
    if(result.value.result ==='ok'){
      processMsg.value = "已完成,请进任务状态页查看执行状态......";
    }else{
      processMsg.value = result.value.result;
    }
    
  });
 
};

const editBtn = (index: number) => {};

const deleteBtn = (index: number) => {};

const tData = ListAllJobs().data;
</script>
