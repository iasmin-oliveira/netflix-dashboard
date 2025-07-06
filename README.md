# netflix-dashboard
Funcionalidades mínimas do dashboard:   
Pelo menos 6 gráficos, destes pelo menos 2 interativos com Plotly ou Matplotlib + widgets (ex: sliders, dropdowns).
Separar em múltiplas páginas Filtros funcionais (ex: por estado, período, categoria, etc.).
Layout organizado (uso de st.sidebar, st.tabs ou st.columns).


# Netflix Dashboard

Projeto básico para visualização interativa de dados da Netflix com Streamlit.

## Como usar

1. Clone o repositório.
2. Coloque o arquivo `netflix_titles.csv` dentro da pasta `data/`.
3. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
