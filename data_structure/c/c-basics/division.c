# include <stdio.h>
/*由于float类型的数据存储时分为符号部分+小数部分+指数部分，小数部分的位数
决定了该float数据的精度，所以有时使用一个很大的float数加上一个比较小的整数，
或者在损失了精度的情况下进行另外的运算都会得到出乎意料的结果*/

int main(){
  float result_1, result_2;
  result_1 = 1.0 / 3.0;
  result_2 = 1.0 / 3.0 * 3;
  printf("result_1:%.6f, result_2:%f", result_1, result_2);
}
