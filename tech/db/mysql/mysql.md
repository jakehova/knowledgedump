## User
* list users: 
    * SELECT User, Host FROM mysql.user;
* see a user permissions: 
    * SHOW GRANTS for <username>
* create user: 
    * CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';
* grant permissions to user: 
    * GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, PROCESS, REFERENCES, INDEX, ALTER, SHOW DATABASES, CREATE TEMPORARY TABLES, LOCK TABLES,
      EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER ON *.* TO
      '<username>'@'%' WITH GRANT OPTION;
* remove user (% = host): 
    * DROP USER '<username>'@'%';
