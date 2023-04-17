#ifndef PROXY_H
#define PROXY_H
#include <fstream>
#include "License.h"
#include "Vehicle.h"

class Proxy
{
    public:
        Proxy();
        virtual ~Proxy();
        void write(License);
        void write(Vehicle);
        void read_v();
        void read_l();
        void _searchl(string);
        void _searchv(string);
        void renew(string);
        void reset();
        int lineNum=0;
        int vNum=0;
        int numl=lineNum/7;
        int numv=vNum/5;
        int numLicenses=0;
        License licenses[10];
        Vehicle vehicles[10];

    protected:

    private:
};

#endif // PROXY_H
