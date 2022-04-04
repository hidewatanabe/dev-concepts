# Interpreter

## Intenção
Dada uma linguagem, definir uma representação para a sua gramática juntamente com um interpretador que usa a representação para interpretar sentenças dessa linguagem

## Tipo
Comportamental de classes

## Motivação

## Aplicabilidade:
Use o padrão **Interpreter** quando houver uma linguagem para interpretar e você puder representar sentenças da linugagem como árvores sintáticas abstratas. O padrão **Interpreter** funciona melhor qunado:
- A gramática da linguagem é simples. Para gramáticas complexas, a hierarquia de classes para a gramática se torna grande e incontrolável. Em tais casos, ferramentas tais como geradores de analisadores são uma alternativa melhor. Elas podem interpretar expressões sem a construção de árvores sintáticas abstratas, o que pode economizar espaço e, possivelmente, tempo.
- A eficiência não é um apreocupação crítica. Os interpretadores mais eficientes normalmente não são implementados pela interpretação direta de árvores de análise estática, mas pela sua tradução para uma outra forma. Por exemplo, expressões regulares são frequentemente transformadas em máquinas de estado. Porém, mesmo assim, o tradutor pode ser implementado pelo padrão **Interpreter**, sendo o padrão, portanto, ainda aplicável.

## Consequências:
- *É fácil de mudar e estender a gramática:* Uma vez que o padrão usa classes para representar regras de gramática, você pode usar a herança para mudar ou estender a gramática. Expressões existentes podem ser modificadas incrementalmente, e novas expressões podem ser definidas como variações de velhas expressões.
- *Implementar a gramática também é fácil:* Classes que definem nós na árvore sintática abstrata tem implementações imilares. Essas classes são fáceis de escrever e frequentemente sua geração pode ser automatizada com um gerador de compiladores ou de analisadores sintáticos.
- *Gramáticas complexas são difíceis de manter:* O padrão **Interpreter** define pelo menos uma classe para cada regra de gramática. Logo, gramáticas que contém muitas regras podem ser difíceis de administrar e manter. Outros padr˜øes de projeto podem ser aplicados para diminuir o problema. Porém, quando a gramática é muito complexa, técnicas como geradores de analisadores ou de compiladores são mais apropriadas.
- *Acrescentando novas formas de interpretar expressões:* O padrão **Interpreter** torna mais fácil resolver uma expressão de maneira nova. Pro exemplo, você pode suportar *pretty printing* ou verificação de tipo de uma expressão pela definição de uma nova operação nas classes de expressão. Se você continua criando novas formas de interpretar uma expressão, então considere a utilização do padrão **Visitor** para evitar mudança nas classes da gramática.

## Padrões relacionados:
- *Composite:* A árvore sintática abstrata é uma instância do padrão **Composite**
- *Flyweight:* Mostra como compartilhar símbolos terminais dentro de uma árvore sintática abstrata
- *Iterator:* O **Interpreter** pode usar um **Iterator** para percorrer a estrutura.
- *Visitor:* Pode ser usado para manter o comportamento em cada elemento da árvore sintática abstrata em uma classe.