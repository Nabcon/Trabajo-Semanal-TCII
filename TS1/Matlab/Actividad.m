clc,clear

Num = [1 -1] ; Den = [1 1] ; % H(s) = (-2s-1)/(s+1)              
Hs = tf(Num, Den);
% figure,
% pzmap(Hs) %% diagrama de polos y ceros
% sgrid;
% hm = findobj(gca, 'type', 'line');
% set(hm(2:end),'LineWidth',3);
% set(hm(2:end),'MarkerSize',10);
% hm(3).Color='red';
[Hw, w]=freqs(Num,Den);

subplot(211)
plot(w,abs(Hw));
ylim([0 2])
subplot(212)
plot(w,angle(Hw));
ylim([0 pi])