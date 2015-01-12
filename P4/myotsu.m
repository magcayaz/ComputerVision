function [T] = myotsu(I,N);
% source: http://stackoverflow.com/questions/10303229/implementing-otsu-binarization-for-faded-images-of-documents
% Martijn Pieters
% create histogram

nbins = N; 

[x,h] = hist(I(:),nbins);

% calculate probabilities

p = x./sum(x);

% initialisation

om1 = 0; 

om2 = 1; 

mu1 = 0; 

mu2 = mode(I(:));


for t = 1:nbins,

    om1(t) = sum(p(1:t));
    om2(t) = sum(p(t+1:nbins));
    mu1(t) = sum(p(1:t).*[1:t]);
    mu2(t) = sum(p(t+1:nbins).*[t+1:nbins]);

end

    sigma = (mu1(nbins).*om1-mu1).^2./(om1.*(1-om1));


idx = find(sigma == max(sigma));

T = h(idx(1))*0.5451/124.0227;