import { Router } from "oh-router";
import { Login } from "../pages/login";

export const router = new Router({
  routes: [
    {
      path: "/login",
      element: <Login />,
    },
  ],
});
