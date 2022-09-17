clc; clear;

n = 3; 
ee = 10^(1/10)-1; e = sqrt(ee);

% K varia desde 1 hasta n
k = 1:n;

% Calculo el valor de a
%a = (1/n) * asinh(1/e);
a = 0.4759917863;

% Calculo parte real del polo
ok = -sinh(a)*sin((2*k-1)*pi/(2*n));
% Calculo parte imaginaria del polo
wk = cosh(a)*cos((2*k-1)*pi/(2*n));
% Los guardo como polos
polos = ok + wk*i;


