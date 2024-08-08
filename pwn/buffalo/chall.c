#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include <unistd.h>


void win(){
        FILE* file;
    int c = 0;

    file = fopen("flag.txt", "r");

    if (NULL == file) {
        fprintf(stderr, "Cannot open flag.txt");
        exit(EXIT_FAILURE);
    } else {
        while (1) {
            c = fgetc(file);
            if (c == EOF)
                break;
            putchar(c);
        }
        fclose(file);
    }
}

int main(void)
{
    char password[32];
    int authorised = 0;

    printf("Enter admin password: \n");
    gets(password);

    if(strcmp(password, "pass") == 0)
    {
        printf("Correct Password!\n");
        authorised = 0;
    }
    else
    {
        printf("Incorrect Password!\n");
    }

    if(authorised)
    {
        printf("Successfully logged in as Admin (authorised=%d) :)\n", authorised);
        win();
    }else{
                printf("Failed to log in as Admin (authorised=%d) :(\n", authorised);
        }

    return 0;
}
