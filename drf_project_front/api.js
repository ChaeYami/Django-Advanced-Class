window.onload = () =>{
    console.log("로딩")
}

async function handleSignin(){
    
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    console.log(email,password)

    const response = await fetch('http://127.0.0.1:8000/users/signup/',{
        headers:{
            'content-type' : 'application/json',

        },
        method:'POST',
        body: JSON.stringify({
            "email" : email,
            "password":password
        })
    })
    console.log(response)
}