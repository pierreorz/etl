
<template>
    <h1>Callback</h1>
  </template>

<script setup>
import { onMounted, getCurrentInstance } from 'vue'
import {CasdoorSDK} from 'casdoor-vue-sdk'
import { useUserStore } from '~/modules/user'
function login() {
  const instance = getCurrentInstance()
  instance.proxy.signin('http://localhost:5000/').then((res) => {
    if (res.status === 'ok') {
      // alert('Login success')
      // if (inIframe()) {
      //   const message = {tag: "Casdoor", type: "SilentSignin", data: "success"};
      //   window.parent.postMessage(message, "*");
      // }
     sessionStorage.setItem("casdoorUser",JSON.stringify(res.user));
     sessionStorage.setItem("isLogin","true");
     window.location.href = '/config'
     
    } else {
      alert(`Login failed: ${res.msg}`)
      window.location.href = '/login'
    }
  })
}

function inIframe() {
  try {
    return window !== window.parent;
  } catch (e) {
    return true;
  }
}

onMounted(() => {
  login()
})
</script>
