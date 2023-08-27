
// # LEETCODE : URL https://leetcode.com/problems/binary-tree-preorder-traversal/


#if 0
gcc -o $0.out $0 && ./$0.out $@
rm -f $0.out
exit
#endif

// # USING RECURSSIVE METHOD > ... 


#include<stdio.h>
#include<stdlib.h>:
#include<string.h>
#include<stdbool.h>

// // Definition for a binary tree node.
struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
 };

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void preorderTraversals(struct TreeNode* node, int* returner, int* i) {
    if (node !=NULL){

    returner[(*i)++] = node->val;
    preorderTraversals(node->left, returner, i);
    preorderTraversals(node->right, returner, i);
    }
}

int* preorderTraversal(struct TreeNode* root, int* returnSize){ 
    int* returner = (int*)malloc(sizeof(int) * (100));
    int i = 0;
    
    preorderTraversals(root, returner, &i);
    *returnSize = i;  
    
    return returner;
}

int main(){
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));  // if we don't use malloc, it will be a pointer to NULL 
    root->val = 1;
    root->left = NULL;
    root->right = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->right->val = 2;
    root->right->left = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->right->left->val = 3;
    root->right->left->left = NULL;
    root->right->left->right = NULL;
    root->right->right = NULL;
    int returnSize = 0;
    int* returner = preorderTraversal(root, &returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", returner[i]);
    }
    return 0;
}
