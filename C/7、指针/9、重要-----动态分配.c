#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void dt()
{
    int x;
    scanf ("%d", &x);
    int *p = (int *)  malloc (x * sizeof (int));

    /*for (int i = 0; i < x; i++)
    {
        p[i] = i + 1;
        printf ("%d	,	%x\n", p[i], p + i);
    }*/

    for (int *px = p, i = 0; px < p + x; px++, i++)
    {
        *p = i + 1;
        printf ("%d\n", *p);
    }

    free (p);
    p = NULL;// 软件工程规范, 不置空，再次释放以及p[i]都回报错
    // 只有空指针，反复释放，都没有问题
}
void main()
{
    dt();
    //void *x = malloc(20); // 开辟内存；
    // 如果x==NULL,分配内存失败
    //free(x); //释放内存
    getchar();
    getchar();
}