

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