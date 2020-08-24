
#讀取
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #sig去掉\nfeff txt編碼問題
        for line in f:
            lines.append(line.strip())
    return lines

#轉換
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == '高愷廷':
            person = '高愷廷'
            continue
        elif line == '林順翔':
            person = '林順翔'
            continue
        elif line == '張博皓':
            person = '張博皓'
            continue
        if person:  #if person有值
            new.append(person + ': ' + line)
    return new


#寫入
def write_file(filename,lines):
    with open(filename, 'w',encoding='utf-8') as f:
        for line in lines:
            f.write(line+'\n')

#執行程式
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt',lines)

main()