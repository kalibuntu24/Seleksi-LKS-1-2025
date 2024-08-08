#include <stdio.h>
#include <string.h>

int main() {
    // Definisikan string yang akan dicek
    char inputString[100];
    // Definisikan flag yang akan dicek
    char flag[] = "SIJA{c3k_fl4g_c4r1_y4ng_b3n4r}";

    // Meminta input dari pengguna
    printf("Masukkan string: ");
    fgets(inputString, sizeof(inputString), stdin);
    
    // Menghapus karakter newline dari input
    size_t len = strlen(inputString);
    if (len > 0 && inputString[len-1] == '\n') {
        inputString[len-1] = '\0';
    }

    // Cek apakah inputString mengandung flag
    if (strstr(inputString, flag) != NULL) {
        printf("Flag benar!\n");
    } else {
        printf("Flag salah.\n");
    }

    return 0;
}
