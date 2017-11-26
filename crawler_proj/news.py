
from newsplease import NewsPlease
#article = NewsPlease.from_url('https://www.nytimes.com/2017/02/23/us/politics/cpac-stephen-bannon-reince-priebus.html?hp')
#print(article.title)

#http://www.bbc.com/news/uk-42123644

#http://www.bbc.com/news/av/world-middle-east-42123092

#http://www.bbc.com/news/world-asia-42124446


fo = open('./data.txt','w')
fi = open('./input.txt','r')

#file = open("sample.txt")
i = 0 
while 1:
    line = fi.readline()
    if not line:
        break
    try:
        article = NewsPlease.from_url(line)
    except:
        continue
    else:
        print(i)
        i = i + 1;
        #fo.write('1\n')
        fo.write(article.title)
        fo.write('\n')
        fo.write(article.description)
        fo.write('\n')
        fo.write(article.text.replace('\n',''))
        fo.write('\n')
        if i % 10 == 0:
            fo.flush()
fi.close();
fo.close();



'''
f = open('./data.txt','w')

for i in range(42123000,42124000):
    try:
        article = NewsPlease.from_url('http://www.bbc.com/news/uk-' + str(i))
    except:
        continue
    else:
        print(i)
        f.write(article.title)
        f.write('\n\n')
        f.write(article.description)
        f.write('\n\n')
        f.write(article.text)
        f.write('\n\n\n\n')
f.close();


f = open('./data2.txt','w')

for i in range(42123000,42124000):
    try:
        article = NewsPlease.from_url('http://www.bbc.com/news/world-asia-' + str(i))
    except:
        continue
    else:
        print(i)
        f.write(article.title)
        f.write('\n\n')
        f.write(article.description)
        f.write('\n\n')
        f.write(article.text)
        f.write('\n\n\n\n')
f.close();
'''
