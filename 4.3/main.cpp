//Given a sorted (increasing order) array,
//write an algorithm to create a binary tree with minimal height
#include <iostream>
#include <stdlib.h>
#include <queue>
using namespace std;

class node{
    public:
    int data;
    node *left;
    node *right;
};

node* new_node(int value){
    node *a = (node*)malloc(sizeof(node*));
    a->data = value;
    a->left = NULL;
    a->right = NULL;
    return a;
}

void preOrder(node* node)
{
    if(node != NULL){
        cout << node->data << " ";
        preOrder(node->left);
        preOrder(node->right);
    }
    else return;
}

node* binary_tree(int x[],int st,int dr){
    if(st > dr)
        return NULL;
    int mid = (st+dr)/2;
    node *mid_elem = new_node(x[mid]);
    //go and find new elements in left and right part
    mid_elem->left = binary_tree(x,st,mid-1);
    mid_elem->right = binary_tree(x,mid+1,dr);
}

int main()
{
    int n;
    cout << "n = "; cin >> n;
    int *sir = (int*)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++){
        cout << "element "<<i<<" = ";
        cin >> sir[i];
    }
    //first element is the root
    node *root = binary_tree(sir,0,n-1);
    preOrder(root);

    return 0;
}
