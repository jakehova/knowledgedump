# Stateless Contract

**Stateless - Used to replace signature authority**
  * Instead of signing like a regular transaction, the signing occurs via logic execution (called a LogicSignature)
  * Two Primary Modes of Use: Contract Accounts and Signature Delegation Authority
    * Contract Accounts - act like an escrow account
      * When compiled it produces an Algorand address
      * Can receive Algos or ASAs
    * Delegate Signature Authority - Logic of the contract is signed by an account or multi-sig account
      * The logic is then shared with another account that can use it to withdraw Algos or ASAs from the signing account based on the logic of the contract