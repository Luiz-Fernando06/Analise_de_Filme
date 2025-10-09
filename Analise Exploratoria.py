'''
Objetivos:

 Identificar os filmes mais lucrativos. FEITO

 Calcular a média de avaliação por gênero. FEITO

 Ver evolução da produção de filmes ao longo dos anos. FEITO

 Indice de popularidade por filme. FEITO

 Quais idiomas tiveram os filmes mais lucrativos? FEITO

 Filmes de aventura mais fomosos. FEITO

 Quais empresas tiveram maior lucro. FEITO
'''

#--------------------------------Analise exploratoria--------------------------------------------------
import pandas as pd
import ast
df = pd.read_csv('tmdb_5000_movies.csv')
print(df.head(2))
df.shape
df.info()

#a coluna release_date não esta convertida em data
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce', infer_datetime_format=True)
print(df.dtypes)

#Verificando nulos
df.isnull().sum()

#Tratando nulos
df = df.dropna(subset=['overview', 'release_date'])
df['runtime'] = df['runtime'].fillna(0)
print(df.isnull().sum())
print(df.shape)
#Manterei os valores nulos de homepage e tagline

#Transformando a tag e a pagina com valores nulos ou não em informações util
tem_homepage = df.homepage.notnull().astype(int)
tem_tagline = df.tagline.notnull().astype(int)
print(tem_homepage)
print(tem_tagline)

#Verificando duplicata
df.duplicated().sum()

#--------------------------------Extraindo informações uteis---------------------------------------------

#Filmes + lucrativos
df['Lucro'] = df['revenue'] - df['budget']
df['Foi lucrativo?'] = df['revenue'] > df['budget'] * 2
filmes_mais_lucrativos = df.sort_values(by='Lucro', ascending=False)
filmes_mais_lucrativos[['Lucro', 'budget', 'revenue']] = filmes_mais_lucrativos[['Lucro', 'budget', 'revenue']].map('R${:,.2f}'.format)
filmes_mais_lucrativos = filmes_mais_lucrativos.rename(columns={'original_title': 'Título Original',
                                                                'budget': 'Orçamento',
                                                                'revenue': 'Bilheteria'})
print(filmes_mais_lucrativos[['Título Original', 'Orçamento', 'Bilheteria', 'Lucro']].head(10))

#Para analises com a popularidade futuramente
df['popularidade_pct'] = df['popularity'] / df['popularity'].max() * 100

#Calculando a média de avaliação por gênero.
df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df['gênero'] = df['genres'].apply(lambda x: [d['name'] for d in x])
df_explode = df.explode('gênero') #Explodir a lista de gêneros — um filme por linha de gênero
media_avaliacao_porGenero = df_explode.groupby('gênero')['vote_average'].mean()
media_avaliacao_porGenero = media_avaliacao_porGenero.sort_values(ascending=False)
media_avaliacao_porGenero = media_avaliacao_porGenero.rename('Media das notas')
print(media_avaliacao_porGenero.map('{:.1f}'.format))

#Ver evolução da produção de filmes ao longo dos anos.
df['Ano de lancamento'] = df['release_date'].dt.year
producao_por_ano = df.groupby('Ano de lancamento').size()#conta todos os elementos incluindo os nulos
producao_por_ano = producao_por_ano.rename('Quantidade de filmes')
producao_por_ano = producao_por_ano.sort_index(ascending=True)
print(producao_por_ano.head(10))

#Indice de popularidade por filme
df['popularidade_pct'] = df['popularity'] / df['popularity'].max() * 100
indice_popularidade = df[['title', 'popularidade_pct']].sort_values(by='popularidade_pct', ascending=False).reset_index(drop=True)
print(indice_popularidade.head(10).style.format({'popularidade_pct': '{:.2f}%'}))

#Quais idiomas tiveram os filmes mais lucrativos?
Idioma_mais_lucrativos = df.groupby('original_language')['Lucro'].sum().sort_values(ascending=False)
print(Idioma_mais_lucrativos.head(10).map('R${:,.2f}'.format))

#Filmes de terror mais fomosos
filme_aventura_famoso = df_explode.loc[df_explode['gênero'] == 'Horror'].sort_values(by='popularidade_pct', ascending=False)
print(filme_aventura_famoso[['title', 'popularidade_pct']].head(10).style.format({'popularidade_pct': '{:.2f}%'}))

#Quais empresas tiveram maior lucro
df['production_companies'] = df['production_companies'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df['Empresas'] = df['production_companies'].apply(lambda x: [d['name'] for d in x])
df_explode2 = df.explode('Empresas')
empresas_mais_lucrativas = df_explode2.groupby('Empresas')['Lucro'].sum().sort_values(ascending=False)
print(empresas_mais_lucrativas.head(10).map('R${:,.2f}'.format))
