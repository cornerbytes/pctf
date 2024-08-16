#include <stdio.h>
#include <string.h>

void decrypt(char *output, const int *input, size_t input_size) {
    for (size_t i=0;i < input_size;i++) {
        output[i] = input[i] ^ 0x532;
    }
}

int main(int argc, char *argv[]) {
    char input[64];
    char flag[64];
    int enc_flag[] = {0x562,0x571,0x566,0x574,0x549,0x558,0x547,0x541,
                      0x546,0x56d,0x546,0x540,0x506,0x551,0x501,0x56d,
                      0x557,0x544,0x557,0x540,0x54b,0x546,0x55a,0x503,
                      0x55c,0x575,0x513,0x513,0x56d,0x56d,0x557,0x504,
                      0x507,0x557,0x503,0x500,0x556,0x505,0x54f};

    printf("Masukkan flag: ");
    fflush(stdout);
    scanf("%s", &input);

    decrypt(flag, enc_flag, (sizeof(enc_flag)/4));

    int checked = strcmp(flag, input);

    if (checked == 0) {
        printf("Selamat! kamu menebak flag dengan benar!");
    } else {
        printf("Flag Salah! Silahkan coba dilain waktu..");
    }

    return 0;
}
