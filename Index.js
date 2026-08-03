var background = document.getElementById("core");

function activate() {
    background.style.backgroundColor = "black";
}

function change() {
    background.style.backgroundColor = "LightSteelBlue";
}

background.onclick = change;