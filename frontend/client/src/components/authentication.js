import { useState, useEffect} from "react"
import { Link } from 'react-router-dom'



export function Signup(){

    
    const [full_name, setfull_name] = useState('')
    const [role, setrole] = useState('')
    const [password, setpassword] = useState('')
    const [password2, setpassword2] = useState('')
    const [email, setemail] = useState('')
    

    const serverbaseurl = "http://localhost:8000"
    const clientbaseurl = "http://localhost:3000"


    const SignUpData ={
        full_name,
        role,
        password,
        password2,
        email
   }
        
        



     const handleSubmit = function(event){

        event.preventDefault()

      
  
    fetch(serverbaseurl+"/accounts/register/",

            {
                method: 'POST',
  
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(SignUpData),

             }).then(response_data => {return response_data.json()
                
            }).then(response=>{
 
                    window.open(clientbaseurl+"/login",'_self')
               
            }).catch(err=>{
                console.log("Ooops, We are sorry, system under maintenance")}
            )
     

}

    return(
        <div>
             <form onSubmit={handleSubmit}>
                        <div className = "sellerformcontainer">
                            
                        <input value={full_name} placeholder='full name' onChange={e=>setfull_name(e.target.value)} type ="text" name = "hello"></input>
                        <input value={role} placeholder='role' onChange={e=>setrole(e.target.value)} type ="text" name = "name"></input>
                        <input value={password} placeholder='password' onChange={e=>setpassword(e.target.value)} type ="text" name = "name"></input>
                        <input value={password2} placeholder='password2' onChange={e=>setpassword2(e.target.value)} type ="text" name = "name"></input>
                        <input value={email} placeholder='email' onChange={e=>setemail(e.target.value)} type ="text" name = "name"></input>
                        
                        
                       
                        <button className='submit' type ="submit" name = "submit">Submit</button> 
                        <Link to="/login">Already have an account</Link>
                        </div>
                    </form>

      </div>
      
    )
}







export function Login(){

    const [password, setpassword] = useState('')
    const [email, setemail] = useState('')
    

    const serverbaseurl = "http://localhost:8000"
    const clientbaseurl = "http://localhost:3000"


    const SignUpData ={
        password,
        email
   }
        
     const handleSubmit = function(event){

        event.preventDefault()

      
  
    fetch(serverbaseurl+"/accounts/login/",

            {
                method: 'POST',
                credentials:'include',
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(SignUpData),

             }).then(response_data => {return response_data.json()
                
            }).then(response=>{
                    
                   
                   localStorage.setItem('access', response.access);
                   localStorage.setItem('refresh', response.refresh);
                    
               
                   window.open(clientbaseurl+"/create-apppointment",'_self')
               
                
                
            }).catch(err=>{
                console.log("Ooops, We are sorry, system under maintenance")}
            )
     

}

    return(
        <div>
             <form onSubmit={handleSubmit}>
                        <div className = "sellerformcontainer">
                            
                        <input value={password} placeholder='password' onChange={e=>setpassword(e.target.value)} type ="text" name = "name"></input>
                        <input value={email} placeholder='email' onChange={e=>setemail(e.target.value)} type ="text" name = "name"></input>
                        
                        
                      
                        <button className='submit' type ="submit" name = "submit">Submit</button> 
                        <Link to="/signup">Don't have an account</Link>
                        </div>
                    </form>

      </div>
      
    )
}

