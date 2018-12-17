#include<iostream>
#include<vector>
// defining a C++ object X
class X
{
public:
    X(auto a, auto b)
    {
        std::cout << "Another initializer" << std::endl;
        // initialize object member variables
        this->a = a;
        this->b = b + 1;
        // array with type passed (i.e. int, float, string)
        this->arr = std::vector<int>();
    }

    float a;
    float b;
    std::vector<int> arr;
};
int main()
{
    // instantiating C++ objects
    X x1(1, 2.0);
    std::cout << x1.a << std::endl;
    for(auto i = 0; i != 10; ++i)
    {
        std::cout << i << std::endl;
    }
    std::cout << "liftoff!" << std::endl;
}