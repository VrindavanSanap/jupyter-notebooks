#include <stdio.h>
int main(){
    int a = 0;
    for (int i = 0; i < 600 * 1000 * 1000; i++)
    {
        a++;
    }
    printf("%d", a);
}