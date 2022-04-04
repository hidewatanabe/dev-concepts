# Command

## Intenção
Encapsular uma solicitação como um objeto, desta forma permitindo parametrizar clientes com diferentes solicitações, enfileirar ou fazer o registro (log) de solicitações e suportar operações que podem ser desfeitas.

## Tipo
Comportamental de objetos

## Também conhecido como:
Action, Transaction

## Motivação

## Aplicabilidade:
Use o padrão **Command** quando você deseja:
- Parametrizar objetos por uma ação a ser executada. Você pode expressar tal parametrização numa linguagem procedural através de uma função *callback*, ou seja, uma função que é registrada em algum lugar para ser chamada em um momento mais adiante. Os **Commands** são uma substituição orientada ao objeto para *callbacks*.
- Especificar, enfileirar e executar solicitações em tempos diferentes. Um objeto **command** pode ter um tempo de vida independente da solicitação original. Se o receptor de uma solicitação pode ser representado de uma maneira independente do espaço de endereçamento, então você pode transferir um objeto **command** para a solicitação para um processo diferente e lá atender a solicitação.
- Suportar desfazer operações. A operação *execute* do **command** pode armazenar estados para reverter seus efeitos no próprio comando. A interface de **command** deve ter acrescentada uma operação *unexecute*, que reverte os efeitos de uma chamada anterior de *execute*. Os comandos executados são armazenados em uma lista histórica. O nível ilimitado de desfazer e refazer operações é obtido percorrendo esta lista para trás e para frente, chamando operações *unexecute* e *execute*, respectivamente.

## Consequências:
O padrão **command** tem as seguintes consequências:
- **Command** desacopla o objeto que invoca a operação daquele que sabe como executá-la.
- **Commands** são objetos de primeira classe, ou seja, podem ser manipulados e estendidos como qualquer outro objeto.
- Você pode montar comandos para formar um comando composto. Em geral, comandos compostos são uma instância do padrão **Composite**.
- É fácil acrescentar novos **commands** poprque você não tem que mudar classes existentes.

## Padrões relacionados:
- Um **Composite** pode ser usaod para implementar **Commands compostos**.
- Um **Memento** pode manter estaod que o **command** necessita para desfazer o seu efeito.
- Um **Command** que deve ser copiado antes de ser colocado na lista histórica funciona como um **prototype**.