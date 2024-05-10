import React, { useEffect, useState } from "react";
import styled from "styled-components";
import { mobile } from "../../Responsive";
import axios from "axios";
import { useHistory } from "react-router-dom";

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  background: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
    url("https://images.pexels.com/photos/3944454/pexels-photo-3944454.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
      center;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
`;
const Wrapper = styled.div`
  padding: 20px;
  width: 40%;
  background-color: white;
  ${mobile({ width: "75%" })}
`;
const Title = styled.h1`
  font-size: 24px;
  font-weight: 300;
`;
const Form = styled.form`
  display: flex;
  flex-wrap: wrap;
`;
const Input = styled.input`
  flex: 1;
  min-width: 40%;
  margin: 20px 10px 0px 0px;
  padding: 10px;
`;
const Agreement = styled.span`
  font-size: 18px;
  margin: 20px 0px;
`;
const Button = styled.button`
  width: 40%;
  border: none;
  padding: 15px 20px;
  background-color: teal;
  color: white;
  cursor: pointer;
`;

const Register = () => {
  const history = useHistory();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [cpassword, setCpassword] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (password === cpassword) {
        const res = await axios.post("http://127.0.0.1:8000/api/register/", {
          username: username,
          email: email,
          password: password,
        });
        console.log(res);
        setUsername("");
        setEmail("");
        setPassword("");
        setCpassword("");
        history.push("/login");
      } else {
        window.alert("Password doesn't match");
      }
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <Container>
      <Wrapper>
        <Title>CREATE AN ACCOUNT</Title>
        <Form>
          {/* <Input placeholder="Name" name="name" required maxLength={20} /> */}
          <Input
            placeholder="Username"
            name="username"
            value={username}
            required
            minLength={4}
            onChange={(e) => setUsername(e.target.value)}
          />
          <Input
            placeholder="Email"
            value={email}
            name="email"
            required
            onChange={(e) => setEmail(e.target.value)}
          />
          {/* <Input
            placeholder="Phone Number"
            name="phone"
            required
            maxLength={10}
            minLength={10}
          /> */}
          <Input
            placeholder="Password"
            name="password"
            type="password"
            required
            value={password}
            minLength={8}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Input
            placeholder="Confirm Password"
            name="cpassword"
            type="password"
            required
            value={cpassword}
            minLength={8}
            onChange={(e) => setCpassword(e.target.value)}
          />
          <Agreement>
            By creating an account, I consent to the processing of my personal
            data in accordance with the <b>PRIVACY POLICY</b>
          </Agreement>
          <Button onClick={handleSubmit}>CREATE</Button>
        </Form>
      </Wrapper>
    </Container>
  );
};

export default Register;
