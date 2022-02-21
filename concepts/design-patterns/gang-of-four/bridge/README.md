# Bridge

## Intenção
Desacoplar uma abstração da sua implementação, de modo que as duas possam variar independentemente.

## Também conhecido como
- Handle
- Body

## Tipo
Estrutural de objetos

## Motivação

## Aplicabilidade:
- Quando se deseja evitar um vínculo entre uma abstração e sua implementação. Isso pode ocorrer, por exemplo, quando a implementação deve ser selecionada ou alterada em tempo de execução.
- Tanto as abstrações como suas implementações tiverem de ser extensíveis por meio de subclasses. Neste caso, o padrão Bridge permite combinar as diferentes abstrações e implementações e estendê-las independentemente.
- Mudanças na implementação de uma abstração não puderem ter impacto sobre os clientes.
- Você deseja ocultar completamente a implementação de uma abstração dos clientes.
- Tiver uma proliferação de classes. Tal hierarquia de classes indica necessidade de separar um objeto em duas partes. 
- Desejar compartilhar uma implementação entre múltiplos objetos e este fato deve estar oculto do cliente.

## Consequências:
- *Desacopla a interface da implementação:* Uma implementação não fica permanentemente presa a uma interface. A implementação de uma abstração pode ser configurada em tempo de execução. É até mesmo possível para um objeto mudar sua implementação em tempo de execução. O desacoplamento da abstração e da implementação também elimina dependências em tempo de ecompilação da implementação. Mudar uma classe de implementação não requer a recompilação da classe de abstração e seus clientes. Essa propriedade é essencial quando você quer assegurar compatibilidade no nível binário entre diferentes versões de uma biblioteca de classes. Além disso, esse desacoplamento encoraja o uso de camadas que podem melhorar a estruturação de um sistema. A parte de alto nível de um sistema somente tem que ter conhecimento da abstraçnao e da implementação.
- *Extensibilidade melhorada:* Você pode estender as hierarquias de abstração e implementação independentemente.
- *Ocultar detalhes de implementação dos clientes:* Você pode proteger e isolar os clientes de detalhes de implementação, tais como o compartilhamento de objetos de implementação e o mecanismo de contagem de referências que os acompanham.

## Padrões relacionados:
- *Abstract factory:* Pode criar e configurar uma **Bridge** específica.
- *Adapter:* (**Adapter**) é orientado para fazer com que classes não-relacionadas trabalhem em conjunto. Ele é normalmente aplicado a sistemas que já foram projetados. Por outro lado, **Bridge** é usado em um projeto, desde o início, para permitir que abstrações e implementações possam variar independentemente.

