# Stateless Contract

**Stateless - Used to replace signature authority**
  * Logic is evaluated when the transaction is submitted vs stateful where the logic is evaluated at block assembly time.
  * Two Primary Modes of Use: Contract Accounts and Signature Delegation Authority
    * **Contract Accounts - act like an escrow account**
      * When compiled it produces an Algorand address
      * Can receive Algos or ASAs
      * How it works: 
        * Compile TEAL code and it creates an Algorand account
        * Works just like any account.  you can fund it, spend from it, run transactions with it.
        * Difference is whenever something leaves the account, then the TEAL logic is run and if it evaluates to true, then the transaction is approved.  
      * Used For: 
        * Escrows
        * HTLC
        * Split Payments
        * Limit Orders
    * **Delegate Signature Authority - Logic of the contract is signed by an account or multi-sig account**
      * The logic is then shared with another account that can use it to withdraw Algos or ASAs from the signing account based on the logic of the contract
      * How it works: 
        * Sign the TEAL logic with your account => creates a Logic Signature
        * Ex: You create TEAL logic that says, allow Gas Company Algorand Account to deduct up to $300 from my Algo account every month.  You sign that Logic and give the signed logic file to the Gas Company. They can submit a transaction to your Algorand account and sign it with the signed logic file. 
      * Used For: 
        * Recurring Payments
        * Limited Account Authority
* Runtime: 
  * Gets run by passing a transaction that includes the TEAL program for the contract and any optional arguments 
  * Parameters: 
    * TEAL program
    * Argument array
  * Each Node contains: 
    * Stack - which interprets the TEAL code line by line
    * Global var (read only) - global variables that the TEAL program can read from 
    * Transaction Properties - properties that belong to the current transaction 
    * Temporary Scratch - used for temporary variables

  

