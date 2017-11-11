#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

bool isPrime(int n) {
    for (int i=2; i < sqrt(n) + 1; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

vector<int> getPrimes(int nr_of_primes) {
    vector<int> primes;
    primes.push_back(1);
    primes.push_back(2);
    int p = 2;
    for (int i=3; p < nr_of_primes; i++) {
        if (isPrime(i)) {
            p++;
            primes.push_back(i);
        }
    }
    return primes;
}

int getDivisors(int s, vector<int> &primes) {

    int* divisors = new int[primes.size()]();

    for (int i=1; i < primes.size(); i++) {
        int s2 = s;
        while (s2 > 0 && s2 % primes[i] == 0) {
            divisors[i]++;
            s2 /= primes[i];
        }
    }

    int d = 1;

    for (int i=0; i < primes.size(); i++) {
        d *= (divisors[i] + 1);
    }

    return d;
}

int main() {

    vector<int> primes = getPrimes(500);

    int s = 0;
    int n = 0;
    int d = 0;

    while (d < 500) {
        n++;
        s += n;

        d = getDivisors(s, primes);
    }

    cout << s << endl;

    return 0;
}
