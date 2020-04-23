#include <iostream>
#include <stdlib.h>
#include <stack>
#include <fstream>

using namespace std;
ifstream fin("paranteze.in");
ofstream fout("paranteze.out");

void afisare(int sol[],int n)
{
    for (int i = 0; i < n; i++){
        if(sol[i] == 0) fout << "(";
        if(sol[i] == 1) fout << ")";
    }
    fout << "\n";
}

//0= (
//1= )
bool verificare_paranteze(int sol[],int n)
{
    stack <int> s;
    s.push(sol[0]);

    for(int i = 1; i < n; i++)
    {
        if(!s.empty())
        {
            if (sol[i] == 1 && s.top() == 0)
            {
                s.pop();
            }
            else
            {
               s.push(sol[i]);
            }
        }
        else s.push(sol[i]);
    }
    if (s.empty())
        return true;
    return false;
}


void bkt(int index,int sol[],int n)
{
    if (index == (n))
    {
        if (verificare_paranteze(sol,n))
            afisare(sol,n);
    }
    else
    {
        for(int i = 0; i <= 1; i++)
        {
            sol[index] = i;
            bkt(index+1,sol,n);
        }
    }
}


int main()
{
    int n;
    fin >> n;
    int *sol = (int*)malloc((n) * sizeof(int));
    bkt(0,sol,n);
    return 0;
}
