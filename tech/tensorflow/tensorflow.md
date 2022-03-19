# Tensorflow

## What?
JS and Python library to develop models, train them, and use them to run ML and AI on many platforms.  It is written in C++ 

## Common Terms
* Deep Learning results feed better Machine Learning Models.  Better Machine Learning Models feed better AI.
* AI - Science of making things smart
    * Narrow AI - A system that can do one or a few things well or better than a human
* Machine Learning - An approach to achieve AI by finding patterns in a set of data
    * Types: 
        * Computer Vision: 
            * Object vs Image Recognition
                * Object Recognition - detects how many and where objects are in an image
                * Image Recognition - detects what is in the image but does not tell you where or how many there are
        * Numerical Prediction 
            * Regression: Predicting a numerical value from other numerical inputs (i.e. predicting house prices based on sq footage)
        * Natural Language 
            * Semantic Analysis and Content Summary analaysis of naturally spoken Language
        * Audio 
            * Speech recognition - Translate audio to text
        * Generative
            * Style Transfer/Creative - Generating realistic images of human faces or transofmring human faces or transforming human voices into musical instruments.

* Deep Learning - A technique for implementing machine Learning.  Involves **Deep Neural Networks (DNN)** code strcutures that are arranged in layers.  Each layer filters a pattern out of other patterns and continues to filter the pattern until an output is given. 
* Keras - This is actually a Python library that outputs models.  Tensorflow can tell the difference and use Kera models in addition to Tensorflow trained models.
    * This works by feeding the Kerans Model the Layers API.  The Core/OPS API then translates the Keras Model to a TensorFlow SavedModel.  

## What is it
TensorflowJS - Javascript library that contains Google's machine learning library 
* Python vs Javascript  
    * Running Tensorflow in NodeJS allows you to leverage CUDA and AVX acceleration to perform a LOT faster than Python. 
    * NodeJS supports integrating with Python Keras and Tensorflow SavedModels created in Python.  
* Server vs Client 
    * Benefits to using Tensorflow Server Side: 
        * can use tensorflow savedmodel without conversion
        * run larger models than client-side (GPU memory limits)
        * Code in 1 language - if you are already using JS then you can continue using JS
        * Performance boost because of C bindings / JIT boost for pre/post processing
    * Benefits of running client side: 
        * Privacy - everything is run on the client's browser to build models so no information is transferred anywhere 
        * Lower Latency - if you need to use a camera or audio input then the processing happens closer to the input so result come quicker
        * Lower Cost - with no server there is no infrastructure server side to pay for 
        * Interactivity - can directly interact with the library using the browser platform
        * Reach & Scale - Running on a browser is basically omnipresent. 

## Structurte
Models --> Layers API --> Core/OPS API
* Layers API - high level api 
    * Allows you to make models without dealing with the mathematics (equivalent to Python's Keras API)
* Core/Ops API (mathematical)
    * Can use linear algebra to build more cuting edge models
    * Contains code with how to work with the platform (i.e. WebBrowser or NodeJS env) and the platform's backend (CPU, WebGL, WASM for Browser or CPU, GPU for NodeJS) it is being used on
        * Backend Types
            * CPU - 
                * always available
                * slowest form of execution
            * WASM - 
                * Fast CPU execution
                * SIMD + Multithreading support for GPU like performance
                * great for smaller models (<10MB)
            * WebGL - 
                * Fast GPU execution
                * 97.6% device support
                * Executes on AMD, NVIDIA, Intel, and more
                * great for larger models (>10MB)
            * WebNN - Supported in the future
                * New web standard in development
                * Even faster native execution 
            * Web GPU - Supported in the future
                * new web standard in development
                * Even faster native execution on GPU 





## Tools
* [Teachable Machine](https://teachablemachine.withgoogle.com/)

