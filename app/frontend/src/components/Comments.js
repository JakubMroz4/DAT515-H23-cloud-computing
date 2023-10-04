import React, { useState, useEffect } from "react";


const Comments = () => {
        const [comments, setComments] = useState([]);
      
        useEffect(() => {
          fetch(process.env.REACT_APP_APIURL + "/get_comments")
            .then((response) => response.json())
            .then((data) => setComments(data));
        }, []);


    return (
        <div className="Comments">
            {comments && comments.map(comment =>
                        <div className="Comment">
                            <div> <h4><strong>{comment.author}</strong> - <em>{comment.date_posted}</em></h4></div>
                              <h3>{comment.text}</h3>
                        </div>
                    )}
        </div>
    )
}
export default Comments;