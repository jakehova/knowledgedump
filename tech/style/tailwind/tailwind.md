# Tailwind CSS

## WHAT

- css styling library

## HOW

- to use:
  - create base css file (i.e. css/my-site-styles.css) and put post-css directives in there:

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

- use tailwind post-css processor to generate css:
  - npx tailwindcss-cli build <loc of css file to process> -o <loc of css output file>
  - i.e. npx tailwindcss-cli build css/my-site-styles.css -o build/built-styles.CSS
- add any other styles that you want to the css file and all will be processed by the tailwind cli utility

## USAGE

**General** 
  - class names begin with the property letter (height => h-?, margin => m-?, background color => bg-blue-600) 
  - can specify direction by adding x or y at the end of the property (padding horizontally same on x axis => px-?) 
  - can specify specific direction by using l, r, t, b (margin top => mt-?) 
  - special properties contain full name (shadow => shadow-?, rounded corners => rounded-?, making text uppercase => uppercase, putting space between each letter => tracking-?) 
  - can apply margin evenly for all properties in a container element by using "space" class => <div class="space-y-6"> would apply margin top of 6 to every element inside that div except for the first one. <div class="space-x-6"> would apply margin left to every element in that div except for first one 
  - font colors and weight are combined ( font that is 600 weight gray color => text-gray-600) 
  - Example of a styled button: 
    - <a class="inline-block px-5 py-3 rounded-lg shadow-lg bg-indigo-500 text-white uppercase tracking-wider font-semibold text-sm" href="#"> This is a button</a>

**Responsive** 
  - grid => class="grid grid-cols-?" => specifies using grid and that the grid has ? columns 
    - can have a div span multiple columns using => col-span-? 
    - to target a media breakpoint, use: <breakpoint abbrev>:<tailwind property> 
    - the media breakpoint style will apply from that breakpoint and up to the next breakpoint, the style without the breakpoint prefix will be the default for any style that is not included specifically 
    - example change background color depending on screen size: <div class="bg-gray-100 sm:bg-yellow-300 md:bg-green-300 lg:bg-pink-300 xl:bg-blue-200 2xl:bg-red-300> - example responsive image: 
      - <img class="rounded-lg shadow-xl sm:mt-8 sm:h-64 sm:w-full sm:object-cover object-center"> 
      - sm:h-64 => specifies height of the image 
      - sm:w-full => specifies that the width of the image should take the whole avail container 
      - sm:object-cover => crops the image in such a way that ensures that the image isnt skeweed. always applies the proper aspect ratio. 
      - object-center: makes sure that the cropping focuses on the center of the image.
      - control visibility by using hidden attribute - hide image on large screens: class="lg:hidden" 
      - show image on large screens only: class="hidden lg:block"

**Interactivitiy** 
  - update tailwind config file => variants property - <property name>: ["<event>"] 
  - eg: backgroundColor: ["active"] => this will say that any the backgroundcolor property can be modified only during active events - putting these key/value pairs in the "extends" property just extends it as opposed to overriding regular behavior
  - hover/focus for background color are on by default. active is not. 
  - some properties are not on (like changing font size) so need to add those. 
  - can target class events by using them as a prefix. 
  - make a button look like it's moving up when mouse is over it: 
    - <a class="hover:bg-indigo-400 hover:-translate-y-0.5 transform transition focus:outline-none focus:ring focus:ring-offset-2 focus:ring-opacity-50 active:bg-indigo-600"> 
    - hover event class says do this on hover 
    - transform class allows for using the translate-y-0.5 animation 
    - transition class applies default animation properties that make the animation look smooth 
    - focus event class says do this when the element has focus 
    - focus:outline-none removes the hard box outline when it has focus 
    - focus:ring puts a ring around the button when it has a focus 
    - focus:ring-offset-2 adds spacing between the button and the ring 
    - active:bg-indigo-600 adds a style for when the button is clicked

**Helpers** 
  - @apply - Can group a series of tailwind styles into it's own class name 
  - We had this style for a button above: <a class="hover:bg-indigo-400 hover:-translate-y-0.5 transform transition focus:outline-none focus:ring focus:ring-offset-2 focus:ring-opacity-50 active:bg-indigo-600"> 
    - We can go to our tailwind css file and BEFORE the @tailwind utilities directive, we can define a "btn" class that can be used in place of all those styles:
```
.btn {
    @apply hover:bg-indigo-400 hover:-translate-y-0.5 transform transition focus:outline-none focus:ring focus:ring-offset-2 focus:ring-opacity-50 active:bg-indigo-600
}
```
    - @layer <tailwind directive that is being overriden> 
      - in the example above the order of the btn class was important because the btn is overriding the default components  
      - instead, you can keep the prime tailwind directives at the top of the page and then do this: 

```
@layer components {
    .btn {
        @apply <tailwind styles>
    }
}
```

**Building a Theme**
  - in tailwind config, update the theme property with the properties to extend: 

```
theme: {
    extend: {
        colors: {
            brand: {
                DEFAULT: "#38383",
                light: "#33333",
                dark: "#444444"
            }
        },
        fontFamily: {
            headline: "Poppins, sans-serif
        }
    }
}
```
    - then use the same properties but with the color specific override: bg-brand, bg-brand-light, etc and font-headline

**Forms  Plugin**
- npm install @tailwindcss/forms
- update tailwind config plugins property => [require('@tailwindcss/forms')]
- this applies minimal styling 
- still would want to use common styling properties like: w-full border-gray-300 rounded-lg shadow-sm all contained within a div that has a mt-1: 

```
<div>
    <label for="inputfield" class="block text-sm font-medium text-gray-700">
        Enter data
    </label>
    <div class="mt-1">
        <input type="text" id="inputfield" name="inputfield" class="w-full border-gray-300 rounded-lg shadow-sm focus:border-indigo-500 focus:ring-indigo-500" />
    </div>
</div>
<div class="flex items-center>
    <input type="checkbox" id="terms" name="terms" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500"/>
    <label for="terms" class="ml-2 block text-sm text-gray-900">
        I agree to the <a href="#" class="text-indigo-600 hover:text-indigo-500">Terms</a> and <a href="#" class="text-indigo-600 hover:text-indigo-500">Privacy Policy</a>
    </label>
</div>
```
    - to set common form styles throught site update the tailwind.css file

```
@layer base { 
    [type='text], 
    [type='email'], 
    <...etc> {
        @apply rounded-lg w-full border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500
    }
}
```

**Improving for Prod**
    - Remove all css that is not used by updating tailwind config => purge property
```
    purge: {        
        content: ["./src/**/*.jsx", "./index.html"]
    }
``` 

      - **IMPORTANT** purge feature literally looks for text in html and if its found then it includes that class.  If you are building those classes dynamically in the code then they will NOT be included. Instead you need to setup variables or properties that include the full class name as a string: 

```
const styleName = {
    height: "h-40",
    width: "w-40"
}
...
<img class=`${styleName.height} ${styleName.width} `>
```


## SETUP

npm init -y
npm install -D tailwindcss postcss autoprefixer vite
update package.json scripts => 
    - "dev": "vite" // for dev
    - "build": "vite build" // for prod
npx tailwindcss init -p => generates tailwind configure file and postcss config file
update index.html file to have link tag with href pointing to css file
