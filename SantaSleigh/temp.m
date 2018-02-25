% First row of data (zero based, skip the header)
firstRow = 1;

% First column of data (zero based, don't skip any columns)
firstCol = 0;
presents = csvread('presents.csv', firstRow, firstCol);
presents = presents(1:200,:);
[rows, columns] = size(presents);
numPresents = rows;

for i = 1:numPresents
    presents(i,:) = [presents(i,1) sort(presents(i,2:end))];
end
%presents(:,2:end) = fliplr(presents(:,2:end));
presentVol = [presents(:,1), presents(:,2).*presents(:,3).*presents(:,4)];
presentVol = sortrows(presentVol,2);  
largePresents = sortrows(presentVol(100:end,:),1);
largepresents = presents(largePresents(:,1),:);
smallPresents = sortrows(presentVol(1:100,:),1);
smallpresents = presents(smallPresents(:,1),:);

%presents = flipud(presents);

% for i = 1:numpresents
%     presents(i,:) = [presents(i,1) sort(presents(i,2:end))];
% end
        