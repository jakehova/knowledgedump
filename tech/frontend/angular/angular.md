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
* Reference vs Value Types

## Managing feature
* LIFT
    * Locate code quickly
        * keep file structure flat
        * Most features should come off the root app folder 
            * this avoids all the "../.../../" type stuff
            * lot of folders off root but it becomes really easy to see exactly where things are at any particular time
            * exception should be if a feature has nested features
        * Each feature should have its own module and routing module.
        * Routing Module: 
            - in the class, create a "static components = []" variable that has all the components that are part of the routing module
            - in the respective feature module, in the declarations section, can just do <rougting module name>.components .  This simplifies and centralizes component declarations.
    * Identify the code at a glance
    * flat structure
    * Be DRY
* Feature Based 
    * Features are organized in their own folder
    * features are self contained
    * easy to find everything related to a feature

## Structuring Components
* Container/Presentation pattern -> Container component retrieves/sends data and contains Child components.  Child components receive data and send data up to container component.
    * Name COntainer component a base name (i.e. CustomerComponent), name the child components the base comoponent witht he prupose of the child before 'Compoinent' (i.e.CustomerEditComponent, CustomerModalComponent)
* Consider using child routes when doing your design.  If you want to give the user the ability to bookmark a page to get right to it (like going straight to a specific item's details), then use child routing to trigger data retrieval
* Child components can initialize data but they should NOT change or retrieve data from anywhere except it's parent component.
* Use OnPush as much as possible to improve performance and ensure that Container/Presentation relationship.  
    * It only runs change detection when: 
        * an input property reference changes
        * an output property/EventEmitter or DOM event fires
        * Async pipe receives an event
        * Change detection is manually invoked via ChangeDetectorRef
    * **Note** Reference vs Value Types: 
        * OnPush will detect a change with native Types
        * OnPush will NOT detect a change to an array or object UNLESS that object was cloned.  So you cant just push an object on to an existing array and except that array to be presented.  Cloning Techniques (Immutable approach): 
            * JSON.parse/stringify
                * JSON.parse(JSON.stringify(customersArray)) => generates a cloned
                * This fails if the object has dates
            *  Clone: npm install clone
```
deepClone<T>(value) : T {
    return clone<T>(value);
}
```
            * Immutable.js library

## Component communication
* Event Bus vs Observable Services
    * Event Bus: receives data from a component and messages other subscribed components
        * this model is used by ngrx
    * Observable Service: Service creates the data and messages other subscribed components

## RxJS
* Subject - send one or more data values to listeners.  Subscribers get emitted data that comes AFTER they have subscribed.
* BehaviorSubject - send one or more data values to listeners.  Subscribers get the directly previous emitted data AND all the following data since they subscribed.
* ReplaySubject - send one or more data values to listeners.  Subscribers can get ANY emitted data AND all the following data since they subscribed.
* AsyncSubject - send one or more data values to listeners.  Subscribers get ONLY the last data was emitted when the sequence is complete.
```
// declaration of source service
private customers: Customer[];
private subject$: Subject<ICustomer>; // always make the subject private.  You do not want this exposed
subjectObservable$: Observable<ICustomer>;  // this is public and will expose the emitted data

// declaration of consumer component
private subjectSub: Subscription;
public customerObservableData: Customer[] = [];
 

// initialize observables
this.subject$ = new Subject();
this.subjectObservable$ = this.subject$.asObservable();

// this function would be in the service
addCustomer(name: string, city: string){
    this.customers.push({
        name, 
        city
    })

    let clone = JSON.parse(JSON.stringify(this.customers));
    this.subject$.next(clone);

    // if its an async subject, then you would, at some point, need to call this.asyncSubject$.complete(); to signal that the async portion of things is completed    
}

// this function would be in the component
viewCustomers() {
    this.subjectSub = this.subjectObservable$.subscribe(custs => this.customerObservableData = custs);
}

ngOnDestroy() {
    // close out subscriptions
    if (this.subjectSub) {
        this.subjectSub.unsubscribe();
    }
}
```

