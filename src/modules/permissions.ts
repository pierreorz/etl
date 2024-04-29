import type { RouteLocationNormalized,NavigationGuardNext } from "vue-router";
import { useUserStore } from "./user";

export function hasRoles(userRoles:string[], requiredRoles:string[]):boolean {
    if (requiredRoles==undefined||requiredRoles.length==0){
        return true
    }
    if (userRoles.length==0){
        return false
    }
    return requiredRoles.some(role=>userRoles.includes(role));
}


export function hasPermissions(userPermissions:string[],requiredPermissions:string[]):boolean{
    return requiredPermissions.every(permission=>userPermissions.includes(permission));
}

export function getUserRoles(userStore: any):string[] {
    return userStore.getUser().roles
}

export function getUserPermissions(userStore:any):string[] {
    return userStore.getUser().permissions
}

export function isLoggedIn(userStore:any){
    console.log(sessionStorage.getItem('casdoorUser'))
    return sessionStorage.getItem('isLogin')=='true'
}

export function routerGuard(to:RouteLocationNormalized,from: RouteLocationNormalized,next:NavigationGuardNext):void{
    const userStore = useUserStore()
    
    if (to.path==='/login'||to.path==='/callback'){
        next();
    }else if (isLoggedIn(userStore)){

        next();
    }else{
        next('/login');
    }
}