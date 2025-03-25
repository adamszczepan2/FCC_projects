"""A vector is an object that has a length (or magnitude) and a direction and it cannot be expressed by a single number. 
In physics, vectors are commonly used to represent forces, velocities, accelerations, and other quantities.
In this project you are going to build a vector space, a set in which a series of operations is defined between the elements in that set. """



In Python, you can enforce the use of keyword-only arguments by adding a * as an additional argument to the function or method signature. Modify both __init__ methods by adding a * as the second parameter (after self). Every parameter placed after that will require the use of a keyword argument in the function/method call.

This means that you need to modify the super().__init__(x, y) call, too. Do it by giving x the value x, and y the value y.

Finally, modify the instantiation of v1 and v2 by using keyword arguments.