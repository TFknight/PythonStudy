//�ж��Ƿ�ƽ�����������һ�ַ��� 

#include <iostream>

#include "Bitree.cpp"
using namespace std;


bool IsBalancedTree( BiTree, int& ); //�ж϶������Ƿ�ƽ��������ͨ�����÷��ظö����������

int main()
{
	BiTree T = NULL;
	CreatBiTree( T );//�����û������봴�������������������� BiTree.h          ͷ�ļ����棡�������� 
	
	int depth = 0;
	if ( IsBalancedTree( T, depth )) cout << "Yes" << endl;           //Ϊʲô�����β��أ��� 
	else cout << "No" << endl;
	
	Destroy(T);//���ٶ����� �� ���������� BiTree.h 
	
	return 0;
}

bool IsBalancedTree( BiTree T, int &depth )
{//�ж϶������Ƿ�ƽ��������ͨ�����÷��ظö����������	
	if (T==NULL) //������TΪ�գ������Ϊ0��ͬʱT��ƽ���� 
	{
		depth = 0;
		return true;
	}
	
	int LDepth, RDepth;
	if ( ! IsBalancedTree( T->lchild, LDepth ) ) return false; //��������ƽ�⣬����false 
	if ( ! IsBalancedTree( T->rchild, RDepth ) ) return false; //��������ƽ�⣬����false
	
	//����������ƽ�⣬���������������֮������жϵ�ǰ��T�Ƿ�ƽ�� 
	int diff = LDepth - RDepth;
	//cout<<diff<<endl; 
	if ( diff > 1 || diff < -1 ) return false;
	
	//���������֮������ƽ���������ʵ�ǰ��T������� ����+1����T��ƽ���� 
	depth = max ( LDepth, RDepth ) + 1; 
	
	return true;	
}
