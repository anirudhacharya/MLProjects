errorMatrix = [1, -1, -1, -1, 1, 1, 1;
              -1, 1, -1, -1, 1, -1, -1;
              -1, -1, 1, -1, -1, 1, -1;
              -1, -1, -1, 1, -1, -1, 1];
% errorMatrix =  [ 1, -1, 1, -1, -1, 1;
%                  1, 1, -1, -1, 1, -1;
%                 -1, 1, -1, 1, -1, 1;
%                 -1, -1, 1, -1, 1, 1];

[erRow,erCol] = size(errorMatrix);

[Xtrain, Ytrain, Xtest, Ytest] = loadData();
[trainDataRow, trainDataCol] = size(Xtrain);

[testDataRow, testDataCol] = size(Xtest);

resultCodeMatY = zeros(testDataRow,erCol); % Will contain the resultant code of the classification of the test data.

for i = 1:erCol
    bus = errorMatrix(1,i);
    saab = errorMatrix(2,i);
    opel = errorMatrix(3,i);
    van = errorMatrix(4,i);
    YtrainNum = zeros(trainDataRow,1);
    %YtrainNum is the classification of the training set for the code
    %of this particular iteration
    for j = 1:trainDataRow
        if strcmp(Ytrain(j),'bus')
            YtrainNum(j) = bus;
        elseif strcmp(Ytrain(j),'saab')
            YtrainNum(j) = saab;
        elseif strcmp(Ytrain(j),'opel')
            YtrainNum(j) = opel;
        else
            YtrainNum(j) = van;
        end
    end
    [YtestNum] = binarySVM(Xtrain, YtrainNum, Xtest);
    resultCodeMatY(:,i) = YtestNum;
end
%resultCodeMatY -- contains the classified code of the test data. We need
%to compare these codes with the different codes from the error matrix and
%classify the test data into the appropriate classes. 'exprYtest' will
%contain that classification.
exprYtest = zeros(size(Ytest));
count = 0;
for i = 1:testDataRow
    busDist = findDist(resultCodeMatY(i,:), errorMatrix(1,:));
    saabDist = findDist(resultCodeMatY(i,:), errorMatrix(2,:));
    opelDist = findDist(resultCodeMatY(i,:), errorMatrix(3,:));
    vanDist = findDist(resultCodeMatY(i,:), errorMatrix(4,:));
    %Compare the exprYtest classification data to the Ytest data available from
    %the dataset and calculate efficiency.
    if min([busDist saabDist opelDist vanDist]) == busDist
        exprYtest(i) = 1;
        if ~strcmp(Ytest(i),'bus')
            count  = count+1;
        end
    elseif min([busDist saabDist opelDist vanDist]) == saabDist
        exprYtest(i) = 2';
        if ~strcmp(Ytest(i),'saab')
            count  = count+1;
        end
    elseif min([busDist saabDist opelDist vanDist]) == opelDist
        exprYtest(i) = 3;
        if ~strcmp(Ytest(i),'opel')
            count  = count+1;
        end
    elseif min([busDist saabDist opelDist vanDist]) == vanDist
        exprYtest(i) = 4;
        if ~strcmp(Ytest(i),'van')
            count  = count+1;
        end
    end
end
errorRate = (count/testDataRow)*100