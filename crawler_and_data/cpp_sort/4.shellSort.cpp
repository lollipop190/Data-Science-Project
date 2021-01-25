template <typename _RIter>
void insert_sort(_RIter st, _RIter ed, int delta) {
    for(_RIter i = st + delta; i < ed; i += delta) {
        for(_RIter j = i; j > st; j -= delta)
            if(*j < *(j - delta)) std::swap(*j, *(j - delta));
            else break;
    }
}
 
template <typename _RIter>
void shell_sort(_RIter st, _RIter ed) {
    for(int delta = ed - st; delta; delta /= 2)
        for(int i = 0; i < delta; i++)
            insert_sort(st + i, ed, delta);
}