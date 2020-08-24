#對話紀錄統計
#讀取
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#分割統計
def count(lines):
    allen_word_count = 0 #文字
    allen_sticker_count = 0 #貼圖
    allen_image_counrt = 0 #圖片
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_counrt = 0
    for line in lines:
        s = line.split(' ') #s是清單
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_counrt += 1
            else:
                for m in s[2:]:     #清單[開始值:結束值]
                    allen_word_count += len(s[2])
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_counrt += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(s[2])
    print('Allen說了', allen_word_count, '字,傳了', allen_sticker_count, '張貼圖,傳了', allen_image_counrt, '張圖片')
    print('Viki說了', viki_word_count, '字,傳了', viki_sticker_count, '張貼圖,傳了', viki_image_counrt, '張圖片')

#執行
def main():
    lines = read_file('LINE.txt')
    lines = count(lines)

main()