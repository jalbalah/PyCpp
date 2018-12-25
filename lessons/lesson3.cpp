#include<string>
#include<iostream>


// a dog has properties and functions (things you can do with it)
class Dog
{
public:
    Dog()
    {
        // define name property
        this->name = "";
        this->weight = 0;
    }
    void set_name(auto new_name)
    {
        this->name = new_name;
    }
    void set_size(auto weight)
    {
        this->weight = weight;
    }
    void get_name()
    {
        std::cout << "My name is " << this->name << std::endl;
    }
    void get_weight()
    {
        std::cout << "I weight" << this->weight << std::endl;
    }

    std::string name;
    int weight;
};
;
int main()
{
    Dog x;
    x.set_name("john");
    x.set_size(40);
    x.get_name();
    x.get_weight();
}