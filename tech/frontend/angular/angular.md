# Angular

## Managing Complexity
* Consists of managing state, flow control, and code volume
* Every grouping of code should do one thing (every component should have one responsibility)
* A component should consume just enough data to satisfy its templates and capture user events to delegate them upwards.  Keep them as thin as possible.
* Components should satisfy inputs using the Async pipe and should have no server communication (oblivious to buisness logic and application state).
* Use Services (Facade) as effective delegation layer between components and the rest of the app
* Server communication and state management should be decopuled

A feature will get a route.  A route will go to a container component.  A container component should contain presentation component(s)


## Data Modeling
