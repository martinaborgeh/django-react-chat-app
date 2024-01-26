import { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import {resendAuthorizeRequest,resendDataRequest,refreshAccessToken} from './refreshtoken';



export function JoinMeeting(){

    const access = localStorage.getItem('access')?localStorage.getItem('access'):null;
    const refresh = localStorage.getItem('refresh')?localStorage.getItem('refresh'):null;

    const [meeting_id, setmeeting_id] = useState('')
    
    
    const serverBaseUrl = "http://localhost:8000";
    const clientBaseUrl = "http://localhost:3000";

    const serverbaseurl = "http://localhost:8000"
    const clientbaseurl = "http://localhost:3000"


    const SignUpData ={
       meeting_id
   }
        
        



     const handleSubmit = function(event){

        event.preventDefault()

      
  
    fetch(serverbaseurl+"/patient-doctor-matching/create-appointment/",

            {
                method: 'POST',
                credentials:'include',
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(SignUpData),

             }).then(response_data => {return response_data.json()
                
            }).then(response=>{
                
                if (response.status === 200){
                    console.log(response.message)
                    window.open(clientbaseurl+"/chat-room")
               
                }else if( response.status ===600){

                    console.log(response.message)
                    
                }else{

                    console.log(response.status)
                }
                
            }).catch(err=>{
                console.log("Ooops, We are sorry, system under maintenance")}
            )
     

}


  // Check if the user is authorized
    useEffect(() => {
     
        fetch(serverBaseUrl + "/patient-doctor-matching/check-page-view-is-authorized-for-patient/", {
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

                              const retry = resendAuthorizeRequest(serverBaseUrl + "/patient-doctor-matching/check-page-view-is-authorized-for-patient/",newAccessToken)
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

    return(
        <div>
             <form onSubmit={handleSubmit}>
                        <div className = "sellerformcontainer">
                                     
                        <input value={meeting_id} placeholder='meeting_id' onChange={e=>setmeeting_id(e.target.value)} type ="text" name = "hello"></input> 
                        <button className='submit' type ="submit" name = "submit">Submit</button> 
                        <Link to="/login">Not logged in? login here</Link>
                        </div>
                    </form>

      </div>
      
    )
}
