document.addEventListener("DOMContentLoaded", () => {
  const numberInput = document.getElementById("number");
  const calculateButton = document.getElementById("calculate");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const errorDiv = document.getElementById("error");
  const factorialResult = document.getElementById("factorial-result");

  calculateButton.addEventListener("click", async () => {
    // Get the input value
    const number = parseInt(numberInput.value);

    // Basic validation
    if (isNaN(number)) {
      showError("Please enter a valid number");
      return;
    }

    if (number < 0) {
      showError("Factorial is not defined for negative numbers");
      return;
    }

    if (number > 170) {
      showError("Number too large. Please enter a number between 0 and 170");
      return;
    }

    // Hide previous results/errors and show loading
    hideAll();
    loadingDiv.classList.remove("hidden");

    try {
      // Make API call
      const response = await fetch("/api/factorial", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ number }),
      });

      const data = await response.json();

      if (!response.ok) {
        showError(data.detail || "An error occurred");
        return;
      }

      // Display result
      factorialResult.textContent = `${number}! = ${data.factorial}`;
      hideAll();
      resultDiv.classList.remove("hidden");
    } catch (error) {
      showError("Failed to connect to the server");
    }
  });

  function hideAll() {
    resultDiv.classList.add("hidden");
    loadingDiv.classList.add("hidden");
    errorDiv.classList.add("hidden");
  }

  function showError(message) {
    hideAll();
    errorDiv.textContent = message;
    errorDiv.classList.remove("hidden");
  }
});
