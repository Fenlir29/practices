def read(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = [i.strip() for i in file.readlines()]
        return content


def sort_bya(content):
    text = sorted(content)
    result = "\n".join(text)
    return result


def newtxt(path,content):
    with open(path,'w',encoding='utf-8') as file:
        file.write(content)
    

def main():
    content = read('music1.txt')
    sort_txt = sort_bya(content)
    newtxt('new_music.txt', sort_txt)


main()