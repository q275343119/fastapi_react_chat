import axios,{AxiosError} from "axios";
import { getToken } from "./token";

export const request = axios.create(
    {
        baseURL:"http://127.0.0.1:8000/api"
    }
)

request.interceptors.request.use(
    (config) =>{
        const token = getToken()
        if(token)config.headers!["authorization"] = "Bearer " + token
        return config
    }
)

request.interceptors.response.use(
    (res) =>{
        if (res.data.code != 200){
            
            throw Error(res.data.msg)
        }
        return res.data.data
    },
    (err:AxiosError) =>{
        if (err.response?.status===401){
            // TODO: 身份验证异常，需要重新登录
            alert(err.response.data.msg)
        }
        throw err
    }
)