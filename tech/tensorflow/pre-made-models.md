# Pre-Made Models

## What are they?
ML Models that have been trained already.  [Tensorflow JS Model Library](https://www.tensorflow.org/js/models) 
Types:
* JS classes that wrap a model
* Raw models that you need to learn to use working at the "Tensor" level
Categories: 
* [Object Detection Model](https://github.com/tensorflow/tfjs-models/tree/master/coco-ssd) 
    * [Demo](https://tensorflow-js-object-detection.glitch.me/)
* [Speech Recognition](https://github.com/tensorflow/tfjs-models/tree/master/speech-commands)
* [Text Toxicity](https://github.com/tensorflow/tfjs-models/tree/master/toxicity) 
    * [Demo](https://storage.googleapis.com/tfjs-models/demos/toxicity/index.html)
* [Face Mesh](https://github.com/tensorflow/tfjs-models/tree/master/face-landmarks-detection) 
    * [Demo](https://storage.googleapis.com/tfjs-models/demos/facemesh/index.html)
* [Body Detection](https://github.com/tensorflow/tfjs-models/tree/master/pose-detection)
    * [PoseNet Demo](https://storage.googleapis.com/tfjs-models/demos/pose-detection/index.html?model=posenet)
    * [MoveNet Demo](https://storage.googleapis.com/tfjs-models/demos/pose-detection/index.html?model=movenet)
    * [BlazePose Demo](https://storage.googleapis.com/tfjs-models/demos/pose-detection/index.html?model=blazepose)
* [Hand Pose Detection](https://github.com/tensorflow/tfjs-models/tree/master/hand-pose-detection)
    * [Demo](https://storage.googleapis.com/tfjs-models/demos/hand-pose-detection/index.html?model=mediapipe_hands)
* [Body Segmentation](https://github.com/tensorflow/tfjs-models/tree/master/body-pix)
    * [Demo](https://storage.googleapis.com/tfjs-models/demos/body-pix/index.html)
    * [Selfie Segementation Demo](https://storage.googleapis.com/tfjs-models/demos/body-segmentation/index.html?model=selfie_segmentation)



## How to use?
* include [tensorflowjs from cdn](https://cdn.jsdelivr.net/npm/@tensorflow/tfjs) and [model you want to use from cdn](https://www.tensorflow.org/js/models)
```
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/qna"></script>

<script>
const searchText = "We believe cats are the real stars of YouTube";
const question = "What is important to YouTube?";

qna.load().then(model => {
    model.findAnswers(question, searchText).then(answers => {
        console.log("Answers", answers);
    })
})
</script>
```

