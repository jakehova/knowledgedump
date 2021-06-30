# TEAL

**What**
* [Documentation](https://developer.algorand.org/docs/reference/teal/specification/)
* [Python Equivalent](https://pyteal.readthedocs.io/en/stable/)
* [Transaction Definitions](https://developer.algorand.org/docs/reference/transactions/#asset-transfer-transaction)
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
* 

**How**
* [Overview](https://www.youtube.com/watch?v=9EpGKexKeMk)
* Bytecode based stack language
  * Push arguments on the stack
  * Pop and execute opcode when an opcode is read
* Returns true/false (one positive value left on stack = true)
* More than 70 OpCodes
* Has access to ASA/Algo Balances
* Read all transactions in a group
* Stateful - Need for stateful information that can be stored globally or locally
* Stateless - Escrow or Delegated Signature use cases

**Example Note** 
* b, bnz, bz are branching options (they do pop the stack)
  * bnz => branch if not zero (goto label if !0 is at top of stack)
  * bz => branch if zero (goto label if 0 is at top of stack)
  * b => branch always (goto)

**State Accessors**
* txn <transaction property name> => current transaction properties
  * txn TypeEnum => returns type of transaction
    * usually followed by "int appl" which converts that type enum value to integer
  * txn OnCompletion => return application transaction sub-type
    * NoOp, etc
* global <global name> => returns global var 
* gtxn <number representing index> <transaction property name> => use gtxn instead of txn when there are multiple transactions passed in to the stateful contract
* app_local_get & app_local_put => OpCodes to put pop two elements 

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

**Debugging**
* [Debugging](https://developer.algorand.org/docs/features/asc1/debugging/)

* Ways to debug: 
  * tealdbg
    * command line tool to launch a debug session 
    * [Github](https://github.com/algorand/go-algorand/blob/master/cmd/tealdbg/README.md)
    * go to algorandnode install folder (- [[algorand-setup]]Setup) and open a command line
    * run the command: ./tealdbg debug <path to teal file> -d <path to dry run file (msgpak)> 
  * generate debug files using js sdk.  
    * tealdbg.msgpak file can be passed to ./tealdbg to debug the session in browser. 
    * dryrun response will return the history of the execution including where it failed (if it did)
    * code to generate tealdbg.msgpak and dryrun response: 
```
async dryrunMultipleTxnDebugging(
    algodclient,
    lsigOfContract,
    unsignedTransactions,
    tealContractFileContents,
    outputToFile
  ) {
    let sources;
    let groupTxn = [];

    for (let i = 0; i < unsignedTransactions.length; i++) {
      groupTxn.push({ txn: unsignedTransactions[i] });
    }
    // sources are related to the source teal program.  so in most cases 
    //  data will be the teal contents.  lsig, approv, or clearp depending on 
    //  what type of contract code it is.  
    sources = [
      new algosdk.modelsv2.DryrunSource('lsig', data.toString('utf8'), 0),
    ];

    const dr = new algosdk.modelsv2.DryrunRequest({
      txns: groupTxn,
      sources: sources,
    });
    let dryrunResponse = await algodclient.dryrun(dr).do();

    if (outputToFile) {
      const drRequestPath = path.join(
        __dirname,
        'app',
        'algo',
        'contract',
        'tealdbg.msgpak'
      );
      let blob = algosdk.encodeObj(dr.get_obj_for_encoding());
      fs.writeFileSync(drRequestPath, blob );      
      
      const dumpFilePath = path.join(
        __dirname,
        'app',
        'algo',
        'contract',
        'dryRunDump.json'
      );
      fs.writeFileSync(dumpFilePath, JSON.stringify(dryrunResponse));
    }
    return dryrunResponse;
  }
```
  * goal clerk dryrun-remote
    * Ouputs a line by line result of the evaluation of the smart contract
  * Ouput all the individual transactions to individual files: 
    * if signed by a regular acct: fs.writeFileSync('./my2.tx', signedUnfreezeTxn);
    * if signed by an lsig: fs.writeFileSync('./my3.tx', signedOptInTx.blob);
  * 


[//begin]: # "Autogenerated link references for markdown compatibility"
[algorand-setup]: ../../algorand-setup "Setup Options"
[//end]: # "Autogenerated link references"