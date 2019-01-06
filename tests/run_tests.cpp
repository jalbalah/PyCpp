#include<string>
#include<sstream>
#include<iostream>
#include<iterator>
#include<fstream>
#include<vector>


// defining a C++ object X
class X
{
    public:
    X()
    {
        ;
    }
    X(auto a, auto b)
    {
        std::cout << "Another initializer" << std::endl;
        // initialize object member variables
        this->a = a;
        this->b = b + 1;
        // array with type passed (i.e. int, float, string)
        this->arr = std::vector<int>();
    }
    void junk()
    {
        auto a = std::vector<int>();
        auto b = std::vector<std::string>();
        auto c = std::vector<float>();
        std::string s("");
    }

    static float x;
    float a;
    float b;
    std::vector<int> arr;
};
class Test
{
    public:
    Test()
    {
        this->arr = std::vector<X>();
        this->x4 = X();
        this->a = std::vector<int>();
    }
    void run_all_tests()
    {
        this->run_obj_range_iter_test();
        this->run_file_test();
        this->run_vector_test();
        this->run_loop_test();
        this->run_find_test();
        this->run_substring_test();
        this->run_find_type_test();
        this->run_join_write_test();
        this->run_join_int_test();
        this->run_build_str_test();
    }
    void run_obj_range_iter_test()
    {
        X x1(1, 2.0);
        std::cout << x1.a<< " " <<  "\n" << std::endl;
        for(auto i = 10; i != 0; i += -1)
        {
            std::cout << i << std::endl;
        }
        std::cout << "liftoff!"<< " " <<  "\n" << std::endl;
        for(auto i = 0; i != 10000; ++i)
        {
            x1.arr.push_back(i);
        }
        for(auto it = x1.arr.begin(); it != x1.arr.end(); ++it)
        {
            auto i = *it;
            if(i > 9995)
            {
                std::cout << i << std::endl;
            }
        }
    }
    void run_file_test()
    {
        std::ofstream f("tests/test.txt");
        f << "hello\nworld";
        f.close();

        std::ifstream file("tests/test.txt");
        std::vector<std::string> f2;
        if(file.is_open()){
            std::string line;
            while (getline(file, line)) {
                f2.push_back(line);
            }; file.close();
        }
        std::cout << "\n" << " " <<  f2[0] << std::endl;
    }
    void run_vector_test()
    {
        auto a = std::vector<int>();
        a.push_back(0);
        a.push_back(1);
        a.push_back(2);
        a.push_back(3);
        a.push_back(4);
        std::vector<int> a2(a.begin() + 0, a.begin() + 3);
        std::cout << a2[0]<< " " <<  "= 0" << std::endl;
        auto b = std::vector<float>();
        b.push_back(1);
        b.push_back(2);
        b.push_back(3);
        b.push_back(4);
        std::vector<float> b2(b.begin() + 0, b.begin() + 3);
        auto i0 = (b2).size();
        std::vector<float> b3(b2.begin() + 1, b2.begin() + i0);
        std::cout << b2[0]<< " " <<  "= 1" << std::endl;
        std::cout << b3[0]<< " " <<  "= 2" << std::endl;
        std::cout << (b2).size()<< " = 3" << std::endl;
        auto a3 = std::vector<float>();
        a3.push_back(0);
        a3.push_back(1);
        a3.push_back(2);
        a3.push_back(3);
        std::vector<float> a4(a3.begin() + 0, a3.begin() + 1);
        auto i4 = (a4).size();
        std::cout << a4[i4]<< " " <<  "= 1" << std::endl;
    }
    void run_loop_test()
    {
        auto c4 = 3;
        while(c4 > 0)
        {
            std::cout << "c4:"<< " " <<  c4 << std::endl;
            c4 -= 1;
        }
    }
    void run_find_test()
    {
        std::string s3("0123456");
        int i1 = s3.find("34");
        auto i2 = i1 + 1;
        std::cout << i2 << std::endl;
        int i3 = s3.find("5");
        auto i4 = (s3).size();
        auto s4 = s3.substr(i3, i4);
        std::cout << s4 << std::endl;
    }
    void run_substring_test()
    {
        std::string s("01234");
        auto s2 = s.substr(0, 3);
        std::cout << s2[0]<< " " <<  "= 0" << std::endl;
        std::string s5("01234567");
        auto s6 = s5.substr(0, 6);
        auto s7 = s6.substr(0, 5);
        auto s8 = s7.substr(0, 4);
        std::cout << s8<< " " <<  "= 0123" << std::endl;
    }
    void run_find_type_test()
    {
        std::string s("0123456");
        auto s2 = s.substr(0, 5);
        auto s3 = s2.substr(0, 4);
        auto s4 = s3.substr(0, 3);
        std::string s5("3");
        auto s6 = s4 + s5;
        std::cout << s6<< " " <<  "= 0123" << std::endl;
    }
    void run_join_write_test()
    {
        auto s7 = std::vector<std::string>();
        for(auto i = 0; i != 1000000; ++i)
        {
            s7.push_back(std::to_string(i));
        }
        std::ostringstream os1546804014999;
        std::copy(s7.begin(), s7.end() - 1, 
              std::ostream_iterator<decltype(s7[0])>(os1546804014999, ","));
        os1546804014999 << *(s7).rbegin();
        std::string s8 = os1546804014999.str();
;
        std::cout << "writing file" << std::endl;
        std::ofstream f("yourcode/test.txt");
        f << s8;
        f.close();

    }
    void run_join_int_test()
    {
        auto a = std::vector<int>();
        for(auto i = 0; i != 1000000; ++i)
        {
            a.push_back(i);
        }
        std::ostringstream os1546804014999;
        std::copy(a.begin(), a.end() - 1, 
              std::ostream_iterator<decltype(a[0])>(os1546804014999, "\n"));
        os1546804014999 << *(a).rbegin();
        std::string s = os1546804014999.str();
;
        std::ofstream f("tests/test.txt");
        f << s;
        f.close();

    }
    void run_build_str_test()
    {
        auto s = std::vector<std::string>();
        for(auto i = 0; i != 10; ++i)
        {
            s.push_back(std::to_string(i));
        }
        std::vector<std::string> s2(s.begin() + 0, s.begin() + 5);
        std::vector<std::string> s3(s2.begin() + 0, s2.begin() + 4);
        std::vector<std::string> s4(s3.begin() + 0, s3.begin() + 3);
        auto s6 = s4;
        s6.push_back("3");
        std::string ss("");
        auto ls6 = (s6).size();
        for(auto i = 0; i != ls6; ++i)
        {
            ss = ss + s6[i];
        }
        std::cout << ss<< " " <<  "= 0123" << std::endl;
    }

    static X x2;
    static std::vector<std::string> x3;
    std::vector<X> arr;
    X x4;
    std::vector<int> a;
};
float X::x = 0.0;
X Test::x2 = X();
std::vector<std::string> Test::x3 = {};
int main()
{
    Test t;
    t.run_all_tests();
    t.x3.push_back("hello");
    t.x3.push_back("world");
    std::cout << t.x4.x << std::endl;
}