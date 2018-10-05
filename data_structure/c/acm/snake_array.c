# include <stdio.h>
# include <string.h>
/*
    10 11 12 1
    9  16 13 2
    8  15 14 3
    7  6  5  4
*/

int main(){
    // 初始化矩阵
    const int MAXN = 20;   // 最大可显示20x20的蛇行数
    int array[MAXN][MAXN];
    memset(array, 0, sizeof(array));

    //读入需要显示的矩阵的大小
    //并设置初始状态为输入维度大小的矩阵的右上角
    //数据填充在初始化矩阵的左上角
    int n, h, w, num;
    scanf("%d", &n);
    h = 0, w = n-1, num=1;
    array[h][w] = num;
    
    while(num < n*n){ // 因为包含了判断是否已经填数了，所以索引不必复杂考虑

        while(h+1<n && !array[h+1][w]) array[++h][w] = ++num;
        while(w-1>=0 && !array[h][w-1]) array[h][--w] = ++num; //h,w是能0的
        while(h-1>=0 && !array[h-1][w]) array[--h][w] = ++num;  
        while(w+1<n && !array[h][w+1]) array[h][++w] = ++num;
    }
    
    //output
    int i, j;
    for(i=0; i<n; i++){
        for(j=0; j<n; j++) printf("%3d", array[i][j]);
        putchar('\n');
    }
    return 0;
}
