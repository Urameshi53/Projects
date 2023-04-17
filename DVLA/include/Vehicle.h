#ifndef VEHICLE_H
#define VEHICLE_H
#include <iostream>

using namespace std;

class Vehicle
{
    public:
        Vehicle();
        virtual ~Vehicle();
        void renew();
        string model;
        string color;
        string name;
        string type;
        string number;

    protected:

    private:
};

#endif // VEHICLE_H
