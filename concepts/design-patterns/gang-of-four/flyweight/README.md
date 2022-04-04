# Flyweight

## Intenção
Usar compartilhamento para suportar eficientemente grandes quantidaes de objetos de granularidade fina.

## Tipo
Estrutural de objetos

## Motivação

## Aplicabilidade:
A eficiência do padrão **Flyweight** depende muito de como e onde ele é usado. Aplique o padrão **Flyweight** quando todas as condições a seguir forem verdadeiras:
- Uma aplicação utiliza um grande número de objetos
- Os custos de armazenamento são altos por causa da grande quantidade de objetos
- A maioria do estados dos objetos pode ser tornada extrínseca
- Muitos grupos de objetos podem ser substituiídos por relativamente poucos objetos compartilhados, uma vez que estados extrísecos são removidos
- A aplicação não depende da identidade dos objetos. Uma vez que objetos **Flyweight** poodem ser compartilhados, testes de identidade produzirão o valor verdadeiro para objetos conceitualmente distintos.

## Consequências:
Os **flyweight** podem introduzir custos de tempo de execução associados com a transferência, prcura e/ou computação de estados extrínsecos, especialmente se esses anteriormente etavam armazenados como um estado intrínseco. Contudo, tais custos são compensados pelas economias de espaço, as quais aumentam à medida que mais **flyweights** são compartilhados.
As economias de armazenamento são uma função de vários fatores:
- a redução do número total de instâncias obtida com o compartilhamento
- a quantidade de estados intrínsecos por projeto
- se o estado extrínseco é computado ou armazenado

Quanto mais **flyweights** são compartilhados, maior a economia de armazenagem. A economia aumenta com a quantidade de estados compartilhados. As maiores economias ocorrem quando os objetos usam quanitdades substanciais tanto de estados intrínsecos como de estados extrínseco, e os estados extrínsecos podem ser melhor computados do que armazenados. Então você economiza a armazenagem de duas maneiras: o compartilhamento reduz o custo dos estados intrínsecos e você troca estados extrínsecos por tempo de computação.
O padrão **Flyweight** é frequentemente combinado com o padrão **Composite** para representar uma estrutura hierárquica tal como um gráfico com nós de folhas compartilhados. Uma consequência do comportamento é que os nós de folhas **flyweight** não podem armazenar um apontador para os seus pais. Em vez disso, o apontador do pai é passado para o **flyweight** como parte do seu estado extrínseco. Isso tem um impacto importante sobre a forma como os objetos na hierarquia se comunicam uns com os outros.

## Padrões relacionados:
O padrão **Flyweight** é frequentemente combinado com o padrão **Composite** para representar uma estrutura hierárquica tal como um gráfico com nós de folhas compartilhados.
Frequentemente é melhor implementar objetos **State** e **Strategy** como **flyweights**.

