import { loginByUserName } from "../apis/user"
import { removeToken, setToken } from "../shared/token"

export const userStore = new(class{
    async loginByUserName(username:string,password:string){
           // TODO: 具体登录逻辑：请求接口，报错token 
           const res = await loginByUserName({username,password});
           setToken(res.access_token)
    }

    async loginByCellPhone(username:string,password:string){
        // TODO: 具体登录逻辑：请求接口，报错token 
 }
 async logout(){
    // TODO: 具体登出逻辑：清理token
    removeToken()
 }
})