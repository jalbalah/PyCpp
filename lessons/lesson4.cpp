#include<string>
#include<iostream>


class Cat
{
    public:
    // this variable is shared between classes
    Cat()
    {
        this->name = "";
        // increment shared variable
        num_cats = num_cats + 1;
    }
    void set_name(auto name)
    {
        this->name = name;
    }

    static float num_cats;
    std::string name;
};
float Cat::num_cats = 0.0;
int main()
{
    Cat c1;
    c1.set_name("Pursippany");
    Cat c2;
    c2.set_name("MeowMeow");
    std::cout << c1.name<< " " <<  " says the number of cats is: "<< " " <<  c1.num_cats << std::endl;
    std::cout << c2.name<< " " <<  " says the number of cats is: "<< " " <<  c2.num_cats << std::endl;
}