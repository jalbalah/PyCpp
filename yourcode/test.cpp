#include<string>
#include<sstream>
#include<vector>
#include<iterator>
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
    auto s7 = std::vector<std::string>();
    for(auto i = 0; i != 10000000; ++i)
    {
        s7.push_back(std::to_string(i));
    }
    std::ostringstream os1546691262093;
    std::copy(s7.begin(), s7.end() - 1, 
              std::ostream_iterator<decltype(s7[0])>(os1546691262093, ","));
    os1546691262093 << *(s7).rbegin();
    std::string s8 = os1546691262093.str();
;
    std::cout << "writing file" << std::endl;
    std::ofstream f("yourcode/test.txt");
    f << s8;
    f.close();

}