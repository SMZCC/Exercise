# include <stdio.h>

/*打印指针值的时候需要使用格式符：%p,旧书上使用的是%o报错，不能通过编译*/

void main(){
    int a[3][4] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23};
    int * p;
    for(p=a[0]; p<a[0]+12; p++){
        printf("addr=%p, value=%2d\n", p, *p);
    }
}
