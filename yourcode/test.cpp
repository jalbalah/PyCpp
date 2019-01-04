#include<string>
#include<iostream>


;
int main()
{
    std::string s("0123456");
    auto s2 = s.substr(0, 5);
    auto s3 = s2.substr(0, 4);
    auto s4 = s3.substr(0, 3);
    std::cout << s4 << std::endl;
}