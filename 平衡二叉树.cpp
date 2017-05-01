//判断是否平衡二叉树的另一种方法 

#include <iostream>

#include "Bitree.cpp"
using namespace std;


bool IsBalancedTree( BiTree, int& ); //判断二叉树是否平衡树，并通过引用返回该二叉树的深度

int main()
{
	BiTree T = NULL;
	CreatBiTree( T );//根据用户的输入创建二叉树，函数定义在 BiTree.h          头文件里面！！！！！ 
	
	int depth = 0;
	if ( IsBalancedTree( T, depth )) cout << "Yes" << endl;           //为什么会多加形参呢？？ 
	else cout << "No" << endl;
	
	Destroy(T);//销毁二叉树 ， 函数定义在 BiTree.h 
	
	return 0;
}

bool IsBalancedTree( BiTree T, int &depth )
{//判断二叉树是否平衡树，并通过引用返回该二叉树的深度	
	if (T==NULL) //二叉树T为空，则深度为0，同时T是平衡树 
	{
		depth = 0;
		return true;
	}
	
	int LDepth, RDepth;
	if ( ! IsBalancedTree( T->lchild, LDepth ) ) return false; //左子树不平衡，返回false 
	if ( ! IsBalancedTree( T->rchild, RDepth ) ) return false; //右子树不平衡，返回false
	
	//左右子树都平衡，还得求两子树深度之差，才能判断当前树T是否平衡 
	int diff = LDepth - RDepth;
	//cout<<diff<<endl; 
	if ( diff > 1 || diff < -1 ) return false;
	
	//两子树深度之差满足平衡条件，故当前树T的深度是 大者+1，且T是平衡树 
	depth = max ( LDepth, RDepth ) + 1; 
	
	return true;	
}
