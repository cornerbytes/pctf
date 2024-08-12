// gcc -o feedback feedback.c
#include <stdio.h>

int main(void) {
    char flag[64];
    char buf[128];
    FILE *flag_file;

    setvbuf(stdout, NULL, _IONBF, 0);

    puts("Tolong beri masukan aplikasi kami!");

    flag_file = fopen("flag.txt", "r");

    if (flag_file == NULL) {
        puts("no flag.txt ?");
        return 0;
    }

    fgets(flag, sizeof(flag), flag_file);
    fclose(flag_file);

    while (1) {
        fgets(buf, sizeof(buf), stdin);
        printf(buf);
    }
    return 0;
}

