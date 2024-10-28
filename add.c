#include <stdio.h>

int main() {
    int R2 = 0; // Base address
    int memory[10] = {10, 20, 30, 0, 0, 0, 0, 0, 0, 0}; // Simulated memory
    int R1 = memory[R2 / 4]; // LOAD R1, 0(R2)
    int R3 = memory[(R2 + 4) / 4]; // LOAD R3, 4(R2)
    int R4 = R1 + R3; // ADD R4, R1, R3
    memory[(R2 + 8) / 4] = R4; // STORE R4, 8(R2)
    int R5 = R1 - R3; // SUB R5, R1, R3
    printf("R4: %d, R5: %d\n", R4, R5);
    return 0;
}
