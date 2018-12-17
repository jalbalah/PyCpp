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
        // array with type ;ed (i.e. int, float, string)
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
    std::cout << x1.a<< " " <<  "\n" << std::endl;
    // range loop
    for(auto i = 10; i != 0; --i)
    {
        std::cout << i << std::endl;
    }
    std::cout << "liftoff!"<< " " <<  "\n" << std::endl;
    for(auto i = 0; i != 10; i += 2)
    {
        ;
    }
    // iterator to loop through container
    x1.arr.push_back(1);
    x1.arr.push_back(2);
    x1.arr.push_back(3);
    for(auto it = x1.arr.begin(); it != x1.arr.end(); ++it)
    {
        auto i = *it;
        std::cout << i + 100 << std::endl;
    }
}