import {Middleware,MiddlewareContext} from "oh-router"
import { getToken } from "../../shared/token"
import { router } from ".."


export class LoginCHeckMIddleware extends Middleware{
    async handler(_ctx: MiddlewareContext<{}>, next: () => Promise<any>): Promise<void> {
        const token = getToken()
        // 处理登录页面逻辑
        if(_ctx.to.pathname === "/login"){
            if(token){
               // 有token 去主页 
                router.navigate("/")
            }
            else{
                // 没有继续（去登录页）
                next()
            }
        }
        // 其他路由
        if(token){
            // 有token继续
            next()
        }
        else{
            // 没有token 去登录页
            router.navigate("/login")
        }
    }
   
}