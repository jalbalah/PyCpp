#include<vector>
#include<string>
#include<iostream>


;
int main()
{
    std::string s("0123456");
    std::string s2("");
    auto s2 = s.substr(0, 5);
    std::string s3("");
    std::vector<float> s3(s2.begin() + 0, s2.begin() + 4);
    std::string s4("");
    auto s4 = s3.substr(0, 3);
    std::cout << s4 << std::endl;
}