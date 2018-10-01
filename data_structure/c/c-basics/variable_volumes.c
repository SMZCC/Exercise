# include <stdio.h>

/*各个数据类型的大小统计：
 1. int:       4
 2. char:      1
 3. float:     4
 4. double:    8
 */

int main(){
    int a = 4;
    char b = 'A';
    float c = 1.2;    
    double d = 2.4;
    
    printf("The size of int is %ld kb\n", sizeof(a));
    printf("The size of char is %ld kb\n", sizeof(b));
    printf("The size of float is %ld kb\n", sizeof(c));
    printf("The size of double is %ld kb\n", sizeof(d));
    
    return 0;
}

