# Sharding

## O que é um shard?
Shard é um fragmento de um banco de dados. É uma partição horizontal de dados de um banco de dados. Cada porção individual é referenciada como um **shard** e é armazenado em uma instância de banco de dados.

## Então o que seria um sharding de banco de dados?
**Sharding** seria uma arquitetura de banco de dados as quais os dados são particionados por linhas e não por colunas (por isso de particionamento horizontal). Cada partição forma parte de um **shard**, que pode ser instalada em instâncias diferentes de banco de dados, em localidades distintas.

## Problemas de não ter uma estratégia de sharding
Um repositório de dados hospedado por um servidor único está sujeito a algumas limitações:
- *Espaço de armazenamento.* Um repositório de dados de grande escala deve conter um grande volume de dados que podem aumentar significativamente ao longo do tempo. Um servidor oferece uma quantidade finita de disco. Durante um certo período de tempo é possível colocar mais discos e aumentar essa capacidade, mas cada vez mais será mais difícil aumentar essa capacidade.
- *Recursos de computação.* Da mesma maneira que a quantidade de dados e volume de dados aumentam significativamente ao longo do tempo, os recursos de computação também são finitos e tal limitação começa a ser sentida em forma de timeouts, erros e falhas cada vez mais frequentes. É mais custosa e difícil o aumento das capacidades de memória RAM e processamento, sem contar que cada aumento desses gera um tempo de indisponibilidade.
- *Largura de banda de rede.* Com a maturação do sistema, geralmente vem junto uma demanda maior de uso das informações de tal sistema, ocasionando um aumento na quantidade de requisições por período de tempo. Caso o volume de dados trafegados exceda a capacidade da rede, as solicitações ocasionarão em falhas de comunicação.
- *Distância geográfica.* Caso seus dados são usados de maneira global, existe um tempo de latência entre o local da requisição e sua origem de dados. Quanto maior a distância, maior o tempo de latência.
- *Utilização de escala vertical.* A utilização de escala vertical (aumento de recursos da mesma máquina - CPU, memória, disco e rede) é uma solução temporária, pois existe um limite para tais ações, conforme especificação das máquinas que estão sendo utilizadas.

## Benefícios da utilização de uma estratégia de sharding
- *Dimensionamento especializado.* Você pode escalar e dimensionar horizontalmente seus dados acrescentando mais **shards** em mais nós de armazenamento
- *Flexibilização de hardware.* Um sistema pode usar hardware disponível no mercado, ao invés de super computadores especializados para cada nó de armazenamento.
- *Utilização racional de hardware.* Você pode reduzir a contenção e melhorar o desempenho equilibrando a carga de trabalho entre os **shards**
- *Possibilidade de utilização de plataformas de computação em nuvem.* Você pode usar provedores de cloud para manter os dados geograficamente mais próximos do consumidores dos mesmos.

## Estratégias de Sharding
Geralmente são utilizadas 3 estratégias para esse particionamento e decidir como serão distribuidos os dados entre os **shards**.
- *Pesquisa.*