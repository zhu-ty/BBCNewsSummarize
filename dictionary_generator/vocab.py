with open('data.out.txt','r') as fid:
  lines = fid.readlines()
f = open('/home/ubuntu/news_sum/data/vocab','w')
for line in lines:
  f.write(line.replace('\n','').split(' ')[1] + ' ' + line.split(' ')[0] + '\n')
f.close
