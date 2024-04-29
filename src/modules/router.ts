import { App } from 'vue'
import generatedRoutes from 'virtual:generated-pages'
import { setupLayouts } from 'virtual:generated-layouts'
import { createRouter, createWebHistory } from 'vue-router'
import { routerGuard } from './permissions'
const routes = setupLayouts(generatedRoutes)

export const router = createRouter({
	routes,
	history: createWebHistory()
})


router.beforeEach(routerGuard)


export default (app: App) => app.use(router)
