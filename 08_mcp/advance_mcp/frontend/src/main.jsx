import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { createStytchClient, Products, StytchProvider } from "@stytch/react";

import "./index.css";
import App from "./App.jsx";

const stytch = createStytchClient(
  "public-token-test-adf97bdb-e55d-479f-a232-92b953ae77af",
);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <StytchProvider stytch={stytch}>
      <App />
    </StytchProvider>
  </StrictMode>,
);
