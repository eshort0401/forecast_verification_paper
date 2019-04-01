syms t;
alpha = @(t) cos(pi * (sin(pi * ((mod(t, 24) / 24) - 0.5)) + 1));
a0 = int(alpha,t,-pi,pi);