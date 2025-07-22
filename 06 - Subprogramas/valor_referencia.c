#include <stdio.h>

void por_valor(int x) {
    x = x + 10;
    printf("Dentro de por_valor: %d\n", x);
}

void por_referencia(int *x) {
    *x = *x + 10;
    printf("Dentro de por_referencia: %d\n", *x);
}

int main() {
    int a = 5;
    
    por_valor(a);
    printf("Após por_valor: %d\n", a);
    
    por_referencia(&a);
    printf("Após por_referencia: %d\n", a);

    return 0;
}
