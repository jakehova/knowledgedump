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
        Store-App<--Product-Display-MFE;
        Store-App<--Checkout-Component-MFE;
        Store-App<--Product-Search-Component-MFE;
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
## Benefits
*  Faster Development (for larger projects)
*  Deployment Independence
*  Smaller Codebases
*  Simplified Testing