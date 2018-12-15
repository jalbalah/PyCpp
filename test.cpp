#include<iostream>
class X
{
    X(auto a,auto b)
    {
        this->a = 1;
        this->b = 2.0;
    }
    x()
    {
        std::cout << 1 << std::endl;
    }
private:
int a;
float b;
};
int main()
{
    std::cout << "hi" << std::endl;
}