import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import React, { useState, useEffect } from "react";


function Comment_Input() {
    const [author, setAuthor] = useState("");
    const [text, setText] = useState("");

    let handleSubmit = async () => {
        try {
          let res = await fetch(process.env.REACT_APP_APIURL + "/submit_comment", {
            method: "POST",
            body: JSON.stringify({
                author: author,
                text: text,
            }),
          });

          window.location.href = "/";

        } catch (err: any) {
          console.log(err);
          alert(err["error"]);
        }
      };

    return (
        <div className="body">      

            <div className="form">
                <h5>Leave a message:</h5>

                <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formName">
                    <Form.Control type="text" placeholder="Your name" value={author} onChange={(e) => setAuthor(e.target.value)}/>
                    <Form.Text className="text-muted">
                    </Form.Text>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formText">
                    <Form.Control type="text" placeholder="Your message" value={text} onChange={(e) => setText(e.target.value)}/>
                </Form.Group>

                <Button variant="primary" type="submit">
                    Submit
                </Button>
                </Form>
      </div>
    </div>
    )
}

export default Comment_Input