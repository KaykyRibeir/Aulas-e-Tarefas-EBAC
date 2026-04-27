# Fixtures: Funções que preparam e limpam dados antes e depois dos testes, permitindo compartilhar configurações e recursos entre múltiplos testes, promovendo a reutilização de código.

# Mocks: Objetos simulados que imitam o comportamento de objetos reais em testes, permitindo isolar o código testado de suas dependências externas.

# PyTest Cov: Uma ferramenta que mede a cobertura de código durante a execução dos testes, ajudando a garantir que o máximo possível do código seja testado.

# PyTest XDist: Uma extensão do PyTest que permite a execução paralela de testes, acelerando o processo de testes em projetos maiores.

# Scopes de Fixtures: Determina o tempo de vida de uma fixture, podendo ser definido como função, classe, módulo ou sessão, otimizando a execução dos testes.

# Stubs: Funções ou objetos que substituem partes do sistema em testes, simulando comportamentos de componentes externos para isolar o código testado.

# Teste de Exceções: Verificação de que o código se comporta corretamente em situações excepcionais, garantindo que exceções sejam lançadas e tratadas adequadamente.




# O que são fixtures no PyTest e por que são importantes?: Fixtures no PyTest são funções que preparam e limpam dados antes e depois dos testes. Elas são importantes porque permitem compartilhar configurações e recursos entre múltiplos testes, promovendo a reutilização de código e mantendo os testes organizados e eficientes.


# Como escolher o escopo correto para uma fixture?: A escolha do escopo correto para uma fixture depende de como e quando você deseja que ela seja executada. Os escopos disponíveis são função, classe, módulo e sessão. Escolher o escopo certo otimiza a execução dos testes, melhorando o desempenho e evitando repetições desnecessárias.


# O que são mocks e stubs e como eles são usados em testes?: Mocks e stubs são técnicas para simular comportamentos de objetos ou funções externas em testes. Eles isolam os testes de interações com dependências externas, tornando-os mais rápidos e controláveis. Isso é especialmente útil para testar o comportamento de uma unidade de código sem depender de sistemas externos.


# Como o PyTest ajuda no teste de exceções e erros?: O PyTest oferece funcionalidades para testar exceções e erros, garantindo que o código se comporte corretamente em situações excepcionais. Isso é feito usando o contexto `pytest.raises`, que verifica se uma exceção específica é levantada durante a execução de um bloco de código.


# Qual é a importância da organização dos testes em um projeto?: A organização dos testes é crucial para manter o código de teste limpo, modular e fácil de entender, especialmente em projetos maiores. Uma boa organização facilita a manutenção, a evolução do software e a colaboração entre desenvolvedores, além de ajudar a identificar rapidamente falhas nos testes.


# O que é o PyTest-cov e como ele é utilizado?: O PyTest-cov é uma ferramenta que mede a cobertura de código durante a execução dos testes. Ele ajuda a identificar quais partes do código estão sendo testadas e quais não estão, permitindo que os desenvolvedores aumentem a cobertura de testes e garantam que o máximo possível do código seja validado.


# Por que a cobertura de testes não deve ser manipulada para atingir 100%?: A cobertura de testes não deve ser manipulada para atingir 100% porque isso pode levar a uma falsa sensação de segurança. O foco deve ser em validar todos os cenários necessários e garantir que o código funcione corretamente, em vez de simplesmente cobrir todas as linhas de código sem considerar a lógica e os casos de uso reais.


# Como a integração contínua (CI/CD) se relaciona com testes unitários?: A integração contínua (CI/CD) automatiza o processo de testes, garantindo que o código seja testado sempre que houver uma alteração. Isso ajuda a identificar rapidamente problemas e a manter a qualidade do software, integrando testes unitários no fluxo de desenvolvimento e implantação.


# Quais são as boas práticas para escrever testes unitários?: Boas práticas para escrever testes unitários incluem estruturar e hierarquizar os testes de forma clara, seguir convenções de nomenclatura e organização de arquivos, e documentar os testes para reduzir erros e facilitar a manutenção. Além disso, é importante garantir que os testes sejam independentes e não dependam de estados globais.
