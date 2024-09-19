import { Router } from "oh-router";
import Login from "../pages/login/login";
import {Chat} from '../pages/chat'

export const router = new Router({
  routes: [
    {
      path: "/login",
      element: <Login />,
    },
    {
      path: "/chat",
      element: <Chat />,
    },
    {
      path:"/",
      redirect:"/login"
    }
  ],
});
