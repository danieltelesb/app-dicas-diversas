# Arquivo: app.py

import streamlit as st
import time # Importa a biblioteca time para usar o time.sleep()
from data import tips_data  # Importa a variável tips_data do arquivo data.py
from utils import filter_tips # Agora, a única definição da função filter_tips

# --- ESTILO CSS EMBUTIDO ---
st.markdown("""
<style>
    /* Estilo para todos os botões, com uma largura padrão */
    div.stButton > button {
        background-color: #00A4EF; /* Cor do Banco PAN */
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
        width: auto; /* Largura padrão */
    }
    div.stButton > button:hover {
        background-color: #0073B4; /* Um tom de azul mais escuro para o hover */
    }

    /* Estilo para as mensagens de erro e info */
    .stAlert.stAlert-error, .stAlert.stAlert-info {
        background-color: #E6F7FF !important; /* Fundo azul claro para consistência */
        border-left: 5px solid #00A4EF !important; /* Borda azul do Banco PAN */
        color: #00A4EF !important; /* Texto na cor azul do Banco PAN */
    }
    .stAlert.stAlert-error p, .stAlert.stAlert-info p {
        color: #00A4EF !important; /* Garante que o texto do parágrafo também seja azul */
    }
    
    /* Estilo para o fundo dos checkboxes */
    .stCheckbox span {
        background-color: #00A4EF;
        border-color: #00A4EF;
        transition: background-color 0.3s, border-color 0.3s;
    }
    .stCheckbox span:hover {
        background-color: #0073B4;
        border-color: #0073B4;
    }

    /* Centraliza os cabeçalhos (headers) na barra lateral */
    .stSidebar .centered-header {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# --- Configuração da Página ---
st.set_page_config(
    page_title="Dicas de SQL e Python",
    layout="centered"
)

# --- Verificação de Estado (para filtros e navegação) ---
# Inicialização de variáveis de estado para navegação e filtros
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'dicas'

if 'filtered_topics' not in st.session_state:
    st.session_state.filtered_topics = ["python", "sql"]

if 'filtered_search_term' not in st.session_state:
    st.session_state.filtered_search_term = ""

if 'show_success_message' not in st.session_state:
    st.session_state.show_success_message = False

# Adicione a inicialização do 'search_term' aqui para evitar o erro
if 'search_term' not in st.session_state:
    st.session_state.search_term = ""

# --- Título e subtítulo do aplicativo ---
st.title("Dicas de SQL e Python")
st.markdown("Guarde suas melhores dicas de programação em um só lugar.")

# --- Filtros na Barra Lateral ---
with st.sidebar:
    st.markdown('<h1 class="centered-header">Menu principal</h1>', unsafe_allow_html=True)
    
    # Cria uma única coluna na barra lateral para garantir que o botão ocupe 100% da largura
    col1, = st.columns([1])
    with col1:
        if st.button("HOME", key="home_button", help="Clique para ir para a página inicial."):
            st.session_state.current_page = 'home'
            st.rerun()

    # Usa st.expander para criar a caixa de filtro colapsável
    with st.expander("Opções de Filtro"):
        st.info("Selecione os tópicos que deseja visualizar.")
        st.markdown("---")
        all_selected = st.checkbox("Todas as Dicas", value=True)
        python_selected = st.checkbox("Python", disabled=all_selected)
        sql_selected = st.checkbox("SQL", disabled=all_selected)
    
        if st.button("Aplicar Filtros"):
            selected_topics = []
            if all_selected:
                selected_topics = ["python", "sql"]
            else:
                if python_selected:
                    selected_topics.append("python")
                if sql_selected:
                    selected_topics.append("sql")
                if not selected_topics:
                    selected_topics = ["python", "sql"]

            st.session_state.filtered_topics = selected_topics
            st.session_state.filtered_search_term = st.session_state.search_term
            st.session_state.show_success_message = True
            st.session_state.current_page = 'dicas' # Volta para a página de dicas ao aplicar o filtro
            st.rerun()

        # Exibe a mensagem de sucesso se o estado indicar
        if st.session_state.get('show_success_message'):
            st.success("Filtros aplicados com sucesso!")
            # Reseta o estado para que a mensagem desapareça na próxima interação
            st.session_state.show_success_message = False

    # Expander para dicas para iniciantes com checkboxes
    with st.expander("Sobre mim"):
        st.info("Conheça um pouco sobre o desenvolvedor do aplicativo.")
        if st.button("Profissão"):
            st.session_state.current_page = 'profissao'
            st.rerun()

# --- Lógica de Exibição da Página Principal ---
if st.session_state.current_page == 'home':
    st.markdown("---")
    st.subheader("Por que este aplicativo é importante?")
    st.markdown("""
    Este aplicativo foi criado para ajudar programadores e estudantes a organizar e acessar suas **dicas e truques de programação** de forma rápida e eficiente. Com ele, você pode:
    
    * **Consolidar conhecimento:** Mantenha todas as suas notas importantes de SQL e Python em um só lugar, evitando a bagunça de múltiplos arquivos e anotações.
    * **Acelerar o desenvolvimento:** Encontre rapidamente a sintaxe ou a função que você precisa, economizando tempo e aumentando sua produtividade.
    * **Aprender e crescer:** Crie sua própria base de dados de conhecimento, revisando e adicionando dicas conforme avança em sua jornada de aprendizado.
    
    O objetivo é que esta ferramenta se torne um recurso valioso para aprimorar suas habilidades de programação e facilitar seu trabalho diário.
    """)

elif st.session_state.current_page == 'profissao':
    st.markdown("---")
    st.subheader("Profissão")
    st.markdown("""
    Sou um **Desenvolvedor Python** com experiência em automação de processos,
    análise de dados e desenvolvimento de aplicações web com Streamlit.
    Meu objetivo é criar soluções eficientes e intuitivas que resolvem problemas reais.
    """)
else:
    # Caso contrário, mostra a página de dicas padrão
    # --- Pesquisa na Área Principal ---
    search_term = st.text_input("Pesquisar dicas...", placeholder="Pesquisar por título ou conteúdo...", key="search_term")
    
    # --- Lógica de Filtragem e Exibição ---
    filtered_tips = filter_tips(tips_data, st.session_state.filtered_topics, st.session_state.filtered_search_term)

    st.markdown("---")
    st.subheader("Dicas Encontradas")

    # Filtra as dicas por tópico
    python_tips = [tip for tip in filtered_tips if tip['topic'] == 'python']
    sql_tips = [tip for tip in filtered_tips if tip['topic'] == 'sql']

    # Agrupa dicas de Python em um contêiner
    if python_tips:
        st.markdown("### Dicas de Python")
        with st.container(border=True):
            for tip in python_tips:
                st.markdown(f"**{tip['title']}**")
                st.markdown(f"*{tip['tip']}*")
                st.markdown(f'<span style="background-color:#E3F2FD; color:#1565C0; padding: 4px 8px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">Python</span>', unsafe_allow_html=True)
                st.markdown("---")

    # Agrupa dicas de SQL em um contêiner separado
    if sql_tips:
        st.markdown("### Dicas de SQL")
        with st.container(border=True):
            for tip in sql_tips:
                st.markdown(f"**{tip['title']}**")
                st.markdown(f"*{tip['tip']}*")
                st.markdown(f'<span style="background-color:#E8F5E9; color:#2E7D32; padding: 4px 8px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">SQL</span>', unsafe_allow_html=True)
                st.markdown("---")

    if not filtered_tips:
        st.info("Nenhuma dica encontrada.")
