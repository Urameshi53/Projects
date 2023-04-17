#include "Proxy.h"
#include <fstream>
#include <iostream>
#include <string.h>
#include <cstdlib>
#include <time.h>

using namespace std;

Proxy::Proxy()
{
    //ctor
}

void Proxy::reset()
{
    fstream file1;
    fstream file2;

    if(numl>0){
        file1.open("db.txt", ios::out);
        for(int i=0; i<numl; i++){
            this->write(licenses[i]);
        }

        file1.close();
    }

    if(numv>0){
        file2.open("db2.txt", ios::out);
        for(int i=0; i<numv; i++){
            this->write(vehicles[i]);
        }
        file2.close();
    }
}

void Proxy::write(License license)
{
    numLicenses += 1;
    fstream vfile;
    vfile.open("db.txt", ios::app);
    if(!vfile){
        cout << "Error while creating the file." << endl;
    }else{
        vfile << license.fname << endl;
        vfile << license.lname << endl;
        vfile << license.dlnum << endl;
        vfile << license.sex << endl;
        vfile << license.age << endl;
        vfile << license.dom << endl;
        vfile << license.expiry << endl;
        //cout << "File for License created successfully.";
        vfile.close();
    }
}

void Proxy::write(Vehicle vehicle)
{
    fstream vfile;
    vfile.open("db2.txt", ios::app);
    if(!vfile){
        cout << "Error while creating the file." << endl;
    }else{
        vfile << vehicle.name << endl;
        vfile << vehicle.model << endl;
        vfile << vehicle.type << endl;
        vfile << vehicle.color << endl;
        vfile << vehicle.number << endl;
        //cout << "File for Vehicle created successfully.";
        vfile.close();
    }
}

void Proxy::read_l(void)
{
    fstream file;
    string text;
    string arr[100];
    file.open("db.txt", ios::in);
    if(!file){
        cout << "File doesn't exist.";
    }else{
        int i = 0;
        while(getline(file, text)){
            arr[i] = text;
            cout << arr[i] << endl;
            lineNum++;
            i++;
        }
    }
    file.close();
    for(int i=0; i<(lineNum/7); i++){
        licenses[i].fname = arr[0+(i*7)];
        licenses[i].lname = arr[1+(i*7)];
        licenses[i].dlnum = arr[2+(i*7)];
        licenses[i].sex = arr[3+(i*7)];
        licenses[i].age = arr[4+(i*7)];
        licenses[i].dom = arr[5+(i*7)];
        licenses[i].expiry = arr[6+(i*7)];
    }
    numl = lineNum/7;
}

void Proxy::read_v(void)
{
    fstream file;
    string text;
    string arr[100];
    file.open("db2.txt", ios::in);
    if(!file){
        cout << "File doesn't exist.";
    }else{
        int i = 0;
        while(getline(file, text)){
            arr[i] = text;
            cout << arr[i] << endl;
            vNum++;
            i++;
        }
    }
    file.close();
    for(int i=0; i<(vNum/5); i++){
        vehicles[i].name = arr[0+(i*5)];
        vehicles[i].model = arr[1+(i*5)];
        vehicles[i].type = arr[2+(i*5)];
        vehicles[i].number = arr[3+(i*5)];
        vehicles[i].color = arr[4+(i*5)];
    }
    numv = vNum/5;
}

void Proxy::_searchl(string num)
{
    srand(time(0));
    License license;
    for(int i=0; i<(lineNum/7); i++){
        //cout << "trial" << i << endl;
        if(licenses[i].dlnum.compare(num)==0){
            cout << "I found it." << endl;
            license.fname = licenses[i].fname;
            license.lname = licenses[i].lname;
            license.age = licenses[i].age;
            license.sex = licenses[i].sex;
            //string d = "GH12345-";
            //license.dlnum = d + to_string((rand()%100));
            license.dlnum = licenses[i].dlnum;
            license.dom = licenses[i].dom;
            license.expiry = "01/01/2043";

            //this->write(license);
            licenses[i] = license;
            cout << "License has been renewed successfully" << endl;

            cout << "First name: " << "\t" << license.fname << endl;
            cout << "Last name: " << "\t" << license.lname << endl;
            cout << "License number " << "\t" << license.dlnum << endl;
            cout << "Gender: " << "\t" << license.sex << endl;
            cout << "Age: " << "\t\t" << license.age << endl;
            cout << "Date of making: " << "\t" << license.dom << endl;
            cout << "Date of expiry: " << "\t" << license.expiry << endl;

            cout << "numl\t" << numl << "lineNum\t" << lineNum << endl;
            this->reset();

            break;
        }else{
            cout << "License number not found" << endl;
        }
    }

}

void Proxy::_searchv(string num)
{
    srand(time(0));
    Vehicle vehicle;
    for(int i=0; i<(lineNum/7); i++){
        //cout << "trial" << i << endl;
        if(vehicles[i].number.compare(num)==0){
            cout << "I found it." << endl;
            vehicle.name = vehicles[i].name;
            vehicle.model = vehicles[i].model;
            vehicle.color = vehicles[i].color;
            string d = "DD12345-";
            vehicle.number = d + to_string((rand()%100));
            vehicle.type = vehicles[i].type;

            this->write(vehicle);
            cout << "Vehicle has been renewed successfully" << endl;

            cout << "Vehicle name: " << "\t" << vehicle.name << endl;
            cout << "Vehicle model: " << "\t" << vehicle.model << endl;
            cout << "Vehicle type: " << "\t" << vehicle.type << endl;
            cout << "Vehicle color: " << "\t" << vehicle.color << endl;
            cout << "Vehicle number: " << "\t\t" << vehicle.number << endl;

            break;
        }else{
            cout << "Vehicle not found" << endl;
        }
    }
}

Proxy::~Proxy()
{
    //dtor
}
