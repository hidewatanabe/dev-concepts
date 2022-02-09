# Chain of Responsability

## Intenção
Evitar o acoplamento do remetente de uma solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação. Encadear os objetos receptores, passando a solicitação ao longo da cadeia até que um objeto a trate.

## Tipo
Comportamental de objetos

## Motivação

## Aplicabilidade:
- Mais de um objeto pode tratar uma solicitação e o objeto que a tratará não conhecido a princípio. O objeto que trata a solicitação deve ser escolhido automaticamente.
- Você quer emitir uma solicitação para um dentre vários objetos, sem especificar explicitamente o receptor.
- O conjunto de objetos que pode tratar uma solicitação deveria ser especificado dinâmicamente.

## Consequências:
- *Acoplamento reduzido.* O padrão libera um objeto de ter que conhecer qual o outro objeto que trata de uma solicitação. Um objeto tem que saber somente que uma solicitação será tratada "apropriadamente". Tanto o receptor como o remetente não têm conhecimento explícito um do outro, e um objeto que está na cadeia não necessita conhecer a estrutura da mesma. Como resultado, **Chain of Responsability** pode simplificar as interconexões de objetos. Ao invés de os objetos manterem referências para todos os receptores-candidatos, eles mantém uma referência única para o seu sucessor.
- *Flexibilidade adicional na atribuição de responsabilidades a objetos.* O **Chain of Responsability** dá uma flexibilidade adicional na distribuição de responsabilidades entre objetos. É possível acrescentar ou mudar responsabilildades para o tratamento de uma solicitação pelo acréscimo ou mudança da cadeia em tempo de execução. Você pode combinar isso com subclasses para especializar estaticamente os *handlers*.
- *A recepção não é garantida.* Uma vez que uma solicitação não tem um receptor explícito, não há garantia de que ela será tratada. Uma solicitação também pode não ser tratada quando a cadeia não estiver configurada apropriadamente.