document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const resultBox = document.getElementById('result-box');
    const spinner = document.getElementById('spinner');

    form.addEventListener('submit', function (e) {
        e.preventDefault();  // Stop page from reloading

        const urlInput = document.querySelector('input[name="url"]').value;
        resultBox.innerHTML = "";
        spinner.style.display = "block";

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `url=${encodeURIComponent(urlInput)}`
        })
        .then(res => res.text())
        .then(html => {
            spinner.style.display = "none";
            // Extract the result div from the returned HTML
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const newResult = doc.getElementById('result-box').innerHTML;
            resultBox.innerHTML = newResult;
        })
        .catch(err => {
            spinner.style.display = "none";
            resultBox.innerHTML = "<div class='result phishing'>⚠️ Error connecting to server</div>";
        });
    });
});
