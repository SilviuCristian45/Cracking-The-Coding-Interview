//Write a program to sort a stack in ascending order
//You should not make any assump-tions about how the stack is implemented
//The following are the only functions that should be used to write
//this program: push | pop | peek | isEmpty
#include <iostream>
#include <stack>
using namespace std;
//sort stack - returns the sorted stack
stack<int> sort_stack(stack <int> s){
    stack <int> aux;
    while (!s.empty()){
        //current top of the stack s
        int vf_s = s.top();
        s.pop();
        while ( !aux.empty() && aux.top() > vf_s){
            //put all the elements from aux stack which are bigger than the top of the stack s
            s.push(aux.top());
            aux.pop();
        }
        //put the old top of stack is aux stack
        aux.push(vf_s);
    }
    return aux;
}

int main()
{
    stack <int> s;
    s.push(7);
    s.push(1);
    s.push(12);
    s.push(2);
    s.push(4);
    stack<int> sorted_stack = sort_stack(s);
    cout << "stack : \n";
    while (!sorted_stack.empty()){
        cout << sorted_stack.top() << "\n";
        sorted_stack.pop();
    }

    return 0;
}
