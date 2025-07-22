**08 – Programação Orientada a Objetos**

**Objetivo**

Demonstrar os conceitos de **orientação a objetos**, como herança, atributos e métodos, por meio de uma hierarquia de classes relacionada ao domínio de personagens de jogos.


**Domínio: Personagens**

Três classes foram criadas:

- `Personagem`: classe base com nome e vida.
- `Guerreiro`: herda de Personagem e tem força.
- `Mago`: herda de Personagem e tem mana.


**Testes**

O código instancia um guerreiro e um mago, e cada um executa seu próprio método `atacar`, mostrando o polimorfismo.


**Conceitos aplicados**

- **Herança**: `Guerreiro` e `Mago` herdam de `Personagem`.
- **Polimorfismo**: Cada classe redefine o método `atacar`.
- **Encapsulamento**: Uso de atributos e construtores.


