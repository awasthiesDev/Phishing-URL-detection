document.getElementById("check-btn").addEventListener("click", function () {
    const urlInput = document.getElementById("url-input");
    const resultDiv = document.getElementById("result");

    const url = urlInput.value.trim();
    
    if (url === "") {
        alert("Please enter a valid URL.");
        return;
    }

    // Show loading animation
    document.getElementById("loading").classList.remove("hidden");
    resultDiv.innerHTML = "";

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url }),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("loading").classList.add("hidden");
            
            if (data.legitimacy_percentage >= 50) {
                resultDiv.innerHTML = `<span class="text-green-600 font-semibold">✅ This URL is ${data.legitimacy_percentage}% safe.</span>`;
            } else {
                resultDiv.innerHTML = `<span class="text-red-600 font-semibold">❌ This URL is ${100 - data.legitimacy_percentage}% unsafe.</span>`;
            }

            // Clear input field after checking
            urlInput.value = "";
        })
        .catch((error) => {
            console.error("Error:", error);
            document.getElementById("loading").classList.add("hidden");
            resultDiv.innerHTML = `<span class="text-red-600">⚠️ Error checking URL. Try again!</span>`;
        });
});
