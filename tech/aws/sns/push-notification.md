# Push Notification 

### What 
* Push notification is a notification directed at a mobile app.  The mobile app receives a notification and decides how to present it to the user

### How
* Setup: 
    * Go to SNS 
    * Create platform application
        * Purpose: This creates an ARN for your application so that when you want to send a push notification to all users of your application, you send to the generated ARN
        * Select which Platform provider to send notifications through (FCM can send to both google and ios)
        * Enter in Platform specific information (like API key)
        * Get Platform ARN 
    * Add endpoints
        * Purpose: This creates an endpoint for a specific device so that if you want to send a push notification to a specific device, you send to the generated ARN
        * Add Device Token (UUID)
        * (Optional) - Enter Additional payload to send with each push 
        * (Optional) - Enter a user identifier
        * Get Device ARN
    * Publish Message to ARN
        * To send push notification to EVERY user that uses the app, send an SNS message to the Platform ARN
        * To send push notification to INDIVIDUAL user that uses the app, send an SNS to Device ARN