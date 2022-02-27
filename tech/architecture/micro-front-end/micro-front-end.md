# Micro FrontEnd Architecture

## Component Architecture
When building a front end application in javascript, it is important to encapsulate code within code blocks of single responsibility.  While this is a generally known coding principle, it is incredibly important in a dynamically typed language like javascript.  Having code that is tied to a single responsibility makes it much easier to write both unit and integration tests. The more tests, the more reliable the code.  In modern Javascript frameworks this single responsiblity ends up being a foundational principle in how the frameworks are structured.  The encapsulated code block is called a "component" and both React and Angular use "component hierarchies" to manage development.  Building a front end using components and component hierarchies makes the code base a lot more manageable and testable.

**NOTE:** - For the duration of the article, I will use an example of a marketplace (i.e. Amazon) to describe patterns.

## Monolithic Architecture
In a monolithic frontend architecture (not to be confused with a mono repo which is focused on single repo containing multiple applications and libraries), an application is designed to match the component hierarchy of the application.  So for the marketplace, you would have an architecture similar to:
```mermaid
    graph TD;
        Store-App-->Product-Display-Component-Tree;
        Product-Display-Component-Tree-->Product-Card-Component;
        Product-Card-Component-->Price-Component;
        Product-Card-Component-->Image-Preview-Component;
        Product-Card-Component-->Description-Component;
        Store-App-->Checkout-Component-Tree;
        Checkout-Component-Tree-->Cart-Component;
        Checkout-Component-Tree-->Cart-Item-Component;
        Checkout-Component-Tree-->Calculated-Total-Component;
        Store-App-->Product-Search-Component-Tree;
        Product-Search-Component-Tree-->Product-Search-TextBox;
        Product-Search-Component-Tree-->Product-Search-Result-ListBox;
        Product-Search-Component-Tree-->Product-Search-Result-ListItem;
```
As you can see, there is one application and that application is broken down into different trees of components.  The leaf nodes of the tree being the most basic components of that tree.  Parent nodes have a responsibility to coordinate communication of data to its child nodes and to pass events from its child nodes, further up the tree.

## Equivalent Micro FrontEnd Architecture
In micro front end architecture component trees are broken out into their own silos to be maintained and iterated on semi-independently of the product as a whole.  So the monlith above can be re-configured into three different applications: 
```mermaid
    graph TD;
        Product-Display-MFE-->Store-App;
        Checkout-Component-MFE-->Store-App;
        Product-Search-Component-MFE-->Store-App;
```
---
```mermaid
    graph TD;
        Product-Display-MFE-->Product-Card-Component;
        Product-Card-Component-->Price-Component;
        Product-Card-Component-->Image-Preview-Component;
        Product-Card-Component-->Description-Component;
```

```mermaid
    graph TD;
        Checkout-Component-MFE-->Cart-Component;
        Checkout-Component-MFE-->Cart-Item-Component;
        Checkout-Component-MFE-->Calculated-Total-Component;
```

```mermaid
    graph TD;
        Product-Search-Component-MFE-->Product-Search-TextBox;
        Product-Search-Component-MFE-->Product-Search-Result-ListBox;
        Product-Search-Component-MFE-->Product-Search-Result-ListItem;
```
---

## Benefits of Micro FrontEnd Architecture
*  Faster Development (for larger projects) & Deployment Independence

Teams can be assigned to each micro front end and work independently of each other.  This allows for independent deployment cycles and independent iteration cycles.  So Product-Search could release new features/bug fixes without coordinating with Checkout or Product Display MFEs.  Front end state management libraries could be leveraged to manage all communication to/from the MFE so any dependence on data from another MFE can largely be abstracted away from the front end code of the MFE itself. 

*  Smaller and Focused Codebases
There is an obvious functionality focus for each MFE, so each MFE's codebase is limited to code aligned with it's output goal.  

*  Simplified Testing


* Lower FCP and FMP values
In addition, from a user perspective, only the front ends that are used need to be loaded in the browser.  So in the marketplace example, we can decrease our time to first contentful paint and first meaningful paint because we are providing a lot less code to the browser for parsing and processing.

## Key Implementation Concepts
* Each MFE can be technology independent and should be built independently of the other MFEs
* Do not rely on shared or global state
* Use MFE prefixes for components/namespaces/local storage vars/events/cookies to ensure no conflict and to ease testing/maintenance
* Use native browser platform for communication between MFEs (i.e. instead of using a custom pub/sub system use browser's native messaging apis), not custom apis or passing values directly to MFEs.  

## Challenges
* Inconsistent user experience.  
    * With multiple teams working independently on a single solution, it can be easy for multiple teams to implement a similar feature in different ways.
    * Mitigate by:
        * Have a central UI/UX team that creates guidelines for all teams to follow
        * Have framework specific repos for common assets (framework wrapped textbox, drop down, calendar, etc) that that has UI testing that tests for adherence to UX guideleines laid out by the organization.
* Poor communication between MFEs
    * Similar to API maintenance and versionining issues that teams have experienced when swithcing to a micro service architecture, the same issue applies here.  When an MFE is documented to accept a specific message/content and is updated to break that contract, then 
    * Mitigate by: 
        * Clearly documenting messaging api support for outgoing and incoming messages.
        * Have integration tests built that test messaging events
        * Have a deprecation strategy for messaging events
* Larger Payloads
    * Since each team is essentially working in a silo, there is a chance for code duplication or handling similar problems in different ways.  This is not necessarily a bad thing as long as the user experience does not suffer from these inconsistentices.  What CAN occur is the duplicative code leads to code glut and payload sizes for each front end 

