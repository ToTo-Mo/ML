import csv

textmsg = open('toy_data\\문자메세지.txt',mode='w',encoding='utf-8')

with open('D:\\github\\문자메세지.csv',newline='') as csvfile:
    file = csv.reader(csvfile,quotechar='"')
    for row in file: 
        print(row)
        row = [item.replace('\r', '') for item in row]
        row = [item.replace('\n', ' ') for item in row]
        row.extend('\n')
        print(row)
        row = ''.join(row)
        print(row)
        textmsg.write(row)

textmsg.close()