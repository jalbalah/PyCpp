#include<string>
#include<iostream>


class X
{
    public:
    X(auto name)
    {
        this->name = "";
        this->set_name(name);
    }
    void set_name(auto name)
    {
        this->name = name;
    }
    void __str__()
    {
        std::cout << this->name << std::endl;
    }

    std::string name;
};
;
int main()
{
    X x("dan");
    x.__str__();
}