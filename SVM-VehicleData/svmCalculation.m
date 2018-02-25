function [W, b, error_percentage] = svmCalculation(Xtrain, Ytrain, XTest, YTest)
X = Xtrain;
Y = Ytrain;
[row, col] = size(X);
A = zeros(2*row, row+col+1);
G = zeros(2*row, 1);

for i = 1:row
    A(i,:) = -1*[Y(i)*X(i,:), Y(i), zeros(1, i-1), 1, zeros(1, row-i)];
    A(row+i,:) = -1*[zeros(1, col+1), zeros(1, i-1), 1, zeros(1, row-i)];
    G(i, 1) = -1;
end

Q = [eye(col, col), zeros(col, row+1); zeros(row+1, col), zeros(row+1, row+1)];

constant = 0.06;
C = [zeros(col+1, 1); (constant*ones(row, 1))];
opts = optimset('MaxIter', 100000);
Z = quadprog(Q,C,A,G,[],[],[],[],[],opts);

W = Z(1:col);
b = Z(col+1);
Eps = Z(col+2:row+col+1);

[row_test, col_test] = size(XTest);
y_calc = zeros(row_test);

for i = 1:row_test
    sum = 0;
    for j = 1:col_test
        sum = sum + W(j)*XTest(i, j);
    end
    sum = sum + b;
    
    if(sum > 0)
        y_calc(i) = 1;
    else 
        y_calc(i) = -1;
    end
end

error = 0;
for i = 1:row_test
    if(YTest(i) ~= y_calc(i))
        error = error + 1;
    end
end

error_percentage = (error*100)/row_test;