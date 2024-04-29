import { resolve } from 'path'
import Tov from './presets/tov'
import { defineConfig,loadEnv } from 'vite'


export default ({mode}) =>defineConfig({
	resolve: {
		alias: {
			'~/': `${resolve(__dirname, 'src')}/`
		}
	},
	
	plugins: [Tov()],
	  //add 配置，自动打开
	  
	server: {
	host: '0.0.0.0',
	port: 8081,
	open: true,
	proxy: {
		'/api': {
		target: loadEnv(mode, process.cwd()).VITE_PROXY_URL,
		
		changeOrigin: true,
		ws: true,
		rewrite: path => path.replace(/^\/api/, '')
			}
		}
	}
})
