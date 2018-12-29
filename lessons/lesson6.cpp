#include<string>
#include<vector>
#include<iostream>


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
    auto s2 = s.substr(1, i);
    std::cout << "length:"<< " " <<  s2 << std::endl;
    // length of list of strings
    auto a = std::vector<std::string>();
    a.push_back("0");
    a.push_back("1");
    a.push_back("2");
    a.push_back("3");
    a.push_back("4");
    auto i2 = (a).size();
    // indexing list of strings
    //a2 = a[3:i2]
    //print(a2[0])
    //a3 = [float]
    //a3.append(0)
    //a3.append(1)
    //a3.append(2)
    //a3.append(3)
    //a4 = a3[0:1]
    //i3 = (a4).size()
    //print(a4[i3])
}