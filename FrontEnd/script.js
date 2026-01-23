// async function returns a "Promise"
async function generateWebsite() {
    const prompt = document.getElementById("prompt").value; // Directly access prompt from html

    // If no prompt after trimming
    if (!prompt.trim()){
        alert("Please enter a description");
        return;
    }
// await pauses function execution until promise is settled
    // Fetch() initiates request
    const response = await fetch("http://127.0.0.1:8000/generate",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt }) // JavaScript value to JSON string
    });
    
    if (!response.ok) {
    alert("Backend error: " + response.status);
    return;
    }
    
    const data = await response.json();

    const html = data.html;
    const css = data.css;

    const iframe = document.getElementById("preview");

    iframe.srcdoc = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Live Preview</title>
    <style>
        ${css}
    </style>
</head>
<body>
    ${html}
</body>
</html>
`;

}
