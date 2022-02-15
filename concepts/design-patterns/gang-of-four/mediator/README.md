# Mediator

## Intenção
Definir um objeto que encapsula a forma como um conjunto de objetos interage. O **Mediator** promove o acoplamento fraco ao evitar que os objetos se refiram uns aos outros explicitamente e permite variar suas interações independentemente.

## Tipo
Comportamental de Objetos

## Motivação

## Aplicabilidade:
- Um conjunto de objetos se comunica de maneiras bem definidas, porém complexas. As interdependências resultantes são desestruturadas e difíceis de entender.
- A reutilização de um objeto é difícil porque ele referencia e se comunica com muitos outros objetos.
- Um comportamento que está distribuído entre várias classes deveria ser customizável, ou adaptável, sem excessiva especialização em subclasses

## Consequências:
- *Ele limita o uso de subclasses.* Um mediador localiza o comportamento que, de outra forma, estaira distribuído entre vários objetos. Mudar esse comportamento exige a introdução de subclasses somente para o **Mediador**. Classes colegas podem ser reutilizadas como estão.
- *Ele desacopla colegas.* Um mediador promove um acoplamento fraco entre colegas. Você pode variar e reutilizar as classes colegas e **Mediador** independentemente.
- *Ele simplifica protocolos dos objetos.* Um mediador substitui interações "N para N" por interações "1 para N" entre o **Mediador** e seus colegas. Relacionamentos "1 para N" são mais fáceis de compreender, manter e estender.
- *Ele abstrai a maneira como os objetos cooperam.* Tornando a mediação um conceito indepentente e encapsulando-a em um objeto, permite-lhe focalizar na maneira como os objetos interagem independente do seu comportamento individual. Isso pode ajudar a esclarecer como os objetos interagem em um sistema.
- *Ele centraliza o controle.* O padrão **Mediator** troca a complexidade de interação pela complexidade no **mediador**. Porque um mediador encapsula protocolos, pode se tornar mais complexo do que qualquer dos colegas individuais. Isso pode tornar o **mediador** um monolito difícil de manter.

## Padrões relacionados:
- *Façade:* Difere do **Mediator** no aspecto em que ele abstrai um subsistema de objetos para fornecer uma interface mais conveniente. Seu protocolo é unidirecional; isto é, objetos **Façade** das solicitações fazem as classes dos subsistemas, mas não vice-versa. Em comparação, o padrão **Mediator** habilita o comportamento cooperativo que objetos-colegas não fornecem ou não podem fornecer, e o protocolo é multidirecional.
- *Observer:* Os colegas podem se comunicar com o mediador usando o padrão **Observer**