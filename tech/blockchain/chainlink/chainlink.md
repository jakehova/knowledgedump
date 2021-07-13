# Chainlink

## What



## Digital Ocean Example connector
VM Root PWD: y%3s1L#EjF9y
DB Information: 
    username = doadmin
    password = bc117hpinkie0xda
    host = chainlink-kovan-db-do-user-9517468-0.b.db.ondigitalocean.com
    port = 25060
    database = defaultdb
    sslmode = require

    PGPASSWORD=bc117hpinkie0xda pg_restore -U doadmin -h chainlink-kovan-db-do-user-9517468-0.b.db.ondigitalocean.com -p 25060 -d defaultdb 

Open Ubuntu Terminal: 
    * ssh root@67.205.173.202 -L 6688:localhost:6688
        * localhost mapping maps port 6683 of VM to localhost:6683
    * type in VM root PWD
    * type logout to exit

# Setting Up A validator Node
    * Create a VM
    * Create a postgres DB
    * Put them both in a private network that have access to each other

# Accessing ETH Node
    * Go to [Alchemy](https://www.alchemy.com/)
    * Create Ethereum app (tie it to Kovan for test network)
    * Copy WebSocket URL (wss://eth-kovan.ws.alchemyapi.io/v2/6DLca5DUwA-YW8V_o2DtDDLAHLZF7RJA)

# Configure VM
    * SSH into VM created above
    * Run: 
        * curl -sSL https://get.docker.com/ | sh => downloads and installs docker
        * sudo usermod -aG docker $USER => allow currently logged in user to run commands against docker
        * exit => terminal needs to be rebooted to have changes persisted
        * Log back in
    * Create kovan directory to hold Chainlink data: mkdir ~/.chainlink-kovan
        * do "ls -al" to list all directories **Note** folders that start with a "." are considered system files so they are hidden
    * Create environment file
        ```
        echo "ROOT=/chainlink
        LOG_LEVEL=debug
        ETH_CHAIN_ID=42
        MIN_OUTGOING_CONFIRMATIONS=2
        LINK_CONTRACT_ADDRESS=0xa36085F69e2889c224210F603D836748e7dC0088
        CHAINLINK_TLS_PORT=0
        SECURE_COOKIES=false
        GAS_UPDATER_ENABLED=true
        ALLOW_ORIGINS=*" > ~/.chainlink-kovan/.env
        ```
    * Update URL with Alchemy Websocket address: 
        ```
        echo "ETH_URL=wss://eth-kovan.ws.alchemyapi.io/v2/6DLca5DUwA-YW8V_o2DtDDLAHLZF7RJA" >> ~/.chainlink-kovan/.env
        ```
    * Setup Remote DB URL:
        * Get remote db url from DO -> DB -> ConnectionString
        ```
        echo "DATABASE_URL=postgresql://doadmin:bc117hpinkie0xda@chainlink-kovan-db-do-user-9517468-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require" >> ~/.chainlink-kovan/.env
        ```
    * Pull the chainlink docker image and run it  docker container.  : 
        * Configure it witht he env file created above and run it locally (to the VM)
        ```
        cd ~/.chainlink-kovan && docker run -p 6688:6688 -v ~/.chainlink-kovan:/chainlink -d --env-file=.env smartcontract/chainlink:0.9.4 local n
        ```
        * Create/Store Password for validator keys: 62Chv%99X3&E
        * Add email and Create New Password for API: jacob@1p.solutions/1a%8Ic9pcZ6j
    * Add shorcuts for controlling docker container:
        * type vim ~/.bashrc
        * type "I" to enter edit mode
        * add the following code to the end of the bashrc file: 
        ```
        alias restart_kovan_primary='docker pull smartcontract/chainlink:0.9.4; docker kill kovan-primary; yes | docker system prune; cd ~/.chainlink-kovan && docker run --restart=always -p 6688:6688 -d --name kovan-primary -v ~/.chainlink-kovan:/chainlink -it --env-file=.env smartcontract/chainlink:0.9.4 local n -p ~/.chainlink-kovan/.password'

        alias tail_kovan_primary='docker logs kovan-primary --tail 10'

        alias follow_kovan_primary='docker logs kovan-primary --follow'
        ```
        * configure the command line to use this bashrc file: "source ~/.bashrc"
        * create password file
            * create a password file: touch /chainlink-kovan/.password
            * update password file with validator keys password
        * use "restart_kovan_primary" alias to kill the chainlink process and restart it.
        * use "tail_kovan_primary" to view the last 10 logs 
        * use "follow_kovan_primary" to view logs as they happen
