#include <iostream>
using namespace std;

//Given a sorted array of n integers that has been rotated an unknown number of
//times, give an O(log n) algorithm that finds an element in the array. You may assume
//that the array was originally sorted in increasing order.
//EXAMPLE:
//Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
//Output: 8 (the index of 5 in the array)

int main()
{
    //Idea
    //If the array was originally sorted at after that , it was sorted
    //It means that at a point in the array , there are 2 elements a[i] and a[i+1]
    //a[i] > a[i+1] . At that point it means that from 0 to point the array is sorted
    //and from p+1 to N , the array is sorted
    //binary search in the first part and binary search in the second part

    return 0;
}
