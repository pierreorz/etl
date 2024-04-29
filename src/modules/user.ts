import {defineStore} from 'pinia'
import {useStorage} from '@vueuse/core'
import {ref, reactive, onMounted} from 'vue'

 const serverLoginAPI="http://localhost:5000"
 

export const useUserStore= defineStore('user',{
    state: ()=>({
        isLogin: false,
        userInfo: {}     
    }),persist:{
        enabled: true
    }
});