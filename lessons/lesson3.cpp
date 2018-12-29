#include<iostream>
#include<string>
#include<vector>


// a dog has properties and functions (things you can do with it)
class Dog
{
public:
    Dog()
    {
        // define name property
        this->name = "";
        this->weight = 0;
        this->nicknames = std::vector<std::string>();
        this->favorite_numbers = std::vector<int>();
    }
    void get_name()
    {
        std::cout << "My name is " + this->name << std::endl;
    }
    void get_weight()
    {
        std::cout << "I weigh: " + this->weight << std::endl;
    }

    std::string name;
    int weight;
    std::vector<std::string> nicknames;
    std::vector<int> favorite_numbers;
};
;
int main()
{
    Dog d;
    d.name = "john";
    d.weight = 40;
    d.nicknames.push_back("funnybones");
    d.nicknames.push_back("ripcurrent");
    d.nicknames.push_back("bowman");
    d.favorite_numbers.push_back(7);
    d.favorite_numbers.push_back(23);
    d.get_name();
    d.get_weight();
    for(auto it = d.favorite_numbers.begin(); it != d.favorite_numbers.end(); ++it)
    {
        auto fav_num = *it;
        std::cout << fav_num << std::endl;
    }
    for(auto it = d.nicknames.begin(); it != d.nicknames.end(); ++it)
    {
        auto nickname = *it;
        std::cout << nickname << std::endl;
    }
}