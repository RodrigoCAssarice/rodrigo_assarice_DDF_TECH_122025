# Relatório de Governança de Dados


Gerado em 2026-01-04 02:40 UTC


Fonte: C:\\Users\\Rodrigo\\Desktop\\py\\Prjt\\DDF_TECH_122025\\notebooks\\data\\electronics_reviews_prepared.parquet


Linhas: 400,000 | Colunas: 14


## Sumário

- Colunas com nulos: 0

- Colunas com arrays/listas: 1 (helpful)


## Dicionário de Dados (perfilamento básico)

| column          | dtype          |   null_pct |   distinct |
|:----------------|:---------------|-----------:|-----------:|
| asin            | object         |          0 |      16005 |
| helpful         | object         |          0 |       2935 |
| helpful_total   | int64          |          0 |        507 |
| helpful_up      | int64          |          0 |        502 |
| month           | int32          |          0 |         12 |
| overall         | float64        |          0 |          5 |
| reviewText      | object         |          0 |     199846 |
| reviewText_len  | int64          |          0 |       5219 |
| reviewTime      | object         |          0 |       5122 |
| review_datetime | datetime64[ns] |          0 |       5122 |
| reviewerID      | object         |          0 |     103709 |
| summary         | object         |          0 |     154167 |
| unixReviewTime  | int64          |          0 |       5122 |
| year            | int32          |          0 |         16 |