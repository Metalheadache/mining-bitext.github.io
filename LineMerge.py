import pandas as pd

dataset = pd.read_csv('Skyscraper.2018.720p.WEB-DL.H264.AC3-EVO.srt', sep='\n', header=None)
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
    if x.at[k,3] is True:
        x.at[k,2]=x.at[k,2]+x.at[k,3]
    k+=1
x.drop(columns=3, inplace= True)



file_path = r'./Skyscraper.2018.720p.WEB-DL.H264.AC3-EVO.xlsx'
writer = pd.ExcelWriter(file_path)
x.to_excel(writer, columns=[0,1,2], index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()
