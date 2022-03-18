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
* How interactions with contracts work: When you call a function on a contract, you broadcast it to a node(s) on the network as a transaction.  The nodes on the network then collect a bunch of transactions and try to solve the block (Proof of Work (PoW)).  Once a node has solved the PoW, the other nodes stop trying to solve the PoW and instead verify that the other node's list of transactions are valid and then accept the block and move on.  
* **ABI** - Application Binary Interface - its a representation of your contracts' methods in JSON format that tells Web3.js how to format function calls in a way your contract will understand
  * When you compile a contract, the Solidity compiler will give you the ABI.
* **Gas** Users have to pay every time they execute a function call to your Solidity Contract.
  * HOw much gas depends on how much you are writing/reading from the blockchain.  If you write, then all nodes need to confirm that block and add it to the chain, so writes cost more.  reading from the chain also costs gas but is not as expensive as writes.
  * How much it costs to execute a function depends on how complex that function's logic is.  Total gas cost is sum of gas costs for all individual operations. 
  * VIEW functions do NOT cost gas when they are called by an external user
  * Using STORAGE is expensive, particularly writes, so try to limit how many writes/reads to the chain actually occur by copying elements from storage to memory in functions when they need to be manipulated or returned. 

* Random Number Generation: Generating random numbers that are SECURE in Solidity is close to impossible so better to use an Oracle for that. If generating a random number isn't something critical the contract, then this would work well enough:
```  
  uint randNonce = 0;
  function randMod(uint _modulus) internal returns(uint) {
    randNonce++;
    return uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % _modulus;
  }
```

## Storage
* storage - Contract Storage - things stored here get written to the blockchain and are permanent.
    * NOTE: This information is PUBLIC.  You can read this information using web3.eth.getStorageAt and point it to the contract address. That will show you all the contract storage variables associated with this contract.        
* memory - Memory Storage  - things stored here are erased between external function calls
* calldata - Memory Storage - used for external functions.
* By default, variables declared outside of functions will be treated as storage.  variables declared in functions will be declared as memory.

## Variables
* Access 
  * public
  * private 
  * constant
