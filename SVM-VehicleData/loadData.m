function [Xtrain, Ytrain, Xtest, Ytest] = loadData()
xai = textscan(fopen('data/xai.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xah = textscan(fopen('data/xah.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xag = textscan(fopen('data/xag.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xaf = textscan(fopen('data/xaf.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xae = textscan(fopen('data/xae.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xad = textscan(fopen('data/xad.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xac = textscan(fopen('data/xac.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xab = textscan(fopen('data/xab.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');
xaa = textscan(fopen('data/xaa.dat'),'%f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %f %s','Delimiter',' ');

Xtrain = [xaa{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xab{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xac{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xad{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xae{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xaf{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xag{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]}];
Ytrain = [xaa{19};
    xab{19};
    xac{19};
    xad{19};
    xae{19};
    xaf{19};
    xag{19}];

Xtest = [xah{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]};
    xai{[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18]}];

Ytest = [ xah{19};
    xai{19}];



