#include<vector>


;
int main()
{
    s = [str]
    for(auto i = 0; i != 10; ++i)
    {
        s.push_back(std::to_string(i))
    }
    std::vector<int> s2(s.begin() + 0, s.begin() + 5);
    std::vector<int> s3(s2.begin() + 0, s2.begin() + 4);
    std::vector<int> s4(s3.begin() + 0, s3.begin() + 3);
    auto s6 = s4;
    s6.push_back("3");
    std::string ss("");
    auto ls6 = (s6).size();
    for(auto i = 0; i != ls6; ++i)
    {
        ix = s6[i]
        ss = ss + ix
    }
    // print(s2, "= 0123")
}