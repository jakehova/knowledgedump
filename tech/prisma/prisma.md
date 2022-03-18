# Prisma

## What 
Used to generate a database from code and perform general database transactions that are typed.

## Setup
npm install prisma -D
npx prisma init

## Model
* ID Fields: 
  * id   Int     @id @default(autoincrement())
  * id   String  @id @default(uuid())
* Data Types: String, DateTime, Int, Boolean
* Relationships: 
  * Create a field in each of the tables that have the relationship by using the Model Type Name and whether its an array or not
    * This field does NOT get persisted to the database
  * Add the "@relation(fields:[<foreign key>] references:[<primary key>])" data annotation field 
  * Create a field of native type that holds the actual relationship field
**Example**
```
model User {
  id     Int     @id @default(autoincrement())
  posts  Post[]
}

model Post {
  id        Int   @id @default(autoincrement())
  author    User  @relation(fields: [authorId], references: [id])
  authorId  Int   // relation scalar field  (used in the `@relation` attribute above)
}
```
  
