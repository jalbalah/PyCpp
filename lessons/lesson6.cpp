#include<vector>
#include<iostream>
#include<string>


;
int main()
{
    // indexing a string
    std::string s("0123456");
    std::cout << s[1] << std::endl;
    std::cout << s[2] << std::endl;
    std::cout << s[3] << std::endl;
    std::cout << "Begin!"<< " " <<  "\n" << std::endl;
    // length of string
    auto i = (s).size();
    std::cout << "length of"<< " " <<  s<< " " <<  "is"<< " " <<  i << std::endl;
    // substring
    auto s2 = s.substr(1, i);
    std::cout << "s2 is"<< " " <<  s2 << std::endl;
    // length of list of strings
    auto a = std::vector<std::string>();
    a.push_back("0");
    a.push_back("1");
    a.push_back("2");
    a.push_back("3");
    a.push_back("4");
    auto i2 = (a).size();
    // indexing list of strings
    std::vector<std::string> a2(a.begin() + 3, a.begin() + i2);
    std::cout << a2[0] << std::endl;
    auto a3 = std::vector<float>();
    a3.push_back(0);
    a3.push_back(1);
    a3.push_back(2);
    a3.push_back(3);
    std::vector<float> a4(a3.begin() + 0, a3.begin() + 1);
    auto i3 = (a4).size();
    std::cout << a4[i3] << std::endl;
}