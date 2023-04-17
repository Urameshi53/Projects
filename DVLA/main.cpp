#include <iostream>
#include "Proxy.h"
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <time.h>

using namespace std;

void printOptions();
//void checkAnswer(int);
int main()
{
    srand(time(0));

    Proxy proxy;
    //proxy.read_l();
    //proxy.read_v();
    int ans=1;
    //cout << quit.compare("no") << endl;
    while(ans!=0){
        printOptions();
        cin >> ans;
        switch(ans)
        {
            case 1:
                {
                    system("CLS");
                    Vehicle vehicle;
                    cout << "Enter Vehicle's name: " << endl;
                    cin >> vehicle.name;
                    cout << "Enter Vehicle's type: " << endl;
                    cin >> vehicle.type;
                    cout << "Enter Vehicle's model: " << endl;
                    cin >> vehicle.model;
                    cout << "Enter Vehicle's color: " << endl;
                    cin >> vehicle.color;
                    string d = "DD12345-";
                    vehicle.number = d + to_string((rand()%100));
                    cout << "Vehicle registered successfully!!!" << endl;
                    proxy.write(vehicle);
                    //printOptions();
                    break;
                }
            case 2:
                {
                    system("CLS");
                    License license;
                    cout << "Enter your first name: " << endl;
                    cin >> license.fname;
                    cout << "Enter your last name: " << endl;
                    cin >> license.lname;
                    cout << "Enter your gender: " << endl;
                    cin >> license.sex;
                    cout << "Enter your age: " <<endl;
                    cin >> license.age;
                    string d = "GH12345-";
                    license.dlnum = d + to_string((rand()%100));
                    license.dom = "06/04/2023";
                    license.expiry = "05/04/2033";
                    proxy.write(license);
                    cout << "Licensed issued successfully." << endl;
                    break;
                }
            case 3:
                {
                    system("CLS");
                    string ren;
                    cout << "Enter your License number: " << endl;
                    cin >> ren;
                    proxy._searchl(ren);
                    //proxy.reset();
                    break;
                }
            case 4:
                {
                    system("CLS");
                    string ren;
                    cout << "Enter car name: " << endl;
                    cin >> ren;
                    proxy._searchv(ren);
                    //proxy.reset();
                    break;
                }
            case 5:
                system("CLS");
                proxy.read_v();
                break;
            case 6:
                system("CLS");
                proxy.read_l();
                break;
            default:
                ans = 0;
                break;
        }
    }
    /*License license1;
    license1.fname = "Zigah";
    license1.lname = "Emmanuel";
    license1.age = "42";
    license1.sex = "Male";
    license1.dlnum = "GH12345-00";
    license1.dom = "02/02/2012";
    license1.expiry = "01/02/2022";
    //proxy.write(license1);

    License license2;
    license2.fname = "Federal";
    license2.lname = "Sedinam";
    license2.age = "33";
    license2.sex = "Female";
    license2.dlnum = "GH39375-01";
    license2.dom = "02/02/2017";
    license2.expiry = "01/02/2027";
    //proxy.write(license2);*/
    //proxy.read();
    //system("CLS");

    return 0;
}

void printOptions()
{
    //system("CLS");
    cout << "------------------ DVLA ----------------" << endl;
    cout << "1. Register Vehicle." << endl;
    cout << "2. Issue License." << endl;
    cout << "3. Renew driver's license." << endl;
    cout << "4. Renew vehicle registration." << endl;
    cout << "5. Open Vehicle database." << endl;
    cout << "6. Open License database." << endl;
    cout << "0. Enter 0 to quit." << endl;
    cout << endl;
}
