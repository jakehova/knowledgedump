# Raw Models

## Types
* Layers Model
    * retain higher level building blocks for ease of use and debugging 
    * NOT optimized
* Graph Model 
    * highly optimized
    * can combine multiple poerations in one batch

## How
* [Documentation](https://js.tensorflow.org/api/latest/#Models-Loading)
* Stored in two file
    * model.json 
        * metadata about model type, architecture, config details
        * declares a "format" key that has either layers model or graph model
    *  one or more ".bin" files.  Typically have "shard<#>of<#>.bin"
        * each bin file is 4MB or less

### Loading a Raw Model
    * tf.loadGraphModel(<path to model>)
    * tf.loadLayerModel(<path to model>)


### Saving a model
    *  Can always save a model for use offline using the command: model.save(<localhost>)

## Inspect
* can use ```model.summary()``` command to provide information about the model.  Provides:
    * model layers
    * output shapes at each layer
    * number of params in each layer
    * total number of params
    * number of trainable and non-trainable params


## Sample Code
```
const MODEL_PATH = 'https://storage.googleapis.com/jmstore/TensorFlowJS/EdX/SavedModels/sqftToPropertyPrice/model.json';
let model = undefined;

async function loadModel() {
  model = await tf.loadLayersModel(MODEL_PATH);
  model.summary();

  // Create a batch of 1.
  const input = tf.tensor2d([[870]]);

  // Create a batch of 3
  const inputBatch = tf.tensor2d([[500], [1100], [970]]);

  // Actually make the predictions for each batch.
  const result = model.predict(input);
  const resultBatch = model.predict(inputBatch);

  // Print results to console.
  result.print();  // Or use .arraySync() to get results back as array.
  resultBatch.print(); // Or use .arraySync() to get results back as array.

  input.dispose();
  inputBatch.dispose();
  result.dispose();
  resultBatch.dispose();
  model.dispose();
}

loadModel();
```
* In this example: 
    * A total of 6 tensors are created when the code is run.
    * 2 tensors are created when the model loads. The 'model.dispose()' method disposes of this tensor.
    * 2 tensors are created, one for each input. The input.dispose() and inputBatch.dispose() methods dispose of these tensors.
    * 2 tensors are created and returned as outputs. The result.dispose() and 'resultBatch.dispose()' methods dispose of these tensors.
