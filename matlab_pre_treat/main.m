%a = dataset(data(:,1),data(:,2));
%b = dataset(vocab(:,1),vocab(:,2));

%d = join(a,b,'key','Var1','Type','outer','MergeKeys',true);

%<span style="font-size: 12.0pt; line-height: 150%; font-family: »ªÎÄÖÐËÎ;" lang="EN-US">c=
%join(a,b,'key','Key1','Type','inner','MergeKeys',true) </span>


clear;
load('data.mat');


for i = 1:100000
    if(i > size(vocab,1))
        break;
    end
    if(isnan(vocab{i,2}))
        vocab = [vocab(1:i-1,:);vocab(i+1:size(vocab,1),:)];
    end
end

k = vocab;

for i = 1:4614
    [h1,h2] = find(strcmp(vocab',data{i,1}));
    if(~isempty(h2))
        k{h2,2} = k{h2,2} + data{i,2};
    else
        k(size(k,1)+1,:) = data(i,:);
    end
    if mod(i,100) == 0
        fprintf('%d\n',i);
    end
end
