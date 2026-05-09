async function analyzeSentiment() {

    const text = document.getElementById("text-input").value;

    const sentimentElement = document.getElementById("sentiment");
    const confidenceElement = document.getElementById("confidence");
    const loading = document.getElementById("loading");

    if(text.trim() === ""){
        alert("Please enter some text");
        return;
    }

    loading.style.display = "block";

    sentimentElement.innerText = "Sentiment: --";
    confidenceElement.innerText = "Confidence: --";

    const response = await fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            text: text
        })
    });

    const data = await response.json();

    loading.style.display = "none";

    let emoji = "";

    if(data.sentiment === "POSITIVE"){

        emoji = "😊";

        sentimentElement.className = "positive";

    } else {

        emoji = "😡";

        sentimentElement.className = "negative";
    }

    sentimentElement.innerText =
        `Sentiment: ${data.sentiment} ${emoji}`;

    confidenceElement.innerText =
        `Confidence Score: ${data.confidence}`;
}