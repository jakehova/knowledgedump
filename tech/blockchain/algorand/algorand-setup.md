# Setup Options

**Using Docker**
- https://github.com/algorand/sandbox
  - clone the github account
  - open git bash
  - run "./sandbox up" to run docker compose and bring up containers

**Install Directly On Windows**
* [Configure Windows Environment](https://developer.algorand.org/tutorials/compile-and-run-the-algorand-node-natively-windows/)
* [Download MSYS2](https://www.msys2.org/)
* Configure Environment
  * Install and Configure msys2:
    * Update package database and base packages: pacman -Syu
    * Update the rest of the packages: pacman -Su
    * Install base dev packages: pacman -S --needed base-devel 
    * install gcc and make: pacman -S --needed mingw-w64-x86_64-toolchain
  * Exit and then open **MSYS2 MinGW 64-bit** (installing msys2 generates 3 different consoles.  using the 64 bit one is mandatory)
    * install git and go: pacman -S --disable-download-timeout --noconfirm git mingw-w64-x86_64-go
  * Exit and then open **MSYS2 MinGW 64-bit** 
    * update bashrc to point to the local go install: echo 'export GOPATH=$HOME/go' >> $HOME/.bashrc
  * Exit and then open **MSYS2 MinGW 64-bit** 
  * Clone the algorand blockchain codebase: git clone https://github.com/algorand/go-algorand
  * switch to that directory: cd go-algorand
  * run the configure dev shell script: ./scripts/configure_dev.sh
  * build the go-algorand project: make

**Install the Node**
  * create a directory off the C drive: mkdir c:\AlgorandNode
  * change into that directory: cd c:\AlgorandNode
  * copy the compiled files from the make to the algorandnode folder: COPY /Y C:\msys64\home\%USERNAME%\go\bin .
  * make a subdirectory named data: mkdir data
  * change into that directory: cd data
  * copy the genesis file to data: COPY /Y C:\msys64\home\%USERNAME%\go-algorand\installer\genesis\testnet\genesis.json .
    * This copies the testnet genesis file but you can copy the beta/main by changing "testnet" to "betanet" or "mainnet" respectively
  * copy the example configuration file and rename it config: COPY /Y C:\msys64\home\%USERNAME%\go-algorand\installer\config.json.example config.json
  * edit the config file: 
    * [Node Config Dictionary](https://developer.algorand.org/docs/reference/node/config/)
    * Update EndpointAddress to have a locally accessible port: 120.0.0.1:8101
      * If you want to be accessble publicy then put just the port: :8101
      * If you want to be accessible locally but from sources that arent just localhost (i.e. postman): 0.0.0.0:8101
    * Update DNSBootstrapID to match the appropriate testnet network: testnet.algodev.network
    * Update EnableDeveloperAPI value to true
    * If you want to store all the blockchain instead of the latest 1000 blocks, then change Archival to true
      * If storing all, then you need at least 200GB of free space
  * configure kmd
    * in algorand node's <data> folder:
      * create kmd-<kmd version> folder
        * in kmd folder create kmd_config.json File
          * create json object with: 
            * address: 0.0.0.0:7833
            * allowed_origins: ""
            * session_lifetime_secs: 60

**Run the node**
  * Open Powershell and navigate to C:\AlgorandNode
  * Start the node: "./goal node start -d data"
  * Verify the node is running: "./goal node status -d data"
    * Stop the node: "./goal node stop -d data"
  * Perform a fast catchup: 
    * Go to the appropriate link and copy the catchpoint provided
      * BetaNet https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/betanet/latest.catchpoint
      * TestNet https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint
      * MainNet https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/mainnet/latest.catchpoint
    * Run: ./goal node catchup <Catchpoint value> -d data
  * Updating a node: ./update.sh -d data
    * force an update ./update.sh -i -c stable -d data

**Usage**
  * goal, kmd, algokey are all in the AlgorandNode folder
  * Token to use for api: 
    * Key: "X-Algo-API-Token"
    * Value: <Value in C:\ALgorandNode\data\algo.token file>
