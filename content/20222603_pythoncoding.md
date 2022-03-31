Title: SOLID Principles
Date: 2022-03-26 10:20
Tags: Python, coding, SOLID
Slug: 
Authors: Mariska van Willigen
Summary: SOLID Principles

# SOLID principles

The principle of SOLID coding is an acronym originated by Robert C. Martin, and it stands for five different conventions of coding.
If you follow, these principles you can improve the reliability of your code by working on its structure and its logical consistency.


The SOLID principles are:
- The Single-Responsibility Principle (SRP)
- The Open-Closed Principle (OCP)
- The Liskov Substitution Principle (LSP)
- The Interface Segregation Principle (ISP)
- The Dependency inversion Principle (DIP)

> Let's go have a look at each one of them!

## The Single-Responsibility Principle
Classes and methods can only do a single thing. A class should not have multiple responsibilities (example: paying should not be part of class Order but the class PaymentProcessor).

``` js
class AlbertHeijnOrder:
    def __init__(self):
        self.products = []
        self.prices = []
        self.status = "open"

    def add_products(self, nasanbr, price):
        self.products.append(nasanbr)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

``` 
So if we let each class only do one thing, we can rewrite this as:
``` js
class AlbertHeijnOrder:
    def __init__(self):
        self.products= []
        self.prices = []
        self.status = "open"

    def add_products(self, nasanbr, quantity, price):
        self.products.append(nasanbr)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
``` 

## The Open-Closed Principle
Extend the code with new functionality, but don't need to change all the existing code.
Create a structure of classes and subclasses where you can add code and functionality, but not changing much of the existent code.
You can do this by adding **abstract methods** for example. 

### Abstract Method example
Below you can find an example of an abstract method in the abstract class **Polygon**. The base module of python to define an abstract class is ABC (Abstract Base Classes). Each child or subclass of the abstract class should have defined the abstract methods of the abstract class.

``` js
from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
 
# Driver code
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
``` 

## The Liskov Substitution Principle
If you have objects in a program, you should be able to replace those objects with instances of their subtyoes or subclasses without changing the correctness of the program
Add a initializer

### Initializer example

``` js
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Using email address: {security_code}")
        order.status = "paid"
``` 
Not every pay method needs a security code, paypal paymethod needs an emailadress. Above we are abusing the abstractmethod pay, by setting an emailadress as security_code altough it is not. That is a violation of the Liskov principle.

Adding an initializer and removing security_code as dependency from the pay method could solve this:

``` js
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_adress):
        self.email_adress = email_adress

    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_adress}")
        order.status = "paid"
``` 


## The Interface Segregation Principle
Interface segragation principle states that overall, it is better to have several specific interfaces as opposed to one general purpose interface
Abstract methods not always necessary. Subclasses

Before:
``` js
class PaymentProcessor(ABC):

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def auth_sms(self, code):
        raise Exception("Credit card payments don't support SMS code authorization.")

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

``` 

You can see above an example where we have specify the abstract class to have auth_sms abstract method. However, if you pay with creditcard, you don't need this class. Making a sub abstractclass can help. This is also called Inheritance.


``` js
class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class PaymentProcessor_SMS(PaymentProcessor):

    @abstractmethod
    def auth_sms(self, code):
        pass

    @abstractmethod
    def pay(self, order):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor_SMS):

    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"
``` 
This can pontentially lead to a lot of inheritanced classes, so a different and sometimes better way to do this is by using Composition:


``` js
class SMSAuthorizer:

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuthorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

authorizer = SMSAuthorizer()
# authorizer.verify_code(465839)
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
processor.pay(order)

``` 

## The Dependency inversion Principle
Classes should depent on abstract methods and not specified classes.

In this example you can see that the payment methods are depending on a specific classtype 'SMSAuth'. So let's make that more depended on abstract classes and methods.

```js
class SMSAuthorizer:

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuthorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"
``` 

``` js

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class Authorizer_SMS(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class Authorizer_Google(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying Google auth code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized

class Authorizer_Robot(Authorizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"
``` 

*
### Reference: 
- ArjanCodes about SOLID principles: https://www.youtube.com/watch?v=pTB30aXS77U 
- CodeExamples from: geeksforgeeks.org

*