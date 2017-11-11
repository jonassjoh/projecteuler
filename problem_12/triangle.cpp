#include <iostream>
#include <math.h>
using namespace std;

bool isPrime(int n) {
    for (int i=2; i < sqrt(n) + 1; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int main() {

    int p = 1;
    int prime = 2;

    for (int i=3; ; i++) {
        if (isPrime(i))
            p++;

        if (p >= 10001) {
            prime = i;
            break;
        }
    }

    cout << prime << endl;

    return 0;
}
