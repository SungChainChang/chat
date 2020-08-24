#把字串中的一部份拿出來

lines = []
with open('3.txt', 'r',encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    #字串可以當作清單看待
    time = s[0][:5]
    name = s[0][5:]
    print('時間: ', time)
    print('人名: ', name)