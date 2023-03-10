# Supervised Learning

## Description
Supervised learning is learning how to get an appropriate output, y, from an input, x given a bunch of "right answers".

| input (x) | output (y) | application |
| ---  | --- | --- |
| email | spam | spam filtering |
| audio | text transcripts | speech recognition | 
| English | Spanish | machine translation |
| ad + user info | click? | online advertising |
| image + radar info | position of cars | self-driving car |
| image of phone | defect? | visual inspection |

* **model** is a formula to determine predicted values of y (called y-hat)
* **parameters** are variables that can be adjusted to improve the accuracy of a model
* **cost function** is a formula to determine how good the model fits the data.  This function is referred to as J(w,b)
* **goal** make J(w,b) as small as possible.  

## Algorithms
* Regression 
  * predict a number from infinitely many possible outputs
* Classification
  * predict a number or category from a finite (usually small) possible outputs 
  * can use one or more inputs mapped to the finite ouputs and determine a boundary to separate outputs into their own categories
  * **Note** outputs of classification algorithims are interchangeable with the terms "class" or "category"

## Linear Regression
* Predicts numbers. many, even infinitely many, number of outputs

* Terminology
  * 'training set' => Data used to train the model
  * 'x' => "input" variable or "feature"
  * 'y' => "output" variable or "target"
  * 'm' => total number of training examples
  * (x,y) => single training example 
  * (x^(i), y^(i)) => ith training example in a dataset 
  * y-hat => prediction for y
  * <i>f</i> => the model equation to draw the line used for the regression algorithm
```
training set (features to target mapping) = feeds => learning algorithm 
learning algorithm = produces => f (function that takes a new input x and ouputs y-hat)
```
* How to represent <i>f</i>?
  * f<sub>w,b</sub>(x) = wx + b
    * w & b are numbers used to fit the model

## Cost Function 
Cost function is used to determine how well a line fits a training set. It takes a prediction (y-hat) and compares it to the target

* **Squared Error Cost Function**
* One type of cost function that is very commonly used.
* **note** y-hat = model result 
$$J(w,b) = 1/(2m) * \displaystyle\sum_{i=1}^m((y-hat^i - y^i)^2)$$

## Classification 
Predicts categories. small number of ouptputs.


Grade & Dissent