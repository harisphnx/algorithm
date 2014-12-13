#include <stdio.h>
#include <stdlib.h>
 
struct node
{
    int data;
    struct node* left;
    struct node* right;
};
 
void printGivenLevel(struct node* root, int level);
int height(struct node* node);
struct node* addnode(int data);
 
void printLevelOrder(struct node* root)
{
  int h = height(root);
  int i;
  printf("height: %d\n",h);
  for(i=1; i<=h; i++)
    printGivenLevel(root, i);
}    
 
void printGivenLevel(struct node* root, int level)
{
  if(root == NULL)
    return;
  if(level == 1)
    printf("%d ", root->data);
  else if (level > 1)
  {
    printGivenLevel(root->left, level-1);
    printGivenLevel(root->right, level-1);
  }
}
 
int height(struct node* node)
{
   if (node==NULL)
       return 0;
   else
   {
     int lheight = height(node->left);
     int rheight = height(node->right);
 
     if (lheight > rheight)
         return(lheight+1);
     else return(rheight+1);
   }
}
 
struct node* addnode(int data)
{
  struct node* node = malloc(sizeof(struct node));
  node->data = data;
  node->left = NULL;
  node->right = NULL;
  return(node);
}
 
int main()
{
  struct node *root = addnode(1);
  root->left        = addnode(6);
  root->right       = addnode(89);
  root->left->left  = addnode(3);
  root->left->right = addnode(67);
 
  printf("Level Order traversal of binary tree is \n");
  printLevelOrder(root);
 
  return 0;
}
