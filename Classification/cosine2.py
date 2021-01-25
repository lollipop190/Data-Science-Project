from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    s1, s2 = add_space(s1), add_space(s2)  # 在字中间加上空格
    cv = CountVectorizer(tokenizer=lambda s: s.split())  # 转化为TF矩阵
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()  # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))

# s1 = "def bubbleSort(arr):" \
# "    for i in range(1, len(arr)):" \
# "        for j in range(0, len(arr)-i):" \
# "            if arr[j] > arr[j+1]:" \
# "                arr[j], arr[j + 1] = arr[j + 1], arr[j]" \
# "    return arr";
# s2 = "def sort(Array):" \
# "    for j in range(1, len(Array)):" \
# "        for i in range(0, len(Array)-i):" \
# "            if Array[i] > Array[i+1]:" \
# "                Array[i], Array[i + 1] = Array[i + 1], Array[i]" \
# "    return Array";
# print(tf_similarity(s1, s2))
