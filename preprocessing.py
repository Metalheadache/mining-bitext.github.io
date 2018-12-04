import pandas as pd
import string
input='./Movie/skyscraper.(2018)/skyscraper.(2018).eng.1cd.(7470647)/Skyscraper.2018.720p.WEB-DL.H264.AC3-EVO.srt'
dataset = pd.read_csv(input, sep='\n\n', header=None)
i = 0
j = 0
k = 1
l = 0
x= pd.DataFrame()

while i<= len(dataset)-1:

    if dataset.at[i,0].isdigit():
        j +=1
        l =0
    x.at[j, l] = dataset.at[i, 0]
    l+=1
    i+=1


while k <= len(x[2]):
    m=3
    while m < x.shape[1]:
        if x.at[k,m] ==x.at[k,m]:
            x.at[k,2]=x.at[k,2]+' '+x.at[k,m]
        m += 1
    k+=1


N=[]
for i in range(len(x[1])):
    if not x.at[i+1,1] == x.at[i+1,1]:
        N.append(i+1)
        x.at[i,2]=x.at[i+1,0]


x.drop(N, inplace= True)
# print(x)

O=[]
for i in x[2]:
    a=str(i).replace('<i>','')
    b= a.replace('</i>', '')
    c=b.replace('♪','')
    O.append(c)

x[2]=O

if len(x[0])==max(int(i) for i in x[0]):
    print('sucess')


# x.drop(O,inplace=True)


x1=x.iloc[:,2]


x1.to_csv(r'./FinalData/skyscraper_EN.txt',index=None,header=None)

file_path = r'./FinalData/skyscraper_EN.xlsx'
writer = pd.ExcelWriter(file_path)
x.to_excel(writer, columns=[0,1,2],header=None, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()
