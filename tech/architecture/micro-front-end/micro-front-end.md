# Micro FrontEnd Architecture

**Traditional Monolithic Architecture**
In a traditional monolithic frontend architecture, component trees are used to segment responsibility of work.  These component architectures 
```mermaid
    graph TD;
        Store-App-->store-app-components;
```

---
**Equivalent Micro FrontEnd Architecture**
```mermaid
    graph TD;
        Store-App-->Product-Display;
        Product-Display-->product-display-components;
        Store-App-->Checkout;
        Checkout-->checkout-components;
        Store-App-->Product-Search;
        Product-Search-->product-search-components;
```

## Benefits
*  Faster Development (for larger projects)
*  Deployment Independence
*  Smaller Codebases
*  Simplified Testing