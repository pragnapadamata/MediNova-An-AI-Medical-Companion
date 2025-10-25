function chatOpen() {
  document.getElementById("chat-open").style.display = "none";
  document.getElementById("chat-close").style.display = "block";
  document.getElementById("chat-window1").style.display = "block";
}

function chatClose() {
  document.getElementById("chat-open").style.display = "block";
  document.getElementById("chat-close").style.display = "none";
  document.getElementById("chat-window1").style.display = "none";
  document.getElementById("chat-window2").style.display = "none";
}

function openConversation() {
  document.getElementById("chat-window1").style.display = "none";
  document.getElementById("chat-window2").style.display = "block";
}

function userResponse() {
  let userInput = document.getElementById("textInput");
  let message = userInput.value.trim();
  if (message === "") return;

  appendMessage("user", message);
  userInput.value = "";

  // Send message to backend
  fetch("/chatbot", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })
  })
    .then(response => response.json())
    .then(data => {
      appendMessage("bot", data.reply);
    });
}

function appendMessage(sender, text) {
  let messageBox = document.getElementById("messageBox");
  let messageDiv = document.createElement("div");
  
  if (sender === "user") {
    messageDiv.className = "first-chat";
    messageDiv.innerHTML = `<p>${text}</p><div class="arrow"></div>`;
  } else {
    messageDiv.className = "second-chat";
    messageDiv.innerHTML = `<div class="circle"></div><p>${text}</p><div class="arrow"></div>`;
  }
  

  messageBox.appendChild(messageDiv);
  messageBox.scrollTop = messageBox.scrollHeight;
}