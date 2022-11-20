//something

class A;

class MyClass1 {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    string myString;  // Attribute (string variable)
};

// Base class
class Vehicle {
  public: 
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

// Derived class
class Car: public Vehicle {
  public: 
    string model = "Mustang";
};

// Base class (parent)
class MyClass2 {
  public: 
    void myFunction();
};

// Derived class (child)
class MyChild: public MyClass2 {
};

// Derived class (grandchild) 
class MyGrandChild: public MyChild
{
};

// Base class
class MyClass3 {
  public: 
    void myFunction();
};

// Another base class
class MyOtherClass {
  public: 
    void myOtherFunction();
};

// Derived class 
class MyChildClass: public MyClass3, public MyOtherClass {
};

