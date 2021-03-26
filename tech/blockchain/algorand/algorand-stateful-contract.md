# Stateful Smart Contracts

**Stateful - Live on the chain and keep track of global and/or local state for the contract**
* Have specific global values and per-user values
* Contract determines how global and per-user values are modified
* Contract code uses special Algorand transactions to call stateful smart Contracts
* Accounts make ApplicationCalls to stateless smart contract
* Lifecycle - Stateful contracts are implemented using two TEAL programs
  * ApprovalProgram
    * Responsible for processing all application calls to the contract (exception being the clear call)
    * Only succeeds if one nonzero value is left on the stack after execution of the code
  * ClearStateProgram
    * Used by Algo accounts to remove the smart contract from their balance record
    * Only succeeds if one nonzero value is left on the stack after execution of the code
  * if either program fails then any global/local changes made will not be applied
* Available ApplicationCall:
  * NoOp - 
    * Generic call to execute approval program
  * OptIn - 
    * Opts user account into partipating in the SSC
    * Sets aside local storage space in the user's account that can be used by the SSC
  * DeleteApplication -     
    * Deletes the Application
  * UpdateApplication - 
    * Updates the TEAL programs for a contract
  * CloseOut - 
    * User accounts use this call to remove themselves from participating in the SSC.
    * This call can fail because of the TEAL logic which prevents the user from stopping their participation in the SSC.
  * ClearState - 
    * Similar to CloseOut but will always remove the user from participating in the contract no matter if the logic fails or not