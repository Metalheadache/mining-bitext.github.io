from pandas import *
import numpy as np

Al1=read_csv("./FinalData/aligned_skyscraper_EN-skyscraper_CN1.txt", sep='\t', names=['EN','CN','0'])
Al2=read_csv("./FinalData/aligned_skyscraper_EN-skyscraper_CN2.txt", sep='\t', names=['EN','CN','0'])
# tok1=read_csv("./FinalData/lalaland_EN.xlsx", sep='\t', names=['EN'])
# tok2=read_csv("./FinalData/lalaland_CN1.xlsx", sep='\t', names=['CN'])
# tok3=read_csv("./FinalData/lalaland_CN2.xlsx", sep='\t', names=['CN'])
tim1=read_excel('./FinalData/skyscraper_EN.xlsx', names=['id','timeline','EN'],header=None,sheet='sheet')
tim2=read_excel('./FinalData/skyscraper_CN1.xlsx',names=['id','timeline','CN1'], header=None,sheet='sheet')
tim3=read_excel('./FinalData/skyscraper_CN2.xlsx',names=['id','timeline','CN2'], header=None,sheet='sheet')




k=-1
com1=[]
for i in range(len(Al1['EN'])):
    EN= Al1['EN'][i]
    if EN!=EN:
        com1[k][1]=com1[k][1]+' '+Al1['CN'][i]
    else:
        com1.append([EN,Al1['CN'][i]])
        k+=1

com2=[]
k=-1
for i in range(len(Al2['EN'])):
    EN= Al2['EN'][i]
    if EN!=EN:
        com2[k][1]=com2[k][1]+' '+Al2['CN'][i]
    else:
        com2.append([EN,Al2['CN'][i]])
        k+=1

if len(com1)>= len(com2):
    finalcom=com1
    subcom=com2
else:
    finalcom=com2
    subcom=com1

semicom={}
for i in range(len(subcom)):
    semicom[subcom[i][0]]=subcom[i][1]

timcom={}
for i in range(len(tim1['timeline'])):
    timcom[tim1['EN'][i]]=tim1['timeline'][i]

for i in range(len(finalcom)):
    EN=finalcom[i][0]
    if EN in semicom.keys():
        finalcom[i].append(semicom[EN])
    else:
        finalcom[i].append(' ')

mixtimeline=[]
k=-1
for i in range(len(finalcom)):
    EN = finalcom[i][0]
    if EN in timcom.keys():
        finalcom[i].append(timcom[EN])
        mixtimeline.append(finalcom[i])
        k += 1
    else:
        mixtimeline[k][1] = str(mixtimeline[k][1]) + ' ' + str(finalcom[i][1])
        mixtimeline[k][0] = str(mixtimeline[k][0]) + ' ' + str(finalcom[i][0])
        mixtimeline[k][2] = str(mixtimeline[k][2]) + ' ' + str(finalcom[i][2])



Final=np.array(mixtimeline).T

id=np.array(range(1,len(mixtimeline)+1,1))
Table=DataFrame({'ID':id,'Timeline':Final[3],'EN':Final[0],'CN1':Final[1],'CN2':Final[2]})


file_path = r'./FinalData/skyscraper_alignment.xlsx'
writer = ExcelWriter(file_path)
Table.to_excel(writer, columns=['ID','Timeline','EN','CN1','CN2'],header=None, index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()