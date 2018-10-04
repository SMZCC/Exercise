# include <stdio.h>
/*当输入的个数不确定时，使用while，利用scanf的返回值,scanf的返回值说明如下：
1. 当scanf读取到符合格式字符串的内容的时候，就会返回1，否则会返回0*
2. 在Ubuntu上按回车键就确定本次输入完毕了，空格与tab不会*/

int main(){
    int a[3], i=0, iscorrect_input;
    while(iscorrect_input = scanf("%d", a+i) == 1){
        if(i>2){printf("The program is ended\n"); break;}
        else printf("Your input is %d\n", *(a+i));
        i++;
    }
    if(!iscorrect_input) printf("You have input invalid data\n");
    return 0;
}
