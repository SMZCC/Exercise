# include <stdio.h>
/*为何会有两个空行*/

int main(){
    char a;
    a = getchar();  // 按下回车，输入一个空行
    putchar(a);     // 输出一个空行，可是结果是显示两个空行，为什么？
    printf("end\n");
    return 0;
}
