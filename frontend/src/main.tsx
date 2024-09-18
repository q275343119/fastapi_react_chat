import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { RouterView } from "oh-router-react";
import { router } from "./router";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterView router={router} />
  </StrictMode>
);
