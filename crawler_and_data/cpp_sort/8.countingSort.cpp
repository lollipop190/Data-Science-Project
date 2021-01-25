
void countingSort(vector<int> &ib, vector<int> &ia, int maxEle)
{
    vector<int> ic;//new vector<int>[11];
    int i = 0;
    ic.resize(maxEle+1,0);
    for(auto x:ia)
    {
        ic[x]++;
    }
    for(i=1; i<=maxEle; i++)
    {
        ic[i]=ic[i]+ic[i-1];
    }
    for(i=ia.size()-1; i>=0; i--)
    {
        ib[ic[ia[i]]-1]=ia[i];
        ic[ia[i]]--;
    }
}
void countingSort(vector<int> &ia, int maxEle)
{
    vector<int> ib(ia);
    countingSort(ia,ib,maxEle);
}
template<typename T>
class Print
{
public:
    Print(){}
    void inline operator()(const T& x) const{cout<<x<<" ";}
};
