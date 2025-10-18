Caracterização do Dataset:

Origem: resultados da Fase 1 (dataset_fase1_validacao.xlsx).
Conteúdo: repositórios mortos e ressuscitados entre 2018–2025, com campos de:

owner/repo, url, stargazers, data_morte, data_ressurreicao, morreu_novamente.

Estrutura:
Aba 1: repositórios mortos (sem revival)

Aba 2: repositórios ressuscitados (com revival detectado)

Aba 3: estatísticas gerais da coleta.

---

O que será analisado

Investigaremos as atividades técnicas e colaborativas que caracterizam o comportamento dos repositórios antes e depois da revivência.

As principais fontes e variáveis extraídas são:

Pull Requests:

> Tamanho (additions/deletions)

> Tempo de revisão e taxa de aceitação

> Qualidade textual (título e body)

Issues:

> Clareza, descrição, uso de labels e tempo de fechamento

Commits:

> Uso de conventional commits e mensagens bem estruturadas

Comentários:

> Volume e engajamento nas PRs e issues

Essas métricas serão coletadas e comparadas pré e pós-ressurreição.

RQs para a análise

RQ1: Quais características nas atividades de Pull Requests, Issues e Commits estão associadas à revivência e manutenção de repositórios OSS?

Métricas ligadas à RQ:

M1.1 — Qualidade dos Pull Requests: tamanho, tempo de revisão, taxa de aceitação, clareza.

M1.2 — Clareza e completude das Issues: descrição, labels, tempo de fechamento.

M1.3 — Aderência a convenções de commits: presença de conventional commits e estrutura textual.

RQ2: Como a dinâmica de contribuição muda após a revivência do repositório?

M2.1 — Número médio de contribuidores ativos por mês (pré vs. pós-revive).

M2.1 — Frequência média de commits por desenvolvedor (atividade individual).

M2.1 — Distribuição de autoria em PRs (centralização x colaboração: ex. Gini index sobre autores de PRs).

RQ3: O comportamento de revisão e feedback técnico se altera após a revivência?

M3.1 — Média de comentários por Pull Request (indicador de revisão colaborativa).

M3.2 — Tempo médio até o primeiro feedback em PRs (responsividade da comunidade).

M4.2 — Percentual de PRs com revisão formal (via “review” object).
