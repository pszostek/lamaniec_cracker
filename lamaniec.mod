reset;
option solver cplex;

param N;    #liczba slow
set LITERY;    #litery alfabetu
param litery_w_slowach{sl in 1..N, l in LITERY};
param litery_dane{l in LITERY};

var slowa{i in 1..N} integer >= 0;

maximize func: sum{i in 1..N}( slowa[i] );
subject to binarne{i in 1..N}: slowa[i] <= 1;
subject to litery_constr{l in LITERY}:
    sum{i in 1..N}( slowa[i]*litery_w_slowach[i, l] ) <= litery_dane[l];

