clear,clc;

% Variables
ee = 10^(1/10) -1;
q = 20/9; 
a = 0.4942; b = 0.9942; c = (2*(q^2)+b)/(q^2);
w = 0:0.001:5;

num1 = [0 1/q 0];
den1 = [1 a/q 1];

num2 = [0 1/q 0];
den2 = [1 0.1348 1.5403];

num3 = [0 1/q 0];
den3 = [1 0.0875 0.6492];

num = conv(num1, conv(num2,num3));
den = conv(den1, conv(den2,den3));
T = freqs(num,den,w);
pzmap(tf(num,den));
%plot(w,abs(T),'linewidth',3);
