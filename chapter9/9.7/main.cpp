//A circus is designing a tower routine consisting of people
//standing atop one another’s shoulders. For practical and aesthetic reasons,
// each person must be both shorter
//and lighter than the person below him or her. Given the heights and weights of each
//person in the circus, write a method to compute the largest possible number
// of people in such a tower.
//EXAMPLE:
//Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
//Output: The longest tower is length 6 and includes from top to bottom: (56, 90)
//(60,95) (65,100) (68,110) (70,150) (75,190)

//Algorithm
//#1 Idea
//Backtracking

//#2 Idea
//Sort after height
//Sort after weight
//Find the long subsequence .
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream fin("date.in");
typedef struct Person
{
    int height;
    int weight;
};

int n,h,w,i=0;
Person p[50];

void read()
{
    fin >> n;
    while (fin >> h >> w)
    {
        p[i].height = h;
        p[i++].weight = w;
    }
}

void display_persons()
{
    for(int i = 0; i < n; i++)
    {
        cout << p[i].height<<" ";
        cout << p[i].weight<<"\n";
    }
}

bool compareHeight(Person x , Person y)
{
    return (x.height > y.height);
}

int compareWeight(Person x , Person y)
{
    return (x.weight > y.weight);
}

//returns the number of possible people in tower
int LargeSubsequence()
{
    int sequence_lenght = 0;
    int max_sequence_lenght = 0;
    //go through the sorted array
    for(int i = 0; i < n-1; i++)
    {
        //daca cele 2 elemente consecutive sunt in ordine descrescatoare
        if(compareHeight(p[i],p[i+1]) != 1 && compareWeight(p[i],p[i+1]) != 1)
        {
            //inseamna ca secventa curenta creste
            sequence_lenght++;
        }
        else
        {
            //inseamna ca secventa curenta e gata
            if((i - sequence_lenght + 1) > max_sequence_lenght)
                max_sequence_lenght = i-sequence_lenght+1;
            //incepe o noua secventa curenta
            sequence_lenght = 0;
        }
        //cout << p[i].height << " " << p[i].weight << endl;
        //cout << p[i+1].height << " " << p[i+1].weight << endl;
        //cout << "sequence lenght : "<<max_sequence_lenght<<endl;
    }
    return max_sequence_lenght;
}

int main()
{
    read();
    sort(p,p+n,compareHeight);
    sort(p,p+n,compareWeight);
    cout << LargeSubsequence()+1;
    fin.close();
    return 0;
}
