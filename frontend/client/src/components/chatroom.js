

import { useState, useEffect} from "react"
import { Link } from 'react-router-dom'
import {resendAuthorizeRequest,resendDataRequest,refreshAccessToken} from './refreshtoken';





export function ChatRoom(){

  const serverbaseurl = "http://localhost:8000"
  const clientbaseurl = "http://localhost:3000"

  const iswelcomed = localStorage.getItem("iswelcomed")?localStorage.getItem("iswelcomed"):null
   
  const access = localStorage.getItem('access')?localStorage.getItem('access'):null;
 

   
   const [send_message, set_send_message] = useState('')
   const [receive_message, set_receive_message] = useState('')
   const [notification, set_notification] = useState('')
  

    


    const SignUpData ={
       send_message,
       meeting_id:'jgghg'
   }
        
        
     const endcall = function(event){

        event.preventDefault()

      
  
     fetch(serverbaseurl + "/patient-doctor-matching/end-call/", {
            method: 'POST',
            
            headers: {
                 'Authorization': `Bearer ${access}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify({"meeting_id":'jgghg'}),
        })
            .then(response => {
                if (!response.ok) {
                    console.log("RESPONSE",response.status)


                         if (response.status === 401) {
                           const newAccessToken = refreshAccessToken();
                           console.log("the new access token",newAccessToken)
                             if (newAccessToken) {

                              const retry = resendDataRequest(serverbaseurl + "/patient-doctor-matching/end-call/",newAccessToken,"POST",SignUpData)
                              console.log("resubmit successful")
                               console.log("retry",retry)
                           
                                 return retry?retry:null


                         }else{
                             console.log("no refresh token. redirect to login")   
                             throw new Error('Not authorized');
                             //window.open(clientbaseurl + "/login", '_self');
                            };

           
                     }else if (response.status === 400){
                    // ignore error
                      console.log("this error is unnecessary")
                      return response.json();
                    }
                    
                }
               
                else{
                return response.json();
               }
            })
            .then(data => {
               //const datainot = data
               //if(datainot){window.open(clientbaseurl+"/chat-room",'_self')}
          })
            .catch(error => {
                // Handle unauthorized access
                console.error('Unauthorized:', error.message);
            });
            }


const sendmessage = function(event){

        event.preventDefault()

      
  
     fetch(serverbaseurl + "/patient-doctor-matching/send-message/", {
            method: 'POST',
            
            headers: {
                 'Authorization': `Bearer ${access}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(SignUpData),
        })
            .then(response => {
                if (!response.ok) {
                    console.log("RESPONSE",response.status)


                         if (response.status === 401) {
                           const newAccessToken = refreshAccessToken();
                           console.log("the new access token",newAccessToken)
                             if (newAccessToken) {

                              const retry = resendDataRequest(serverbaseurl + "/patient-doctor-matching/send-message/",newAccessToken,"POST",SignUpData)
                              console.log("resubmit successful")
                               console.log("retry",retry)
                           
                                 return retry?retry:null


                         }else{
                             console.log("no refresh token. redirect to login")   
                             throw new Error('Not authorized');
                             //window.open(clientbaseurl + "/login", '_self');
                            };

           
                     }else if (response.status === 400){
                    // ignore error
                      console.log("this error is unnecessary")
                      return response.json();
                    }
                    
                }
               
                else{
                return response.json();
               }
            })
            .then(data => {
               //const datainot = data
               //if(datainot){window.open(clientbaseurl+"/chat-room",'_self')}
          })
            .catch(error => {
                // Handle unauthorized access
                console.error('Unauthorized:', error.message);
            });
            }

    

//handling welcome message

useEffect(() => {

     
        fetch(serverbaseurl + "/patient-doctor-matching/call-welcome-message/", {
            method: 'POST',
         
            headers: {
                'Authorization': `Bearer ${access}`,
                'Content-Type': 'application/json', // Include Content-Type
            },
             body: JSON.stringify({meeting_id:'jgghg'}),
        })
            .then(response => {
                if (!response.ok) {
                    console.log("RESPONSE",response)


                         if (response.status === 401) {
                           const newAccessToken = refreshAccessToken();
                           console.log("the new access token",newAccessToken)
                             if (newAccessToken) {

                              const retry = resendAuthorizeRequest(serverbaseurl + "/call-welcome-message/",newAccessToken)
                           
                              console.log("after new access obtained", retry)
                             return retry?retry:null


                            }else{
                             console.log("no refresh token. redirect to login")   
                             throw new Error('Not authorized');
                             //window.open(clientbaseUrl + "/login", '_self');
                            };

           
                     }else{
                    // unhandled error
                      console.log("unhandled error with status code", response.status)
                      //return response.json();
                    }
                    
                }
               
                else if (response.ok){
                 
                    console.log("giving welcome message",response.status)
                    return response.status;
               }
            })
            .then(data => {
                // Handle successful response if needed
                console.log('status:', data);
                //setMessage(data); // Assuming there is a 'message' field in the response
            })
            .catch(error => {
                // Handle unauthorized access
                console.error('Unauthorized:', error.message);
            });
    }); // Make sure to include authToken as a dependency in the dependency array



// Check if the user is authorized

useEffect(() => {
     
        fetch(serverbaseurl + "/patient-doctor-matching/check-page-view-is-authorized-for-doctor/", {
            method: 'POST',
         
            headers: {
                'Authorization': `Bearer ${access}`,
                'Content-Type': 'application/json', // Include Content-Type
            },
        })
            .then(response => {
                if (!response.ok) {
                    console.log("RESPONSE",response)


                         if (response.status === 401) {
                           const newAccessToken = refreshAccessToken();
                           console.log("the new access token",newAccessToken)
                             if (newAccessToken) {

                              const retry = resendAuthorizeRequest(serverbaseurl + "/check-page-view-is-authorized-for-doctor/",newAccessToken)
                              console.log("after new access obtained", retry)
                             return retry?retry:null


                            }else{
                             console.log("no refresh token. redirect to login")   
                             throw new Error('Not authorized');
                             //window.open(clientBaseUrl + "/login", '_self');
                            };

           
                     }else{
                    // unhandled error
                      console.log("unhandled error with status code", response.status)
                      //return response.json();
                    }
                    
                }
               
                else if (response.ok){
                    console.log("checking authorization",response.status)
                  
                    return response.status;
               }
            })
            .then(data => {
                // Handle successful response if needed
                console.log('status:', data);
                //setMessage(data); // Assuming there is a 'message' field in the response
            })
            .catch(error => {
                // Handle unauthorized access
                console.error('Unauthorized:', error.message);
            });
    },[access]); // Make sure to include authToken as a dependency in the dependency array


  

const handleData = (event) => {
    const messageData = JSON.parse(event.data);
    console.log("type is",messageData)
    if (messageData.status ==="new_user_notification"){
       set_notification(messageData.message);
     }else if (messageData.status ==="new_message"){
       set_receive_message(messageData.message)
    }
  };

  useEffect(() => {
    const socket = new WebSocket(
      'ws://localhost:8000/ws/meeting/jgghg/' // Replace with your actual WebSocket URL
    );

    socket.addEventListener("message", handleData);

    return () => {
      // Cleanup function to close the WebSocket connection when component unmounts
      socket.close();
    };
  }, [receive_message,notification])


    return(
        <div>
             <form onSubmit={sendmessage}>
                        <div className = "sellerformcontainer">
                        <input value={send_message} placeholder='send message' onChange={e=>set_send_message(e.target.value)} type ="text" name = "hello"></input>  
                        <input value={receive_message} placeholder='receive message' onChange={e=>set_receive_message(e.target.value)} type ="text" name = "hello"></input>
                        <input value={notification} placeholder='notification' onChange={e=>set_notification(e.target.value)} type ="text" name = "hello"></input>
                        <button className='submit' type ="submit" name = "submit">Submit</button> 
                        <button onClick={endcall}>End Call</button>
                        <Link to="/login">Not logged in? login here</Link>
                        </div>
                    </form>

      </div>
      
    )
}
