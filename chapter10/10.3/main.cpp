#include <iostream>
//Given two lines on a Cartesian plane,
//determine whether the two lines would inter-sect
using namespace std;

typedef struct Line
{
    pair <float,float> A;
    pair <float,float> B;
    float m;//panta
};

int main()
{
    Line line1;
    Line line2;
    line1.m = 4;
    line2.m = 4;

    //the lines wont intersect ever if the m fields are equals
    if(line1.m == line2.m)
        cout << "no";
    else cout << "yes";


    return 0;
}
