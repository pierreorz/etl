import 'virtual:windi-base.css';
import 'virtual:windi-components.css';
// 你自定义的 css
import './styles/main.css';

import 'virtual:windi-utilities.css';
import 'virtual:windi-devtools';

import App from './App.vue';
import Casdoor from 'casdoor-vue-sdk'

const config = {
  serverUrl: "http://119.45.37.204:8000", // Casdoor server URL
  clientId: "42c63fbfc6d4bd093b0c",
  organizationName: "built-in",
  appName: "app-built-in",
  redirectPath: "/callback",
};

const app = createApp(App);

app.use(Casdoor, config)

// 插件自动加载
const modules = import.meta.globEager('./modules/*.ts');
Object.values(modules).map((v) => {
  v.default?.(app);
});

app.mount('#app');
