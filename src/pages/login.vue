<template>
  <div>
  </div>

</template>

<script setup>
  import { onMounted, getCurrentInstance } from 'vue'


  onMounted(() => {
    let instance=getCurrentInstance();
    window.location.href = instance.proxy.getSigninUrl();
    
  });
</script>