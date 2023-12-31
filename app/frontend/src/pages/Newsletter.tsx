import { useState } from "react";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import React from 'react';

function Newsletter() {
  const [email, setEmail] = useState("");

  let handleSubmit = async () => {
    try {
      let res = await fetch(process.env.REACT_APP_APIURL + "/add_data", {
        method: "POST",
        body: JSON.stringify({
          email: email,
        }),
      });
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="body">      

      <div className="form">
      <h5>Sign up for our newsletter</h5>

        <Form onSubmit={handleSubmit}>
          <Form.Group className="mb-3" controlId="formEmail">
            <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.target.value)}/>
            <Form.Text className="text-muted">
              We'll never share your email with anyone else.
            </Form.Text>
          </Form.Group>

          <Button variant="info" type="submit">
            Sign up
          </Button>
        </Form>
      </div>
    </div>
  );
}

export default Newsletter;