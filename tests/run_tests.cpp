#include<vector>
#include<fstream>
#include<string>
#include<iostream>


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
        // instantiating C++ objects
        X x1(1, 2.0);
        std::cout << x1.a<< " " <<  "\n" << std::endl;
        // range loop
        for(auto i = 10; i != 0; i += -1)
        {
            std::cout << i << std::endl;
        }
        std::cout << "liftoff!"<< " " <<  "\n" << std::endl;
        for(auto i = 0; i != 10000; ++i)
        {
            x1.arr.push_back(i);
        }
        // iterator to loop through container
        for(auto it = x1.arr.begin(); it != x1.arr.end(); ++it)
        {
            auto i = *it;
            if(i > 9995)
            {
                std::cout << i << std::endl;
            }
        }
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
        this->run_loop_test();
        this->run_vector_test();
        this->run_find_test();
        this->run_substring_test();
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
        std::cout << (b2).size()<< "= 3" << std::endl;
        auto a3 = std::vector<float>();
        a3.push_back(0);
        a3.push_back(1);
        a3.push_back(2);
        a3.push_back(3);
        std::vector<float> a4(a3.begin() + 0, a3.begin() + 1);
        auto i4 = (a4).size();
        std::cout << a4[i4]<< " " <<  "= 0" << std::endl;
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