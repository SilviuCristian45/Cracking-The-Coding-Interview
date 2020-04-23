#include <iostream>
#include <stdlib.h>
using namespace std;

struct Nod {
    int data;
    Nod *left;
    Nod *right;
};

//return a Nod* object , elemnt of a binary tree
Nod* new_node(int data){
    //alocate memory
    Nod *x = (Nod*)malloc(sizeof(Nod));
    x->data = data;
    x->left = NULL;
    x->right = NULL;
    return x;
}

//maximum depht
int max_depht(Nod *root){
    if(root == NULL)
        return -1;
    else {
        //maximul dintre dinstantele de pe subarborele din stanga si
        //cel din dreapta
        return max(1+max_depht(root->left),1+max_depht(root->right));
    }
}

int min_depht(Nod *root){
    if(root == NULL)
        return -1;
    else
        return min(1+min_depht(root->left),1+min_depht(root->right));
}

bool isBalanced(Nod *root){
    int min_d = min_depht(root);
    int max_d = max_depht(root);
    if(max_d-min_d <= 1)
        return true;
    return false;
}

int main()
{
    //a is the root
    Nod *a = new_node(23);
    Nod *b = new_node(46);
    Nod *c = new_node(88);
    Nod *d = new_node(51);

    a->left = b;
    b->left = d;
    a->right = c;

    cout << isBalanced(a);

    return 0;
}
