void bucketSort(int a[], int n, int max)
{
    int i,j;
    int buckets[max];

    memset(buckets, 0, max*sizeof(int));

    for(i = 0; i < n; i++) 
        buckets[a[i]]++; 

    for (i = 0, j = 0; i < max; i++) 
    {
        while( (buckets[i]--) >0 )
            a[j++] = i;
    }
}