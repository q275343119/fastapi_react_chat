import { Router } from "oh-router";
import Login from "../pages/login/Login";
import { Chat } from "../pages/chat";
import { LoginCHeckMIddleware } from "./middlewares/loginCheck";

export const router = new Router({
  middlewares: [new LoginCHeckMIddleware()],

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
      path: "/",
      redirect: "/chat",
    },
    {
      path: "*",
      element: <div>404</div>,
    },
  ],
});
