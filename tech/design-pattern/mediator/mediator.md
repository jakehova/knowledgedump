# Mediator Design Pattern

## What
Encapsulates how objects interact and promotes loose couping between objects by avoiding objects communicating directly with each other
Composed of: 
    * Mediator: defines communication between colleagues (typically abstract base class)
    * Concrete Mediator: implement communication between colleagues (inherits Mediator)
    * Colleague: communicate only with the Mediator (abstract base class and only references Mediator)
    * Concrete Colleague: receives messages from the mediator (inherits Colleague)

## When
Use when a lot of objects need to be managed with a common messaging system.
For example: 
    * for web systems, Mediator takes in a request object and returns a response object.  The mediator would have a list of all request handlers in the system and when a request comes in, the mediator sends out the message to all handlers. 
    * 