#include<vector>
#include<fstream>
#include<string>
#include<iostream>


;
int main()
{
    auto s = "xoxoxo\nhello world";
    std::ofstream fw("tests/test.txt");
    fw << s;
    fw.close();

    std::ifstream file("tests/test.txt");
    std::vector<std::string> fr;
    if(file.is_open()){
        std::string line;
        while (getline(file, line)) {
            fr.push_back(line);
        }; file.close();
    }
    std::cout << fr[0] << " " << fr[1] << std::endl;
    for(auto it = fr.begin(); it != fr.end(); ++it)
    {
        auto line = *it;
        std::cout << line << std::endl;
    }
}