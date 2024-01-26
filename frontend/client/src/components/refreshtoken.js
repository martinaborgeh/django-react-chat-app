
const setTokensInLocalStorage = (accessToken, refreshToken) => {
    localStorage.setItem('access', accessToken);
    localStorage.setItem('refresh', refreshToken);
};


async function refreshAccessToken (){

    const serverBaseUrl = "http://localhost:8000";
    const refreshToken = localStorage.getItem('refresh');
    console.log(refreshToken)

    const response = await fetch(`${serverBaseUrl}/accounts/login/refresh/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken }),
    });

    if (response.ok) {
        const data = await response.json();
        console.log("new refresh token obtained now")
        const newAccessToken = data.access;
        setTokensInLocalStorage(newAccessToken, refreshToken);
        return newAccessToken;
    } else {
          console.log("You do not have any refresh token")
        // Handle refresh failure (e.g., redirect to login)
        return null;
    }
};


async function resendAuthorizeRequest(url,newAccessToken){


   const retryrequest = await fetch(url, {
                   method: 'GET',
                   headers: {
                   Authorization: `Bearer ${newAccessToken}`,
                  'Content-Type': 'application/json',
                   },
                  
               })

              if (retryrequest.ok) {
                const data = await retryrequest.json();
                return data
        
              } else {
                console.log("You do not have any refresh token")
                // Handle refresh failure (e.g., redirect to login)
               return null;
            }
};


async function resendDataRequest(url,newAccessToken,method,data){
   const serverBaseUrl = "http://localhost:8000";

   const retryrequest = await fetch(url, {
                   method: method,
                   headers: {
                   Authorization: `Bearer ${newAccessToken}`,
                  'Content-Type': 'application/json',
                   },
                   body: JSON.stringify(data),
               })

              if (retryrequest.ok) {
                 
                const data = await retryrequest.json();
                 console.log("data",data)
                return data
        
              } else {
                console.log("nothing")
               return null;
            }
};

                            
module.exports = {refreshAccessToken,resendAuthorizeRequest,resendDataRequest}