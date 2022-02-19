# Template Method

## Intenção
Definir o esqueleto de um algoritmo em uma operação, postergando alguns passos para as subclasses. *Template Method* permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo

## Tipo
Comportamental de classes

## Motivação

## Aplicabilidade:
- Para implementar as partes invariantes de um algoritmo uma só vez e deixar para as subclasses a implementação do comportamento que pode variar.
- Quando o comportamento comum entre subclasses deve ser fatorado e concentrado numa classe comum para evitar a duplicação de código. Este é um bom exemplo de "refatorar para generalizar". Primeiramente, você identifica as diferenças no código existente e então separa as diferenças no código existente e então separa as diferenças em novas operações. Por fim, você substitui o código que apresentava as diferenças por um **template method** que chama uma dessas novas operações.
- Para controlar extensões de subclasses. Você pode definir um **template method** que chama **hook operations** em pontos específicos, desta forma permitindo extensões somente nesses pontos. 

## Consequências:
Os **template methods** são uma técnica fundamental para reutilização de código. São particularmente importantes em bibliotecas de classe porque são os meios para a fatoração dos comportamentos comuns.s
Os **template methods** conduzem a uma estrutura de inversão de controle, algumas vezes chamada de "o princípio de Hollywood", ou seja "não nos chame, nós chamamos você". Isso se refere a como uma classe mãe chama as operações de uma subclasse. e não o contrário.
Os **template methods** chamam os seguintes tipos de operações:
- Operações concretas em classes concretas ou abstratas
- Operações abstratas
- *Factory Methods*
- *Hook Operations*: Que fornecem comportamento-padrão que subclasses podem estender se necessário. Uma **hook operation** frequentemente não executa nada por padrão.


## Padrões relacionados:
- *Factory Method:* são frequentemente chamados por **template methods** para criação de objetos.
- **Strategy**: **template methods** usam a herança para variar parte de um algoritmo. Estratégias usam a delegação para variar o algoritmo inteiro.

