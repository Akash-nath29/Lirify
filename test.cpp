#include <iostream>
#include <cstring>
using namespace std;

void secret() {
    cout << "You got into the secret function!" << endl;
}

void processInput(char *input) {
    char buffer[16];
    strcpy(buffer, input);
    cout << "Input processed: " << buffer << endl;
}

void loopStuff(int n) {
    int sum = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            for (int k = 0; k < n; ++k)
                sum += (i + j + k) % 7;
    cout << "Loop result: " << sum << endl;
}

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;
    loopStuff(30);
    processInput(argv[1]);
    return 0;
}
