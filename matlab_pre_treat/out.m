a = fopen('2.txt','w');
%fprintf(a,'%s %d',k{1,1},k{1,2});

for i = 1:14580
    fprintf(a,'%s %d\n',k{i,1},k{i,2});
end
fclose(a);