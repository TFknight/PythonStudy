/*BiTree.h ͷ�ļ�������ջ�Ķ��弰���ò���������
��Ӧ�����Ķ�����ƽ�������.cpp*/ 


typedef char ElemType;

typedef struct BiTNode
{ElemType data;
struct BiTNode *lchild,*rchild;
}BiTNode,*BiTree;


int CreatBiTree(BiTree &T);
void Destroy(BiTree T);


