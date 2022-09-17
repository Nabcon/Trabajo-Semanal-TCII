ee = 10^(1/10) -1;
A = sqrt(1/(ee*64));
wn = 0:0.001:10;
w = 40000.*wn;

num = [A 0 0 0 0];
den1 = [0.9865 0.2795 1];
den2 = [0.279 0.6738 1];
den = conv(den1,den2);

T = freqs(num,den,wn);
plot(w,abs(T),'linewidth',3);