<template>
  <div class="m-10 flex justify-between w-100">
    <el-input v-model="search" placeholder="输入关键字查询 " />
  </div>

  <div>
    <el-table
      :data="tData.jobs?.filter(
          (data) =>
            !search || data.id.toLowerCase().includes(search.toLowerCase())
        )">
      <el-table-column prop="id" label="任务ID" width="300" />
      <el-table-column prop="status" label="任务状态" width="200" >
        <template #default="scope">
         
          <el-tag :type="scope.row.status==='RUNNING'?'success':''">{{ scope.row.status }}</el-tag>

          </template>

        </el-table-column>
      <el-table-column fixed="right" label="操作" width="120">
        <template #default="scope">
          <el-link type="primary" :href="url" target="_blank">查看详情</el-link>
          </template></el-table-column>

    </el-table>

 

  </div>
</template>

<script lang="ts" setup>

import {getAllTask,getFlinkConfig} from '~/api/test';

const search = ref('');

const tData=reactive({jobs:[{id:'',status:''}]})
 
const tableData = getAllTask().data

watch(tableData, () => {
    tData.jobs=tableData.value.jobs
});

const reload: any = inject('reload');
const tableForm = reactive({
    host: '',
    port: '',
    status: '',
  });

const url=ref("")

const result=getFlinkConfig().data

watch(result, () => {
    url.value="http://"+result.value.host+":"+result.value.port
    console.log(url)
});





</script>
