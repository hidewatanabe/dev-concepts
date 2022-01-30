# Singleton

## Intenção
Garantir que uma classe tenha somente uma instância e fornecer um ponto global de acesso para a mesma

## Tipo
Criacional

## Motivação

## Aplicabilidade:
- For preciso haver apenas uma instância de uma classe, e essa instância tiver que dar acesso aos clientes através de um ponto bem conhecido;
- A única instância tiver de ser extensível através de subclasses, possibilitando aos clientes usar uma instância estendida sem alterar seu código.

## Consequências:
- *Acesso controlado à instância única.* Como a classe **Singleton** encapsula a sua única instância, possui controle total sobre como e quando os clientes a acessam.
- *Espaço de nomes reduzido.* O padrão **Singleton** representa uma melhoria em relação ao uso de variáveis globais. Ele evita a poluição do espaço de nomes com variáveis globais que armazenam instâncias únicas.
- *Permite um refinamento de operações e de representação.* A classe **Singleton** pode ter subclasses e é fácuil configurar uma aplicação com uma instância dessa classe estendida. Você pode configurar a aplicação com uma instância. Você pode configurar a aplicação com uma instância da classe q de que necessita em tempo de execução.
- *Permite um número variävel de instâncias.* O padrão torna fácil mudar de idéia, usar a mesma abordagem para controlar o número de instâncias que a aplicação utiliza. Somente a operação que permite acesso à instância de **Singleton** necessita ser mudada.
- *Mais flexível do que operações de classe.* Uma outra maneira de empacotar a funcionalidade de um **Singleton** é usando operações de classes (métodos estáticos). Porém, as técnicas das linguagens OO tornam difícil mudar um projeto para permitir mais que uma instância de uma classe. Além disso, os métodos estáticos nunca são virtuais, o que significa que as subclasses não podem redefini-las poliformicamente.

## Padrões relacionados:
- *Abstract Factory:* Pode ser implementado usando o padrão **Singleton**.
- *Builder:* Pode ser implementado usando o padrão **Singleton**.
- *Prototype:* Pode ser implementado usando o padrão **Singleton**.
