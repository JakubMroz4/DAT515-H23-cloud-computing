import React, { useState, useEffect } from "react";
import Comments from "../components/Comments";
import Comment_Input from "../components/Comment_input";

function Main() {

    return (
      <div className="Body">

          <Comment_Input/>
          <Comments/>
          
      </div>
    );
  }
  
  
  export default Main;




