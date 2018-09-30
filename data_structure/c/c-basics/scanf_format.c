# include <stdio.h>
/*scanf()函数中的第一个参数：格式化字符串与输入之间有着严格的对应关系
  1. “%d%d”: 从控制台输入的数字之间可以有一个活者多个空格，甚至可以是Enter、Tab分隔
  2. "%d %d": 同"%d%d"
  3. "%d,%d": 必须要使用逗号隔开各个数字,至于逗号之后还有多少个空格，是不管的,也不可     使用回车来隔开字符，否则，从变量中读出来的值就是原来内存中的垃圾值*/

int main(){
    int a, b;
    int c, d;
    scanf("%d%d", &a, &b);
    printf("a=%d, b=%d\n", a, b);
    
    scanf("%d %d", &c, &d);
    printf("c=%d, d=%d\n", c, d);

    int e, f;
    scanf("%d,%d", &e, &f);
    printf("e=%d, f=%d\n", e, f);
}
