#include <stdio.h>
#include <stdlib.h>

void s3cr3t(char *flag, size_t flag_size) {
    FILE *flag_file;

    flag_file = fopen("flag.txt", "r");

    if (flag_file == NULL) {
        printf("No flag.txt?");
        exit(0);
    }

    fgets(flag, flag_size, flag_file);
}

void aisatsu(int key){
    char nama[64];
    char flag[64];

    printf("Masukkan nama: ");
    gets(nama);
    if(key != 0xd34dc0d3){
        s3cr3t(flag, sizeof(flag));
        printf("%s\n", flag);
    }
    else{
        printf("Selamat datang, %s!\n", nama);
    }
}
int main(int argc, char* argv[]){
    setvbuf(stdout, NULL, _IONBF, 0);

    printf(R"EOF(
 ________  ___  ________  ________  _________  ________  ___  ___
|\   __  \|\  \|\   ____\|\   __  \|\___   ___\\   ____\|\  \|\  \
\ \  \|\  \ \  \ \  \___|\ \  \|\  \|___ \  \_\ \  \___|\ \  \\\  \
 \ \   __  \ \  \ \_____  \ \   __  \   \ \  \ \ \_____  \ \  \\\  \
  \ \  \ \  \ \  \|____|\  \ \  \ \  \   \ \  \ \|____|\  \ \  \\\  \
   \ \__\ \__\ \__\____\_\  \ \__\ \__\   \ \__\  ____\_\  \ \_______\
    \|__|\|__|\|__|\_________\|__|\|__|    \|__| |\_________\|_______|
                  \|_________|                   \|_________|


 ________  ________  ________
|\   __  \|\   __  \|\   __  \
\ \  \|\  \ \  \|\  \ \  \|\  \
 \ \   __  \ \   ____\ \   ____\
  \ \  \ \  \ \  \___|\ \  \___|
   \ \__\ \__\ \__\    \ \__\
    \|__|\|__|\|__|     \|__|

)EOF");

    aisatsu(0xd34dc0d3);
    return 0;
}
