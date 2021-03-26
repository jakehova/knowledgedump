# YAML


* validate at yamllint.com
* file starts with ---
* superset of JSON (you can parse JSON with a YAML parser)
* newlines and spaces are important (dont use tabs)
* order matters
* has extension YAML or yml
* newline separates key/value pairs (elements).  no comma to celebrate lines.  
* children just need to have a consistent amt of spaces before them to show they are at the same level
* array is newline with each new element is indented in and has a hyphen before it
  * ex: \
    &nbsp;&nbsp;issues:  
       &nbsp;&nbsp;&nbsp;&nbsp;- hood dent \
       &nbsp;&nbsp;&nbsp;&nbsp;- fender rust
* object is <object name>: /n key/value pairs of properties
  * ex: \
    &nbsp;&nbsp;specs:  \
    &nbsp;&nbsp;&nbsp;&nbsp;hp: 400 \
    &nbsp;&nbsp;&nbsp;&nbsp;weight: 4 ton \
    &nbsp;&nbsp;&nbsp;&nbsp;type: 4 door