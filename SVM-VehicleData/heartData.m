heart = load('data/HeartDataSet.mat');
[Y] = binarySVM(heart.Xtrain, heart.Ytrain, heart.Xtest);
count = 0;
i = 1;
while i <= 70
    if (Y(i) * heart.Ytest(i)) < 0
        count = count + 1;
    end
    i = i + 1;
end
successRate = ((70-count)/70) * 100