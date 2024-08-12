// gcc -o pythonic pythonic.c -I/usr/include/python3.11 -lpython3.11
#include <python3.11/Python.h>
#include <stdio.h>

#define DECKEY 0x41

unsigned char payload[] = {0x4b, 0x27, 0x2d, 0x20, 0x26, 0x61, 0x7c, 0x61, 0x28, 0x2f, 0x31, 0x34, 0x35, 0x69, 0x63, 0xc, 0x20, 0x32, 0x34, 0x2a, 0x2a, 0x20, 0x2f, 0x61, 0x27, 0x2d, 0x20, 0x26, 0x7b, 0x61, 0x63, 0x68, 0x4b, 0x24, 0x2f, 0x22, 0x61, 0x7c, 0x61, 0x1a, 0x73, 0x70, 0x6d, 0x61, 0x77, 0x6d, 0x61, 0x70, 0x76, 0x6d, 0x61, 0x72, 0x6d, 0x61, 0x77, 0x73, 0x6d, 0x61, 0x70, 0x79, 0x6d, 0x61, 0x75, 0x74, 0x6d, 0x61, 0x70, 0x70, 0x76, 0x6d, 0x61, 0x73, 0x77, 0x6d, 0x61, 0x74, 0x74, 0x6d, 0x61, 0x75, 0x79, 0x6d, 0x61, 0x75, 0x72, 0x6d, 0x61, 0x73, 0x73, 0x6d, 0x61, 0x73, 0x77, 0x6d, 0x61, 0x74, 0x72, 0x6d, 0x61, 0x74, 0x74, 0x6d, 0x61, 0x70, 0x70, 0x76, 0x6d, 0x61, 0x72, 0x75, 0x6d, 0x61, 0x74, 0x74, 0x6d, 0x61, 0x72, 0x77, 0x6d, 0x61, 0x75, 0x71, 0x6d, 0x61, 0x73, 0x77, 0x6d, 0x61, 0x75, 0x70, 0x6d, 0x61, 0x70, 0x70, 0x77, 0x6d, 0x61, 0x75, 0x77, 0x6d, 0x61, 0x70, 0x70, 0x79, 0x6d, 0x61, 0x75, 0x78, 0x6d, 0x61, 0x75, 0x74, 0x6d, 0x61, 0x70, 0x70, 0x77, 0x6d, 0x61, 0x73, 0x73, 0x6d, 0x61, 0x70, 0x73, 0x73, 0x6d, 0x61, 0x70, 0x71, 0x71, 0x6d, 0x61, 0x73, 0x77, 0x6d, 0x61, 0x72, 0x79, 0x6d, 0x61, 0x72, 0x72, 0x6d, 0x61, 0x70, 0x70, 0x77, 0x6d, 0x61, 0x72, 0x77, 0x6d, 0x61, 0x70, 0x73, 0x74, 0x6d, 0x61, 0x70, 0x70, 0x77, 0x6d, 0x61, 0x70, 0x70, 0x74, 0x6d, 0x61, 0x70, 0x73, 0x74, 0x6d, 0x61, 0x74, 0x77, 0x1c, 0x4b, 0x24, 0x2f, 0x22, 0x33, 0x38, 0x31, 0x35, 0x61, 0x7c, 0x61, 0x2d, 0x20, 0x2c, 0x23, 0x25, 0x20, 0x61, 0x39, 0x7b, 0x61, 0x2e, 0x33, 0x25, 0x69, 0x39, 0x68, 0x61, 0x1f, 0x61, 0x77, 0x78, 0x4b, 0x28, 0x27, 0x61, 0x69, 0x1a, 0x6b, 0x2c, 0x20, 0x31, 0x69, 0x24, 0x2f, 0x22, 0x33, 0x38, 0x31, 0x35, 0x6d, 0x61, 0x27, 0x2d, 0x20, 0x26, 0x68, 0x1c, 0x61, 0x7c, 0x7c, 0x61, 0x24, 0x2f, 0x22, 0x68, 0x7b, 0x4b, 0x61, 0x61, 0x61, 0x61, 0x31, 0x33, 0x28, 0x2f, 0x35, 0x69, 0x63, 0xa, 0x20, 0x2c, 0x34, 0x61, 0x2c, 0x24, 0x2f, 0x24, 0x23, 0x20, 0x2a, 0x61, 0x27, 0x2d, 0x20, 0x26, 0x61, 0x25, 0x24, 0x2f, 0x26, 0x20, 0x2f, 0x61, 0x23, 0x24, 0x2f, 0x20, 0x33, 0x60, 0x63, 0x68, 0x4b, 0x24, 0x2d, 0x32, 0x24, 0x7b, 0x4b, 0x61, 0x61, 0x61, 0x61, 0x31, 0x33, 0x28, 0x2f, 0x35, 0x69, 0x63, 0x2, 0x2e, 0x23, 0x20, 0x61, 0x2d, 0x20, 0x26, 0x28, 0x60, 0x63, 0x68, 0x4b};
const size_t payload_len = sizeof(payload);

void decrypt(unsigned char *data, size_t len, unsigned char key) {
    for (size_t i = 0; i < len; i++) {
        data[i] ^= key;
    }
}

int main(int argc, char *argv[])
{
    decrypt(payload, payload_len, DECKEY);

    Py_Initialize();
    PyRun_SimpleString(payload);
    Py_Finalize();

    return 0;
}

