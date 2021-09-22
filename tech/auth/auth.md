# Auth

## Resources
[OAuth 2.0 Full Explanation](https://www.oauth.com/)

## Forms Authentication
* Process: 
    * username & pwd =>  DB => one way hash pwd to see if valid, lookup user info, => return cookie if everything checks out
* Downsides: 
    * Security
    * Maintenance

## Main Problem
* Delegated Authorization - I trust Gmail and I kind of trust Yelp, Give Yelp access to JUST my contacts
 
## OAuth 2.0 - Use for authorization.  Do not use for authentication.
* Resource Owner - the person that owns the data (the user that owns the contacts and gives the okay to access the contacts)
* Client - the application (yelp)
* Authorization server - the system used to say yes to get access (acct.google.com)
* Resource server - the api/system that holds the data (contacts.google.com)
* Authorization Grant - the thing that proves the user said yes to accessing the data (a cookie from auth server)
* Redirect URI - callback url
* Access Token - the way the key 
* Scope - authorization server has a list of actions that can be taken against resource server (i.e. view contacts, delete contacts).  
* Consent - the notification screen from auth server saying what scopes the client is requesting
* Back Channel (highly secure channel) - communication between back end servers 
* Front Channel (less secure channel) - communication from browser/stand alone system to api/server
* Example "code" Process - use when you have a front and back channel: 
    1) User on a site clicks the "Connect with Google" button 
    2) Redirect to authorization server (acct.google.com)
        a) includes a redirect uri, requested scopes, response type 
            i) "code" is a type of authorization grant the client wants.  (i.e. code grant is a common one)
                * "token" is another type of authorization grant for when you want "implicit" flow (front channel only)
            ii) scopes are the actions the client wants to be able to perform on behalf of the user
        b) **Note** - when adding integration with that auth server, client has registered with auth server and has received a client id and client secret that is stored on the server.  the client id is not secure info.
    3) User Type in credentials 
    4) User is prompted for consent to grant the client what scopes the client is requesting (i.e. notification that Yelp is trying to view contacts)
        a) If Yes, then redirected to client via redirect uri (i.e. yelp/callback url).
            i) redirect includes an authorization code (depending on what the response type requested is)  
            ii) the callback server takes the redirect and sends the authorization code back to the auth server in exchange for an access token
                1) in order to get the access token, you would need the machine key from the callback server thats been configured to work with the auth server
        b) If No, then process fails and redirect back to client with no other data
    5) Client can access the resource server using the access token returned from the authorization server (i.e. use the information returned to callback to access resource server (contacts.google.com))
        a) access token specifies scopes the user has
        b) **Note** the access token never goes back to the user.  its stored on the client server 
* Alternatives to "code" flow: 
    * implicit flow front channel only - use when only have front channel
        1) same flow as code, but the token returned after consent is used as the token to be used with resource server
    * Resource Ownder Password Credentials flow back channel only  - machine to machine comm but for legacy systems
    * Client Credentials flow back channel only - machine to machine comm

## OpenID Connect - used for authentication. do not use for authorization (use oauth 2)
* Used with OAuth.  Adds: 
    * ID token (JWT) - this gets included with the access token during the authorization event
    * UserInfo endpoint for getting more user information 
    * Standard set of scopes
    * Standardized implementation
* Same process flow as Code process flow above.  Differences are: 
    * During redirect to authorization server, "openid" scope is included.  This tells auth server to use open id connect for authentication.
    * When callback happens from authorization server back to client server, an ID Token (JWT) is included with the Access Token.

## SAML - Generally used for SSO
* Older version 

* Which grant type (flow) do I use: 
    * Web app w/server backend: code flow with openid included in the scopes
    * Native Mobile App: code flow + PKCE (proof code for key exchange aka Pixie) -> This flow works the same as code flow 
    * SPA with API Backend (where you dont own the API): implicit flow 
