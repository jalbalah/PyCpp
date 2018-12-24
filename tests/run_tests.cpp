#include<iostream>
#include<string>
#include<vector>
#include<fstream>


// defining a C++ object X
class X
{
public:
    X()
    {
        ;;
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
        // f = open('tests/test.txt', 'w')
        // f.write('hello\nworld')
        std::ifstream file("tests/test.txt");
        std::vector<std::string> f2;
        if(file.is_open()){
            std::string line;
            while (getline(file, line)) {
                f2.push_back(line);
            }; file.close();
        }
        std::cout << "\n"<< " " <<  f2[0] << std::endl;
    }

    static X x2;
    static std::vector<std::string> x3;
    std::vector<X> arr;
    X x4;
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
}