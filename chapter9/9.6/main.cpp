#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input.txt");
//Given a matrix in which each row and each column is sorted,
//write a method to find
//an element in it.

int m[100][100];
int n,x = 5;

void read()
{
    fin >> n;
    for(int i =0 ; i < n; i++)
        for(int j = 0; j < n; j++)
            fin >> m[i][j];
}

bool find_in_matrix()
{
    int left1=0,right1=n-1;
    int left2=0,right2=n-1;

    while (left1 <= right1)
    {
        int mid1 = (left1+right1)/2;

        //optimize idea
        //search in this line just if
        //x >= a[mid1][0] and x <= a[mid1][n-1]
        if(x >= m[mid1][0] && x <= m[mid1][n-1])
        {
            left2 = 0;
            right2 = n-1;
            while(left2 <= right2)
            {
                int mid2 = (left2+right2)/2;

                if(m[mid1][mid2] == x)
                    return true;
                else if(x > m[mid1][mid2])
                    left2 = mid2+1;
                else
                    right2 = mid2-1;
            }
        }

        if(x > m[mid1][n-1])
            left1 = mid1+1;
        if(x < m[mid1][0])
            right1 = mid1-1;
    }
    return false;
}

int main()
{
    //Algorithm
    //double binary search
    //one binary search for first line
    //one binary search in the line's elements
    read();
    cout << find_in_matrix();
    fin.close();
    return 0;
}
