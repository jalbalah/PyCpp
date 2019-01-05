#include<vector>
#include<string>


;
int main()
auto {
    s = std::vector<std::string>()
    for(auto i = 0; i != 10; ++i)
    {
        s.push_back(std::to_string(i))
    }
    std::vector<std::string> s2(s.begin() + 0, s.begin() + 5);
    std::vector<std::string> s3(s2.begin() + 0, s2.begin() + 4);
    std::vector<std::string> s4(s3.begin() + 0, s3.begin() + 3);
    auto s6 = s4;
    s6.push_back("3");
    std::string ss("");
    auto ls6 = (s6).size();
    for(auto i = 0; i != ls6; ++i)
    auto {
        ix = s6[i]
        ss = ss + ix
    }
    // print(s2, "= 0123")
}