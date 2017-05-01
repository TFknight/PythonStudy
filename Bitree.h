/*BiTree.h 头文件，包含栈的定义及常用操作的声明
相应操作的定义在平衡二叉树.cpp*/ 


typedef char ElemType;

typedef struct BiTNode
{ElemType data;
struct BiTNode *lchild,*rchild;
}BiTNode,*BiTree;


int CreatBiTree(BiTree &T);
void Destroy(BiTree T);


