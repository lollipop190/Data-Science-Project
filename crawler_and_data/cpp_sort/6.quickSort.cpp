
int partition(int arr[], int left, int right){
    int pivot = arr[right];                 
    int curr = left;
    for(int i=left; i<right; i++){
        if(pivot > arr[i]){                 /
            swap(arr[curr], arr[i]);
            curr++;
        }
    }
    swap(arr[curr], arr[right]);           
    return curr;
}

void quicksort(int arr[], int left, int right){
    if(left < right){
        int p = partition(arr, left, right);
        quicksort(arr, left, p-1);
        quicksort(arr, p+1, right);
    }
}


