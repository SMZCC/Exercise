# include <stdio.h>
/*初始化一个数组，其内的所有值都是3
 使用初始化: int a[10]={[0 ... 9]=3}; 注意...两端要有空格*/

int main(){
    int a[10]={3}, i=0;  // 只有第一个元素是3，其余元素全部是0
    int b[10] = {[0 ... 9]=3};  //注意...两端有空格
    for(;i<9;i++) printf("%d ", *(a+i));
    if(i == 9) printf("%d\n", *(a+i));

    for(i=0;i<9;i++) printf("%d ", *(b+i));
    if(i==9) printf("%d\n", *(b+i));
    return 0;
}
