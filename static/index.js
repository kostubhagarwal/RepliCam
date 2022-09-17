// Handle form submission


let form = document.getElementById("file-form")
form.addEventListener("submit", function(e) {
    e.preventDefault();
    console.log("form submit");
    let file = document.querySelector('input[type="file"]');
    let data = new FormData();
    data.append("file", file.files[0]);
    fetch("/upload", {
        method: "POST",
        body:data
    })
    .then(response => response.blob())
    .then(blob => {
            var url = window.URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = "filename.xlsx";
            document.body.appendChild(a); // we need to append the element to the dom -> otherwise it will not work in firefox
            a.click();    
            a.remove();  //after
    });
});
