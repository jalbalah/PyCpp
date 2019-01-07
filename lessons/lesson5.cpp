#include<vector>
#include<string>
#include<iostream>


class Student
{
    public:
    Student()
    {
        this->name = "";
    }
    void get_name(auto student_num)
    {
        std::cout << student_num + ") " + this->name << std::endl;
    }

    std::string name;
};
class Classroom
{
    public:
    Classroom()
    {
        this->students = std::vector<Student>();
    }
    void add_student(auto name)
    {
        Student s;
        s.name = name;
        this->students.push_back(s);
    }
    void get_students()
    {
        std::cout << "Students:" << std::endl;
        auto c = 1;
        for(auto it = this->students.begin(); it != this->students.end(); ++it)
        {
            auto i = *it;
            i.get_name(c);
            c = c + 1;
        }
    }

    std::vector<Student> students;
};
;
int main()
{
    Classroom c;
    c.add_student("John");
    c.add_student("Jane");
    c.get_students();
}