import axios from 'axios'
import { ElMessage } from 'element-plus'
import { localGet } from '.'




// import { loadEnv,mode,process } from 'vite'

// // 这边由于后端没有区分测试和正式，姑且都写成一个接口。
// axios.defaults.baseURL = loadEnv(mode, process.cwd()).VITE_APP_NAME.baseUrl
// 携带 cookie，对目前的项目没有什么作用，因为我们是 token 鉴权
axios.defaults.withCredentials = true
// 请求头，headers 信息
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers.common['token'] = localGet('token') || ''
// 默认 post 请求，使用 application/json 形式
axios.defaults.headers.post['Content-Type'] = 'application/json'

// 请求拦截器，内部根据返回值，重新组装，统一管理。
axios.interceptors.response.use((res:any) => {
  if (typeof res.data !== 'object') {
    ElMessage.error('服务端异常！')
    return Promise.reject(res)
  }
  if (res.data.resultCode != 200) {
    if (res.data.message) ElMessage.error(res.data.message)
    if (res.data.resultCode == 419) {
      console.log('router add')
    }
    return Promise.reject(res.data)
  }

  return res.data.data
})

export default axios