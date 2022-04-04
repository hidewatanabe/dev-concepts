# Adapter

## Intenção
Converter a interface de uma classe em outra interface, esperada pelos clientes. O **Adapter** permite que classes com interaces incompatíveis trabalhem em conjunto - o que, de outra forma, seria impossível.

## Tipo
Estrutural de classes e de objetos

## Também conhecido como
Wrapper

## Motivação

## Aplicabilidade:
Use o padrão **adapter** quando:
- quiser usar uma classe existente, mas sua interface não corresponde à interface de que necessita.
- quiser criar uma classe reutilizável que coopere com classes não-relacionadas ou não-previstas, ou seja, classes que não necessariamente tenham interfaces compatíveis.
- (somente para objetos) precisar usar várias subclasses existentes, porém, for impraticável adaptar essas interfaces criando subclasses para cada uma. Um adaptador de objeto pode adaptar a interface da sua classe-mãe.

## Consequências:
Os adaptadores de classes e objetos têm diferentes soluções de compromisso. 
Um adaptador de classe:
- adapta **Adaptee** a **Target** através do uso efetivo de uma classe **Adapter** concreta. Em consequência, um adaptador de classe não funcionará quando quisermos adaptar uma classe e todas suas subclasses.
- permite a **Adapter** substituir algum comportamento do **Adaptee**, uma vez que **Adapter** é uma subclasse de **Adaptee**.
- introduz somente um objeto, e não é necessário endereçãmento indireto adicional por ponteiros para chegar até o **Adatpee**.
Um adaptador de objetos:
- permite a um único **adapter** trabalhar com muitos **adaptee** - isto é, o **Adaptee** em si e todas suas subclasses (se existirem). O **Adapter** também pode acrescentar funcionalidade a todos os **Adaptees** de uma só vez.
- torna mais difícil redefinir um comportamento de **Adaptee**. Ele exigirá a criação de subclasses de **Adaptee** e fará com que **Adapter** referencie a subclasse ao invés do **Adaptee** em si.

## Padrões relacionados:
- O padrão **Brigde** tem uma estrutura similar a um adaptador de objeto, porém, **Bridge** tem uma intenção diferente: tem por objetivo separar uma interface de sua implementação, de modo que elas possam variar fácil e independentemente. Um adaptador se destina a mudar a interface de um objeto existente.
- O padrão **Decorator** aumenta outro objeto sem mudar sua interface. Dessa forma, um **Decorator** é mais transparente para a aplicação do que um **adapter**. Como consequência, **Decorator** suporta a composição recursiva, a qual não é possível com adaptadores puros.
- O **Proxy** define um representante ou "procurador"para outro objeto e não muda a sua interface.