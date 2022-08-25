# SVG

## SVG vs HTML Canvas
* [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
    * XML Syntax
    * each shape is a DOM element
    * **Note** - Not performant at large scale (anything more than 2k elements or over 1k elements for animation)
* [HTML Canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
    * JS API
    * one canvas element on the DOM contains shapes.  Shapes are inaccessible once drawn.
    * VERY performant, especially for animations
    * **Note** - Hard to build interactions

## Viewport & Coordinate System
* an svg exists with no boundaries
* a viewport defines what the user can see of that svg (so part of the svg could be out of the viewing area)
* x increases left to right.  y increases top to bottom.
    * 0,0 is top left corner of viewport 

## Elements
* <circle>
    * attributes: 
        * r (required)
        * cx, cy (optional)
* <rect>
    * attributes: 
        * width/height (required)
        * x,y (optional) 
* <path>
    * attributes:
        * d (required)
* <text>
    * attributes: 
        * x, y, text-anchor (start, middle, end), dy (optional)

### Path
* d attribute explanation
    * d defines how to draw the path
    * commands: 
        * Move To - Mx,y - Pick the pen off the paper and put it down at x,y
        * Line To - Lx,y - Draw a line from where the pen is now to the x,y defined here
        * Curve To - Cx,y x,y x,y - Draw a line from where pen is now to 3rd x,y.  Use 1st x,y to pull the line up from the initial point.  Use 2nd x,y to pull line up from 3rd x,y.  
* Sample:
```
<svg width=100 height=100 style='overflow: visible; margin: 5px;'>
  <path d='M0,0 C50,40 50,70 20,100 L0,85 L-20,100 C-50,70 -50,40 0,0'
    fill='none' stroke='#000' stroke-width=2 transform='translate(50,0)' />
</svg>
```
* explanation of sample: 
    * put pen at 0.0 (top left)
    * draw line from 0,0 to 20,100
    * apply curve from 0,0 to 50,40
    * apply curve from 20,100 to 50,70
    * draw line from 20,00 to 0,85
    * draw line from 0,85 to -20,100
    * draw line from -20,100 to 0,0
    * apply curve from -20,100 to -50,70
    * apply curve from 0,0 to -50,40


