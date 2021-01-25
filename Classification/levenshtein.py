# s1 = "def bubbleSort(arr):\n" \
#      "    for i in range(1, len(arr)):\n" \
#      "        for j in range(0, len(arr)-i):\n" \
#      "            if arr[j] > arr[j+1]:\n" \
#      "                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n" \
#      "    return arr"
# with open('../crawler_and_data/python sort/insertion_sort.py') as f:
#     s2 = ''.join(f.readlines())



def levenshtein(str1, str2):
    dif = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        dif[i][0] = i
    for i in range(len(str2) + 1):
        dif[0][i] = i

    temp = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                temp = 0
            else:
                temp = 1

            dif[i][j] = min(dif[i - 1][j - 1] + temp, dif[i][j - 1] + 1, dif[i - 1][j] + 1)
    return 1 - dif[len(str1)][len(str2)] / max(len(str1), len(str2))

