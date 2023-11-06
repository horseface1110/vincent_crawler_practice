
path = r"C:\Users\oloom\我的雲端硬碟 (oloomb7@gmail.com)\self_study_notion\自學\日文\單字\N5\形容詞.md"
path = path.replace("\\","/")
print(path)

output = ""
main = open(path,'r+',encoding='utf-8')
listt = open("japanese.txt",'w',encoding='utf-8')

lines = main.readlines()

for i in lines[1:]:
    tmp = i.split("|")
    output = tmp[1] + ":::" + tmp[2] + "\t\t" + tmp[3] + "  " + tmp[4] + "\n"
    print(output)
    listt.writelines(output)





