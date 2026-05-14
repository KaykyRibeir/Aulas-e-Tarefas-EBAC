# Deployments: Um recurso do Kubernetes que gerencia a criação e atualização de um conjunto de pods, garantindo que o número desejado de réplicas de uma aplicação esteja sempre em execução.

# Ingress: Um recurso do Kubernetes que gerencia o acesso externo aos serviços em um cluster, geralmente HTTP, fornecendo balanceamento de carga, terminação SSL e hospedagem virtual baseada em nome.

# LoadBalancer: Um tipo de serviço no Kubernetes que expõe a aplicação ao tráfego externo, distribuindo automaticamente o tráfego de entrada entre as réplicas de um serviço.

# NodePort: Um tipo de serviço no Kubernetes que expõe um serviço em um número de porta estático em cada nó do cluster, permitindo o acesso externo à aplicação.

# Políticas de Rede: Regras que definem como os pods se comunicam entre si e com outros endpoints, permitindo controlar o tráfego de rede para aumentar a segurança e a eficiência.

# Prometheus: Uma ferramenta de monitoramento e alerta de código aberto que coleta e armazena métricas como séries temporais, permitindo a análise do desempenho de aplicações em Kubernetes.

# Services: Um recurso do Kubernetes que define um ponto de acesso estável para um conjunto de pods, permitindo a descoberta de serviços e o balanceamento de carga entre eles.

# Velero: Uma ferramenta de código aberto para backup e recuperação de clusters Kubernetes, permitindo a criação de backups completos e incrementais, além de migrações de cluster.




# O que é Kubernetes e por que é importante para a orquestração de contêineres?: Kubernetes é uma plataforma de código aberto para automação de implantação, escalonamento e operações de contêineres de aplicativos. Ele é importante porque facilita a gestão de aplicações em contêineres, permitindo que desenvolvedores e operadores gerenciem a infraestrutura de forma eficiente e escalável.


# Como o Kubernetes ajuda na escalabilidade de aplicações FastAPI?: O Kubernetes ajuda na escalabilidade de aplicações FastAPI através de Deployments, que gerenciam versões e atualizações controladas, e da configuração de escalabilidade automática, que ajusta o número de pods conforme a carga. Isso garante que a aplicação tenha sempre o número necessário de instâncias para atender à demanda.


# O que são Deployments e Services no Kubernetes?: Deployments no Kubernetes são objetos que gerenciam a implantação de aplicações, permitindo atualizações e escalonamento controlados. Services são objetos que expõem uma aplicação em execução em um conjunto de pods como um serviço de rede, fornecendo um ponto de acesso estável para comunicação entre pods e com o mundo exterior.


# Qual é a função do Ingress no Kubernetes?: O Ingress no Kubernetes é um objeto que gerencia o roteamento de tráfego HTTP e HTTPS para serviços dentro de um cluster. Ele permite que requisições de diferentes fontes sejam direcionadas para os endpoints corretos dentro da aplicação, facilitando o gerenciamento de tráfego externo.


# Como a comunicação entre pods é gerenciada no Kubernetes?: A comunicação entre pods no Kubernetes é gerenciada através de endereços IP dinâmicos e Services, que fornecem pontos de acesso estáveis. Políticas de rede são usadas para controlar a comunicação entre pods, aumentando a segurança e a eficiência da rede.


# Por que as estratégias de backup são importantes no Kubernetes?: As estratégias de backup são importantes no Kubernetes porque a plataforma não oferece soluções de backup e recuperação por padrão. Implementar estratégias como full backup e incremental backup, com ferramentas como Velero, é essencial para garantir a segurança dos dados e a continuidade dos serviços.


# O que são NodePort e LoadBalancer no contexto do Kubernetes?: NodePort e LoadBalancer são tipos de serviços no Kubernetes que expõem aplicações para o exterior. NodePort permite o acesso a um serviço através de um número de porta específico em cada nó do cluster, enquanto LoadBalancer distribui a carga entre múltiplas réplicas de uma aplicação, garantindo alta disponibilidade e balanceamento de carga.


# Como o monitoramento é realizado em um ambiente Kubernetes?: O monitoramento em um ambiente Kubernetes é realizado usando ferramentas como Prometheus e Grafana, que coletam e exibem métricas de desempenho. Além disso, a ELK Stack é utilizada para a coleta de logs e diagnóstico de problemas, proporcionando uma visão abrangente do estado e desempenho das aplicações.


# O que é Velero e como ele é utilizado no Kubernetes?: Velero é uma ferramenta de código aberto para backup e recuperação de clusters Kubernetes. Ele é utilizado para criar backups de recursos e volumes persistentes, permitindo a recuperação de dados em caso de falhas ou desastres. Velero suporta tanto backups completos quanto incrementais.


# Qual é a importância de automatizar backups no Kubernetes?: Automatizar backups no Kubernetes é importante para garantir a segurança dos dados e a continuidade dos serviços sem intervenção manual constante. Usar agendadores automáticos, como Cron jobs, para realizar backups regulares ajuda a proteger contra perda de dados e facilita a recuperação em caso de falhas.
