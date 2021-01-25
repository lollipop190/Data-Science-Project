void Heapify(int* A,int i,int size);
void BuildHeap(int* A,int size);
void HeapSort(int* A,int size);

void Heapify(int *A,int i,int size)
{
int large=0;
int newsize=0;
int l=i*2;
int r=i*2+1;
if(l<size&&A[l]>A[i])
large=l,newsize=size-l+1;
else
large=i;
if(r<size&&A[r]>A[large])
large=r,newsize=size-r+1;
if(large!=i)
{
int temp=A[i];
A[i]=A[large];
A[large]=temp;
Heapify(A,large,newsize);
}
}
void BuildHeap(int* A,int size)
{
for(int i=size/2;i>0;i--)
{
Heapify(A,i,size-i);
}
}
void HeapSort(int * A,int size)
{
BuildHeap(A,size);
for(int i=size;i>1;i--)
{
int temp=A[i];
A[i]=A[1];
A[1]=temp;
size--;
Heapify(A,1,size);
}
}