# Visitor

## Intenção
Representar uma operação a ser executada nos elementos de uma estrutura de objetos. Visitor permite definir uma nova operação sem mudar as classes dos elementos sobre os quais opera.

## Tipo
Comportamental de objetos

## Motivação

## Aplicabilidade:
- Quando uma estrutura de objetos contém muitas classes de objetos com interfaces que diferem e você deseja executar operações sobre esses objetos que dependem das suas classes concretas;
- Quando muitas operações distintas e não-relacionadas necessitam ser executadas sobre objetos de uma estrutura de objetos, e você deseja evitar "a poluição das suas classes com essas operações. **Visitor** lhe permite manter juntas operações relacionadas, definindo-as em uma única classe. Quando a estrutura do objeto for compartilhada por muitas aplicações, use **Visitor** para por operações somente naquelas aplicações que as necessitem.
- Quando as classes que definem a estrutura do objeto raramente mudam, porém, você frequentemente deseja definir novas operações sobre a estrutura. A mudança das classes da estrutura do objeto requer a redefinicão da interface para todos os visitantes, o que é potencialmente oneroso. Se as classes da estrutura do objeto mudam com frequência, provavelmente é melhro definir as operações nessas classes.

## Consequências:
- *Visitor torna fácil a adição de novas operações:* Os **visitors** tornam fácil acrescentar operações que dependem dos componenetes de objetos complexos. Você pode definir uma nova operação sobre uma estrutura de objetos simplesmente acrescentando um novo visitante. Em contraste a isso, se você espalha funcionalidade sobre mutias classes, então tem que mudar cada classe para definir uma nova operação.
- *Um visitante reúne operações relacionadas e separa as operações não-relacionadas:* O comportamento relacionado nõa é espalhado pelas classes que definem a estrutura do objeto. Ele está localizado em um visitante. Conjuntos de comportamentos não-relacionados são particionados em suas próprias subclasses visitantes. Isso simplifica tanto as classes que definem os elementos como os algoritmos definidos nos visitantes. Qualquer estrutura de dados específica de um algoritmo pode ser ocultada no visitante.
- *É difícil acrestentar novas classes de elementos concretos:* O padrão **Visitor** torna diíficl acrescentar novas subclasses de elementos. Cada novo elemento concreto dá origem a uma nova operação abstrata em **Visitor** e uma correspondente implementação em cada classe **ConcreteVisitor**. Algumas vezes, uma implementação-padrão pode ser fornecida em **Visitor**, a qual pode ser herdadea pela maioria dos **ConcreteVisitors**, mas isso é exceção, não a regra. Assim, a consideração-chave na aplicação do padrão **Visitor** é: qual a mudançna mais provável? A do algoritmo aplicado sobre uma estrutura de objetos ou a das classes de objetos que compõem a estrutura? A hierarquia de classes de **Visitor** pode ser difícil de ser mantida quando novas classes de elementos concretos são crescentadas com frequência. Em tais casos, provavelmente, serão mais fácil simplesmente definir operações nas classes que compões a esturutra. Se a estrutura de classe dos elementos for estável, mas você estiver continuamente adicionado operações ou mudando algoritmos, o padrão **Visitor** vai ajudar a controlar as mudançãs.
- *Visitando hierarquias de classes:* Um iterator pode visitar objetos numa estrutura à medida que os percorre pela chamada das suas operações. Mas um iterator não pode agir sobre estruturas de objetos com distintos tipos de elementos. O padrão **Visitor** não tem essa restrição. Ele pode visitar objetos que não compartilham uma mesma classe-mãe. Você pode acrescentar qualquer tipo de objeto à interface de um **Visitor**.
- *Acumulando estados:* Os **Visitors** podem acumular estados à medida que visitam ada elemento na estrutura do objeto. Sem um visitante, estes dados seriam passados como argumentos extras para as operações que executam o percurso, ou eles poderiam aparecer como variáveis globais. 
- *Rompendo o encapsulamento:* A abordagem do padrão **Visitor** assume que a interface do elemento concreto é poderosa o suficiente para permitir aos visitantes executarem o seu trabalho. Como resultado, o padrão frequentemente força a fornecer operações públicas que acessam o estado interno de um elemento, o que pode comprometer seu encapsulamento.

## Padrões relacionados:
- *Composite:* Os **Visitors** podem ser usados para aplicar uma operação sobre uma estrutura de objetos definida no padrão **Composite**
- **Interpreter:** O **Visitor** pode ser aplicado para efetuar a interpretação.

