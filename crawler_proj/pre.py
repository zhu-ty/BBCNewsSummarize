with open('/home/ubuntu/crawler/txtnews/data.txt','r') as fid:
  lines = fid.readlines()
article = []
abstract = []
result = []
i = 1
for line in lines:
  if i % 3 == 2:
    abstract.append(line.replace('\n',''))
    i = i + 1
  elif i % 3 == 0:
    article.append(line.replace('\n',''))
    i = i + 1
  else:
    i = i + 1
for j in range(len(article)):
  result.append(('article=<d> <p> <s> ' + ' . </s> <s> '.join(article[j].split('.'))[:-12].replace('=','') + ' . . </s> </p> </d>\tabstract=<d> <p> <s> ' + abstract[j].replace('=','') + ' </s> </p> </d>\tpublisher=AFP' + '\n').lower())

with open('/home/ubuntu/crawler/txtnews/text_BBC_data','w') as fid:
  fid.writelines(result)
