#include<iostream>
class X
{
public:
    X()
    {
        std::cout << "Default initializer" << std::endl;
    }
    X(auto a, auto b)
    {
        std::cout << "Another initializer" << std::endl;
        this->a = a;
        this->b = b;
    }

    float a;
    float b;
};
int main()
{
    X x0();
    X x1(1, 2.0);
    std::cout << x1.a << std::endl;
}