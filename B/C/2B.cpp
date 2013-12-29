/*
	http://codeforces.com/problemset/problem/2/B
	http://CodingForSpeed.com
	http://HelloACM.com
*/

#include <iostream>

using namespace std;

int arr[1000][1000];
int a[1000][1000][2] = {9999999999};
char d[1000][1000][2] = {'\0'};

int get(int i, int n) {
    int c = 0;
    while ((i > 0) && ((i % n) == 0)) {
        c ++;
        i /= n;
    }
    return c;
}

void print(int i, int j, int k) {
    if ((i >= 0) && (j >= 0)) {
        if (d[i][j][k] == 'D') {
            print(i - 1, j, k);
        } else {
            print(i, j - 1, k);
        }
        if (d[i][j][k] != '\0') {
            cout << d[i][j][k];
        }
    }
}

int main()
{
    int n;
    cin >> n;
    bool zero = false;
    int x, y;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) {
            cin >> arr[i][j];
            if (arr[i][j] == 0) {
                zero = true;
                arr[i][j] = 10;
                x = i;
                y = j;
            }
        }
    }
    a[0][0][0] = get(arr[0][0], 2);
    a[0][0][1] = get(arr[0][0], 5);
    for (int i = 1; i < n; i ++) {
        a[i][0][0] += get(arr[i][0], 2) + a[i - 1][0][0];
        a[i][0][1] += get(arr[i][0], 5) + a[i - 1][0][1];
        a[0][i][0] += get(arr[0][i], 2) + a[0][i - 1][0];
        a[0][i][1] += get(arr[0][i], 5) + a[0][i - 1][1];
        d[i][0][0] = 'D';
        d[i][0][1] = 'D';
        d[0][i][0] = 'R';
        d[0][i][1] = 'R';
    }
    for (int i = 1; i < n; i ++) {
        for (int j = 1; j < n; j ++) {
            int prev_two1 = a[i][j - 1][0];
            int prev_five1 = a[i][j - 1][1];
            int prev_two2 = a[i - 1][j][0];
            int prev_five2 = a[i - 1][j][1];
            int c2 = get(arr[i][j], 2);
            int c5 = get(arr[i][j], 5);
            prev_two1 += c2;
            prev_two2 += c2;
            prev_five1 += c5;
            prev_five2 += c5;
            if (prev_two1 < prev_two2) {
                a[i][j][0] = prev_two1;
                d[i][j][0] = 'R';
            } else {
                a[i][j][0] = prev_two2;
                d[i][j][0] = 'D';
            }
            if (prev_five1 < prev_five2) {
                a[i][j][1] = prev_five1;
                d[i][j][1] = 'R';
            } else {
                a[i][j][1] = prev_five2;
                d[i][j][1] = 'D';
            }
        }
    }
    int cost = min(a[n - 1][n - 1][0], a[n - 1][n - 1][1]);
    int k = 0;
    if (a[n - 1][n - 1][0] > a[n - 1][n - 1][1]) {
        k = 1;
    }
    if ((zero && (cost > 0))) {
        cout << 1 << endl;
        for (int k = 0; k < x; k ++) {
            cout << 'D';
        }
        for (int k = 0; k < y; k ++) {
            cout << 'R';
        }
        for (int k = 0; k < n - y - 1; k ++) {
            cout << 'R';
        }
        for (int k = 0; k < n - x - 1; k ++) {
            cout << 'D';
        }
    }
    else {
        cout << cost << endl;
        print(n - 1, n - 1, k);
    }
    return 0;
}
