const first_showup = document.querySelector("#qure_gen");
first_showup.addEventListener('click',()=>{
    const first = document.querySelector(".ser"); 
    first.style.display ="block";
    const sec1 = document.querySelector(".user_pol").style.display ="none";
    const news = document.querySelector('.news').style.display ="none";
});

const second_showup = document.querySelector("#up");
second_showup.addEventListener('click',()=>{
    const first = document.querySelector(".user_pol"); 
    first.style.display ="block";
    const sec1 = document.querySelector(".ser").style.display ="none";
    const news = document.querySelector('.news').style.display ="none";
});

const third_showup = document.querySelector("#newsing");
third_showup.addEventListener('click',()=>{
    const first = document.querySelector(".user_pol").style.display ="none";
    const sec1 = document.querySelector(".ser").style.display ="none";
    const news = document.querySelector('.news').style.display ="block";
});

const searching = document.querySelector("#search");
searching.addEventListener('click',()=>{
    window.location.href ="/";
});