#include<iostream>


// this is called a class
class Square
{
public:
    Square()
    {
        std::cout << "I am a square" << std::endl;
    }
};
// this is another class
class Rectangle
{
public:
    Rectangle(auto attitude)
    {
        std::cout << "I am a "<< " " <<  attitude<< " " <<  " circle" << std::endl;
    }
};
;
int main()
{
    // create a square object
    Square s;
    // create a rectangle, and pass in an argument
    Rectangle r("funny");
}