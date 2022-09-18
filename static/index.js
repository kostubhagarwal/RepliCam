let storedURL = ""; // name of file to request


// Add option to download file
function createDownload() {
    let div = document.createElement("div");
    div.id = "download-header"
    div.innerHTML = `<a href="/download/${storedURL}" download="${storedURL}">Download</a>`;
    document.body.appendChild(div);
}

// Handle form submission

let form = document.getElementById("file-form")
form.addEventListener("submit", function(e) {
    e.preventDefault();
    console.log("form submit");
    let file = document.querySelector('input[type="file"]');
    let data = new FormData();
    data.append("file", file.files[0]);
    return fetch("/upload", {
        method: "POST",
        body:data
    })
    .then(response => response.json())
    .then(data => {
        storedURL = data.filename;
        createDownload();
    });
});
