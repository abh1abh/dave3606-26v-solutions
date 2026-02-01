
// c. 
int sum(int* data, int length) {
    int s = 0;
    for (int i = 0; i <= length - 1 ; i++) {
        s += data[i];
    }
   return s;
}


int main() {
    int array[] = {1, 2, 3, 4, 5};
    int result = sum(array, 5);
    return 0;
}
