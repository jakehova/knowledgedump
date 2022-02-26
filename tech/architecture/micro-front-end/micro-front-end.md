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
        Store-App-->Product-Display-MFE;
        Product-Display-MFE-->product-display-components;
        Store-App-->Checkout-MFE;
        Checkout-MFE-->checkout-components;
        Store-App-->Product-Search-MFE;
        Product-Search-MFE-->product-search-components;
```

## Benefits
*  Faster Development (for larger projects)
*  Deployment Independence
*  Smaller Codebases
*  Simplified Testing