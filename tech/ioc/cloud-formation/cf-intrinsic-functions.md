# Intrinsic Functions

* built in cloud formation function to dynamically assign values during runtime
* can only be used in certain section of stack definitions:
    * resource properties
    * outputs
    * metadata attributes
    * update policy attributes
* Functions
    * Fn::Base64 (JSON) - !Base64 (YAML)
        * returns base64 represenatation of input string 
        * !Base64 <value to encode>
    * Fn::FindInMap
        * MapName is logical name of mapping declared in mappings section that contains the keys and values
        * TopLevelKey is a key name for a list of key value pairs
        * SecondLevelKey key name which is a set to one of the keys from the list assigned to TopLevelKey
        * Syntax: Fn::FindInMap: [<MapName>, <TopLevelKey>, <SecondLevelKey>]