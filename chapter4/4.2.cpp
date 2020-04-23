//Given a directed graph, design an algorithm
//to find out whether there is a route be-tween two nodes
#include <iostream>
#include <fstream>
using namespace std;
ifstream f("date.in");
const int N_MAX = 500;

void read_graph(int &n,int m[N_MAX][N_MAX]){
    f >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            f >> m[i][j];
}

bool visited[N_MAX];
//ok always starts with 0
//it means that we suppose that there is no route between given
//nodes
void checkIfRoute(int n,int m[N_MAX][N_MAX],int x,int y,int &ok){
    visited[x] = true;
    if(x == y)
        ok = 1;
    for (int i = 0; i < n; i++){
        //if x -> i and node i is not already visited
        if(m[x][i] == 1 && !visited[i]){
            checkIfRoute(n,m,i,y,ok);
        }
    }
}


int main()
{
    int n,m[N_MAX][N_MAX],y,x,ok=0;
    //reading
    read_graph(n,m);
    f >> x;
    f >> y;
    for(int i = 0; i < n; i++)
        visited[i] = false;
    checkIfRoute(n,m,x,y,ok);
    cout << ok;


    f.close();
    return 0;
}
