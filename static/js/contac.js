const menu = document.querySelector('.right_button');
let navi=10;
menu.addEventListener('click',()=>{
    setTimeout(()=>{
    menu.innerHTML ="close";
    const nav = document.querySelector('.navbar');
    if (navi === 10){
        nav.style.transition ="0.3s"
        nav.style.height ="220px";
        setTimeout(() => {
            const btn = document.querySelector('.res_btn');
            btn.style.visibility = "visible";
        }, 100);
        navi =5;
    }
    else if(navi===5){
        nav.style.height = "56px"
        nav.style.transition ="0.3s"
        const btn = document.querySelector('.res_btn');
        btn.style.visibility = "hidden";
        navi =10;
        menu.innerHTML ="Menu";
    }
    },200);
});
function pol(){
    tranfer("more");
}
function ser(){
    tranfer("");
}

const tranfer =(value)=>{
    window.location.href =`/${value}`
}