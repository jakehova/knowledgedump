# Push Notification 
https://github.com/department-of-veterans-affairs/vanotify-team/tree/master/Architecture/push-notifications

## Background 
Push notification is a notification directed at a mobile app.  The mobile platform OS receives a notification and decides how to present it to the user.   Apple and Android both have integration platforms to allow for push notifications.  Apple has [Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html) and Android has  [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging).  

## Push Notifications via AWS
AWS has the SNS service which can be configured to send messages to both Android/Apple notification platforms.  AWS assigns an ARN (Amazon Resource Name) to the mobile app itself that you can use to send a push notification to ALL mobile app installations.  AWS also assigns an ARN to each individual device installation so that you can send notifications directly to a device. 

### How
* AWS Manual Setup: 
    * Go to SNS 
    * Create platform application
        * Purpose: This creates an ARN for your application so that when you want to send a push notification to all users of your application, you send to the generated ARN
        * Select which Platform provider to send notifications through (FCM can send to both google and ios)
        * Enter in Platform specific information (like API key)
        * Get Platform ARN 
    * Add endpoints
        * Purpose: This creates an endpoint for a specific device so that if you want to send a push notification to a specific device, you send to the generated ARN
        * Add Device Push Token
        * (Optional) - Enter Additional payload to send with each push 
        * (Optional) - Enter a user identifier
        * Get Device ARN
    * Publish Message to ARN
        * To send push notification to EVERY user that uses the app, send an SNS message to the Platform ARN
        * To send push notification to INDIVIDUAL user that uses the app, send an SNS to Device ARN