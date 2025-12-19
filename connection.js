// Create websocket connection
const socket = new WebSocket("ws://localhost:8080")

// Open connection
socket.addEventListener("open", (event) => {
    socket.send("Hello Server!");
})

// Server is listening for messages
socket.addEventListener("message", (event) => {
    console.log("Message from server", event.data)
})
