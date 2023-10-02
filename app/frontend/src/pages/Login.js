import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';


function Login() {
    const [email, setEmail] = useState({email: ""});
    const [password, setPassword] = useState({password: ""});

    let handleSubmit = async (e) => {
        e.preventDefault();
        try {
          let res = await fetch(process.env.REACT_APP_APIURL + "/login", {
            method: "POST",
            body: JSON.stringify({
              email: email,
              password: password,
            }),
          });
        } catch (err) {
          console.log(err);
          alert(err["error"]);
        }
      };

    return (
        <div className="body">      

            <div className="form">
                <h5>Sign up</h5>

                <Form onSubmit={handleSubmit}>
                <Form.Group className="mb-3" controlId="formEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" value={email} onChange={(e) => setEmail(e.target.value)}/>
                    <Form.Text className="text-muted">
                    </Form.Text>
                </Form.Group>

                <Form.Group className="mb-3" controlId="formPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                </Form.Group>

                <Button variant="primary" type="submit">
                    Submit
                </Button>
                </Form>
      </div>
    </div>
    )
}

export default Login