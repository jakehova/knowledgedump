# Tensor

## What
* Primary data structure in tensorflow models 
* Similar to arrays that can have multiple dimensions.  **ONLY contain numerical data**
* ML models take tensors as inputs and output tensors
* Tensor is a class
* Need to explicitly dispose tensors when they are no longer needed
    * tf.dispose() => to destroy a specific tensor
    * tf.tidy() => dispose any tensor(s) created in the same function
* Terminology: 
    * DataType (DType) => either integer or floating point
    * Shape => Number of elements present along each axis of the tensor (a cube would have a shape of [3,3,3] if it had 3 elements on each axis)
    * Rank => # of "Axis" in the tensor.  6 Axis is max number tensorflow handles
    * Size => total elements in the tensor
* Example: 
    * 0 Dimensions: 
        ```
        // js 0 dimension 
        let value = 6;

        // tf 0 dimension
        let tensor = tf.scalar(6);
        ```
    * 1 Dimensional: example as a x,y,x coordinates on a 3 dimensional plane
        ```
        // js 1 dimension
        let value = [1,2,3];

        // tf 1 dimension.  
        let tensor = tf.tensor1d([1,2,3]);
        ```
    * 2 Dimensional: example grayscale image
        ```
        // js 2 dimension
        let values = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]

        // tf 2 dimensional
        let tensor = tf.tensor2d([
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]);
        ```
    * 3 Dimensiona: exmaple rgb image where each pixel would need a rgb array value
    * 4 Dimensional: example video where the rgb images above now have a time component associated with it

## Code
```
/**
 * Line below creates a 2D tensor. 
 * Printing its values at this stage would give you:
 * Rank: 2, shape: [2,3], values: [[1, 2, 3], [4, 5, 6]]
 **/
let tensor = tf.tensor2d([[1, 2, 3], [4, 5 ,6]]);

// Create a Tensor holding a single scalar value:
let scalar = tf.scalar(2);

// Multiply all values in tensor by the scalar value 2.
let newTensor = tensor.mul(scalar);

// Values of newTensor would be: [[2, 4, 6], [8, 10 ,12]]
newTensor.print();

// You can even change the shape of the Tensor.
// This would convert the 2D tensor to a 1D version with
// 6 elements instead of a 2D 2 by 3 shape.
let reshaped = tensor.reshape([6]);
```

