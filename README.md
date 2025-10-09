# Análise Exploratória de Filmes (TMDb)

Este projeto realiza uma análise exploratória detalhada de um conjunto de dados de filmes do TMDb (The Movie Database), buscando extrair insights sobre popularidade, performance financeira, gêneros e produção cinematográfica ao longo do tempo.

Objetivos

O principal objetivo deste estudo é compreender padrões e tendências dentro do universo cinematográfico, a partir de diversas perspectivas, como:

Identificar os filmes mais lucrativos.

Calcular a média de avaliação por gênero.

Analisar a evolução da produção de filmes ao longo dos anos.

Criar um índice de popularidade por filme.

Avaliar quais idiomas estão associados aos filmes mais lucrativos.

Identificar os filmes de determinados gêneros mais famosos, como aventura e terror.

Determinar quais empresas de produção geraram maior lucro.

Descrição do Código

O código realiza uma análise exploratória estruturada, incluindo as seguintes etapas:

Leitura e inspeção dos dados:
O dataset é carregado e são verificados os tipos de dados, valores ausentes e duplicatas.

Tratamento de dados ausentes:
Colunas essenciais como overview e release_date são preenchidas ou removidas quando necessário, enquanto outros campos opcionais, como homepage e tagline, são convertidos em indicadores binários (presente ou ausente).

Criação de métricas financeiras:

Lucro: diferença entre receita (revenue) e orçamento (budget).

Filmes lucrativos: definidos como aqueles cuja receita foi pelo menos duas vezes maior que o orçamento.

Popularidade e avaliação:

Um índice de popularidade percentual é calculado com base na coluna popularity.

A média de avaliação por gênero é obtida após transformar os gêneros, originalmente em formato de lista de dicionários, em linhas individuais para cada gênero.

Análise temporal:

Extração do ano de lançamento de cada filme.

Contagem da produção de filmes por ano, permitindo observar tendências ao longo do tempo.

Exploração de idiomas e empresas:

Agrupamento dos filmes por idioma original e por empresa de produção para identificar aqueles com maior lucro total.

Filmes por gênero e popularidade:

Seleção de filmes de gêneros específicos, como terror e aventura, classificados de acordo com o índice de popularidade.

Resultados

O projeto permite responder perguntas estratégicas sobre o cinema, tais como:

Quais filmes geraram maior lucro e quais foram os mais populares.

Quais gêneros apresentam melhor avaliação média pelo público.

Como a produção cinematográfica evoluiu ao longo dos anos.

Quais idiomas e empresas de produção estão associados aos maiores sucessos financeiros.

O código é modular, com tratamento de dados, criação de métricas e análise de resultados bem estruturados, facilitando a expansão ou adaptação para outros conjuntos de dados cinematográficos.
