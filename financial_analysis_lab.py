import streamlit as st
import importlib.util
import os

# 1. CONFIGURAÇÃO DA PÁGINA (Ponto único de entrada)
st.set_page_config(
    page_title="Laboratório de Análise Financeira",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. ESTILIZAÇÃO "BOUTIQUE ACADÊMICA" (CSS Injetado)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

    /* Variáveis de Cores */
    :root {
        --navy: #1e293b;
        --gold: #b45309;
        --slate: #475569;
        --cream: #f8fafc;
        --white: #ffffff;
    }

    .main {
        background-color: var(--cream);
        font-family: 'Montserrat', sans-serif;
    }

    /* Títulos Merriweather */
    h1, h2, h3, .stHeader {
        font-family: 'Merriweather', serif !important;
        color: var(--navy);
    }

    /* Sidebar Customizada */
    [data-testid="stSidebar"] {
        background-color: var(--navy);
    }
    [data-testid="stSidebar"] * {
        color: var(--white) !important;
    }
    .stSelectbox label {
        color: var(--white) !important;
    }

    /* Boxes Estilizados */
    .welcome-card {
        background-color: var(--white);
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid var(--gold);
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        right: 15px;
        font-size: 0.75rem;
        color: var(--slate);
        opacity: 0.6;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MAPEAMENTO DOS 15 MÓDULOS DO CURSO
# O dicionário mapeia o nome amigável para o nome do arquivo .py correspondente
modulos_aula = {
    "Página Inicial": "home",
    "Módulo 01 - Introdução à Análise Financeira": "modulo1_laboratorio",
    "Módulo 02 - Estrutura e Lógica das Demonstrações": "modulo2_laboratorio",
    "Módulo 03 - Princípios e Qualidade da Informação": "modulo3_laboratorio",
    "Módulo 04 - Leitura e Interpretação do Balanço": "modulo4_laboratorio",
    "Módulo 05 - Análise da Performance (DRE)": "modulo5_laboratorio",
    "Módulo 06 - Demonstração dos Fluxos de Caixa": "modulo6_laboratorio",
    "Módulo 07 - Análise Horizontal e Vertical": "modulo7_laboratorio",
    "Módulo 08 - Análise de Liquidez e Capital de Giro": "modulo8_laboratorio",
    "Módulo 09 - Endividamento e Estrutura de Capital": "modulo9_laboratorio",
    "Módulo 10 - Análise de Rentabilidade e Retorno": "modulo10_laboratorio",
    "Módulo 11 - Análise Integrada Modelo DuPont": "modulo11_laboratorio",
    "Módulo 12 - Análise Comparativa e Benchmarking": "modulo12_laboratorio",
    "Módulo 13 - Qualidade do Lucro e Sinais de Alerta": "modulo13_laboratorio",
    "Módulo 14 - Análise para Tomada de Decisão": "modulo14_laboratorio",
    "Módulo 15 - Estudo de Caso e Revisão Geral": "modulo15_laboratorio"
}

# 4. BARRA LATERAL (SIDEBAR) - NAVEGAÇÃO E LOGO
with st.sidebar:
    st.markdown("<h2 style='color: #b45309; text-align: center;'>📊 LAB ANALYST</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 0.9rem;'>Laboratório de Análise de Demonstrações Financeiras</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    escolha = st.selectbox(
        "Selecione o Módulo de Aula:",
        options=list(modulos_aula.keys()),
        index=0
    )
    
    st.markdown("---")
    st.write("**Status do Analista:**")
    st.caption("✅ Navegação Ativa")
    st.caption("✅ Identidade Visual Carregada")
    st.caption(f"📍 {escolha}")

# 5. FUNÇÃO DE CARREGAMENTO DINÂMICO
def carregar_modulo(nome_arquivo):
    if nome_arquivo == "home":
        renderizar_home()
    else:
        path = f"{nome_arquivo}.py"
        if os.path.exists(path):
            # Lógica para importar e executar o arquivo independente
            spec = importlib.util.spec_from_file_location(nome_arquivo, path)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)
            
            # Convenção pedagógica: todo módulo deve ter a função run()
            if hasattr(modulo, 'run'):
                modulo.run()
            else:
                st.error(f"Erro de Estrutura: O arquivo `{path}` não contém a função `run()`.")
        else:
            renderizar_em_desenvolvimento(selecao=escolha)

# 6. PÁGINAS AUXILIARES (Home e Placeholder)
def renderizar_home():
    st.markdown("<h1>Bem-vindo ao Laboratório de Análise</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="welcome-card">
            <h3>Excelência em Diagnóstico Financeiro</h3>
            <p>Este aplicativo é o seu ambiente de experimentação prática. Para cada uma das 15 aulas 
            do nosso curso de graduação, preparamos exercícios, simuladores e estudos de caso que 
            transformam os conceitos contábeis em ferramentas de decisão real.</p>
            <p><strong>Instruções:</strong> Utilize o menu lateral para selecionar a aula correspondente 
            ao conteúdo que deseja praticar hoje.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Objetivo:** Consolidar a teoria através da prática interativa.")
    with col2:
        st.success("**Metodologia:** Discussão, Exercícios e Quizzes de fixação.")
    with col3:
        st.warning("**Ferramentas:** Dashboards dinâmicos e árvores DuPont.")

def renderizar_em_desenvolvimento(selecao):
    st.subheader(f"🚧 {selecao}")
    st.warning("O conteúdo deste módulo está sendo processado pelo conselho pedagógico.")
    st.markdown("""
        <div style='text-align: center; padding: 50px;'>
            <p style='color: #64748b;'>Aguarde a liberação do arquivo python correspondente.</p>
        </div>
    """, unsafe_allow_html=True)

# 7. EXECUÇÃO DO HUB
if __name__ == "__main__":
    carregar_modulo(modulos_aula[escolha])
    st.markdown("<div class='footer'>© 2024 Lab Analyst | Curso de Análise de Demonstrações Financeiras</div>", unsafe_allow_html=True)