#include<iostream>
#include"Bitree.h"
using namespace std;

int CreatBiTree(BiTree &T)
{
	char ch;
	cin>>ch;
	if(ch == '#')
		return 0;
	else
	{
		T = new BiTNode;
		T->data = ch;
		T->lchild = NULL;
		T->rchild = NULL;
		CreatBiTree(T->lchild);
		CreatBiTree(T->rchild);
		return 0;
	}
}

void Destroy(BiTree T)
{
	if(!T)
		return; 
	Destroy(T -> lchild);
	Destroy(T -> rchild);
	delete T;
}
