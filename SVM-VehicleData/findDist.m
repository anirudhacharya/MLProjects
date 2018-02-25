function [errorDist] = findDist(code1, code2)
diff = code1 - code2;
[codeRow,codeCol] = size(diff);
errorDist = 0;
for i = 1:codeCol
    errorDist = errorDist + (diff(i)*diff(i));
end
