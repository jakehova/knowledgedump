# Playwright

## What 
Automated Testing Library that works across Java, NodeJS, and .NET.  Can test multiple browsers and mobile.  

## Setup
* Installation
    * Node: npm i -D playwright
    * .NET: 
        * dotnet tool install --global Microsoft.Playwright.CLI    
        * dotnet add package Microsoft.Playwright
* Enable type-checking in a js file in VSCode add "//@ts-check" to the top of the file

## Usage
* Record Scripts: npx playwright codegen wikipedia.org
**NodeJS Example**
```
const { chromium, firefox, webkit } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: false });
  // Create pages, interact with UI elements, assert values
  await browser.close();
})();
```