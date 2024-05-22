const len = document.querySelector('.google');
const divver = document.querySelector('.online-result');

if (len.innerHTML.trim() === "None") {
    divver.style.visibility = "hidden";
} else {
    divver.style.visibility = "visible";
}
