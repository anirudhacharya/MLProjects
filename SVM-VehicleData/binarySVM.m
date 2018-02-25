function [Y] = binarySVM(Xtrain,Ytrain,Xtest)
[N,M] = size(Xtrain);
C = 0.3;
H = [eye(M) zeros(M,N+1);
    zeros(N+1,M) zeros(N+1,N+1)];
f = [zeros(M+1,1);
    ones(N,1).*C];
A = zeros(2*N, N+M+1);
for i = 1:N
    A(i,:) = -1*[Ytrain(i)*Xtrain(i,:), Ytrain(i), zeros(1, (i-1)), 1, zeros(1,(N-i))];
end
for i = 1:N
    A(N+i,:) = -1*[zeros(1,M+1), zeros(1,i-1), 1, zeros(1,N-i)];
end
b = [-ones(N,1) zeros(N,1)];
Aeq = [];
beq = [];
LB = [];
UB = [];
X0 = [];

options = optimset('MaxIter', 1000000);
z = quadprog(H,f,A,b,Aeq,beq,LB,UB,X0,options);
w = z(1:M+1);
%b = z(col+1);
xi = z(M+2:N+M+1);

[testRow,testCol] = size(Xtest);
Y = transpose(w) * transpose([Xtest ones(testRow,1)]);
for i = 1:testRow
    if Y(i)<0
        Y(i) = -1;
    else
        Y(i) = 1;
    end
end
Y = transpose(Y);