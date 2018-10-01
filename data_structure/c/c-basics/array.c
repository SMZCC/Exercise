# include <stdio.h>
/*定义的数组中的值,分为两种情况：
  1.没有对数组进行赋初值的话，数组的值都是内存中的垃圾值
  2.对数组中部分元素赋初值，那么其余的元素均是0，其余的元素依旧是
    原来内存中的垃圾值*/

int main(){
    int array_1[10], array_2[]={1};
    int i;
    // array_1
    for(i=0;i<10;i++){
        if(i != 9) printf("%d ", array_1[i]);
        else printf("%d\n", array_1[i]);
    }

    // array_2
    for(i=0; i<10; i++){
        if(i != 9) printf("%d ", array_2[i]);
        else printf("%d\n", array_2[i]);
    }
    return 0;   
}
