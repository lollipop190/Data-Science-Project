void select_sort(int a[], int n)
{
    int i;    
    int j;       
    int min;   

    for(i=0; i<n; i++)
    {
        min=i;

        for(j=i+1; j<n; j++)
        {
            if(a[j] < a[min])
                min=j;
        }

        if(min != i)
            swap(a[i], a[min]);
    }
}