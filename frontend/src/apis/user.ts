import { request } from "../shared/request";

interface Token {
    token_type: string
    expires_in: number
    access_token: string
  }




export async function loginByUserName(opts: { username: string; password: string; }) {
    return request.post<any,Token>("/auth/token",opts)
    
}