#include<vector>
#include<iostream>
#include<algorithm>
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
    // find in string
    int i3 = s.find("23");
    std::cout << "position of 23:"<< " " <<  i3 << std::endl;
    // find in list of strings
    int i4 = std::find(a.begin(), a.end(), "3") - a.begin();
    std::cout << "position of 3:"<< " " <<  i4 << std::endl;
}