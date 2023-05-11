# Embeddings

## What are they
Embeddings are encodings of text into a floating point array.  The floating point array is called a vector. The algorithm uses multiple dimensions to establish a "meaning" of the text. 

In the case of text embeddings, an algorithm is used to generate the vector.  The vector is then stored in a vector database.  In the db, phrases that are similar will be proximal to other phrases that comes close in meaning.  So if you had 3 phrases: 1) Jacob likes hot dogs 2) Mustand and ketchup are condiments for hot dogs 3) A pool is filled with chlorine water, the first two would be proximal to each other in the database and the third one wouldn't be close.  

## Solutions
Embedding Generation: 
    * OpenAI has an api that generates embeddings from phrases.  The algorithm their api uses is called: "text-embedding-ada-002".  The embeddings generated have a dimensionality of 1536 dimenions.  
    * Llama index 
Embedding Storage: 
    * PineconeDB is a vector DB that can be used to store vectors
    * Supabase has a vector DB

## Theory 
Linear algebra offers 3 methods for determining similarity: 
    * Cosine Similarity
    * Dot Product
    * Euclidian Distance
These methods can be applied to vectors in a database with a embedding of a query term to determine what vectors in the database are most similar.  





