# include <stdio.h>
/*float 单精度浮点类型数据，有效精度位数为7位有效数字，
double双精度类型数据，有效位数为9位有效数字;
注：
  1.小数点也是算一位的
  2.不同的编译系统的精确位数可能不同，
    我这个Ubuntu float 能精确9位，double能精确至少13位*/

int main(){
  float a;
  double b;
  a = 123456.897;  // out: 123456.898438其中8438是误差
  b = 123456.891234;  // out: 123456.891234
  printf("a:%.6f, b:%.6f", a, b);
  return 0;
}
