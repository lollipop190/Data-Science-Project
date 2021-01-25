
void myrandom(int a[],int len)
{
	srand((unsigned)  time(NULL));
	for(int i=0;i<len;i++)
	a[i]=rand()%range+1;
}
void InsertionSort(int a[],int len)
{
	int k,current;
	for(int i=1;i<len;i++)
	{
		k=a[i];
		current=i-1;
		for(;current>=0&&a[current]>k;current--)
		{
			a[current+1]=a[current];
		}
		a[current+1]=k;
	}
}
