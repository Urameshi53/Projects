#ifndef LICENSE_H
#define LICENSE_H
#include <iostream>

using namespace std;

class License
{
    public:
        License();
        virtual ~License();
        string fname;
        string lname;
        string dlnum;
        string expiry;
        string dom;
        string sex;
        string age;

    protected:

    private:
};

#endif // LICENSE_H
