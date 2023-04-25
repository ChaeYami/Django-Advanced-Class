console.log("로딩")

window.onload=()=>{
    const payload = localStorage.getItem("payload");

    // 가져온 payload 를 사용하기 위해서 Object 형태로 바꿔줘야 함
    const payload_parse = JSON.parse(payload)
    
    // 원하는 속성을 가져와서 사용할 수 있다.
    console.log(payload_parse.email)

    const intro = document.getElementById("intro")
    intro.innerText = payload_parse.email
}