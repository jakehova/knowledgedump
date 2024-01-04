## Document Loaders
* [Langchain](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html)


# Evaluation of LLM
## Perplexity
* quantifies how well a language model predicts a given sequence of words
  * easier read: perplexity represents the avg number of choices a language model has for predicting the next word
* lower the score, better the model
* `Perplexity = 2^(-Σ(log2(p(w)))`
  * p(w) is the probability assigned by the language model to each word in the test set.

## Burstiness
* 