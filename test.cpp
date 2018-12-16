#include<iostream>
class X
{
public:
    X()
    {
        std::cout << "initializing, dude" << std::endl;
    }
    X(auto a, auto b)
    {
        this->a = a;
        this->b = b;
    }

    float a;
    float b;
};
int main()
{
    X x(1, 2.0);
    std::cout << x.a << std::endl;
}