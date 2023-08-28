import React, { useState, useEffect } from "react";
import './App.css';

function App() {
    const [data, setdata] = useState({
        course: "",
        semester: "",
        assignment: "",
    });

    useEffect(() => {
      // fetching from flask server
      fetch("/get_data").then((res) =>
          res.json().then((data) => {
              // setting the data
              setdata({
                  course: data.Course,
                  semester: data.Semester,
                  assignment: data.Assignment,
              });
          })
      );
  }, []);

  return (
    <div className="App">
            <header className="App-header">
                <h1></h1>
                {/* calling data from backend */}
                <p>Course: {data.course}</p>
                <p>Semester: {data.semester}</p>
                <p>Assignment number: #{data.assignment}</p>
 
            </header>
        </div>
  );
}


export default App;
