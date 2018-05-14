# riversimulator
simula um rio onde habitam peixes e ursos.
O objetivo deste trabalho e escrever um programa em Python para simular
um ecosistema, que consiste de ursos e peixes, vivendo em um rio. A
simulacãp prossegue em ciclos, nos quais os animais envelhecem, um subconjunto
deles migra para outros locais, outros se acasalam e alguns morrem,
de acordo com certas regras.
A variavel de objeto river representa um rio como uma lista, cujas celulas
são referencias para objetos pertencentes a classe Animal, que representa
formas de vida (ursos e peixes).
Uma celula pode ser nula, signicando que não contem nem um urso
ou um peixe. Animal e uma classe abstrata. Cada animal possui um campo genero e
um campo idade.
A classe Fish modela peixes. Um peixe vive no maximo ate o final do
seu quarto ano (ciclos de cinco anos), a menos que seja morto antes.
A classe Bear modela ursos. Um urso vive ate o final de seus 9 anos
(ciclos de dez anos), a menos que seja morto antes. Um urso possui
uma forca que varia de acordo com a sua idade, da seguinte maneira:
Age      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
Strength | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 | 0
