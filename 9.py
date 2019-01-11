int main() 
{ 
    cout << "1 Test\n"; 
    int arr1[] = {4, 5, 6, 7, 8, 4, 4}; 
    int size = sizeof(arr1)/sizeof(arr1[0]); 
    int k = 3; 
    moreThanNdK(arr1, size, k); 
  
    cout << "\n2 Test\n"; 
    int arr2[] = {4, 2, 2, 7}; 
    size = sizeof(arr2)/sizeof(arr2[0]); 
    k = 3; 
    moreThanNdK(arr2, size, k);
    cout << "\n3 Test\n"; 
    int arr3[] = {2, 7, 2}; 
    size = sizeof(arr3)/sizeof(arr3[0]); 
    k = 2; 
    moreThanNdK(arr3, size, k); 
    cout << "\n4 Test\n"; 
    int arr4[] = {2, 3, 3, 2}; 
    size = sizeof(arr4)/sizeof(arr4[0]); 
    k = 3; 
    moreThanNdK(arr4, size, k); 
  
    return 0;
}
