# Composite

## Intenção
Compor objetos em estruturas de árvore para representarem hierarquias partes-todo. Composite permite aos clientes tratarem de maneira uniforme objetos individuais e composições de objetos.

## Tipo
Estrutural de objetos

## Motivação

## Aplicabilidade:
Use o padrão **composite** quando:
- quiser representar hierarquias partes-todo de objetos.
- quiser que os clientes sejam capazes de ignorar a diferença entre composições de objetos e objetos individuais. Os clientes tratarão todos os objetos na estrutura composta de maneira uniforme.

## Consequências:
O padrão **composite**:
- define hierarquias de classe que consistem de objetos primitivos e objetos compostos. Os objetos primitivos podem compor objetos mais complexos, os quais, por sua vez, também podem compor outros objetos, e assim por diante, recursivamente. Sempre que o código do cliente esperar um objeto primitivo, ele também poderá aceitar um objeto composto.
- torna o cliente simples. Os clientes podem tratar estruturas compostas e objetos individuais de maneira uniforme. Os clientes normalmente não sabem (e não deveriam se preocupar com isso) se  estão tratando com uma folha ou um componente composto. Isto simplifica o código a ser escrito nas classes-cliente, porque evita o uso de comandos do tipo *case* com os rótulos classes que definem a composição.
- torna mais fácil de acrescentar novas espécies de componentes. Novas subclasses definidas, **Composite** ou **Leaf**, funcionam automaticamente com as estruturas existentes e o código do cliente. Os clientes não precisam ser alterados para tratar novas classes **Component**.
- pode tornar o projeto excessivametne genérico. A desvantagem de facilitar o acréscimo de novos componentes é que isso torna mais difícil restringir os componentes de uma composição. Algumas vezes, você deseja uma composição que tenha somente certos componentes. Com **Composite**, você não pode confiar no sistema de tipos para garantir a obediência a essas restrições. Ao invés disso, terá que usar verificações e testes em tempo de execução.

## Padrões relacionados:
- Frequentemente, a ligaçõa componente-pai é usada para o padrão **Chain of Responsability**.
- O padrão **Decorator** é frequentemente usaod com o padrão **Composite**. Quando decoradores e composições são usados juntos, eles tem normalmente uma classe-mãe comum. Assim, decoradores terõa que suportar a interface de **Component** com operações como Add, Remove e GetChild.
- O **Flyweight** permite compartilhar componentes, porém estes não mais pode referenciar seus pais.
- O padrão **Iterator** pode ser usado para percorrer os compostos.
- O padrão **Visitor** pode ser usado para localizar operações e comportamentos que seriam de outra forma distribuídos entre classes **Composite** e **Leaf**.