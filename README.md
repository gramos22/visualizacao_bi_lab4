# LAB04: Visualização de Dados utilizando uma Ferramenta de BI - Análise de Repositórios Ressuscitados

## Visão Geral

Este repositório contém o código e a documentação para o Laboratório 04 do curso de Engenharia de Software, focado na experimentação de software. O objetivo principal é criar um dashboard interativo utilizando uma ferramenta de Business Intelligence (BI) – Microsoft Power BI, no nosso caso – para apresentar os resultados da análise de repositórios "ressuscitados" no GitHub.  Analisaremos atividades técnicas e colaborativas antes e depois da revivência desses repositórios, buscando identificar fatores associados à sua manutenção.

## Objetivo do Dashboard

O dashboard terá duas partes principais:

1.  **Caracterização do Dataset:** Apresentar as características do dataset de repositórios mortos e ressuscitados, incluindo estatísticas gerais da coleta.
2.  **Visualizações para as Questões de Pesquisa (RQs):** Desenvolver visualizações que respondam às questões de pesquisa propostas, focando em atividades de Pull Requests, Issues e Commits.

## Dataset

O dataset utilizado é o resultado da Fase 1 (dataset_fase1_validacao.xlsx) e contém informações sobre repositórios mortos e ressuscitados entre 2018 e 2025.  Os campos incluem:

*   `owner/repo`: Nome do proprietário e nome do repositório.
*   `url`: URL do repositório no GitHub.
*   `stargazers`: Número de estrelas.
*   `data_morte`: Data da morte do repositório.
*   `data_ressurreicao`: Data da ressurreição do repositório.
*   `morreu_novamente`: Indica se o repositório morreu novamente após a ressurreição.

A planilha contém três abas:

*   **Aba 1: repositórios mortos (sem revival)** - Repositórios que foram considerados mortos e não foram ressuscitados.
*   **Aba 2: repositórios ressuscitados (com revival detectado)** - Repositórios que foram considerados mortos e posteriormente ressuscitados.
*   **Aba 3: estatísticas gerais da coleta** - Estatísticas resumidas sobre o dataset.

## O que Será Analisado

Investigaremos as atividades técnicas e colaborativas que caracterizam o comportamento dos repositórios antes e depois da revivência. As principais fontes e variáveis extraídas são:

*   **Pull Requests:** Tamanho (additions/deletions), Tempo de revisão e taxa de aceitação, Qualidade textual (título e body).
*   **Issues:** Clareza, descrição, uso de labels e tempo de fechamento.
*   **Commits:** Uso de conventional commits e mensagens bem estruturadas.
*   **Comentários:** Volume e engajamento nas PRs e issues.

Essas métricas serão coletadas e comparadas pré e pós-ressurreição.

## RQs para a Análise

Este laboratório busca responder às seguintes questões de pesquisa:

**RQ1: Quais características nas atividades de Pull Requests, Issues e Commits estão associadas à revivência e manutenção de repositórios OSS?**

*   **M1.1:** Qualidade dos Pull Requests: tamanho, tempo de revisão, taxa de aceitação, clareza.
*   **M1.2:** Clareza e completude das Issues: descrição, labels, tempo de fechamento.
*   **M1.3:** Aderência a convenções de commits: presença de conventional commits e estrutura textual.

**RQ2: Como a dinâmica de contribuição muda após a revivência do repositório?**

*   **M2.1:** Número médio de contribuidores ativos por mês (pré vs. pós-revive).
*   **M2.2:** Frequência média de commits por desenvolvedor (atividade individual).
*   **M2.3:** Distribuição de autoria em PRs (centralização x colaboração: ex. Gini index sobre autores de PRs).

**RQ3: O comportamento de revisão e feedback técnico se altera após a revivência?**

*   **M3.1:** Média de comentários por Pull Request (indicador de revisão colaborativa).
*   **M3.2:** Tempo médio até o primeiro feedback em PRs (responsividade da comunidade).
*   **M3.3:** Percentual de PRs com revisão formal (via “review” object).

## Setup

*   **Ferramenta de BI:** Microsoft Power BI
*   **Linguagem:** Python (para manipulação e limpeza dos dados, se necessário).
*   **Bibliotecas:** Pandas (para manipulação de dados).

## Contributing

Este projeto é desenvolvido por [Gabriel Ramos Ferreira](https://github.com/gramos22/) e [João Pedro Braga](https://github.com/joaopedro-braga). Contribuições são bem-vindas, mas por favor, entre em contato conosco antes de propor mudanças significativas. A participação de todos os membros do grupo é obrigatória nas apresentações em aula.

## Referências

*   [Link para o cronograma do laboratório](https://github.com/joaopauloaramuni/laboratorio-de-experimentacao-de-software/tree/main/CRONOGRAMA)
