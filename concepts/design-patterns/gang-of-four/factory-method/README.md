# Factory Method

## Intenção
Definir uma interface para criar um objeto, mas deixar as subclasses decidirem que classe instanciar. O **Factory Method** permite adiar a instanciação para subclasses.

## Também conhecido como
Virtual Constructor

## Tipo
Criacional de objetos

## Motivação

## Aplicabilidade:
- Quando uma classe não poder antecipar a classe de objetos que deve criar
- Quando uma classe quer que suas subclasses especifiquem os objetos que criam
- Classes delegam responsabilidade para uma dentre várias subclasses auxiliares e você quer localizar o conhecimento de qual subclasse auxiliar que é a delegada.

## Consequências:
Os **Factory Methods** eliminam a necessidade de anexar classes específicas das aplicações no código. O código lida somente com a interface de **Product**. Portanto, ele pode trabalhar com quaisquer classes concretas do produto definidas pelo usuário.
Uma desvantagem em potencial dos **Factory Methods** é que os clientes podem ter que fornecer subclasses da classe **Creator** somente para criar um objeto concreto do produto em particular. Usar subclasses é bom quando o cliente tem que fornecer subclasses a **Creator** de qualquer maneira, caso contrário, o cliente deve lidar com outro ponto de evolução.
- *Fornece hooks para subclasses:* Criar objetos dentro de uma classe com um **Factory Method** é sempre mais flexível do que criar um objeto diretamente. *Factory Method* dá às subclasses um hook para fornecer uma versão extendida de um objeto.
- * Conecta hierarquias de classes paralelas:* Nos exemplos que consideramos até aqui, o **Factory Method** é somente chamado por **Creators**. Mas isso não precisa ser obrigatoriamente assim. Os clientes podem achar os **Factory Methods** úteis, especialmente no caso de hierarquias de classes paralelas. Hierarquia de classes paralelas ocorrem quando uma classe delega alguma das suas responsabilidades para outra classe separada. Considere, por exemplo, figuras que podem ser manipuladas interativamente. Implementar tias interações não é sempre fácil. Isso frequentemente requer armazenar e atualizar informação que registra o estado da manipulaçãon num certo momento. Esse estado é necessário somente durante a manipulação. Portanto, não necessita ser mantido no "objeto figura".Além do mais, diferentes figuras se comportam de modo diferente quadno são manipuladas pelo usuário. Por exemplo, esticar uma linha pode ter o efeito de mover um dos extremos, enquanto que esticar um texto pode mudar o espaçamento de linhas. Com essas restrições, é melhor usar um objeto **Manipulator** separado, que implementa a interação e mantém o registro de qualquer estado específico da manipulação caso necessário. Diferentes figuras utilização diferentes subclasses **Manipulator** para para tratar interações específicas. A hierarquia de classes **Manipulator** resultante é paralela à hierarquia de classe de **Figure8*

## Padrões relacionados:
- **Abstract Factory** é frequentemente implementado utilizando o padrão **Factory Method**. O exemplo em relação de Motivação no padrão **Abstract Factory** também ilustra o padrão **Factory Method**
- **Template Methods**: **Factory Methods** são usualmente chamados dentro de **Template Methods**.
- **Prototype:** **Prototypes** não exigem subclassificação de Creator. Contudo, frequentemente necessitam uma operação **initialize** na classe de produto. A classe criadora usa initialize para iniciar o objeto. O **Factory Method** não exige uma operação desse tipo.