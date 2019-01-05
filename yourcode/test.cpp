#include<string>
#include<vector>


;
int main()
{
    auto s = std::vector<std::string>();
    for(auto i = 0; i != 10; ++i)
    {
        s.push_back(std::to_string(i));
    }
    std::vector<std::string> s2(s.begin() + 0, s.begin() + 5);
    ////s3 = s2[0:4]
    //s4 = s3[0:3]
    //s5("3");
    //s6 = s4 + s5
    //print(s6, "= 0123")
}