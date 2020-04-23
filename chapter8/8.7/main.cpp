#include <iostream>

using namespace std;
//Given an infinite number of quarters (25 cents),
//dimes (10 cents), nickels (5 cents) and
//pennies (1 cent), write code to calculate the number of
// ways of representing n cents

int currency[] = {1,5,10,25};

int value(int sol[],int index)
{
    int s = 0;
    for(int i = 0; i < index; i++)
        s += currency[sol[i]];
    return s;
}

void print_solution(int sol[],int i)
{
    for(int j = 0; j < i; j++){
        cout << currency[sol[j]]<<" ";
    }
    cout << "\n";
}

void bkt(int sol[],int index,int n)
{
    print_solution(sol,index);;
    //if (value(sol,index) == n)
        //print_solution(sol,index);
    //else
    {
        for(int i = 0; i < 4; i++){
            sol[index] = i;
            //nu are rost sa mergem mai departe daca suma pana
            //la indexul curent e mai mare
            if(value(sol,index) <= n)
                bkt(sol,index+1,n);
        }
    }
}

int main()
{
    int n = 10;//100 cents
    int sol[1000];

    bkt(sol,0,n);


    return 0;
}
