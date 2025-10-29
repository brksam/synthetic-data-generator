# 🧠 Synthetic Data Generator

Gerador de dados sintéticos desenvolvido em **Python** utilizando a biblioteca **SDV (Synthetic Data Vault)**.  
O objetivo é criar dados artificiais realistas a partir de tabelas de bancos de dados — útil para testes, simulações e projetos que exigem privacidade de dados.

---

## 🚀 Funcionalidades

- Conexão direta com bancos de dados MySQL (via SQLAlchemy).  
- Leitura automática de tabelas reais.  
- Geração de novas amostras com **padrões estatísticos semelhantes aos dados originais**.  
- Suporte a múltiplas tabelas relacionadas (ex: `clientes` e `pedidos`).  
- Exportação dos dados gerados em formato **CSV**.  

---

## 🧩 Estrutura do Projeto
```
synthetic-data-generator/
│
├── main.py # Código principal (lógica de geração de dados)
├── config.json # Configurações de conexão e parâmetros
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos a serem ignorados pelo Git
└── clientes_sinteticos.csv / pedidos_sinteticos.csv # Dados gerados
```

## ⚙️ Como Executar

### 1️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
source venv/Scripts/activate   # No Windows
```
2️⃣ Instale as dependências
```
pip install -r requirements.txt
```
3️⃣ Configure o arquivo config.json
```
{
  "database_url": "mysql+pymysql://root:@localhost/testdb",
  "table": "clientes",
  "samples": 500
}
```
4️⃣ Execute o script
```
python main.py
```
Os dados gerados serão salvos automaticamente em arquivos .csv.

🧠 Tecnologias Utilizadas

- Python 3.12+

- SDV (Synthetic Data Vault)

- SQLAlchemy

- Pandas

- PyMySQL

- XAMPP / MariaDB
- 
📊 Exemplo de Saída
```
id, nome, idade, salario
123654, Ana, 29, 3250.0
789456, João, 41, 4150.0
456789, Maria, 32, 2890.0
```
🧱 Futuras Melhorias

- Interface web para geração de dados.

- Suporte a outros bancos (PostgreSQL, SQLite).

- Opção de upload direto para Google Drive.

👨‍💻 Autor

Desenvolvido por Samuel Souto (brksam)

💼 Projeto voltado para portfólio e demonstração de conhecimento em Python, banco de dados e IA de dados sintéticos.

🪪 Licença

Este projeto é distribuído sob a licença MIT.
Sinta-se à vontade para usar e modificar.

⭐ Se gostou do projeto, não esqueça de deixar uma estrela no repositório!


---

Quer que eu adicione uma **versão com badges e imagem de preview** (tipo “feito com Python”, “status do projeto”, “licença MIT” e um banner bonito)?  
Fica muito mais visual e ajuda o repositório a se destacar.











