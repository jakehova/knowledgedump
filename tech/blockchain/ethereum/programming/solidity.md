# Solidity

## Basics
* variables starting with an "_" are local variables and arent stored anywhere in the contract
* Refer to the contract address you are in by using this operator: address(this);
* This is what an empty contract looks like: 
```
contract HelloWorld { 

}
```
* Each contract SHOULD start with a line that tells the Ethereum VM what version the solidity code is.  This "version" is defined by using "pragma solidity <version number or range of version number>;".  As an example: pragma solidity >=0.5.0 means this code can be compiled by any compiler that is equal or more up to date than vesion 0.5.0.  pragma solidity >=0.5.0 <0.6.0; means this code can be compiled by any compiler that is equal or more up to date than 0.5.0 but is less than version 0.6.0
```
pragma solidity >=0.5.0 <0.6.0;

contract HelloWorld { 

}
```

## Best Practices
* set an owner of the contractor when the contract is created.  Use the below Ownable contract and inherit from it 
```
/**
 * @title Ownable
 * @dev The Ownable contract has an owner address, and provides basic authorization control
 * functions, this simplifies the implementation of "user permissions".
 */
contract Ownable {
  address private _owner;

  event OwnershipTransferred(
    address indexed previousOwner,
    address indexed newOwner
  );

  /**
   * @dev The Ownable constructor sets the original `owner` of the contract to the sender
   * account.
   */
  constructor() internal {
    _owner = msg.sender;
    emit OwnershipTransferred(address(0), _owner);
  }

  /**
   * @return the address of the owner.
   */
  function owner() public view returns(address) {
    return _owner;
  }

  /**
   * @dev Throws if called by any account other than the owner.
   */
  modifier onlyOwner() {
    require(isOwner());
    _;
  }

  /**
   * @return true if `msg.sender` is the owner of the contract.
   */
  function isOwner() public view returns(bool) {
    return msg.sender == _owner;
  }

  /**
   * @dev Allows the current owner to relinquish control of the contract.
   * @notice Renouncing to ownership will leave the contract without an owner.
   * It will not be possible to call the functions with the `onlyOwner`
   * modifier anymore.
   */
  function renounceOwnership() public onlyOwner {
    emit OwnershipTransferred(_owner, address(0));
    _owner = address(0);
  }

  /**
   * @dev Allows the current owner to transfer control of the contract to a newOwner.
   * @param newOwner The address to transfer ownership to.
   */
  function transferOwnership(address newOwner) public onlyOwner {
    _transferOwnership(newOwner);
  }

  /**
   * @dev Transfers control of the contract to a newOwner.
   * @param newOwner The address to transfer ownership to.
   */
  function _transferOwnership(address newOwner) internal {
    require(newOwner != address(0));
    emit OwnershipTransferred(_owner, newOwner);
    _owner = newOwner;
  }
}
```

## Storage
* storage - Contract Storage - things stored here get written to the blockchain and are permanent.
    * NOTE: This information is PUBLIC.  You can read this information using web3.eth.getStorageAt and point it to the contract address. That will show you all the contract storage variables associated with this contract.        
* memory - Memory Storage  - things stored here are erased between external function calls
* By default, variables declared outside of functions will be treated as storage.  variables declared in functions will be declared as memory.

