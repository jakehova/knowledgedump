# Stateful Smart Contracts

**Stateful - Live on the chain and keep track of global and/or local state for the contract**
* Logic is evaluated at block assembly time vs stateless contracts Logic is evaluated when the transaction is submitted 
* Have specific global values and per-user values
* Contract determines how global and per-user values are modified
* Lifecycle - Stateful contracts are implemented using two TEAL programs
  * ApprovalProgram
    * Responsible for processing all application calls to the contract (exception being the clear call)
    * Only succeeds if one nonzero value is left on the stack after execution of the code
  * ClearStateProgram
    * Used by Algo accounts to remove the smart contract from their balance record
    * Only succeeds if one nonzero value is left on the stack after execution of the code
  * if either program fails then any global/local changes made will not be applied
* Deploy a stateful smart contract, you get an appid back
* Communicate with it with application transactions (as opposed to account transactions)
  * Available Transactions against App are called ApplicationCall:
    * NoOp - 
      * Generic call to execute approval program
    * OptIn - 
      * Opts user account into partipating in the SSC
      * Sets aside local storage space in the user's account that can be used by the SSC
      * **Note** - If contract does not use local state then user does NOT need to optin for it
    * DeleteApplication -     
      * Deletes the Application
      * **Note** - Can put in code to prevent this
    * UpdateApplication - 
      * Updates the TEAL programs for a contract
      * **Note** - Can put in code to prevent this
    * CloseOut - 
      * User accounts use this call to remove themselves from participating in the SSC.
      * This call can fail because of the TEAL logic which prevents the user from stopping their participation in the SSC.
    * Clear - 
      * Similar to CloseOut but will always remove the user from participating in the contract no matter if the logic fails or not
* Runtime: 
  * Gets run when someone passes an application call to the account block that contains the Stateful Contract
  * Parameters: 
    * Transaction:
      * Application ID array with max size of 2
        * Application ID = Stateful Contracts ID
        * Allows you to read those application's global state
      * Account array with max size of 4
        * In addition to the transaction sending account, you can include 4 more accounts
        * You can modify the local state for all 5 of those accounts 
      * Argument Array 
  * Each Node contains: 
    * The TEAL program
      * This is added to the node on create/update application calls
    * Stack - which interprets the TEAL code line by line
    * Global var (read only) - global variables that the TEAL program can read from 
    * Transaction Properties (read only) - properties that belong to the current transaction 
    * Temporary Scratch - used for temporary variables
    * Global State - Read/Write array of up to 64 key/value pairs that is managed by the stateful contract and available on every application call
      * Values are limited to byte[] and uint
      * 64 bytes per array
    * Local State - Read/Write array of up to 16 key/value pairs that 
      * Values are limited to byte[] and uint
      * 64 bytes per array


