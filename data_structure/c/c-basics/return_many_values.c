# include <stdio.h>
/*return 只能返回一个值，不可像python一样返回多个值，
即使写成return a, b, c也只是返回逗号表达式的返回值(最后一个元素)*/

int checkReturnValues(){
  return 1, 2, 3;
}

int main(){
  int a=5, b=6, c=7;
  a, b, c =  checkReturnValues();
  printf("a:%d, b:%d, c:%d", a, b, c);
}
