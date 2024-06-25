// 제출 이벤트를 받는다  (이벤트 핸들링)
// 제출된 입력 값들을 참조한다
//입력값에 문제가 있는 경우 이를 감지한다

const form = document.getElementById("form")

// 익명함수
form.addEventListener("submit", function(event){
    event.preventDefault()

    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userGender = event.target.gender.value
    let userPhone = event.target.phone.value
    let userPosition = event.target.position.value
    let userEmail = event.target.email.value
    let userIntro = event.target.intro.value

    if(userId.length < 8){
        alert("아이디가 너무 짧습니다. 8자 이상 입력해주세요")
        return
    }

    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    document.body.innerHTML = ""
    document.write(`<h1>${userName}님의 가입을 환영합니다!</h1>`)
    document.write(`<h2>${userName}님의 가입정보는 아래와 같습니다!</h2>`)
    document.write(`<P>아이디 : ${userId}<P>`)
    document.write(`<P>이름 : ${userName}<P>`)
    document.write(`<P>전화번호 : ${userPhone}<P>`)
    document.write(`<P>원하는 직무 : ${userPosition}<P>`)


})