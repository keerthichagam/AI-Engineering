const result = document.getElementById("result");
const button = document.getElementById("predictBtn");
const hoursInput = document.getElementById("hours");

button.addEventListener("click", function() {
    const hours = hoursInput.value;
    if (hours === "") {
    result.textContent = "Please enter your study hours.";
    return;
}
    if (Number(hours) < 0) {
    result.textContent = "Study hours cannot be negative.";
    return;
}
if (Number(hours) > 24) {
    result.textContent = "Study hours cannot be more than 24 hours.";
    return;
}
    console.log("Hours studied:", hours);

    fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            hours_studied: Number(hours)
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        result.textContent = "Predicted Marks: " + data.predicted_marks;
    });

    result.textContent = "You studied " + hours + " hours.";
});