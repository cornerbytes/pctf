// gcc -fno-stack-protector -no-pie -o chall chall.c
#include <stdio.h>

void batubaflag(int arg1)
{
    char flag[64];
    FILE *flag_file;

    flag_file = fopen("flag.txt", "r");

    if (flag_file == NULL) {
        printf("no flag.txt ?");
	fflush(stdout);
    }

    if (arg1 == 0xdeadbeef) {
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

    printf("\nKurang keras sweeper\n");
    fflush(stdout);

    return 0;
}
