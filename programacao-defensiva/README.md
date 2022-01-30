# Programação defensiva
## O que é?
Um conjunto de técnicas de projetos objetivando a estabilidade e a segurança de um software independente do imprevisível.
A ideia pode ser vista como forma de reduzir ou eliminar a hipótese de algo inesperado ou imprevisível acontecer. Técnicas de programação defensiva começaram a serem desenvolvidas quando softwares começaram a fazer parte do core da sociedade.

## Recomendações
### Para o dev:
O dev de hoje em dia deve se preocupar para não cair nas seguintes situações:
- *Estruturas de tamanho constante*
- *Funções de dados de tamanho dinâmico sem checagem*
- *Alta complexidade de código*
- *O código está seguro até que se prove o contrário*
- *Meu código só roda dentro dessa máquina, então vou usar permissão de root mesmo...*

E alguns pontos que, mesmo não sendo a proteção como principal motivador, nos ajuda a ter um software menos vulnerável:
- *Arquitetura desacoplada:*

### Para as corps:
- *Auditoria de código:* Ferramentas de SAST e DAST
- *Infraestrutura monitorada, atualizada e testada:*

## Programação defensiva - Por que em 2022 é tão polêmica?
Durante algumas horas de leitura para entender melhor, algumas coisas me veio a cabeça:
- Por que a programação defensiva é vista somente como "defensiva" e não "informativa-defensiva"?
Ex: Quando se tem um método que executa uma divisão de 2 valores passados pelo usuário, você pode somente validar se o valor do divisor é igual a zero ou você pode propagar uma exceção para camadas superiores, com o intuito de informar quem chama a função de que um argumento inválido foi passado. Em resumo técnico, você pode "fazer um if divisor != 0: return None" ou você pode propagar um erro "ZeroDivisionError" para quem chamou sua função.