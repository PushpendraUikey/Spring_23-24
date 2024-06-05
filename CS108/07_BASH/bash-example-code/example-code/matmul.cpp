/*
Author: Guramrit Singh
Description: GDB Activity, Midsem CS-108, Spring 2023-24
*/

#include <iostream>

using namespace std;

int main() {
    int k, n, m, l;

    // input dimensions
    cin >> m >> n;
    cin >> k >> l;

    int matrix1[m][n];
    int matrix2[k][l];

    // check if provided dimensions are valid
    if(n <= 0 || m <= 0 || k <= 0 || l <= 0) {
        cout << "Invalid dimensions" << endl;
        return 0;
    }
    if(n != k ) {
        cout << "Invalid dimensions" << endl;
        return 0;
    }

    // input matrix1
    for(unsigned int i = 0; i < m; i++) {
        for(unsigned int j = 0; j < n; j++) {
            cin >> matrix1[i][j];
        }
    }

    // input matrix2
    for(unsigned int i = 0; i < k; i++) {
        for(unsigned int j = 0; j < l; j++) {
            cin >> matrix2[i][j];
        }
    }

    int product[m][l];    
    // Calculate product using the formula: 
    // product[i][j] = sum(matrix1[i][k] * matrix2[k][j]) for k = 0 to c-1 where c is the number of columns in matrix1
    for(unsigned int i = 0; i < m; i++) {
        for(unsigned int j = 0; j < l ; j++) {
            product[i][j] = 0;
            for(unsigned int a{0}; a < n; a++) {
                product[i][j] += matrix1[i][a] * matrix2[a][j];
            }
        }
    }

    // print product
    for(unsigned int i = 0; i < m; i++) {
        for(unsigned int j = 0; j < l; j++) {
            cout << product[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
