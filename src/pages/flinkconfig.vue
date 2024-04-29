<template>
  <div style="display: flex;">

  <el-card style="max-width: 500px;margin: 10px;">
    <template #header style="font-weight: bold;
    margin: auto;
    width: 100%;">flink配置<div> <div class="flex gap-2 mt-4">
      <el-tag  :type="tableForm.status === '正常'?'success':'danger'" >{{ tableForm.status }}</el-tag>
      <el-tag v-if="tableForm.host">{{ tableForm.host }}</el-tag>
      <el-tag>{{tableForm.port}}</el-tag>
  </div></div></template>
    <img
      src="/img/flink.png" style="max-height: 100px;
    max-width: 200px;"    
    />
    <el-button type="primary" :icon="Edit" style="width:100%;" @click="editBtn()"  />
  </el-card>
</div>
<el-dialog
      v-model="dialogFormVisible"
      title="配置flink环境信息"
    >
      <el-form :model="tableForm">

        <el-form-item label="flink服务器IP" :label-width="250">
          <el-input v-model="tableForm.host" autocomplete="off" />
        </el-form-item>
        <el-form-item label="flink服务器端口号" :label-width="250">
          <el-input v-model="tableForm.port" autocomplete="off" />
        </el-form-item>
       
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="dialogConfirm"> 确认 </el-button>
        </span>
      </template>
    </el-dialog>
</template>

<script lang="ts" setup>
import {
  Edit
} from '@element-plus/icons-vue';
import {getFlinkConfig, updateFlinkConfig} from '~/api/test'

const dialogFormVisible = ref(false);
const editBtn = () => {
  dialogFormVisible.value = true;
};
interface FlinkConfig{
  host: string,
  port: string,
  status: string
}
const tableForm = reactive({
    host: '',
    port: '',
    status: '',
  });
  const result=getFlinkConfig().data
  watch(result, () => {
    tableForm.host=result.value.host
    tableForm.port=result.value.port
    tableForm.status=result.value.status
    });

const dialogConfirm=()=>{
  const {data} = updateFlinkConfig({
      host: tableForm.host,
      port: tableForm.port
    });
  dialogFormVisible.value = false;
  watch(data, () => {
    tableForm.host=data.value.host
    tableForm.port=data.value.port
    tableForm.status=data.value.status
    });
}

</script>