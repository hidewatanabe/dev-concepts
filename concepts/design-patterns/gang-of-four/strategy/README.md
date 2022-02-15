# Strategy

## Intenção
Definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

## Tipo
Comportamental de Objetos

## Também conhecido como
Policy

## Motivação

## Aplicabilidade:
- Muitas classes relacionadas diferem somente no seu comportamento. As **estratégias** fornecem uma maneira de configurar uma classe com um dentre muitos comportamentos;
- Você necessita de variantes de um algoritmo. Por exemplo, pode definir algoritmos que refletem diferentes soluções de compromisso entre espaço/tempo. As **estratégias** podem ser usadas quando essas variantes são implementadas como uma hierarquia de classes de algoritmos;
- Um algoritmo usa dados dos quais os clientes não deveriam ter conhecimento. Use o padrão **Strategy** para evitar a exposição das estruturas de dados complexas, específicas do algoritmo.
- Uma classe define muitos comportamentos, e estes aparecem em suas operações como múltiplos comandos condicionais da linguagem. Em vez de usar muitos comandos condicionais, mova os ramos condicionais relacionados para a sua própria classe **Strategy**.

## Consequências:
- *Família de algoritmos relacionados.* Hierarquias de classes **Strategy** definem uma família de algoritmos e comportamentos para os contextos reutilizarem.
- *Uma alternativa ao uso de subclasses.* A herança oferece uma outra maneira de suportar uma variedade de algoritmos ou comportamentos. Você pode especializar uma classe de contexto para lhe dar diferentes comportamentos. Mas isso congela o comportamento no contexto, misturando a implementação do algoritmo com a do contexto, tornando o contexto mais difícil de compreender, manter e estender. E não se pode variar de algoritmo dinamicamente. Você acaba tendo muitas classes relacionadas cuja única diferença é o algoritmo ou um comportamento que elas emprega. Encapsular os algoritmos em classes **Strategy** separadas permite variar o algoritmo independentemente do seu contexto, tornando mais fácil trocá-los, compreendê-los e estendê-los.
- *Estratégias eliminam comandos condicionais da linguagem de programação.* O padrão **Strategy** oferece uma alternativa ao uso de comandos condicionais para a seleção de comportamentos desejados. Quando diferentes comportamentos são agrupados em uma classe é difícil evitar o uso de comandos condicionais para a seleção do comportamento correto. O encapsulamento do comportamento em classes **Strategy** separadas elimina estes comandos condicionais. Um código que contém muitos estados frequentemente indica a necessidade de aplicar o padrão **Strategy**.
- *A possibilidade de escolha de implementações.* As **estratégias** podem fornecer diferentes implementações do mesmo comportamento. O cliente pode escolher entre **estratégias** com diferentes compromissos entre tempo e espaço.
- *Os clientes devem conhecer diferentes estratégias.* O padrão tem uma deficiência potencial no fato de que um cliente deve compreender como **Strategies** diferem, antes que ele possa selecionar o mais apropriado. Os clientes podem ser expostos a detalhes e aspectos de implementação. Protanto, você deveria usar o padrão **Strategy** somente quando a variação em comportamento é relevante para os clientes.
- *Custo de comunicação entre Strategy e Context.* A interface de **Strategy** é compartilhada por todas as classes que implementam essa interface, quer os algoritmos que elas implementem sejam triviais ou complexos. Daí ser provável que algumas implementações não usem toda a informação passada através desta interface. Implmentações ismples podem não usar quaisquer dessas informações! Isso significa que existirão situações em que o contexto criará e iniciará parâmetros que nunca serão usados. Se esse for um problema, você necessitará de um acoplamento maior entre **Strategy** e contexto.
- *Aumento do número de objetos.* **Strategies** aumentam o número de objetos numa aplicação. Algumas vezes, você pode reduzir esse custo pela implementação de **estratégias** como objetos sem estados que os contextos possam compartilhar. Qualquer estado residual é mantido pelo contexto, que o passa em cada solicitação para o objeto **Strategy**.

## Padrões relacionados:
- *Flyweight:* Objetos **Strategy** geralmente são bons **Flyweight**.
