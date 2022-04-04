# Machine Learning

## What is it 
* Numbers In -> Numbers Out.  Computers only understand numbers so all inputs have to be numbers.  So both input and output of a model will be numerical.   
* All models are initially **untrained**

## Types
* Supervised Learning - Train by labeled examples
    * You provide data and label them in categories (i.e. you provide weight & color attributes for fruit and then you label the fruit with it's name.)
    * Only works well if you provide diverse and well-labeled data.  
    * Steps: 
        1) Provide numerical input data representing the objects and their labels
        2) Train the model using a machine learning algorithim to learn a line that can separate the different types of objects
        3) Have the model classify each object as a labled object  based on which side of the line it falls on.
    * Used for: Spam detection, text categorization, object recognition
* Unsupervised Learning - Finding patterns in unlabled data.  Leverages clustering to group items that closely share similar measured attributes.
    * Used for: Clustering problems like Product Recommendation Engines
* Reinforcement Learning - Set a reward function and let ML program figure out the best way to solve. 
    * Trial and Error with accurate "trials" providing rewards.  
    * Used for Gaming development and robotics

## How to Train ML systems
1) Identify features and attributes of the objects you want to train against
    a) The # of features/attributes = # of dimensions
    b) image recognition requires each pixel being a feature 
    c) for a high # of features the computer can use a hyperplane (one dimension less than the features you have) to separate instead

### Classification vs Regression
* Classification - trying to predict from features 
* Regression - trying to predict a number from other numbers

## Ways to use 
* Use Pre-Trained models - resuse state of the art models that already exist (i.e. monitoring body movements models for skeletal tracking)
* Transfer Learning - take a pre-trained models and re-train  it to do what you need
* Custom Models - Writing your own models from a blank canvas 
* **Note** - Tensorflow.js supports the execution of other forms of Tensorflow models through the command line converter.  This helps to see what has been done on other platforms.
* Tools: 
    * MediaPipe: a C++ framework for building applied ML pipelines that some researchers choose to use 
    * TensorFlow Hub: repository of trained ML models that can be reused
    * TensorFlow Lite: Google's ML framework that focuses on mobile native and IoT devices.  **Note:** TensorflowJS can also run on these platforms but TensorFlow Lite is optimized for them.
    * ONNX: The Open Neural Network Exchange is an open-source AI ecosystem of tech companies and research orgs.  ONNX establishes open standards for representing ML algorithms in a way agnostic to the library it was written in. 

## Selecting a Model
* Understand the problem by asking the client questions: 
    * What type of app does the customer need
    * is it a web app? does it need to run on the client-side or the server-side?
    * how important is privacy, speed, accuracy?
* Populate the list of models that can be used to solve the problem
* Use Inference speed (lower the better), file size of the model, RAM in MB to compare models
    * calc inference speed: 
    ```
    async function calculateInferenceSpeed() {
        //  Record timestamp before model execution
        const timeStart = performance.now();
        // Execute model
        let results = await useSomeModel();
        // Record timestamp after model execution
        const timeEnd = performance.now();
        // Calculate time taken for model execution
        const timeTaken = timeEnd - timeStart;
        console.log(`Time taken ${timeTaken} ms.`);
        // Convert ms to FPS
        console.log(`Frames per sec: ${1000 / timeTaken}`);
    }
    ```
    * file size: check model's documentation or pull up the model and look at file size on chrome dev tools
        * models are json or bin files.  add up all the json/bin files that re pulled down and you have your model size
    * Use memory tab in chrome dev tools 
        * load the model, go to memory tab, click create snapshot => view total ram in the statistics drop down option 


    