* Data Types: 
    * boolean
    * int/uint - integer - unsigned integeter (defaults to uint256 but uint8, uint16, uint32, etc are options).    
    * fixed/ufixed - fixed point number
    * address - 20 byte value (size of Ethereum address)
    * address payable - same as address but has methods for transfer and send [full method/property list](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#address-related)
      * convert a regular address to a payable address using:
      ```
      function transferToOwner(){
        address _owner = 0x0038...;                                       // get the contract owner's address (doesnt have to be contract owner, this is just an example)
        address payable _ownerPayableAccount = address(uint160(_owner));  // convert contract owner's address to a payable address
        _ownerPayableAccount.transfer(address(this).balance);             // transfer money from the contract to the contract owner's account
      }

      function refundToMe() external payable {
        uint restocingFee = 0.001 ether;
        msg.sender.transfer(msg.value - restockingFee);
      }
      ```
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
      * Only use an array value for the mapping IF it is immutable.  The writes to re-order the array or manipulate the array will be VERY expensive.
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

## Iterators
* For loop
```
for (uint = 1; i< 10; i++) {

}
```

## Structs - used for logical data grouping.  A way to group variables that all describe the same thing.
```
<<<<<<< HEAD
var Election = artifacts.require("./Election.sol");
contract("Election", function(accounts){
    it("initializes with two candidates", function(){
        return Election.deployed().then(function(instance){
            return instance.candidatesCount();
        }).then(function(count){
            assert.equal(count, 2);
        })
    })
}) ;
```
**Deploying a Contract to Local Ganache** 
* Open Remix and paste in contract, compile it
* In console run: geth --http --http.corsdomain https://remix.ethereum.org command to start geth connection to remix
* In Remix, go to publish and select Web3Provider, select contract, deploy
=======
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
    * NOTE: YOu can pass a struct as an argument to private and internal functions.  
      * WHen passing a struct to a function, use the "storage" storage identifier so that a storage pointer is used.       
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
* **Function Modifiers**
* Access Modifiers
  * private - only available to that contract
  * public - available to anybody including anybody that calls the contract
  * internal - same as private, except contracts that inherit have access to it (i.e. protected in C#)
  * external - same as public, except can ONLY be called from outside the contract (cant be called by other functions inside the contract)
* Storage Indicators
  * view - only reading from storage (the chain) - if you are not changing any variables that belong to the contract and only returning a value then you can add the "view" modifier to the function to let the Solidity Compiler know 
  * pure - not reading or writing from storage (the chain) - if you are not changing any variables AND you aren't using any variables in the contract and only returning a value then you can use the "pure" modifier to the function.
```
function addTwoNumbers(uint _firstNumber, uint _secondNumber) public pure returns(uint){
return _firstNumber + _secondNumber;
}

string greeting = "Hello World!"
function sayHello() public view returns (string memory){
return greeting;
}
```
* Specialty Modifiers
  * modifier - partial functions that are used to modify other functions.  
    * Usually to check requirements before execution. 
    * Uses the keyword "modifier" instead of "function"
    * name of modifier is appended to the end of a function header to say "run the modifier before running the code in the function"
    * when it hits the "_", it returns control to the calling function
  * You can apply multiple modifiers to a function by just including them at the end (use space as separation not comma or semi-colons)
  ```
  modifier onlyOwner() {
  require(isOwner());
  _;
  }

  function setNewOner(address _address) public onlyOwner {
  ...
  }

  modifier olderThan(uint _age, uint _userId){
  require(age[_userId) >= _age]);
  _;
  }

  function canDriveCar(uint _userId) public returns (bool) olderThan(16, _userId){
  return true;
  }
  ```
  * payable - denotes that this function call can receive ether.  If this is left off and someone tries to send money to the function, an error will be thrown.
  ```
  function buyShirt(uint _shirtId) external payable {
  Shirt shirt = shirtMapping[_shirtId]; // get the shirt struct value
  require(shirt.cost > 0.001 ether);    // verify the shirt has a minimum cost to it     
  require (msg.value == shirt.cost);    // verify that the amount of money passed in is equal to the cost of the shirt
  _transferOwnership(msg.sender, _shirtId); // transfer the shirt to the person sending the payment
  }
  ```
* Parameters
  * indexed - updates logging structure so that you can filter logs by that parameter.  It creates an index in the log for that parameter
    * can mark up to 3 parameters as "indexed".  

## Libraries 
* libraries extend a type with added functionality
* "library" keyword replaces "contract" keyword
* To use a library in your contract: using <library name> for <type to extend>
  * i.e. use SafeMath for uint256

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
* require - function to validate something before continuing with the next part of code. If this fails it WILL refund the user the rest of their gas.
    * NOTE: To see if a mapping exists, you can check to see if does not equal 0.  i.e. require(addressBook[msg.sender] == 0);
```
function divideTwoNumbers(uint _x, uint _y) public view returns (uint) {
    require (_y <> 0);
    return _x / _y 
}
```
* assert - function to validate something before continuing with the next part of the code.  If this fails it WILL NOT refund the user the rest of their gas.
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
* now, seconds, minutes, hours, days, weeks, years - now returns current unix timestamp of the latest block.  the rest can be used as time units (in number of seconds) to convert a uint
```
uint lastUpdated;

function updateTimestamp() public {
  lastUpdated = now;
}

function fiveMinutesHavePassed() public view returns (bool) {
  return (now >= (lastUpdated + 5 minutes));
}
```
* selfdestruct(<owner address>) - removes code from the blockchain - any remaining Ether in the contract is sent to a designated target

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
* When using structs: 
  * Use the min sized type for what you are trying to do.  dont use a uint256 when a uint8 is good enough. 
  * Cluster like types organized from smallest to largest to save gas.  The compiler will group similar types into the same storage space.  
    * example: you have a struct with declarations in this order: uint c, uint32 a, uint32 b will cost less gas than a struct with uint32 a, uint c, uint32 b.  

## Tokens 
* A token is essentially a smart contract that implements a standard set of functions that keep track of balances and allow for transfer to/from other users.
* Best Practice: Create an interface for the token you are building and put it in it's own solidity file.  Then Import that file and have your contract inherit it and implement the interface
* For ERC20 (tokens that are used like money and are divisible so can trade fractions of them) tokens they implement: 
  * function transferFrom(address _from, address _to, uint256 _tokenId)
  * function balanceOf(address _owner)
  * mapping(address => uint256) balances;
* For ERC721 (tokens that are not divisible.  can only trade in whole units and each one has a unique id) tokens they implement: 
  * event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);
  * event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);
  * function balanceOf(address _owner) external view returns (uint256);
  * function ownerOf(uint256 _tokenId) external view returns (address);
  * function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
  * function approve(address _approved, uint256 _tokenId) external payable;
```
pragma solidity >=0.5.0 <0.6.0;

contract ERC721 {
  event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);
  event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);

  function balanceOf(address _owner) external view returns (uint256);
  function ownerOf(uint256 _tokenId) external view returns (address);
  function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
  function approve(address _approved, uint256 _tokenId) external payable;
}
```

## Security 
* overflow/underflow
  * Problem defintion: when performing a function on a number, it goes beyond the bounds of the type
  * Example: 
  ```
  // overflow example
  uint8 shortNumber = 255;  // this is the max number uint8 can hold
  shortNumber++;            // this would make shortNumber = 256 which isn't possible.  It will reset to 0 in this case 

  // underflow example
  uint8 shortNumber = 0;  // this is the lowest number a uint can hold
  shortNumber--;          // this would make shortNumber = -1 which isnt possible.    
  ```
  * Resolution: Use [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) library of Eth smart contracts to perform common functions (like math functions) 
  * import 'openzeppelin-solidity/contracts/math/SafeMath.sol'; library "SafeMath" to prevent issues like this. Copy the OpenZeppelin SafeMath sol that includes safemath library (in samples/zombie-game/contracts).  Extend the type that you want to use the safemath library with (i.e. using SafeMath for uint256)
  ```
  contract Example {
    using SafeMath for uint256;

    uint256 a = 1;
    uint256 b = a.add(2); // 1 + 2 = 3
    uint256 c = b.mul(2); // 3 * 2 = 6
  }
  ```
>>>>>>> c9328cea6d23c8a91c9344af84c7f8b7be544622
