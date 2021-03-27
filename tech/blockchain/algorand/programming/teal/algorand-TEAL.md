# TEAL

**What**
* [Documentation](https://developer.algorand.org/docs/reference/teal/specification/)
* [Python Equivalent](https://pyteal.readthedocs.io/en/stable/)
* .teal extension
* Primary purpose is to return true or false
* Will return true if and only if one positive value is left on the stack at the completion of execution.  Returns false otherwise.
* For stateless contracts, true/false determines whether to approve a transaction
* For stateful contracts, code may modify global and/or local state. if it returns false then any changes to global and/or local state will be cancelled.
* Uses [OpCodes](https://developer.algorand.org/docs/reference/teal/opcodes/) to operate on stack values 
  * Some opcodes are only available to certain contract types (stateful or stateless)
  * In OpCode definition, if "Mode" attribute is present then it is restricted to one or the otherwise.
  * If Mode == Application then only can be used in Stateful contracts
  * If Mode == Signature then only can be used in Stateless contracts
  * store/load => used to interact with scratchpad
    * store 1 => pop the top stack and store that value in position 1 of scratch pad
    * load 1 => push position 1 of scratch pad to stack 

**How**
* [Overview](https://www.youtube.com/watch?v=9EpGKexKeMk)
* Bytecode based stack language
  * Push arguments on the stack
  * Pop and execute opcode when an opcode is read
* Returns true/false (one positive value left on stack = true)
* More than 70 OpCodes
* Has access to ASA/Algo Balances
* Read all transactions in a group
* Stateful - Global/Local storage calls
* Stateless - Signature verification
Example 1: 
  ```
  #pragma version 2

  txn Amount
  int 1000
  >=
  byte "counter"
  app_global_get
  +

  1) Push txn Amount on stack
    a) txn is an opCode that pushes the value of the transaction field on to the stack (ie transaction["Amount"])
  2) Push int 1000 on the stack 
    a) pushes the uint 1000 on to the stack
  3) OpCode >= encountered so pop 1000 and txnAmount off the stock and apply opcode => transaction[Amount] >= 1000 and then pushes the result on to the stack (1 for true 0 for false)
  4) push byte "counter"
  5) OpCode app_global_get encountered so pop byte "counter" off stack and retrieve "counter" from global state and then push result on to stack 
  6) OpCode + encountered so pop twice and execute op, then push result back on stack 
  ```
Example 2: branching example
```
#pragma version 2

txn NumAppArgs  // push tx["NumAppArgs]
int 2           // push 2
==              // pop twice and run opcode == against them
                //  push result
bz fin          // pop once and if its 0 then go to "fin"
                //  else continue to next line
byte "myarg"    // push string "myarg"
txn ApplicationArgs 0 //push tx[ApplicationArgs[0]]
==              // pop twice and compare 
                //  push result
bnz check_second_arg  // pop once and if positive then go to
                      //  else continue to next line
int 0           // push uint 0
return          // pop and return respective true/false
check_second_arg: // define label entry point "check_second_arg"
txn ApplicationArgs 1 // push txn[ApplicationArgs[1]]
btoi            // convert byte array to int (?? he passed in an int and for some reason it converted it to byte array)
int 100         // push 100
>               // pop twice and compare (first pop value goes on the right of the argument)
bnz fin         // pop once and if positive then go to fin
                  // else go to next line
int 0           // push uint 0
return          // pop and return respective true/false
fin:            // define label entry point "fin"
int 1           // push 1
return          // pop and return respective true/false
 
```

**Example Note** 
* b, bnz, bz are branching options (they do pop the stack)
  * bnz => if theres a positive value at top of stack then branch to the label, otherwise keep going
  * bz => if theres a 0 at the top of thes stack then branch to the label, otherwise keep going
  * b => always branch to the label

**State Accessors**
* txn <transaction property name> => current transaction properties
  * txn TypeEnum => returns type of transaction
    * usually followed by "int appl" which converts that type enum value to integer
  * txn OnCompletion => return application transaction sub-type
    * NoOp, etc
* global <global name> => returns global var 
* gtxn <number representing index> <transaction property name> => use gtxn instead of txn when there are multiple transactions passed in to the stateful contract
* app_local_get & app_local_put => OpCodes to put pop two elements 
* 

**Notes**
* [Resolving issue with running tealdbg in windows](https://github.com/algorand/go-algorand/issues/1809) and [another resolution](https://github.com/algorand/go-algorand/pull/1977)

**Debugging**
* [Debugging](https://developer.algorand.org/docs/features/asc1/debugging/)
* Ways to debug: 
  * tealdbg
    * command line tool to launch a debug session 
    * [Github](https://github.com/algorand/go-algorand/blob/master/cmd/tealdbg/README.md)
    * setup: 
      * 
  * goal clerk dryrun-remote
    * Ouputs a line by line result of the evaluation of the smart contract