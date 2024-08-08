#include <stdio.h>
#include <stdlib.h>

unsigned int balance = 1000;

void showItems() {
    printf("Barang yang tersedia:\n");
    printf("1. Laptop - 500\n");
    printf("2. Handphone - 300\n");
    printf("3. Televisi - 700\n");
    printf("4. Flag (spesial) - 100000\n");
}

void getFlag() {
    FILE *file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("Error: Tidak bisa membuka file flag.txt\n");
        return;
    }
    char flag[256];
    if (fgets(flag, sizeof(flag), file) != NULL) {
        printf("Selamat! Anda telah membeli flag.\n");
        printf("%s\n", flag);
    } else {
        printf("Error: Tidak bisa membaca flag dari file\n");
    }
    fclose(file);
}

void buyItem(int choice, int price) {
    unsigned int requiredPrices[] = {500, 300, 700, 100000};
    unsigned int requiredPrice = requiredPrices[choice - 1];

    // Check if the price is negative and if it is, perform the integer overflow
    if (price < 0) {
        balance += (unsigned int) (-price);
        printf("Saldo Anda sekarang: %u\n", balance);
        return;
    }

    if (price != requiredPrice) {
        printf("Harga yang dimasukkan tidak sesuai.\n");
        return;
    }

    if (balance >= price) {
        balance -= price;
        if (choice == 4) {
            getFlag();
        } else {
            printf("Anda telah membeli barang pilihan %d\n", choice);
        }
    } else {
        printf("Saldo tidak cukup untuk membeli barang ini.\n");
    }

    printf("Saldo Anda sekarang: %u\n", balance);
}

int main() {
    int choice;
    int price;

    while (1) {
        printf("\nSaldo Anda: %u\n", balance);
        showItems();

        printf("Pilih barang yang ingin dibeli (1-4, atau 0 untuk keluar): ");
        scanf("%d", &choice);

        if (choice == 0) {
            printf("Terima kasih telah berbelanja!\n");
            break;
        } else if (choice > 0 && choice <= 4) {
            printf("Masukkan harga barang: ");
            scanf("%d", &price);
            buyItem(choice, price);
        } else {
            printf("Pilihan tidak valid.\n");
        }
    }

    return 0;
}
