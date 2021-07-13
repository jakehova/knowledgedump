# Prisma

- npm install prisma --save-dev
- npm install @prisma/client
  - type-safe db client thats generated from Prisma model definition. 
  - Can expose CRUD operations that are tailored specifically to your models
  - update the client with the latest model: prisma generate 
- NOTE: use npx when wanting to run something in the local nodemodules
- npx prisma init
- migrating db: npx prisma migrate dev --name init
  - this creates a "migrations" directory under the prisma folder
- configure db in prisma/schema.prisma file: 
```
datasource db {
  provider = "sqlite"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}
```
- configure ./env: 
```
# DATABASE_URL="postgresql://johndoe:randompassword@localhost:5432/mydb?schema=public"
# DATABASE_URL="file:./dev.db"
```
- 