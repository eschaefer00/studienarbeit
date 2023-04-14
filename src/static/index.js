let prompt;
let imgUrl;

function presentImage() {
    let button = document.getElementById("submit-button");
    button.disabled = true;
    fetch('/generateImage', {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({prompt: document.getElementById("prompt").value})
    }).then(_res => _res.json()).then(json => {
        console.log(JSON.stringify(json))
        let img = document.createElement("img");
        img.src = json.imageUrl;
        img.alt = "Your generated image";
        img.id = "img";
        let src = document.getElementById("img_div");
        if (src.hasChildNodes()) {
            src.removeChild(src.lastChild)
        }
        src.appendChild(img);
        prompt = document.getElementById("prompt")
        prompt.value = json.prompt;
        imgUrl = json.imageUrl;
    });
}


function unlockButton() {
    let button = document.getElementById("submit-button");
    button.disabled = false;

}