#include<iostream>
#include<sstream>
#include<string>


;
int main()
{
    //s("0123456");
    //s2 = s[0:5]
    //s3 = s2[0:4]
    //s4 = s3[0:3]
    //s5("3");
    //s6 = s4 + s5
    //print(s6, "= 0123")
    std::string s7("");
    for(auto i = 0; i != 100; ++i)
    {
        std::ostringstream ss1546611134461;
        ss1546611134461 << (i);
        std::string s8(ss1546611134461.str());

        s7 = s7 + ", (" + s8 + ")";
    }
    auto l7 = (s7).size();
    auto s9 = s7.substr(2, l7);
    std::cout << s9 << std::endl;
}