# 12 Factors

## 2011, Heroku

## O que é?
Metodologia de construção de "Softwares as a Service" que:
- Usam formatos declarativos para automatizar a configuração inicial, minimizar o tempo e custo para novos desenvolvedores participarem do projeto;
- Tem um contrato claro com o sistema operaciona que o suporta, oferecendo portabilidade máxima entre os ambientes que o executem;
- São adequados para implantação em modernas plataformas em nuvem, evitando a necessidade por servidores e administradores de sistemas;
- Minimizam a divergência entre desenvolvimento e produção, permitindo a implantação contínua para máxima agilidade;
- E podem escalar sem significativas mudanças em ferramentas, arquiteturas ou práticas de programação.

# Quais são os 12 fatores?
## 1. Codebase:
Uma base de código com rastreamento utilizando controle de versão, muitos deploys.

### Como fazer?

### O que não fazer?

## 2. Dependencies:
Declare e isole explicitamente as dependências.

#### Como fazer?
- Utilizar gerenciadores de pacotes

### O que não fazer?

## 3. Configurations:
Armazene as configurações no ambiente.

### Como fazer?

### O que não fazer?

## 4. Backing Services:
Trate serviços de apoio como recursos anexados.

### Como fazer?

### O que não fazer?

## 5. Build, Release and Run:
Separe estritamente os builds e execute em estágios.

### Como fazer?

### O que não fazer?

## 6. Processes:
Execute a aplicação como um ou mais processos que não armazenam estado.

### Como fazer?

### O que não fazer?

## 7. Port Binding:
Exporte serviços por ligação de porta.

### Como fazer?

### O que não fazer?

## 8. Concurrency:
Dimensione por um modelo de processo.

### Como fazer?

### O que não fazer?

## 9. Disposability:
Maximizar a robustez com inicialização e desligamento rápido.

### Como fazer?

### O que não fazer?

## 10. Dev/Prod parity:
Mantenha o desenvolvimento, teste, produção o mais semelhante possível.

### Como fazer?

### O que não fazer?

## 11. Logs:
Trate logs como fluxo de eventos.

### Como fazer?

### O que não fazer?

## 12. Admin process:
Executar tarefas de administração/gerenciamento como processo pontuais.

### Como fazer?

### O que não fazer?