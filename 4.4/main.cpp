//Given a binary search tree, design an algorithm which creates a linked list of all
//the nodes at each depth (i e , if you have a tree with depth D, you’ll have D linked lists)
#include <iostream>
#include <stdlib.h>
#include <vector>

using namespace std;

struct ListNode{
    int data;
    ListNode *next;
    //insert at the ending
    void display_list(){
        ListNode *t = new ListNode;
        t = this;
        while (t->next != NULL){
            cout << t->data << " ";
            t = t->next;
        }
        cout << t->data;
        cout << "\n";
    }
};

struct TreeNode{
    int data;
    TreeNode *left;//adress to the left son
    TreeNode *right;//adress to the right son
};

TreeNode* new_Node(int info){
    TreeNode *node = new TreeNode;
    node->data = info;
    node->left = NULL;
    node->right = NULL;
    return node;
}
//returneaza inaltimea arborelui
//se apeleaza h(root)
int Height(TreeNode *current){
    if(current == NULL)
        return -1;
    else {
        int left_height = Height(current->left);
        int right_height = Height(current->right);
        //luam inaltimea maxima dintre inaltimea subarborelui stang si a subarborelui drept
        if(left_height > right_height)
            return (left_height+1);
        else return (right_height+1);
    }
}

void AppendToList(ListNode*& a,int info){
    struct ListNode *aux = new ListNode;
    aux->data = info;
    aux->next = NULL;
    if(a == NULL){
        a = aux;
    }
    else {
        //merg pana la final
        while (a->next != NULL){
            a = a->next;
        }
        a->next = aux;
    }
}

//
//nivel incepe de la 1
//am un vector de vizitati
//presupun ca datele nodurilor sunt distincte
//afiseaza nodurile de pe un nivel dat
//si le pune intr-un nivel
void dfs(struct TreeNode *root , int nivel , struct ListNode *&a){
    if (root == NULL)
        return;
    if(nivel == 1){
        //cout << root->data << " ";
        AppendToList(a,root->data);
    }
    else {
        dfs(root->left , nivel-1 , a);
        dfs(root->right , nivel-1 , a);
    }
}

void solve(int height , struct TreeNode* root){
    //e height+1 acolo pt ca height-ul e numarul de muchii pana la cea mai
    //indepartata frunza de root
    //pac pac
    for(int level = 1 ; level <= height+1; level++){
        struct ListNode *level_list = new ListNode;
        dfs(root,level,level_list);
        level_list->display_list();
    }
}

int main()
{
    //generare noduri
    struct TreeNode *root = new_Node(7);
    struct TreeNode *a = new_Node(6);
    struct TreeNode *b = new_Node(10);
    struct TreeNode *c = new_Node(2);
    struct TreeNode *d = new_Node(3);

    //legaturi
    root->left = a;
    root->right = b;
    a->left = c;
    a->right = d;

    int height = Height(root);
    /*
    GATA METODA VECHE TICU
    TRECEM PE CEVA NOU
    CA NE PERMITEM
    */
    solve(height,root);
    return 0;
}
