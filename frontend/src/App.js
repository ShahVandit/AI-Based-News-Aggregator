import React from "react";
import Home from "./Home";
import { Route, Switch, Redirect } from "react-router-dom";
import DetailPage from "./components/Detail/DetailPage";

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Login from "./components/login/Login";
import Register from "./components/register/Register";
const App = () => {
  return (
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route exact path="/register" component={Register} />
      <Route exact path="/:id" component={DetailPage} />
    </Switch>
  );
};

export default App;
