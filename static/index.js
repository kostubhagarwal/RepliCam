let storedURL = ""; // name of file to request
let uploaded = false;

// Add option to print once a model has been uploaded
function showPrintOption() {
    let div = document.createElement("div");
    div.id = "print-header"
    div.innerHTML = `<a href="/print/${storedURL}" print="${storedURL}">Print</a>`;
    document.getElementById("file-form").appendChild(div);
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
        if (!uploaded) {
            uploaded = true;
            showPrintOption();
        }
    });
});
