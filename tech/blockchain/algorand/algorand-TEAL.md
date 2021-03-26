# TEAL

**What**
* [Documentation](https://developer.algorand.org/docs/reference/teal/specification/)
* [Python Equivalent](https://pyteal.readthedocs.io/en/stable/)
* Primary purpose is to return true or false
* Will return true if and only if one positive value is left on the stack at the completion of execution.  Returns false otherwise.
* For stateless contracts, true/false determines whether to approve a transaction
* For stateful contracts, code may modify global and/or local state. if it returns false then any changes to global and/or local state will be cancelled.
* Uses [OpCodes](https://developer.algorand.org/docs/reference/teal/opcodes/) to operate on stack values 
  * Some opcodes are only available to certain contract types (stateful or stateless)
  * In OpCode definition, if "Mode" attribute is present then it is restricted to one or the otherwise.
  * If Mode == Application then only can be used in Stateful contracts
  * If Mode == Signature then only can be used in Stateless contracts