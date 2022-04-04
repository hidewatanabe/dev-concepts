# State

## Intenção
Permite a um objeto alterar seu comportamento quando o seu estado interno muda. O objeto parecerá ter mudado sua classe.

## Tipo
Comportamental de objetos

## Motivação

## Aplicabilidade:
Use o padrão **State** em um dos dois casos seguintes:
- O comportamento de um objeto depende do seu estado e ele pode mudar seu comportamento em tempo de execução, dependendo desse estado
- Operações tem comandos condicionais grandes, de várias alternativas, que uma ou mais constantes enumeradas. Frequentemente, várias operações conterão essa mesma estrutural condicional. O padrão **State** coloca cada ramo do comando adicional em uma classe separada. Isto lhe permite tratar o estado do objeto como um objeto propriamente dito, que pode variar indepentendemente de outros objetos.

## Consequências:
- *Ele confina comportamento específico de estados e particiona o comportamento para estados diferentes.* O padrão **State** coloca todo o comportamento associado com um estado particular em um objeto. Como todo o código específico a um estado reside numa subclasse de **state**, novos estados e transições de estado podem ser facilmente adicionaods pela definição de novas subclasses. Uma alternativa é usar valores de dados para definir estados internos, tendo operações de **Context** que verificam explicitamente os dados. Mas, em consequência, teríamos instruções parecidas, condicionais ou de seleção espalhadas por toda a implementação de contexto. O acréscimo de um novo estado poderia exigir a mudança de várias operações, o que complicaria a manutenção. O padrão **state** evita esse problema, mas introduz um outro, porque o padrão distribui o comportamento para diversos estados entre várias subclasses de **state**. Isso aumenta o número de classes e é nemos compacto do que ter uma única classe. Proém, tal distribuição é, na realidade, boa se existirem muitos estados, pois de outro modo necessitaríamos de grandes comandos condicionais. Do mesmo modo que procedures longas são indesejáveis, também o são comandos condicionais grandes. Eles são monolíticos e tendem a tornar o código menos explícito, o que, por sua vez torna-os difíceis de modificar e estender. O padrão **state** oferece uma maneira melhor para estruturar o código específico de estados. A lógica que determina as transições de estado não se localiza em comandos monolíticos **if** ou **switch**, mas é particionada entre as subclasses de **state**. O encapsulamento de cada transição de estado e ação associada entre uma classe eleva a idéia de um estado de execução ao status de um objeto propriamente dito. Isso impõe uma estrutura ao código e torna a sua intençnao mais clara.
- *Ele torna explícitas as transições de estado.* Quando um objeto define o seu estado corrente unicamente em termos de valores de dados internos, suas transições de estado não tem representação explícita. Elas apenas aparecem como atribuições de valores a algumas variáveis. A introdução de objetos separados, para estados diferentes, torna as transições mais explícitas. Os objetos **state** também podem proteger o contexto de estados internos inconsistentes porque, da perspectiva do contexto, as transições de estado são atômicas. Elas acontecem pela revinculação de uma variável que contém o objeto **state** de contexto, e não de várias.
- *Objetos **state** podem ser compartilhados.* Se os objetos **state** não possuem variáveis de instância - ou seja, o estado que elas representam está codificado internamente no seu tipo - então contextos podem compartilhar um objeto **state**. Quando estados são compartilhados dessa maneira, eles são essencialmente **flyweights**, sem estado intrínseco, somente comportamento.

## Padrões relacionados:
- O padrão **flyweight** explica quando e como objetos **state** podem ser compartilhados.
- Objetos **state** são frequentemente **singletons**.