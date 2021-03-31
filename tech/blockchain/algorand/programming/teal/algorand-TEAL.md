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
* You cant get the current time, but you can get the last block creation time which should bring you within a few seconds by addressing the global LatestTimestamp
  * Format is in Unix timestamp (seconds since 1/1/1970): 

| Human Readable Time | seconds |
| --- | --- |
| 1 Hour | 3600 Seconds | 
| 1 Day | 86400 Seconds |
| 1 Week | 604800 Seconds | 
| 1 Month | 2629743 |
| 1 Year | 31556926 Seconds |


**Installing on Windows**
* [Configure Windows Environment](https://developer.algorand.org/tutorials/compile-and-run-the-algorand-node-natively-windows/)
* [Download MSYS2](https://www.msys2.org/)
  * Install and Configure msys2:
    * Update package database and base packages: pacman -Syu
    * Update the rest of the packages: pacman -Su
    * Install base dev packages: pacman -S --needed base-devel 
    * install gcc and make: pacman -S --needed mingw-w64-x86_64-toolchain
    * install Git: pacman -S --disable-download-timeout --noconfirm git 
      * Installs in the msys64/usr/bin directory
    * install go: pacman -S --disable-download-timeout --noconfirm mingw-w64-x86_64-go 
    * install gcc: pacman -S gcc vim make    
    * install golint: go get -u golang.org/x/lint/golint
    * install stringer: go get -u golang.org/x/tools/cmd/stringer
    * install swagger: go get -u github.com/go-swagger/go-swagger github.com/go-swagger/go-swagger/cmd/swagger
    * install msgp: go get -u github.com/algorand/msgp
    * instal sqlite3: pacman -S sqlite3
  * Exit from the msys terminal and then re-open it. 
  * Update the $HOME/User/.bashrc file by appending to the end: 
    * path to the go exe: export PATH="/mingw64/lib/go/bin":$PATH
    * the path to go output: export GOPATH=$HOME/go
  * Exit from the msys terminal and then re-open it
  * Clone the go-algorand git repo: git clone https://github.com/algorand/go-algorand
    * install required libraries for algo(./scripts/configure_dev.sh -f): pacman -S --disable-download-timeout --noconfirm git automake autoconf m4 libtool make mingw-w64-x86_64-gcc mingw-w64-x86_64-boost mingw-w64-x86_64-python mingw-w64-x86_64-jq unzip procps
    * install dependencies for the algo libraries 
      * ./scripts/configure_dev-deps.sh
  * Run make: make
  * 

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

