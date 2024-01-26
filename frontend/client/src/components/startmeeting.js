import { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import {resendAuthorizeRequest,resendDataRequest,refreshAccessToken} from './refreshtoken';



export function DoctorStartMeeting() {
    const access = localStorage.getItem('access')?localStorage.getItem('access'):null;
    const refresh = localStorage.getItem('refresh')?localStorage.getItem('refresh'):null;

    //const [message, setMessage] = useState('');

    const [meeting_id, setmeeting_id] = useState('')
    const serverBaseUrl = "http://localhost:8000";
    const clientBaseUrl = "http://localhost:3000";

    const signUpData = {
       
        meeting_id
    };

    const handleSubmit = function (event) {
        console.log(signUpData)
        event.preventDefault();

        fetch(serverBaseUrl + "/patient-doctor-matching/start-meeting/", {
            method: 'POST',
            
            headers: {
                 'Authorization': `Bearer ${access}`,
                "Content-Type": "application/json",
            },
            body: JSON.stringify(signUpData),
        })
            .then(response => {
                if (!response.ok) {
                    console.log("RESPONSE",response.status)


                         if (response.status === 401) {
                           const newAccessToken = refreshAccessToken();
                           console.log("the new access token",newAccessToken)
                             if (newAccessToken) {

                              const retry = resendDataRequest(serverBaseUrl + "/patient-doctor-matching/start-meeting/",newAccessToken,"POST",signUpData)
                              console.log("resubmit successful")
                               console.log("retry",retry)
                           
                                 return retry?retry:null


                         }else{
                             console.log("no refresh token. redirect to login")   
                             throw new Error('Not authorized');
                             //window.open(clientBaseUrl + "/login", '_self');
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
               const datainot = data
               if(datainot){window.open(clientBaseUrl+"/chat-room",'_self')}
          })
            .catch(error => {
                // Handle unauthorized access
                console.error('Unauthorized:', error.message);
            });
    };


 // Check if the user is authorized
    useEffect(() => {
     
        fetch(serverBaseUrl + "/patient-doctor-matching/check-page-view-is-authorized-for-doctor/", {
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

                              const retry = resendAuthorizeRequest(serverBaseUrl + "/check-page-view-is-authorized-for-doctor/",newAccessToken)
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
                    console.log(response.status)
                    console.log(response.message)
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

    return (
        <div>
            <h1>Start meeting</h1>
            <form onSubmit={handleSubmit}>
                <div className="sellerformcontainer">
                    <input value={meeting_id} placeholder='meeting_id' onChange={e=>setmeeting_id(e.target.value)} type ="text" name = "hello"></input> 
                    
                    <button className='submit' type="Create" name="submit">Submit</button>
                    <Link to="/login">Not logged in? Login here</Link>
                </div>
            </form>
            
        </div>
    );
}

