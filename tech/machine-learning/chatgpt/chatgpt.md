# ChatGPT

## How to use it with your own data
* ways to query chatgpt: 
    * stuffing - taking a chunk of text to apply context to your question and then ask question

### Process
* Ingestion/Embedding Process - index documents 
   1) take document and run it through an embedding model
   2) embedding model generates a vector
   3) **optional** store the vector in a vector db (i.e. pinecone)
   4) tools: 
      * langchain
      * llamaindex
* Query Process - query through documents
   1) question is run through encoder to generate a vector
   2) search vector is run against index to find relevant documents
   3) use relevant documents to establish context with chat gpt
   4) ask question given context 

## Vector DB
* Vector DBs stores data as "vectors".
  * The same word can have different meanings, they should be further apart in the vector db
  * Different words or groups of words can have the same meaning, they should be closer together in the vector db
* when a search is run in a db: 
  * The search query is encoded into a vector
  * The vector gets a fence of some size around on it depending on how precise you want it to be
  * Any other vectors that are in the fence are considered matches to varying degrees (how close one vector is to the search vector = quality of the match)

## Langchain
* Ingestion/Embedding
  * Document Loaders - Load text from files, webpages, notion, etc into common format
    * Format includes metadata and text 
* Query Process
  * Question to - Embedding Model to generate vector
  * Query pinecone to get relevant context(s)
  * run relevant context 
* Query Engines
    * VectorDBQA - handles query process like above
    * VectorDBQA with sources - includes answer + source of data
    * ChatVectorDBQA - includes history of chat with more context with the question process 
* Considerations to improve searching
  * Chunking
    * Split to about 1000 characters 
    * Allow for some overlap

## Proprietary data
* Generte a new model if you want to train a new model on proprietary data. [Hugging Face](https://huggingface.co)
* 

## Development
* python tools (pip install -qU): langchain openai tiktoken pinecone-client[grpc] datasets apache_beam 