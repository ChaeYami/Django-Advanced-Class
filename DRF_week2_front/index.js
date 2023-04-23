console.log("js불러왔음!")


window.onload - async function loadAritcles (){
    const response = await fetch('http://127.0.0.1:8000/articles/', {method : 'GET'})

    response_json = await response.json()

    console.log(response_json)

    const articles = document.getElementById("articles")

    response_json.forEach(element => {
        console.log(element)        
    });


}  