## Variables
* Data Types: 
    * boolean
    * int/uint - integer - unsigned integeter (defaults to uint256 but uint8, uint16, uint32, etc are options).    
    * fixed/ufixed - fixed point number
    * address - 20 byte value (size of Ethereum address)
    * address payable - same as address but has methods for transfer and send [full method/property list](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#address-related)
    * Contract Types
    * bytes1 - Fixed size byte array - (bytes2, bytes3, ..., bytes32) holds a sequence of bytes from 1 up to 32
    * bytes - Dynamically size byte array
    * string - Dynamically szied UTF-8 encoded string 
        * Escape Characters: 
        * \<newline> (escapes an actual newline)
        * \\ - backslash
        * \' - single quote
        * \" - double quote
        * \n - newline
        * \r - carrige return
        * \t - tab
        * \xNN - hex escape
        * \uNNNN - unicode escape
    * Arrays
        * uint[2] - fixed array
        * uint[] - dynamic array
    * Structs - define an organized group of attributes.  More information below.
    * Mappings - define a lookup type that makes it easier to organize and lookup a group of different objects that have the same type. More information below.
    * Events
        * event <EventName>(<Event Parameters>);
            ```
            // contract code 
             event AddedNumberEvent(uint x, uint y, uint sum);
             
             function addNumbers(uint _x, uint _y) public returns (uint) {
                 uint sum = _x + _y;
                 emit AddedNumberEvent(_x, _y, sum);
                 return sum;
             }
             ...
             // front end code
             <Contract Object>.AddedNumberEvent(function(error, result) {
                 // result properties will be x, y, and sum;
                 if (error) return;
                 alert(`the sum of ${result.x} + ${result.y} is ${result.sum}`);
             })
             ```
* State Variables - These types of variables are permanently stored in contract storage.  
* Accessor Method - can declare any variable "public" and Solidity will automatically create a getter method for it.  For example: "int[] public scores;" - other contracts can read from but NOT write to this array

## Accessibilty - how functions or variables can be accessed in different ways
* private - only available to that contract
* public - available to anybody including anybody that calls the contract
* internal - same as private, except contracts that inherit have access to it (i.e. protected in C#)
* external - same as public, except can ONLY be called from outside the contract (cant be called by other functions inside the contract)
* modifier - only used for Functions.  This is used to run common validation checks prior to running any function code. 
```
  modifier onlyOwner() {
    require(isOwner());
    _;
  }

  function setNewOner(address _address) public onlyOwner {
    ...
  }
```
## Structs - used for logical data grouping.  A way to group variables that all describe the same thing.
```
struct Person {
    uint age;
    uint heightInCm;
    string eyeColor;
}
```

## Mappings - used for logical data grouping.  Use for data that needs to be looked up and all has the same type
```
// create an address book where last name is the lookup key and a Person struct is the result of that lookup. This is just an example and would assume that every last name is unique (so obviously not a realistic mapping)
mapping (string => Person) public addressBook;
// create a bank account lookup where the lookup key is the user's Ethereum Address and the result of that lookup is their Ether balance. 
mapping (address => uint) public bankAccounts;
```

## Events - broadcasts messages to listeners (commonly will be your front end code that is listening)
* denoted using the "event" type 

## Functions - grouped code.
* This example has two parameters.  
    * _destination - string type that is stored in memory rather than on the chain.  
    * _numberOfSteps - uint type that is not stored in memory
    * NOTE: These variable names start with an underscore.  This is a best practice so that you can tell variables that were passed in (i.e. local variables) from variables that you declared in your contract (i.e. global variables)
* This function is marked as "public" which means anybody can call this function.  
    * NOTE: Functions are DEFAULT public.  It is a best practice to explicitly show a function's accessibilty by putting either "public" or "private" declaration on it. 
    * NOTE: If a function is private, it should follow the same convention of starting with an underscore
```
function walkTo(string memory _destination, uint _numberOfSteps) public {
 
}
```
* Returning values from a function - To return a value from a function you update the function's signature (***) after the public/private keyword with returns (<type being returned> <if it's a variable being returned then use "memory">)    
```
string greeting = "Hello World!";
function sayHello() public returns (string memory) {
    return greeting;
}
```
    * You can return multiple values from a function: 
```
    function generateMultipleResponses() public returns (uint a, string b, uint c){
        // can do 1) 
        a = 1;
        b = "2";
        c = 3
        // or can do 2) 
        return (1, "2", 3);
    }

    function getMultipleResponses() public {
        // get all the responses
        (returnedA, returnedB, returnedC) = generateMultipleResponses();
        // get some of the responses
        (,,returnedC) = generateMultipleResponses();
    }
```
* Modifiers - 
    * view - if you are not changing any variables that belong to the contract and only returning a value then you can add the "view" modifier to the function to let the Solidity Compiler know 
    * pure - if you are not changeing any variables AND you aren't using any variables in the contract and only returning a value then you can use the "pure" modifier to the function.
```
function addTwoNumbers(uint _firstNumber, uint _secondNumber) public pure returns(uint){
    return _firstNumber + _secondNumber;
}

string greeting = "Hello World!"
function sayHello() public view returns (string memory){
    return greeting;
}
```

## Built in Functions - 
* msg.sender - returns the address of the account that is calling the contract.
```

mapping(address => Person) addressBook;

function addPersonToAddressBook(string _name, uint _age) {
    addressBook[msg.sender] = Person(_name, _age);
}

function getMyName() public view returns (string){
    return addressBook[msg.sender].name;
}
```
* require - function to validate something before continuing with the next part of code
    * NOTE: To see if a mapping exists, you can check to see if does not equal 0.  i.e. require(addressBook[msg.sender] == 0);
```
function divideTwoNumbers(uint _x, uint _y) public view returns (uint) {
    require (_y <> 0);
    return _x / _y 
}
```
* keccak256(bytes) - hash function - a Hash function is a function that converts one value into another value.  A hash function should create a completely different output when any change to the input occurs but should always create the same output when the same input is used.
    * The keccak256 hash function takes an input and outputs a 256 bit hexadecimal number
    * this is an INSECURE random-number generator.  Do not use it if you are using hashing for security reasons.
    * To pass in bytes from a string, use the abi.encodePacked method: keccak256(abi.encodePacked("this is a string"));
```
function _generateRandomDna(string memory _str) private view returns (uint) {
    uint rand = uint(keccak256(abi.encodePacked(_str)));
    return rand % dnaModulus;
}
```

## Inheritance
* A contract can include code from another contract by using inheritance.  
```
contract Animal {
    function walk(uint _numberOfSteps) public {}
}

contract Dog is Animal {
    // because Dog is inheriting Animal, this contract automatically includes a public function called walk so you dont need to write a new one here
}

contract Cat is Animal {
    // because Cat is inheriting Animal, this contract automatically includes a public function called walk so you dont need to write a new one here
}
```

## Import 
* A contract can import another contract using the "import" statement
* import uses physical relative location to the file doing the importing (so folder/file organization is important)
```
// assume there is a contract called animal.sol in the same folder as this contract
import "./animal.sol";

contract Dog is Animal {

}
```

## Interacting with Contracts
* To interact with another contract on the blockchain, need to: 
    * define an Interface signature that reflects the communication pathways to the contract we are communicating with. This is done by making a new contract block that lists out the function headers in the target contract with a semicolon at the end.
    * instantiate the connection to that contract by passing the contract address to the Interface constructor.
* Best practice 
  * dont hard code external contract addresses.  pass them in when you are setting them up and create a function that allows you to change it (make sure that function verifies that YOU are the only one that can change that address)
```
// contract on the blockchain that we want to communicate with
contract Dog {
    function bark() public view returns (uint howManyTimesItBarked){
        howManyTimesItBarked = 7;
        return howManyTimesItBarked;
    }
}

// another contract you are writing that you are going to deploy
// define interface signature  to Dog Contract
contract IDog {
    function bark() public view returns (uint howManyTimesItBarked);
}

// Instantiate the connection to the Dog contract by passing the contract address to the interface constructor
contract AnimalTalker {
    address private _owner;

    address IDogAddress = 0x0338...; // address to the Dog Contract
    IDog dogContract = IDog(IDogAddress);

  constructor() internal {
    _owner = msg.sender;
  }

    function setDogContractAddress(address _address) external {
      require(msg.sender == _owner);
      dogContract = IDog(_address);
    }

    function talk() public {
        uint talkedThisManyTimes = dogContract.bark();
    }
}
```