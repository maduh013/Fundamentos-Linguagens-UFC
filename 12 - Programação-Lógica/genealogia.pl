Exemplo: Árvore Genealógica com Prolog

% Fatos
pai(joao, maria).
pai(joao, jose).
mae(ana, maria).
mae(ana, jose).
pai(carlos, joao).
mae(marta, joao).

% Regras
irma(X, Y) :-
    pai(P, X), pai(P, Y),
    mae(M, X), mae(M, Y),
    X \= Y,
    feminino(X).

feminino(maria).
feminino(ana).
feminino(marta).

masculino(joao).
masculino(jose).
masculino(carlos).
