function sendCodeToPi(code, colorName) {
    // Display 'Searching' notification
    displayNotification(`Searching for ${colorName.toUpperCase()}...`);

    // Send the code to the Raspberry Pi via a POST request
    fetch('http://<raspberry_pi_ip>:<port>/send_code', {  // Replace <raspberry_pi_ip> and <port>
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ code: code })  // Send the code as a JSON object
    })
    .then(response => response.json())
    .then(data => {
        // Simulate a delay to mimic the process of detection
        setTimeout(() => {
            if (data.detected) {
                displayNotification(`${colorName.toUpperCase()} Detected, car stopped.`);
            } else {
                displayNotification(`${colorName.toUpperCase()} not detected.`);
            }
        }, 2000); // Delay of 2 seconds
    })
    .catch(error => {
        console.error('Error sending code to Raspberry Pi:', error);
        displayNotification(`Failed to send ${colorName.toUpperCase()} code.`);
    });
}
