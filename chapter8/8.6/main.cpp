#include <iostream>
#include <fstream>
//Implement the “paint fill” function that one might see on
//many image editing programs. That is, given a screen (represented
//by a 2 dimensional array of Colors), a
//point, and a new color, fill in the surrounding area until you hit a
//border of that color.’
using namespace std;
ifstream fin("date.in");
ofstream fout("date.out");

void Read_Paint(int &n,int matrix[100][100],pair<int,int> &x)
{
    fin >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            fin>>matrix[i][j];
    fin >> x.first;
    fin >> x.second;
}
//N-E-S-V
int direction_i[] = {-1,0,1,0};
int direction_j[] = {0,1,0,-1};

int isOk(int line,int col, int m[100][100], int n)
{
    if(line >= 0 && line < n && col >= 0 && col < n && m[line][col] != 1)
        return true;
    return false;
}

int color = 5;
int visited[100][100];

void Fill_SurroundingArea(int n,int matrix[100][100],int line,int column)
{
    visited[line][column] = 1;
    matrix[line][column] = color;

    for(int i = 0; i < 4; i++)
    {
        int i_vecin = line + direction_i[i];
        int j_vecin = column + direction_j[i];

        if(isOk(i_vecin,j_vecin,matrix,n) && visited[i_vecin][j_vecin] == 0)
            Fill_SurroundingArea(n,matrix,i_vecin,j_vecin);
    }
}

int main()
{
    int matrix[100][100],n;
    pair <int,int> point;

    Read_Paint(n,matrix,point);
    Fill_SurroundingArea(n,matrix,point.first,point.second);

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
            fout<<matrix[i][j]<<" ";
        fout << "\n";
    }

    fin.close();
    fout.close();
    return 0;
}
