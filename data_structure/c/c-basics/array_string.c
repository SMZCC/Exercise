# include <stdio.h>

/*字符数组的输入输出可以利用%c一个字符一个字符的输入输出，也可利用%s,将整个
  字符串进行输入输出*/

int main(){
    char a[5];
    char b[5];

    // 一次性读入整个字符数组
    printf("Using %%s, input a string:");
    scanf("%s", a);
    printf("%s\n",a );
    
    // 一次读入一个字符数组
    int i;
    char c;
    printf("Using %%c, input a string:");
    getchar();  // 由于上面输入完之后会有一个回车，此时内存缓冲区会有一个回车符
                // 那么下面的循环中i=0的时候会先直接读入一个回车符，而这个回车符
                // 对于该程序来说是个垃圾值,所以在这里直接消耗掉该垃圾值
 
    for(i=0;(c=getchar()) != '\n', i < 5; i++){ // 该for是能把最后的回车符消耗掉
        b[i] = c;                      //的，当i=5时，依旧运行了getchar()函数
        printf("c[%d]:%c\n", i, c);
    }
    for(i=0; i<5; i++){
        if(i != 4) printf("%c", b[i]);
        else printf("%c\n", b[i]);
    }

    //如果字符数组的长度大于字符串的有效长度，那么上面的问题中的回车符会产生吗？
    //==> 会产生,内存缓冲区依旧会多出最后的回车，也就是说字符数组是不吃回车的，
    // 但是getchar()是吃回车的
    char d[7];
    //if(getchar() == '\n') printf("After last input fetching \\n");
    printf("Input china:");
    scanf("%s", d);
    if (getchar() == '\n') 
        printf("True, there is a \'\\n\' in the RAM cache !!!\n");
    else printf("False, there is no \'\\n\' in the RAM cache !!!\n");
}
