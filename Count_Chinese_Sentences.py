import re
s="我/是/一个/测试/句子/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/大家/赶快/来/统计/我/吧/，/重要/事情/说/三遍/！"
l=list(re.split('/|。|！| ，',s))
d,Count,SUM={},0,0
for i in range(len(l)):
    d[l[i]] = i
del d['']
del d['，']
for j in d.keys():
    for k in l:
        if j==k:
            Count+=1
    d[j]=Count
    SUM+=1
    Count=0
print(d)
print('Different words:',SUM)
