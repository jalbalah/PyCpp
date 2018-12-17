#include<vector>
#include<iostream>
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
        // array with type ;ed (i.e. int, float, string)
        this->arr = std::vector<int>();
    }

    int static x;
    float a;
    float b;
    std::vector<int> arr;
};
int main()
{
    // instantiating C++ objects
    X x1(1, 2.0);
    std::cout << x1.a<< " " <<  "\n" << std::endl;
    // range loop
    for(auto i = 10; i != 0; i += -1)
    {
        std::cout << i << std::endl;
    }
    std::cout << "liftoff!"<< " " <<  "\n" << std::endl;
    for(auto i = 0; i != 10000; ++i)
    {
        x1.arr.push_back(i);
    }
    // iterator to loop through container
    for(auto it = x1.arr.begin(); it != x1.arr.end(); ++it)
    {
        auto i = *it;
        if(i > 9995)
        {
            std::cout << i << std::endl;
        }
    }
}