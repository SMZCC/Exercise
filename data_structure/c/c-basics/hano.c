# include <stdio.h>

/*递归就是通过不断调用自身来将问题分解到能够解决的程度，然后再使用已经解决的
 问题去解决尚未解决的问题，其中，尚未解决的问题与原问题是同性质的问题，只是规模
 更小罢了

 例如： 经典的汉诺塔：如何将A柱上的n个盘子经过B的协助移动到C柱上(盘子顺序不变)
 能够解决的问题是：只有一个盘子的时候，直接从A柱上移动到C柱上，要想A柱上只有一
                   个盘子，只有先将A柱上n-1个盘子先移动到B柱上
 尚未解决的问题是：如何将B柱上的n-1个盘子经过A柱的协助移动到C柱上，与原来的问题
                   是同性质的问题
 */


int move(char a, char b){
    printf("%c --> %c\n", a, b);
    return 0;
}

int hano(int n, char a, char b, char c){  // 将A柱上的盘子经过B柱的协助移动到C柱
    if(n == 1) move(a, c);  //只有一个盘子的已解决问题
    else{  // 通过不断调用自身，缩小问题规模，直到达到能够被解决的状态
        hano(n-1, a, c, b);  
        move(a, c);
        hano(n-1, b, a, c);
    }
    return 0;
}

int main(){
    int n;
    printf("Input the number of disks:");
    scanf("%d", &n);
    hano(n, 'A', 'B', 'C');
}

