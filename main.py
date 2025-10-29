import pandas as pd
from sdv.multi_table import HMASynthesizer
from sqlalchemy import create_engine
import json
from sdv.metadata import MultiTableMetadata 

#config - abre o arquivo json, salva ele na variavel f e depois transforma em dicionario em python dentro da variavel config
with open("config.json") as f:
    config = json.load(f)

#conexao com o banco 
engine = create_engine(config["database_url"])
tabela = config["table"]

#ler os dados 
clientes = pd.read_sql(f"SELECT * FROM clientes", engine)
pedidos = pd.read_sql(f"SELECT * FROM pedidos", engine)

#objeto null
metadata = MultiTableMetadata() 

#detecta as estruturas
metadata.detect_table_from_dataframe(table_name="clientes", data=clientes)
metadata.detect_table_from_dataframe(table_name="pedidos", data=pedidos)

#relacoes das tabelas
metadata.set_primary_key("clientes", "id")
metadata.set_primary_key("pedidos", "id")
metadata.add_relationship(parent_table_name="clientes", parent_primary_key="id", child_table_name="pedidos", child_foreign_key="cliente_id")



modelo = HMASynthesizer(metadata) #cria o modelo SDV
modelo.fit({"clientes": clientes, "pedidos": pedidos}) #.fit para fazer o modelo analisar as relações entre as tabelas

#sinteticos
dados_sinteticos = modelo.sample(scale=2.0)

#salvar
for tabela, df in dados_sinteticos.items():
    df.to_csv(f"{tabela}_sinteticos.csv", index=False)
    print(f"{len(df)} Linhas geradas em {tabela}_sinteticos.csv")