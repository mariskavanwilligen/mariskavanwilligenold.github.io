Title: Inheritance
Date: 2022-01-07 11:20
Modified: 2022-01-07 15:34
Tags: Python, Classes, Inheritance, Subclasses, object-oriented
Slug: Inheritance
Authors: Mariska van Willigen
Summary: Basics of Object-oriented python programming: Inheritance explained

## Inheritance
Inheritance is a very important feature of object oriented programming (OOP). It refers to a class that uses almost all attributes and methods of another class. The new class is called the **child** or **subclass**. The already existing class is called the **parent** or **base class**. 
There are different options to modify or extend the inherinted class, such as overriding some attributes or overriding some methods.

## Overriding attributes
You can override an attribute of the parent class in the subclass:
``` js
class Product(object):
    product = "Coca Cola"

class NewProduct(Product):
    product = "Fanta"
```
Any instance of the new class will have the *Fanta* as product. Any instance of the parent/original class will have as product *Coca Cola*.

## Overriding methods
Same as with overriding methods:
``` js
class Product(object):
    def forecast_product(self, lift_factor=5)
        forecast = self.last_sales * factor
        return forecast

class NewProduct(Product):
    def forecast_product(self, lift_factor=5)
        forecast = self.last_sales * lift_factor * math.sqrt(2)
        return forecast

```
The subclass has a changed *forecast_product* function. Instances from the parent/original class will still have the old function *forecast_product* from the parent class.

However, if you override something in the subclass, be aware of the OOP principles. The subclass should always be substantially similar to its parents. *Liskov Substitution Principle* refers to the principle which says that objects of a parentclass shall be replaceable with objects of its subclasses without breaking the application.

## Extending methods
Sometimes you want to extend the *__intit__*. With the **super()** function you can call methods from the parentclass in your childclass. You can extend the functionallity of this inherited method. 

Example from *realpython.com*:
``` js
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length
square = Square(4)
quare.area()        
``` 
Because the methods are so similar you can call superclass **__init__** function with **super()**. With a small extention that will set the length and width equal and you only need to give a signle length parameter to the square class.

## Check inheritances
With the functions **isinstance()** and **issubclass()** you can check the inheritance.

**isinstance(object, clasinfo)** checks whether a specific object is an instance of a class
**issubclass(class, classinfo)** checks whether one class is a subclass of another class

``` js
class X:
    pass
     
class Y(X):
    pass

x = X()
y = Y()  

isinstance(y, X)
# True
isinstance(x, Y)
# False

issubclass(Y, X)
# True
issubclass(X, Y)
# False
issubclass(X, X)
# True
```
## Advantages of inheritance
1.  Modular Codebase
    - Code is broken down into modules, which makes it easier to understand. 
2.  Code Reusability
    - The childs reuses code from the parentclass without rewriting them. This saves time and coding effort.
3. Less Development
    - Changes made in the parentclass will be inherited by all the childclasses. With good written code you only have to add your chnages at one place. This will save time and costs.

## Weakness of inheritance
1. Decrease of execution speed
    - You have to load multiple classes because they are interdependent on each other
2. Tightly Coupled Classes
    - Parent classes can be executed independently, but child classes can not be executed without defining their parent classes.
3. Explosion of subclasses
    - The book *Gang of Four* states that a crucial weakness of inheritance as a design strategy is that a class often needs to be specialized along several different design axes at once, leading to an explosion of subclasses to support every combination.
