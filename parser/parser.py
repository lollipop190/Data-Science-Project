import argparse
import math
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm
import os
import re


def complex_sort(language):
    if language == 'python':
        lst = ['counting_sort.py', 'max_heap_sort.py', 'quick_sort.py']
        for i in range(3):
            with open("../crawler_and_data/python_sort/" + lst[i]) as f:
                print("{}:{}".format(i+1, lst[i].split('.')[0]))
                file = ''.join(f.readlines())
                print(file)
    elif language == 'java':
        lst = ['8.countingSort.java', '7.heapSort.java', '6.quickSort.java']
        for i in range(3):
            with open("../crawler_and_data/java_sort/" + lst[i],encoding='utf-8') as f:
                print("{}:{}".format(i+1, lst[i].split('.')[1]))
                file = ''.join(f.readlines())
                print(file)
    elif language == 'cpp':
        lst = ['8.countingSort.cpp', '7.heapSort.cpp', '6.quickSort.cpp']
        for i in range(3):
            with open("../crawler_and_data/cpp_sort/" + lst[i], encoding='utf-8') as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[1]))
                file = ''.join(f.readlines())
                print(file)

def stability_sort(language):
    print("stable sort:")
    if language == 'python':
        lst = ['bubble_sort.py', 'insertion_sort.py', 'merge_sort.py']
        for i in range(3):
            with open("../crawler_and_data/python_sort/" + lst[i]) as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[0]))
                file = ''.join(f.readlines())
                print(file)
    elif language == 'java':
        lst = ['1.bubbleSort.java', '3.insertionSort.java', '5.mergeSort.java']
        for i in range(3):
            with open("../crawler_and_data/java_sort/" + lst[i], encoding='utf-8') as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[1]))
                file = ''.join(f.readlines())
                print(file)
    elif language == 'cpp':
        lst = ['1.bubbleSort.cpp', '3.insertionSort.cpp', '5.mergeSort.cpp']
        for i in range(3):
            with open("../crawler_and_data/cpp_sort/" + lst[i], encoding='utf-8') as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[1]))
                file = ''.join(f.readlines())
                print(file)

def encrypt_recom(language):
    if language == 'python':
        lst = ['RSA.py', 'AES.py', 'DES.py']
        for i in range(3):
            with open("../crawler_and_data/encrypt/" + lst[i], encoding='utf-8') as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[0]))
                file = ''.join(f.readlines())
                print(file)
    elif language == 'java':
        lst = ['DES.java', '3DES.java']
        for i in range(2):
            with open("../crawler_and_data/encrypt/" + lst[i], encoding='utf-8') as f:
                print("{}:{}".format(i + 1, lst[i].split('.')[0]))
                file = ''.join(f.readlines())
                print(file)


def main():
    parser = argparse.ArgumentParser(usage="classify codes and recommend the best.")

    parser.add_argument('-c', '--classification', help='give us a filename and it will automatically classify the code '
                                                       'according to its language and function.\n'
                                                       '\nexample: python parser.py -c filename')
    # 给定文件名，进行分类

    parser.add_argument('-r', '--recommend', help='input the function(sort, encrypt) + language(java, python, cpp) '
                                                  'or '
                                                  'the filename to get the recommended code accordingly.\n'
                                                  '\nexample:\n 1.python parser.py -r sort+java\n'
                                                  '2.python parser.py -r sort+cpp\n'
                                                  '3.python parser.py -r encrypt+java\n'
                                                  '4.python parser.py -r sort,encrypt+python\n')
    # 推荐：
    # 第一种情况：不带文件名，则可以输入1，2，3来指定 要排序，还是加密，还是两种都要
    # 第二种情况：带文件名，则根据文件中的内容去推荐对应语言的算法
    #

    args = parser.parse_args()
    if args.recommend:
        arg = str(args.recommend)
        if arg.startswith("sort,encrypt") or arg.startswith('encrypt,sort'):
            print("sort algorithm listed by time complex:")
            complex_sort(arg.split("+")[1])
            print("and encrypt:")
            encrypt_recom(arg.split("+")[1])
            # 先排序后加密
        elif arg.startswith("encrypt"):
            print("encrypt:")
            encrypt_recom(arg.split("+")[1])
            # 加密
        elif arg.startswith("sort"):
            print("listed by time complex:")
            complex_sort(arg.split("+")[1])
            print("\n\n\n")
            stability_sort(arg.split("+")[1])
            # 排序
        else:
            filename = args.recommend
            with open(filename, encoding='utf-8') as f:
                file_content = ''.join(f.readlines())
            if 'encrypt' in file_content.lower():
                if filename.endswith('.py'):
                    encrypt_recom('python')
                elif filename.endswith('.java'):
                    encrypt_recom('java')
                elif filename.endswith('.cpp') or filename.endswith('.h'):
                    pass
            elif 'sort' in file_content.lower():
                if filename.endswith('.py'):
                    print("sort algorithm listed by time complex:")
                    complex_sort('python')
                    stability_sort('python')
                elif filename.endswith('.java'):
                    print("sort algorithm listed by time complex:")
                    complex_sort('java')
                    stability_sort('cpp')
                elif filename.endswith('.cpp') or filename.endswith('.h'):
                    print("sort algorithm listed by time complex:")
                    complex_sort('cpp')
                    stability_sort('cpp')
