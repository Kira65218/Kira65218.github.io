var background = document.getElementById("core");

function activate() {
    background.style.backgroundColor = "black";
}

background.onclick = function change() {
    background.style.backgroundColor = "LightSteelBlue";
}