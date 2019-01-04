#include<string>
#include<iostream>


;
int main()
{
    std::string s("0123456");
    auto s2 = s.substr(0, 5);
    auto s3 = s2.substr(0, 4);
    auto s4 = s3.substr(0, 3);
    std::string s5("3");
    auto s6 = s4 + s5;
    std::cout << s6<< " " <<  "= 0123" << std::endl;
    // s("");
    // for i in range(0, 100):
    //     s += i
    // print(s)
}