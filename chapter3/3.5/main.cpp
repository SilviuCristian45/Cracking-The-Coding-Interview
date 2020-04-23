//Implement a MyQueue class which implements a queue using two stacks
#include <iostream>
#include <stack>
using namespace std;

class MyQueque{
    stack <int> s1;
    stack <int> s2;
    //s2 will be the reverse of s1
    //s1 will store only the new elements
    public:void add(int data){
        s1.push(data);
    }
    //get the first element of the queue
    public:int peek(){
        if(!s2.empty())
            return s2.top();
        else
        {
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }
    public:void remov(){
        if(!s2.empty()){
            s2.pop();
        }
        else
        {
            while(!s1.empty()){
                s2.push(s1.top());
                s1.pop();
            }
            s2.pop();
        }
    }

};


int main()
{
    MyQueque q;
    q.add(45);
    q.add(24);
    q.add(22);
    q.add(78);
    cout << q.peek();
    q.remov();
    cout << q.peek();
    return 0;
}
