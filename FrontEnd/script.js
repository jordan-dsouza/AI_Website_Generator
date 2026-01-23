let generatedHTML = "";
let generatedCSS = "";

// async function returns a Promise
async function generateWebsite() {
    const prompt = document.getElementById("prompt").value;

    if (!prompt.trim()) {
        alert("Please enter a description");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });

    if (!response.ok) {
        alert("Backend error: " + response.status);
        return;
    }

    const data = await response.json();

    generatedHTML = data.html;
    generatedCSS = data.css;

    const iframe = document.getElementById("preview");

    iframe.srcdoc = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Live Preview</title>
    <style>
        ${generatedCSS}
    </style>
</head>
<body>
    ${generatedHTML}
</body>
</html>
`;
}
