# Decorator

## Intenção
Dinamicamente, agregar responsabilidades adicionais a um objeto. Os Decorators fornecem uma alternativa flexível ao uso de subclasses para extensão de funcionalidades.
## Tipo
Estrutural de objetos

## Também conhecido como
Wrapper

## Motivação

## Aplicabilidade:
- Para acrescentar responsabilidades a objetos individuais de forma dinâmica e transparente, ou seja, sem afetar outros objetos
- Para responsabilidades que podem ser removidas
- Quando a extensão através do uso de subclasses não é prática. Às vezes, um grande número de extensões independentes é possível e isso poderia produzir uma explosão de subclasses para suportar cada combinação. Ou a definição de uma classe pode estar oculta ou não estar disponível para a utilização de subclasses.

## Consequências:
- *Maior flexibilidade do que a herança estática.* O padrão **Decorator** fornece uma maneira mais flexêvel de acrescentar responsabilidades a objetos do que pode ser feito com herança estática. Com o uso de **decoradores**, responsabilidades podem ser acrescentadas e removidas em tempo de execução simplesmente associando-as e disassociando-as de um objeto. Em comparação, a herança requer a criação de uma nova classe para cada responsabilidade adicional. Isso dá origem a muitas classes e aumenta a complexidadede um sistema. Além do mais, fornecer diferentes classes **Decorators** para uma específica classe **Component** permite combinar e associar responsabilidades. Os **Decorators** também tornam fácil acrescentar uma propriedade duas vezes.
- *Evita classes sobrecarregadas de características na parte superior da hierarquia.* Um **Decorator** oferece uma abordagem do tipo "use quando for necessário" para adição de responsabilidades. Em vez de tentar suportar todas as características previsíveis em uma classe complexa e customizada, você pode definir uma classe simples e acrescentar funcionalidade de modo incremental com objetos **Decorator**. A funcionalidade necessária pode ser composta a partir de peças simples. Como resultado, uma aplicação não necessita incorrer no custo de características e recursos que não usa. Também é fácil definir novas espécies de **Decorators** independentemente das classes de objetos que eles estendem, mesmo no caso de extensões não-previstas. Estender uma classe complexa tende a expor detalhes não-relacionados com as responsabilidades que você está adicionando.
- *Um decorator e seu componente não são idênticos.* Um **decorator** funciona como um envoltório transparente. Porém, do ponto de vista da identidade de um objeto, um componente **decorator** não é idêntico ao próprio componente. Daí não poder dependere da identidade de objetos quando você utiliza **decorators**.
- *Grande quantidade de pequenos objetos.* Um projeto que usa **decorators** frequentemente resulta em sistemas compostos por uma grande quantidade de pequenos objetos parecidos. Os objetos diferem somente na maneira como são interconectados, e não nas suas classe ou no valor de suas variáveis. Embora esses sistemas sejam fáceis de customizar por que os compreende, podem ser difíceis de aprender e depurar.
