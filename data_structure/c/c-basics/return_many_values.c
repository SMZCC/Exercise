# include <stdio.h>
/*return 只能返回一个值，不可像python一样返回多个值，
即使写成return a, b, c也只是返回逗号表达式的返回值(最后一个元素)
注意：
  1. 由于函数调用只能得到一个返回值，若想使得函数调用获得多个返回值，可以将这些
     返回值设置成全局变量 从而函数调用后可以将结果存在这些全局变量中
  2. 将需要被修改的变量的地址传递给函数，通过指针来修改这些变量*/

int checkReturnValues(){
  return 1, 2, 3;
}

int main(){
  int a=5, b=6, c=7;
  a, b, c =  checkReturnValues();
  printf("a:%d, b:%d, c:%d", a, b, c);
}
