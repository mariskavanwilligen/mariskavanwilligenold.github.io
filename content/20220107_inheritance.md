Title: Inheritance
Date: 2022-01-07 11:20
Modified: 2022-01-07 15:34
Tags: Python, Classes, Inheritance, Subclasses, object-oriented
Slug: Inheritance
Authors: Mariska van Willigen
Summary: Basics of Object-oriented python programming: Inheritance explained

## Inheritance

## Overriding attributes
``` js
class Product(object):
    product = "Coca Cola"

class NewProduct(Product):
    product = "Fanta"
```

## Overriding methods
``` js
class Circle(object):
...
    def grow(self, factor=2):
        """grows the circle's diameter by factor"""
        self.diameter = self.diameter * factor
...

class NewCircle(Circle):
...
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = self.diameter * math.sqrt(2)
```