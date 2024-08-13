#include <stdio.h>

void batubaflag()
{
    char flag[64];
    FILE *flag_file;

    flag_file = fopen("flag.txt", "r");

    if (flag_file == NULL) {
        printf("no flag.txt ?");
        fflush(stdout);
    } else {
        fgets(flag, sizeof(flag), flag_file);
        fclose(flag_file);
        printf("%s", flag);
        fflush(stdout);
    }
}

int main()
{
    char buffer[32];

    printf("Coba panggil flag: ");
    fflush(stdout);
    scanf("%s", buffer);

    printf("\nLebih keras!\n");
    fflush(stdout);

    return 0;
}
