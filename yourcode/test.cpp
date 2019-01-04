#include<string>
#include<sstream>
#include<fstream>
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
    std::string s7("");
    for(auto i = 0; i != 100000; ++i)
    {
        std::ostringstream ss1546611735803;
        ss1546611735803 << (i);
        std::string s8(ss1546611735803.str());

        s7 = s7 + ", (" + s8 + ")";
    }
    auto l7 = (s7).size();
    auto s9 = s7.substr(2, l7);
    std::cout << "writing file" << std::endl;
    std::ofstream f("yourcode/test.txt");
    f << s9;
    f.close();

}