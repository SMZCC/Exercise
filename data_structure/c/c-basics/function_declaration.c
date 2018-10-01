# include <stdio.h>

/*在编译阶段，编译系统需要检查主调函数中调用的各种函数是否合法，对于我们
  自定义的函数，如果是在主调函数之前定义的，由于编译系统已经见识过自定义的函数
  所以无需告知编译系统我们自定义的函数的情况；若是被调函数是在主调函数之后定义
  的，那么我们则需要通过函数声明(函数原型)告知编译系统，这个自定义函数的类型，
  形参的个数，以及各个形参的顺序、类型等等检查信息*/

// 被调函数add()在主调函数main前面定义，主调函数main()中不需要进行声明
int add(int a, int b){
    return a+b;
}

int main(){
    int sum;
    sum = add(1, 3);
    printf("1 add 3 is: %d\n", sum);
    return 0;
}


/*

int main(){
    int sum;
    int add(int, int);  // 这里对被调函数进行声明,告诉编译系统被调函数的类型、
    sum = add(1, 3);    // 名称、形参的顺序、类型等
    printf("1 add 3 is: %d\n", sum);
    return 0;

int add(int a, int b){
    return a+b;
}

*/


