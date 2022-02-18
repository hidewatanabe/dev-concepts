# Facade

## Intenção
Fornecer de forma unificada para um conjunto de interfaces em um subsistema. Facade define uma interface de nível mais alto que torna o susbsistema mais fácil de ser usado.

## Tipo
Estrutural de Objetos

## Motivação

## Aplicabilidade:
- Você deseja fornecer uma interface simples para um subsistema complexo. Os subsistemas se tornam mais complexos à medida que evoluem. A maioria dos padões, quando aplicados, resulta em mais e menores classes. Isso torna o subsistema mais reutilizável e mais fácil de customizar, porém, também se torna mais difícil de usar para os clientes que não precisam customizá-lo. Uma fachada pode fornecer, por comportamento-padrão, uma visão simples do sistema, que é boa o suficiente para a maioria dos clientes. Somente os clientes que demandarem maior customização necessitarão olhar além da fachada.
- Existirem muitas dependências entre clientes e classes de implementação de uma abstração. Ao introduzir uma fachada para desacoplar o subsistema dos clientes e de outros subsistemas, estar-se-á promovendo a independência e portabilidade dos subsistemas.
- Você desejar estruturar seus subsistemas em camadas. Use uma fachada para definir o ponto de entrada para cada nível de subsistema. Se os subsistemas são independentes, você pode simplificar as dependências entre eles fazendo com que se comuniquem uns com os outros exclusivamente através das suas fachadas.

## Consequências:
- Isola os clientes dos componentes do subsistema, dessa forma reduzindo o número de objetos com que os clientes tem que lidar e tornando o subsistema mais fácil de usar.
- Promove um acoplamento fraco entre o subsistema e seus clientes. Frequentemente os componentes num subsistema são fortemente acoplados. O acoplamento permite variar os componentes do subsistema sem afetar os seus clientes. As fachadas ajudam a estratificar um sistema e as dependências entre os objetos. Elas podem eliminar dependências complexas ou circulares. Isso pode ser uma consequencia importante quando o cliente e o subsistema são implementados independentemente. Reduzir as dependências de compiliação é um aspecto vital em grandes sistemas de software. Você deseja economizar tempo através da minimização da recompilação, quando as classes do subsistema sofrem transformações. A redução das dependências de compilação com o uso de façades pode limitar a recompilação necessária para uma pequena mudança num subsistema importante. Uma fachada também pode simplificar a migração de sistemas para outras plataformas, porque é menos provável que a construção de um subsistema exija construir todos os outros.
- Não impede as aplicações de utilizarem as classes do subsistema caso necessitem fazê-lo. Assim, você pode escolher entre a facilidade de uso e a generalidade.

## Padrões relacionados:
- *Abstract Factory:* pode ser usado com *Facade* para fornecer uma interface para a criação de objetos do subsistema de forma independente do subsistema. Uma *Abstract Factory* pode ser usada como uma alternativa a *Facade* para ocultar classes específicas de plataformas.
- *Mediator:* é semelhante a *Facade* no sentido em que ele abstrai a funcionalidade de classes existentes. Contudo, a finalidade de *Mediator* é abstrair comunicações arbitrárias entre objetos-colegas, frequentemente centralizando funcionalidades que não pertencem a nenhum deles. Os colegas do *Mediator* estão cientes do mesmo e se comunicam com o *Mediator* em vez de se comunicarem uns com os outros diretamente. Por contraste, uma fachada meramente abstrai uma interface para objetos subsistemas para torná-los mais fáceis de serem utilizados. Ela não define novas funcionalidades e as classes do subsistema não tem o conhecimento dela.
- *Singleton:* geralmente objetos *Facade* são *Singletons*.