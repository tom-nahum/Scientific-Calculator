# Scientific Calculator

## Description <img align="right" src="Calculator.gif">
This is a scientific calculator program, built using python's <ins>tkinter</ins> library. 

A calculator's gui consist of 3 main parts:
  * <ins>Screen</ins>: Basically the lower layer of the calculator.
  * <ins>Buttons</ins>: Which responsible for the user's input and calculaltions.
  * <ins>Display banner</ins>: That presents the current expression and it's calculation on the screen.

## Calculator Properties
The calculator has the following functionalities:
  * Basic arithmetic operands.
  * Advanced functions as cosine sine and tangent.
  * Floor and ceil functions.
  * 'Ans' key, which enable to use previous answer.
  * 'DEL' key, which allow to delete an element according to cursor location.
  * 'AC', which resets the calculation.
  * Arrows keys, to allow to repair previous elements.
  * Errors handling (Mathematical errors, Syntax errors etc).

## Design
###### calculuator.py
I've created a calculator class, which has the following fields: 
 * A tkinter object called 'screen'.
 * An array that holds the current expression entered by the user. 
   I've used this data structore in order to use python's slicing functionality. 
 * Booleans that indicates whether an error occured.
 * A <ins>StringVar</ins> object, which responsible for presenting the current expression on the display banner.
In order to calculate an expression, I've used python's **eval()** method, which gets a string and calculate it's value.

###### my_button.py
In this calculator, we have 5 types of buttons. According to **open-close principle**, I've created     
an abstract class called MyButton. All the buttons inherits from this class, which includes 
all the attributes of a button (size, color, font and location on the screen).
In addition, this class has a method 'create' which place a button on the screen. 
This design allowed me to implement **Factory design patten**, as a method which creates buttons     
according to their type.
 
  
