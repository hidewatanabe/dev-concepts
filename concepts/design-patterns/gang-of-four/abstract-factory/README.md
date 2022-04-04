# Abstract Factory

## Intenção
Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

## Também conhecido como
Kit

## Tipo
Criacional de objetos

## Motivação

## Aplicabilidade:
Use o padrão Abstract Factory quando:
- um sistema deve ser independente de como seus produtos são criados, compostos ou representados
- um sistema deve ser configurado como um produto de uma família de múltiplos produtos
- uma família de objetos-produto for projetada para ser usada em conjunto, e você necessita garantir esta restrição
- você quer fornecer uma biblioteca de classes de produtos e quer revelar somente suas interfaces, não suas implementações

## Consequências:
O padrão **abstract factory** tem os seguintes benefícios e desvantagens:
- *Ele isola as classes concretas.* O padrão **Abstract Factory** ajuda a controlar as classes de objetos criadas por uma aplicação. Uma vez que a fábrica encapsula a responsabilidade e o processo de criar objetos-produto, isola os clientes das classes de implementação. Os clientes manipulam as instâncias através de suas interfaces abstratas. Nomes de classes-produtos ficam isolados na implementação da fábrica concreta; eles não aparecem no código do cliente.
- *Ele torna fácil a troca de famílias de produtos.* A classe de uma fábrica concreta aparece apenas uma vez numa aplicação - isto é, quando é instanciada. Isso torna fácil mudar a fábrica concreta que uma aplicação usa. Ela pode usar diferentes configurações de produtos simplesmente trocando a fábrica concreta. Uma vez que a fábrica abstrata cria uma família completa de produtos, toda família de produtos muda de uma só vez. No nosso exemplo de interface de usuário, podemos mudar de widgets do Motif para widgets do Presentation Manager simplesmente trocando os correspondentes objetos-fábrica e recriando a interface.
- *Ela promove a harmonia entre produtos.* Quando objetos-produto numa família são projetados para trabalharem juntos, é importante que uma aplicação use objetos de somente uma família de cada vez. **Abstract Factory** torna fácil assegurar isso.
- *É difícil de suportar novos tipos de produtos.* Estender fábricas abstratas para produzir novos tipos de Produtos não é fácil. Isso se deve ao fato de que de que a interface de **Abstract Factory** fixa o conjunto de produtos que podem ser criados. Suportar novos tipos de produto exige estender a interface da fábrica, o que envolve mudar a classe **Abstract Factory** e todas as suas subclasses.

## Padrões relacionados:
- As classes **Abstract Factory** são frequentemente implementadas com métodos-fábrica (**Factory Method**), mas elas também podem ser implementadas usando **Prototype**.
- Uma fábrica concreta é frequentemente um **Singleton**.