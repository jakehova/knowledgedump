# Micro FrontEnd Architecture

**Traditional Monolithic Architecture**
In a traditional monolithic frontend architecture, component trees are used to segment responsibility of work.  These component architectures 
```mermaid
    graph TD;
        Store-App-->n-components;
```

---
**Equivalent Micro FrontEnd Architecture**
```mermaid
    graph TD;
        Store-App-->Product-Display;
        Product-Display-->n-components;
        Store-App-->Checkout;
        Checkout-->n-components;
        Store-App-->Product-Search;
        Product-Search-->n-components;
```

## Benefits
*  Faster Development (for larger projects)
*  Deployment Independence
*  Smaller Codebases
*  Simplified Testing