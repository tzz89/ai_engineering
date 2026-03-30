import "./App.css";

import { StytchLogin, IdentityProvider, useStytchUser } from "@stytch/react";

function App() {
  const { user } = useStytchUser();

  const config = {
    products: ["passwords"],
    passwordOptions: {
      loginRedirectURL: "https://www.stytch.com/login",
      resetPasswordRedirectURL: "https://www.stytch.com/reset-password",
    },
    otpOptions: {
      methods: [],
      expirationMinutes: 5,
    },
  };

  return (
    <div>{!user ? <StytchLogin config={config} /> : <IdentityProvider />}</div>
  );
}

export default App;
