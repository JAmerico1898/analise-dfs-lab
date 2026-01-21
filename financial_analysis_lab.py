"""
Laboratório de Análise de Demonstrações Financeiras
Hub Central - Aplicativo Principal
====================================================
Curso de Análise de Demonstrações Financeiras
COPPEAD/UFRJ - Prof. José Américo
"""

import streamlit as st
import importlib.util
import os

# =============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Laboratório de Análise Financeira",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# 2. ESTILIZAÇÃO BOUTIQUE ACADÊMICA
# =============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');

    /* Variáveis de Cores */
    :root {
        --navy: #1e293b;
        --navy-light: #334155;
        --gold: #b45309;
        --gold-light: #d97706;
        --slate: #475569;
        --cream: #f8fafc;
        --white: #ffffff;
        --success: #22c55e;
        --warning: #f59e0b;
        --danger: #ef4444;
    }

    /* Fundo principal */
    .main {
        background-color: var(--cream);
        font-family: 'Montserrat', sans-serif;
    }

    /* Títulos com Merriweather */
    h1, h2, h3, h4 {
        font-family: 'Merriweather', serif !important;
        color: var(--navy);
    }

    h1 {
        border-bottom: 3px solid var(--gold);
        padding-bottom: 10px;
        margin-bottom: 20px;
    }

    /* Sidebar Customizada */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--navy) 0%, var(--navy-light) 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: var(--white) !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: var(--gold-light) !important;
        font-weight: 600;
    }

    /* Card de Boas-vindas */
    .welcome-card {
        background: linear-gradient(135deg, var(--white) 0%, #f1f5f9 100%);
        padding: 30px;
        border-radius: 15px;
        border-left: 6px solid var(--gold);
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .welcome-card h3 {
        color: var(--gold) !important;
        margin-bottom: 15px;
    }

    /* Cards de módulos */
    .module-card {
        background: var(--white);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        margin-bottom: 15px;
    }

    .module-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border-color: var(--gold);
    }

    /* Badges de status */
    .badge-active {
        background-color: var(--success);
        color: white;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .badge-progress {
        background-color: var(--warning);
        color: white;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    /* Estatísticas do curso */
    .stat-box {
        background: var(--white);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #e2e8f0;
    }

    .stat-box h2 {
        color: var(--gold) !important;
        font-size: 2.5rem;
        margin: 0;
    }

    .stat-box p {
        color: var(--slate);
        margin: 5px 0 0 0;
        font-size: 0.9rem;
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: var(--navy);
        color: var(--white);
        padding: 8px 20px;
        font-size: 0.75rem;
        text-align: center;
        z-index: 999;
    }

    .footer a {
        color: var(--gold-light);
        text-decoration: none;
    }

    /* Tabs customizadas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: var(--white);
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        border: 1px solid #e2e8f0;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--navy) !important;
        color: var(--white) !important;
    }

    /* Métricas */
    [data-testid="stMetricValue"] {
        color: var(--navy);
        font-family: 'Merriweather', serif;
    }

    /* Botões */
    .stButton > button {
        background: linear-gradient(135deg, var(--gold) 0%, var(--gold-light) 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(180, 83, 9, 0.3);
    }

    /* Expanders */
    .streamlit-expanderHeader {
        background-color: var(--white);
        border-radius: 8px;
    }

    /* DataFrames */
    .dataframe {
        font-size: 0.85rem;
    }

    /* Esconder elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# 3. MAPEAMENTO DOS MÓDULOS
# =============================================================================
MODULOS = {
    "home": {
        "nome": "Página Inicial",
        "arquivo": "home",
        "icone": "🏠",
        "descricao": "Visão geral do laboratório"
    },
    "modulo1": {
        "nome": "Módulo 01 - Introdução à Análise Financeira",
        "arquivo": "modulo1_laboratorio",
        "icone": "📚",
        "descricao": "Fundamentos e objetivos da análise"
    },
    "modulo2": {
        "nome": "Módulo 02 - Estrutura das Demonstrações",
        "arquivo": "modulo2_laboratorio",
        "icone": "🏗️",
        "descricao": "Lógica e inter-relação dos relatórios"
    },
    "modulo3": {
        "nome": "Módulo 03 - Princípios e Qualidade",
        "arquivo": "modulo3_laboratorio",
        "icone": "⚖️",
        "descricao": "Qualidade da informação contábil"
    },
    "modulo4": {
        "nome": "Módulo 04 - Leitura do Balanço",
        "arquivo": "modulo4_laboratorio",
        "icone": "📋",
        "descricao": "Interpretação do Balanço Patrimonial"
    },
    "modulo5": {
        "nome": "Módulo 05 - Análise da DRE",
        "arquivo": "modulo5_laboratorio",
        "icone": "📈",
        "descricao": "Performance e resultado"
    },
    "modulo6": {
        "nome": "Módulo 06 - Fluxo de Caixa (DFC)",
        "arquivo": "modulo6_laboratorio",
        "icone": "💰",
        "descricao": "Geração e uso de caixa"
    },
    "modulo7": {
        "nome": "Módulo 07 - Análise Horizontal e Vertical",
        "arquivo": "modulo7_laboratorio",
        "icone": "📊",
        "descricao": "Tendências e estrutura"
    },
    "modulo8": {
        "nome": "Módulo 08 - Liquidez e Capital de Giro",
        "arquivo": "modulo8_laboratorio",
        "icone": "💧",
        "descricao": "Capacidade de pagamento"
    },
    "modulo9": {
        "nome": "Módulo 09 - Estrutura de Capital",
        "arquivo": "modulo9_laboratorio",
        "icone": "🏛️",
        "descricao": "Endividamento e alavancagem"
    },
    "modulo10": {
        "nome": "Módulo 10 - Rentabilidade e Retorno",
        "arquivo": "modulo10_laboratorio",
        "icone": "🎯",
        "descricao": "ROE, ROA e análise DuPont"
    },
    "modulo11": {
        "nome": "Módulo 11 - Modelo DuPont Expandido",
        "arquivo": "modulo11_laboratorio",
        "icone": "🔬",
        "descricao": "Análise integrada de 5 fatores"
    },
    "modulo12": {
        "nome": "Módulo 12 - Análise Setorial",
        "arquivo": "modulo12_laboratorio",
        "icone": "🏭",
        "descricao": "Benchmarking e comparação"
    },
    "modulo13": {
        "nome": "Módulo 13 - Qualidade do Lucro",
        "arquivo": "modulo13_laboratorio",
        "icone": "🚨",
        "descricao": "Red flags e sinais de alerta"
    },
    "modulo14": {
        "nome": "Módulo 14 - Tomada de Decisão",
        "arquivo": "modulo14_laboratorio",
        "icone": "🎯",
        "descricao": "Crédito e investimento"
    },
    "modulo15": {
        "nome": "Módulo 15 - Projeto Final",
        "arquivo": "modulo15_laboratorio",
        "icone": "🏆",
        "descricao": "Análise integrada completa"
    },
    "contato": {
        "nome": "📬 Contato com o Professor",
        "arquivo": "contato_professor",
        "icone": "📬",
        "descricao": "Dúvidas, sugestões e feedback"
    }
}

# Lista para o selectbox
OPCOES_MENU = [info["nome"] for info in MODULOS.values()]

# Inicializar session_state
if 'modulo_selecionado' not in st.session_state:
    st.session_state['modulo_selecionado'] = OPCOES_MENU[0]

# =============================================================================
# 4. SIDEBAR - NAVEGAÇÃO
# =============================================================================
with st.sidebar:
    # Logo e título
    st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h1 style='color: #b45309; font-size: 1.8rem; margin: 0;'>📊 LAB ANALYST</h1>
            <p style='color: #94a3b8; font-size: 0.85rem; margin-top: 5px;'>
                Análise de Demonstrações Financeiras
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Determinar índice atual baseado no session_state
    try:
        indice_atual = OPCOES_MENU.index(st.session_state['modulo_selecionado'])
    except ValueError:
        indice_atual = 0
    
    # Seletor de módulo com callback para atualizar session_state
    def atualizar_modulo():
        st.session_state['modulo_selecionado'] = st.session_state['selectbox_modulo']
    
    escolha = st.selectbox(
        "🎓 Selecione o Módulo:",
        options=OPCOES_MENU,
        index=indice_atual,
        key='selectbox_modulo',
        on_change=atualizar_modulo,
        help="Escolha a aula que deseja acessar"
    )
    
    # Atualizar session_state com a escolha atual
    st.session_state['modulo_selecionado'] = escolha
    
    st.markdown("---")
    
    # Informações do módulo selecionado
    modulo_key = [k for k, v in MODULOS.items() if v["nome"] == escolha][0]
    modulo_info = MODULOS[modulo_key]
    
    st.markdown(f"""
        <div style='background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px;'>
            <p style='font-size: 1.5rem; margin: 0; text-align: center;'>{modulo_info['icone']}</p>
            <p style='font-size: 0.8rem; color: #94a3b8; text-align: center; margin-top: 10px;'>
                {modulo_info['descricao']}
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Status
    st.markdown("""
        <div style='font-size: 0.8rem;'>
            <p style='margin: 5px 0;'>✅ Sistema Ativo</p>
            <p style='margin: 5px 0;'>📚 15 Módulos Disponíveis</p>
            <p style='margin: 5px 0;'>🎯 Exercícios Interativos</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Créditos
    st.markdown("""
        <div style='text-align: center; font-size: 0.7rem; color: #64748b;'>
            <p>COPPEAD/UFRJ</p>
            <p>Prof. José Américo</p>
            <p>© 2024-2025</p>
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# 5. FUNÇÕES DE RENDERIZAÇÃO
# =============================================================================

def carregar_modulo(nome_arquivo):
    """Carrega e executa um módulo Python dinamicamente."""
    if nome_arquivo == "home":
        renderizar_home()
    elif nome_arquivo == "contato_professor":
        renderizar_contato()
    else:
        path = f"{nome_arquivo}.py"
        if os.path.exists(path):
            try:
                spec = importlib.util.spec_from_file_location(nome_arquivo, path)
                modulo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modulo)
                
                if hasattr(modulo, 'run'):
                    modulo.run()
                else:
                    st.error(f"⚠️ O arquivo `{path}` não contém a função `run()`.")
            except Exception as e:
                st.error(f"❌ Erro ao carregar módulo: {str(e)}")
        else:
            renderizar_em_desenvolvimento(escolha)


def renderizar_home():
    """Página inicial do laboratório."""
    
    st.markdown("<h1>📊 Laboratório de Análise de Demonstrações Financeiras</h1>", unsafe_allow_html=True)
    
    # Card de boas-vindas
    st.markdown("""
        <div class="welcome-card">
            <h3>🎓 Bem-vindo ao Ambiente de Aprendizagem Interativa</h3>
            <p>Este laboratório foi desenvolvido para transformar conceitos teóricos de análise financeira 
            em habilidades práticas de diagnóstico empresarial. Cada módulo combina teoria, exercícios 
            interativos, simuladores e estudos de caso reais.</p>
            <p><strong>Como usar:</strong> Selecione o módulo correspondente à aula no menu lateral 
            e explore os exercícios, simuladores e casos práticos disponíveis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Estatísticas do curso
    st.markdown("### 📈 Visão Geral do Curso")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="stat-box">
                <h2>15</h2>
                <p>Módulos de Aula</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="stat-box">
                <h2>45+</h2>
                <p>Exercícios Práticos</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="stat-box">
                <h2>20+</h2>
                <p>Simuladores</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="stat-box">
                <h2>10+</h2>
                <p>Estudos de Caso</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Estrutura do curso
    st.markdown("### 📚 Estrutura do Curso")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background: white; padding: 20px; border-radius: 12px; border-left: 4px solid #3b82f6;'>
                <h4>📘 Bloco 1: Fundamentos (Módulos 1-6)</h4>
                <ul>
                    <li>Introdução à análise financeira</li>
                    <li>Estrutura das demonstrações</li>
                    <li>Balanço Patrimonial</li>
                    <li>Demonstração de Resultados</li>
                    <li>Fluxo de Caixa</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: white; padding: 20px; border-radius: 12px; border-left: 4px solid #22c55e;'>
                <h4>📗 Bloco 2: Indicadores (Módulos 7-11)</h4>
                <ul>
                    <li>Análise horizontal e vertical</li>
                    <li>Indicadores de liquidez</li>
                    <li>Estrutura de capital</li>
                    <li>Rentabilidade e retorno</li>
                    <li>Modelo DuPont</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background: white; padding: 20px; border-radius: 12px; border-left: 4px solid #f59e0b;'>
                <h4>📙 Bloco 3: Aplicações (Módulos 12-14)</h4>
                <ul>
                    <li>Análise setorial e benchmarking</li>
                    <li>Qualidade do lucro e red flags</li>
                    <li>Tomada de decisão</li>
                    <li>Análise de crédito</li>
                    <li>Análise de investimento</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: white; padding: 20px; border-radius: 12px; border-left: 4px solid #ef4444;'>
                <h4>📕 Bloco 4: Integração (Módulo 15)</h4>
                <ul>
                    <li>Projeto final completo</li>
                    <li>Análise integrada</li>
                    <li>Relatório profissional</li>
                    <li>Apresentação e defesa</li>
                    <li>Avaliação por pares</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Metodologia
    st.markdown("### 🎯 Metodologia de Aprendizagem")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
            **📖 Conceitos Teóricos**
            
            Revisão dos fundamentos com 
            explicações claras e exemplos 
            práticos do mercado brasileiro.
        """)
    
    with col2:
        st.success("""
            **🔧 Simuladores Interativos**
            
            Ferramentas para experimentar 
            cenários e entender o impacto 
            de diferentes variáveis.
        """)
    
    with col3:
        st.warning("""
            **📊 Estudos de Caso**
            
            Casos reais de empresas para 
            aplicar os conceitos em 
            situações práticas.
        """)
    
    st.markdown("---")
    
    # Acesso rápido com botões funcionais
    st.markdown("### ⚡ Acesso Rápido aos Módulos")
    
    # Primeira linha (Módulos 1-5)
    cols1 = st.columns(5)
    for i in range(5):
        with cols1[i]:
            modulo_num = i + 1
            modulo_key = f"modulo{modulo_num}"
            if modulo_key in MODULOS:
                info = MODULOS[modulo_key]
                if st.button(
                    f"{info['icone']}\n\nMódulo {modulo_num:02d}",
                    key=f"btn_mod_{modulo_num}",
                    use_container_width=True,
                    help=info['descricao']
                ):
                    st.session_state['modulo_selecionado'] = info['nome']
                    st.rerun()
    
    # Segunda linha (Módulos 6-10)
    cols2 = st.columns(5)
    for i in range(5):
        with cols2[i]:
            modulo_num = i + 6
            modulo_key = f"modulo{modulo_num}"
            if modulo_key in MODULOS:
                info = MODULOS[modulo_key]
                if st.button(
                    f"{info['icone']}\n\nMódulo {modulo_num:02d}",
                    key=f"btn_mod_{modulo_num}",
                    use_container_width=True,
                    help=info['descricao']
                ):
                    st.session_state['modulo_selecionado'] = info['nome']
                    st.rerun()
    
    # Terceira linha (Módulos 11-15)
    cols3 = st.columns(5)
    for i in range(5):
        with cols3[i]:
            modulo_num = i + 11
            modulo_key = f"modulo{modulo_num}"
            if modulo_key in MODULOS:
                info = MODULOS[modulo_key]
                if st.button(
                    f"{info['icone']}\n\nMódulo {modulo_num:02d}",
                    key=f"btn_mod_{modulo_num}",
                    use_container_width=True,
                    help=info['descricao']
                ):
                    st.session_state['modulo_selecionado'] = info['nome']
                    st.rerun()


def renderizar_contato():
    """Página de contato com o professor."""
    import requests
    from datetime import datetime
    
    st.markdown("<h1>📬 Contato com o Professor</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>💬 Canal de Comunicação Direta</h3>
            <p>Use este formulário para enviar dúvidas sobre o conteúdo, reportar problemas técnicos, 
            sugerir melhorias ou dar feedback sobre sua experiência de aprendizado. 
            Sua mensagem será enviada diretamente para o professor.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Configuração do Pushover
    try:
        PUSHOVER_USER_KEY = st.secrets.get("PUSHOVER_USER_KEY", "")
        PUSHOVER_API_TOKEN = st.secrets.get("PUSHOVER_API_TOKEN", "")
        pushover_configured = bool(PUSHOVER_USER_KEY and PUSHOVER_API_TOKEN)
    except:
        PUSHOVER_USER_KEY = ""
        PUSHOVER_API_TOKEN = ""
        pushover_configured = False
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Envie sua Mensagem")
        
        with st.form(key="contact_form", clear_on_submit=True):
            # Dados do usuário
            col_a, col_b = st.columns(2)
            
            with col_a:
                user_name = st.text_input("👤 Seu nome *", placeholder="Digite seu nome completo")
            
            with col_b:
                user_email = st.text_input("📧 Seu e-mail *", placeholder="seu.email@exemplo.com")
            
            # Categoria e módulo
            col_a, col_b = st.columns(2)
            
            with col_a:
                category = st.selectbox(
                    "📂 Categoria *",
                    options=[
                        "🤔 Dúvida sobre conteúdo",
                        "💡 Sugestão de melhoria",
                        "🐛 Erro/Bug no aplicativo",
                        "⭐ Elogio/Feedback positivo",
                        "💬 Outro assunto"
                    ]
                )
            
            with col_b:
                module = st.selectbox(
                    "📚 Módulo relacionado",
                    options=["Geral / Não se aplica"] + [f"Módulo {i:02d}" for i in range(1, 16)]
                )
            
            # Mensagem
            message = st.text_area(
                "💬 Sua mensagem *",
                placeholder="Descreva sua dúvida, sugestão ou feedback em detalhes...",
                height=150
            )
            
            char_count = len(message) if message else 0
            st.caption(f"{char_count}/2000 caracteres")
            
            submitted = st.form_submit_button("📤 Enviar Mensagem", use_container_width=True)
        
        # Processamento
        if submitted:
            errors = []
            if not user_name or len(user_name.strip()) < 2:
                errors.append("Por favor, informe seu nome.")
            if not user_email or "@" not in user_email:
                errors.append("Por favor, informe um e-mail válido.")
            if not message or len(message.strip()) < 10:
                errors.append("A mensagem deve ter pelo menos 10 caracteres.")
            
            if errors:
                for error in errors:
                    st.error(f"❌ {error}")
            elif not pushover_configured:
                st.warning("⚠️ Sistema de envio não configurado. Entre em contato por e-mail.")
            else:
                try:
                    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
                    pushover_message = f"""📬 Lab Análise Financeira

📅 {timestamp}
👤 {user_name}
📧 {user_email}
📂 {category}
📚 {module}

💬 Mensagem:
{message}"""
                    
                    response = requests.post(
                        "https://api.pushover.net/1/messages.json",
                        data={
                            "token": PUSHOVER_API_TOKEN,
                            "user": PUSHOVER_USER_KEY,
                            "message": pushover_message,
                            "title": f"Lab Finanças - {category}",
                            "priority": 1 if "Erro" in category else 0
                        },
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        st.success("✅ Mensagem enviada com sucesso! O professor responderá em breve.")
                        st.balloons()
                    else:
                        st.error("❌ Erro ao enviar. Tente novamente.")
                except Exception as e:
                    st.error(f"❌ Erro: {str(e)}")
    
    with col2:
        st.markdown("""
            <div style='background: #dbeafe; padding: 20px; border-radius: 12px;'>
                <h4>💡 Dicas</h4>
                <ul style='font-size: 0.85rem;'>
                    <li>Seja específico na descrição</li>
                    <li>Indique o módulo relacionado</li>
                    <li>Para bugs, descreva os passos</li>
                    <li>Inclua prints se necessário</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background: #dcfce7; padding: 20px; border-radius: 12px;'>
                <h4>⏱️ Tempo de Resposta</h4>
                <p style='font-size: 0.85rem;'>
                    <strong>Dúvidas:</strong> 24-48h<br>
                    <strong>Bugs:</strong> Priorizados<br>
                    <strong>Sugestões:</strong> Semanal
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # FAQ
    st.markdown("---")
    st.markdown("### ❓ Perguntas Frequentes")
    
    with st.expander("Como reportar um erro no aplicativo?"):
        st.markdown("""
            Ao reportar erros, inclua:
            1. **Módulo** onde ocorreu o problema
            2. **Ação** que estava executando
            3. **Mensagem de erro** (se houver)
            4. **Navegador** que está usando
        """)
    
    with st.expander("Posso sugerir novos exercícios ou casos?"):
        st.markdown("""
            Sim! Adoramos receber sugestões de:
            - Novos exercícios práticos
            - Casos de empresas brasileiras
            - Melhorias nos simuladores
            - Novos indicadores ou análises
        """)
    
    with st.expander("Como tirar dúvidas sobre exercícios específicos?"):
        st.markdown("""
            Para dúvidas sobre exercícios:
            1. Indique o **módulo e aba** específicos
            2. Descreva **o que tentou fazer**
            3. Explique **onde encontrou dificuldade**
            4. Se possível, inclua **seus cálculos**
        """)


def renderizar_em_desenvolvimento(selecao):
    """Placeholder para módulos não encontrados."""
    st.markdown(f"### 🚧 {selecao}")
    
    st.warning("""
        **Módulo em Desenvolvimento**
        
        O arquivo correspondente a este módulo ainda não foi encontrado no diretório.
        Verifique se o arquivo `.py` está na mesma pasta do hub principal.
    """)
    
    st.info("""
        **Arquivos esperados:**
        - `modulo1_laboratorio.py` até `modulo15_laboratorio.py`
        - Cada arquivo deve conter a função `run()`
    """)


# =============================================================================
# 6. EXECUÇÃO PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    # Identificar módulo selecionado
    modulo_key = [k for k, v in MODULOS.items() if v["nome"] == escolha][0]
    arquivo = MODULOS[modulo_key]["arquivo"]
    
    # Carregar módulo
    carregar_modulo(arquivo)
    
    # Footer
    st.markdown("""
        <div class='footer'>
            📊 <strong>Laboratório de Análise de Demonstrações Financeiras</strong> | 
            COPPEAD/UFRJ | Prof. José Américo | 
            <a href='#'>Termos de Uso</a>
        </div>
    """, unsafe_allow_html=True)