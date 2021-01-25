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
