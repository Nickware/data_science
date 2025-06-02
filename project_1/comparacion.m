% Comparacion de Soluciones Estocasticas de Ginzburg-Landau
% Este script compara soluciones estocasticas del modelo de Ginzburg-Landau
% para diferentes temperaturas, mostrando la influencia de la temperatura
% en la amplitud de las fluctuaciones.
% y la estabilidad del sistema.

% Parametros
Tc = 7.2;
T = linspace(4, 10, 100);
psi = zeros(size(T));

for i = 1:length(T)
    if T(i) < Tc
        psi(i) = sqrt(Tc - T(i)) + 0.1*randn();  % Fluctuaciones
    end
end

plot(T, psi, 'o');
xlabel('Temperatura (K)');
ylabel('\psi');
title('Solución Estocástica de Ginzburg-Landau');