#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin("input.txt");
//Given a sorted array of strings which is interspersed with empty strings,
//write a method to find the location of a given string.
//Example: find “ball” in [“at”, “”, “”, “”, “ball”, “”, “”, “car”, “”, “”,
//“dad”, “”, “”] will return 4
//Example: find “ballcar” in [“at”, “”, “”, “”, “”, “ball”, “car”, “”,
// “”, “dad”, “”, “”] will return -1

bool find_string(string strings[],int n,string s)
{
    int stanga = 0;
    int dreapta = n-1;
    int aux;
    while(stanga <= dreapta)
    {
        //cout << stanga << " " << dreapta;
        int mid = (stanga+dreapta)/2;
        if(strings[mid] == s)
        {
            return true;
        }
        //go to the right till we find a string different of "_"
        while (mid < dreapta && strings[mid]=="_")
            ++mid;
        //cout << mid<<endl;
        if (s == strings[mid])
            return true;
        else if(s > strings[mid])
            stanga = mid+1;
        else
            dreapta = mid-1;
    }
    return false;
}

//find / -size +10M -ls
int main()
{
    //Algorithm : basic binary search but pay attention
    //to the ""
    string strings[1000];
    int contor = 0;

    while(fin >> strings[contor])
    {
        contor++;
    }
    //cout << ("ball" < "car");
    cout << find_string(strings,contor,"b");

    fin.close();
    return 0;
}