# 根据文件中的代码推荐相应的代码
    elif args.classification:
        filename = args.classification  # 获取用户输入的filename
        filename = str(filename)
        with open(filename, encoding='utf-8') as f:
            file_content = ''.join(f.readlines())
            if 'encrypt' in file_content.lower():
                if filename.endswith('.py'):
                    print('python encrypt')
                elif filename.endswith('.java'):
                    print('java encrypt')
                elif filename.endswith('.cpp') or filename.endswith('.h'):
                    print('cpp encrypt')
            elif 'sort' in file_content.lower():
                if filename.endswith('.py'):
                    print('python sort')
                elif filename.endswith('.java'):
                    print('java sort')
                elif filename.endswith('.cpp') or filename.endswith('.h'):
                    print('cpp sort')
            else:
                if filename.endswith(".py"):
                    # file_content = py_clearComments.py_clear(filename)
                    file_content = py_clear(filename)
                    flag = False
                    path = '../crawler_and_data/python_sort'
                    file_list = os.listdir(path)
                    for file in file_list:
                        with open(path + '/' + file) as f:
                            similarity = compute_cosine(''.join(f.readlines()), file_content)
                            # similarity = cosine.compute_cosine(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('python sort')
                                break
                            similarity = levenshtein(''.join(f.readlines()),file_content)
                            # similarity = levenshtein.levenshtein(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('python sort')
                                break
                            similarity = tf_similarity(''.join(f.readlines()),file_content)
                            # similarity = cosine2.tf_similarity(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('python sort')
                                break
                    if not flag:
                        print('python encrypt.')
                elif filename.endswith('.java'):
                    # file_content = java_clear(filename)
                    file_content = java_clear(filename)
                    # file_content = java_clearComments.java_clear(filename)
                    flag = False
                    path = '../crawler_and_data/java_sort'
                    file_list = os.listdir(path)
                    for file in file_list:
                        with open(path + '/' + file) as f:
                            similarity = compute_cosine(''.join(f.readlines()), file_content)
                            # similarity = cosine.compute_cosine(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('java sort')
                                break
                            similarity = levenshtein(''.join(f.readlines()), file_content)
                            # similarity = levenshtein.levenshtein(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('java sort')
                                break
                            similarity = tf_similarity(''.join(f.readlines()), file_content)
                            # similarity = cosine2.tf_similarity(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('java sort')
                                break
                    if not flag:
                        print('java encrypt.')
                elif filename.endswith('.cpp'):
                    file_content = java_clear(filename)
                    # file_content = java_clearComments.java_clear(filename)
                    flag = False
                    path = '../crawler_and_data/cpp_sort'
                    file_list = os.listdir(path)
                    for file in file_list:
                        with open(path + '/' + file) as f:
                            similarity = compute_cosine(''.join(f.readlines()), file_content)
                            # similarity = cosine.compute_cosine(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('cpp sort')
                                break
                            similarity = levenshtein(''.join(f.readlines()), file_content)
                            # similarity = levenshtein.levenshtein(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('cpp sort')
                                break
                            similarity = tf_similarity(''.join(f.readlines()), file_content)
                            # similarity = cosine2.tf_similarity(''.join(f.readlines()), file_content)
                            if similarity > 0.5:
                                flag = True
                                print('cpp sort')
                                break
                    if not flag:
                        print('cpp encrypt.')


