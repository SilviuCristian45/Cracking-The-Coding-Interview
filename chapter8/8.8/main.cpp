#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
//Write an algorithm to print all ways of arranging eight queens
//on a chess board so that none of them share the same row, column or diagonal
ifstream fin("input.txt");
ofstream fout("output.txt");

char board[100][100];
int N;

bool isOk(int sol[],int index)
{
    //lines are different because the from 0 ,... index
    //are different
    for(int i = 0; i <= index-1; i++)
    {
        if(sol[i] == sol[index])
            return false;
        if(abs(i-index) == abs(sol[i]-sol[index]))
            return false;
    }
    return true;
}

void read_board()
{
    fin >> N;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            fin >> board[i][j];
}

void print_board()
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            fout << board[i][j]<<" ";
        fout << "\n";
    }
}

void reset_board()
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < N; j++)
            board[i][j] = '-';

    }
}

void print_solution(int sol[])
{
    for(int i = 0; i < N; i++)
    {
        board[i][sol[i]] = '*';
    }
}

int ok = 0;//check if it is found the first arrangement
void print_queens(int sol[],int index)
{
    if(index == N)
    {
        print_solution(sol);
        print_board();
        ok = 1;
    }
    else
    {
        if(ok == 0)
        {
            for(int col = 0; col < N; col++)
            {
                sol[index] = col;
                if(index < N && isOk(sol,index))
                    print_queens(sol,index+1);
            }
        }
    }
}

int main()
{
    int sol[100];
    read_board();

    print_queens(sol,0);

    fin.close();
    fout.close();
    return 0;
}
