import React, { useState, useEffect } from "react";
import './App.css';

function App() {
    const [data, setdata] = useState({
        name: "",
        code: "",
        semester: "",
    });

    useEffect(() => {
      // fetching from flask server
      fetch(process.env.REACT_APP_APIURL + "/get_data").then((res) =>
          res.json().then((data) => {
              // setting the data
              setdata({
                    name: data.courses[0].name,
                    code: data.courses[0].code,
                    semester: data.courses[0].semester,
              });
          })
      );
  }, []);

  return (
    <div className="App">
            <header className="App-header">
                {/* calling data from backend */}
                <p>Course: {data.name}</p>
                <p>Course code: {data.code}</p>
                <p>Semester: {data.semester}</p>
 
            </header>
        </div>
  );
}


export default App;
