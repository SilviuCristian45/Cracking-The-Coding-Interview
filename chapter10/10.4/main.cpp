#include <iostream>
//Write a method to implement *, - , / operations
// You should use only the + operator
using namespace std;

float multiply(float a,float b)
{
    float m = 0;
    for(int i = 1; i <= b; i++)
        m += a;
    return m;
}

//a-b
float substract(float a, float b)
{
    return a + (-1)*b;
}

//a/b - vedem aflam exact numarul pentru care nr * b == a
//sau scadem din a pe b pana a ramane 0s
float divide(float a, float b)
{
    if(b != 0)
    {
        float result = 0;

        while(multiply(result,b) < a)
            result++;
        if (result == a)
            return result;
        else
            return result-1;
    }
    else
        cout << "error";

}

int main()
{
    cout << multiply(5,3) << endl;
    cout << substract(5,3) << endl;
    cout << divide(15,8) << endl;
    return 0;
}
