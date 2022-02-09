# Proxy

## Intenção
Fornece um substituto *(Surrogate)* ou marcador da localização de outro objeto para controlar o acesso a esse objeto.

## Tipo
Estrutural de objetos

## Motivação

## Aplicabilidade:
- Um **remote proxy** fornece um representante local para um objeto num espaço de endereçamento diferente. Também conhecido como **ambassor**
- Um **virtual proxy** cria objetos caros sob demanda.
- Um **protection proxy** controla o acesso ao objeto original. Os **proxies** de proteção são úteis quando os objetos devem ter diferentes direitos de acesso.
- Um **smart reference** é um substituto para um simples ponteiro que executa ações adicionais quando um objeto é acessado. Usos típicos são:
    - Contar o número de referências para o objeto real, de modo que o mesmo possa ser liberado automaticamente quando não houver mais referências (**smart pointers**).
    - Carregar um objeto persistente para a memória quando ele for referenciado pela primeira vez.
    - Verificar se o objeto real está bloqueado antes de ser acessado, para assegurar que nenhum outro objeto possa mudá-lo

## Consequências:
- Um **proxy remoto** pode ocultar o fato de que um objeto reside num espaço de endereçamento diferente.
- Um **proxy virtual** pode executar otimizações, ais como a criação de um objeto sob demanda.
- Tantos **proxies de proteção** quanto os **smart references** permitem tarefas adicionais de organização quando um objeto é acessado.