const chatDiv = document.getElementById("chat");
const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("send");

sendBtn.addEventListener("click", async () => {
    const msg = messageInput.value.trim();
    if (!msg) return;

    appendMessage("You", msg);
    messageInput.value = "";

    try {
        const res = await fetch("http://127.0.0.1:8000/api/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sessionId: "abc123", message: msg })
        });
        const data = await res.json();
        appendMessage("Assistant", data.reply);
    } catch (err) {
        appendMessage("Assistant", "Error connecting to server.");
        console.error(err);
    }
});

function appendMessage(sender, text){
    const div = document.createElement("div");
    div.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatDiv.appendChild(div);
    chatDiv.scrollTop = chatDiv.scrollHeight;
}