def compute_cosine(text_a, text_b):
    # 找单词及词频
    words1 = text_a.split(' ')
    words2 = text_b.split(' ')
    # print(words1)
    words1_dict = {}
    words2_dict = {}
    for word in words1:
        # word = word.strip(",.?!;")
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        # print(word)
        if word != '' and word in words1_dict.keys():
            num = words1_dict[word]
            words1_dict[word] = num + 1
        elif word != '':
            words1_dict[word] = 1
        else:
            continue
    for word in words2:
        # word = word.strip(",.?!;")
        word = re.sub('[^a-zA-Z]', '', word)
        word = word.lower()
        if word != '' and word in words2_dict.keys():
            num = words2_dict[word]
            words2_dict[word] = num + 1
        elif word != '':
            words2_dict[word] = 1
        else:
            continue
    dic1 = sorted(words1_dict.items(), key=lambda asd: asd[1], reverse=True)
    dic2 = sorted(words2_dict.items(), key=lambda asd: asd[1], reverse=True)

    # 得到词向量
    words_key = []
    for i in range(len(dic1)):
        words_key.append(dic1[i][0])  # 向数组中添加元素
    for i in range(len(dic2)):
        if dic2[i][0] in words_key:
            # print 'has_key', dic2[i][0]
            pass
        else:  # 合并
            words_key.append(dic2[i][0])
    vect1 = []
    vect2 = []
    for word in words_key:
        if word in words1_dict.keys():
            vect1.append(words1_dict[word])
        else:
            vect1.append(0)
        if word in words2_dict.keys():
            vect2.append(words2_dict[word])
        else:
            vect2.append(0)

    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(vect1)):
        sum += vect1[i] * vect2[i]
        sq1 += pow(vect1[i], 2)
        sq2 += pow(vect2[i], 2)
    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    return result


def tf_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    s1, s2 = add_space(s1), add_space(s2)  # 在字中间加上空格
    cv = CountVectorizer(tokenizer=lambda s: s.split())  # 转化为TF矩阵
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()  # 计算TF系数
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))


def java_clear(filename):
    file = ''
    multiline_comments = False
    with open('../parser/' + filename ,encoding='utf-8') as f:
        for line in f.readlines():
            if multiline_comments:
                if '*/' in line:
                    multiline_comments = False
                    if not line.split('*/')[1].isspace():
                        line = line.split('*/')[1]
                    else:
                        line = ''
                else:
                    line = ''
                    continue
            if line == '\n':
                line = ''
            elif '//' in line:
                line = line.split('//')[0]
                if not line.isspace() and line != '':
                    line += '\n'
                else:
                    line = ''
            elif '/*' in line and '*/' in line:
                first_part = line.split('/*')[0]
                second_part = line.split('*/')[1]
                line = first_part + second_part
            elif '/*' in line:
                multiline_comments = True
                if not line.split('/*')[0].isspace():
                    line = line.split('/*')[0] + '\n'
                else:
                    line = ''
            elif '*/' in line:
                multiline_comments = False
                if not line.split('*/')[1].isspace():
                    line = line.split('*/')[1]
                else:
                    line = ''
            # print(line,sep='')
            file += line
    return file



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

def py_clear(filename):
    file = ''
    with open('../parser/' + filename,encoding='utf-8') as f:
        for line in f.readlines():
            if line == '\n':
                line = ''
            elif '#' in line:
                line = line.split('#')[0]
                if not line.isspace():
                    line += '\n'
                else:
                    line = ''
            file += line
    return file

if __name__ == "__main__":
    main()
