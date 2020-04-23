#include <iostream>
#include <stack>
#include <cmath>
using namespace std;

int rods_movement(stack <int> &a, stack <int> &b){
    //#1 part
    if(a.empty() && b.empty())
        return 0;
    if(a.empty() && !b.empty()){
        a.push(b.top());
        b.pop();
        //return 0 is for stopping the function to go to #2 part
        return 0;
    }
    if(!a.empty() && b.empty()){
        b.push(a.top());
        a.pop();
        return 0;
    }
    //#2 part
    if(a.top() < b.top()){
        //punem vf lui a in b
        b.push(a.top());
        //stergem varf a
        a.pop();
    }
    else {
        //analog mai sus
        a.push(b.top());
        b.pop();
    }
    return 0;
}
void print_stack(stack <int> a){
    while (!a.empty()){
        cout << a.top() << "\n";
        a.pop();
    }
}
void Hanoi (stack <int> a, stack <int> b,stack <int> c, int n){
    bool isFinished = false;
    int pasi = 0;
    int possible_moves = pow(2,n)-1;
    while (true){
        //step1
        rods_movement(a,c);
        pasi+=1;
        if(c.size() == n)
            break;
        //step2
        rods_movement(a,b);
        pasi += 1;
        if(c.size() == n)
            break;
        //step3
        rods_movement(b,c);
        pasi += 1;
        if(c.size() == n)
            break;
        //if all the disks are moved
    }
    cout << "pasi : "<<pasi<<"\n";
    cout << "stack c \n";
    print_stack(c);
}

int main()
{
    int n = 3;
    stack <int> a;
    stack <int> b;
    stack <int> c;
    a.push(10);
    a.push(8);
    a.push(5);
    Hanoi(a,b,c,n);
    return 0;
}
