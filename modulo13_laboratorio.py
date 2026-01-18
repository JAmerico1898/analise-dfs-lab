import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 13.
    Foco: Qualidade do Lucro (Earnings Quality) e Red Flags.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .red-flag-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #ef4444; /* Vermelho para alerta */
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .quality-header {
            color: #1e293b;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.3rem;
            margin-bottom: 15px;
        }
        .alert-box {
            background-color: #fef2f2;
            color: #991b1b;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #fee2e2;
        }
        .highlight-gold {
            color: #b45309;
            font-weight: bold;
        }
        .checklist-item {
            font-size: 0.95rem;
            margin-bottom: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 13: Qualidade do Lucro e Sinais de Alerta</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, assumimos o papel de detetives. Vamos aprender a identificar quando um lucro 'bonito' no papel esconde uma realidade operacional frágil.")

    st.divider()

    # --- 1. ESTUDO DE CASO: CRESCIMENTO ARTIFICIAL ---
    st.subheader("1. Estudo de Caso: O Lucro 'Maquiado' da Alpha S.A.")
    st.markdown("""
    Analise os dados da **Alpha S.A.** abaixo. A empresa reportou um crescimento recorde no lucro líquido. 
    Contudo, o analista atento percebe uma divergência perigosa.
    """)

    # Dados do Caso
    dados_caso = {
        "Indicador (R$ Milhões)": ["Lucro Líquido", "Fluxo de Caixa Operacional (FCO)", "Receita Líquida", "Estoques"],
        "Ano Anterior": [100, 95, 1000, 150],
        "Ano Atual": [160, 20, 1100, 320]
    }
    df_caso = pd.DataFrame(dados_caso)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.table(df_caso.set_index("Indicador (R$ Milhões)"))
    
    with col2:
        st.markdown("<div class='red-flag-card'>", unsafe_allow_html=True)
        st.markdown("<p class='quality-header'>Investigação Analítica</p>", unsafe_allow_html=True)
        st.write("O lucro subiu <span class='highlight-gold'>60%</span>, mas o caixa operacional caiu <span class='highlight-gold'>79%</span>.", unsafe_allow_html=True)
        st.write("Qual o sinal de alerta mais óbvio neste cenário?")
        
        escolha_alerta = st.radio(
            "Diagnóstico:",
            [
                "Excelente controle de custos e despesas.",
                "Crescimento de estoque muito acima das vendas (estoque parado).",
                "O lucro é de alta qualidade pois a receita cresceu."
            ],
            key="radio_alerta"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Validar Investigação"):
        if "estoque" in escolha_alerta.lower():
            st.balloons()
            st.success("Exato! O lucro está crescendo 'no papel', mas o dinheiro está ficando preso no estoque ou sendo gerado por manobras de competência sem entrada de caixa. Isso é um sinal clássico de baixa qualidade do lucro.")
        else:
            st.error("Cuidado! Lucro que não se transforma em caixa é uma ilusão contábil. Observe a variação brutal dos estoques vs. Receita.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. CHECKLIST DE SINAIS DE ALERTA FINANCEIRO ---
    st.subheader("2. Checklist do Analista: Red Flags")
    st.info("Utilize este checklist para avaliar a confiabilidade das demonstrações de qualquer empresa.")

    with st.container():
        st.markdown("<div class='red-flag-card' style='border-left: 5px solid #b45309;'>", unsafe_allow_html=True)
        st.markdown("<p class='quality-header'>Sinais de Alerta (Marque se identificar):</p>", unsafe_allow_html=True)
        
        st.checkbox("Divergência persistente entre Lucro Líquido e Caixa Operacional.", help="O caixa deve acompanhar o lucro no longo prazo.")
        st.checkbox("Variação de Estoques e Clientes crescendo muito acima da Receita Líquida.", help="Pode indicar vendas 'empurradas' para o canal ou estoques obsoletos.")
        st.checkbox("Ganhos 'não recorrentes' (venda de ativos) recorrentes todos os anos.", help="Empresa vendendo os anéis para manter o lucro.")
        st.checkbox("Mudança frequente em critérios contábeis (ex: taxas de depreciação).", help="Pode ser uma tentativa de 'ajustar' o lucro para bater metas.")
        st.checkbox("Aumento súbito de despesas antecipadas ou ativos diferidos.", help="Empresa escondendo gastos no balanço em vez de lançar na DRE.")
        
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. QUESTÕES DISCURSIVAS ANALÍTICAS ---
    st.subheader("3. Laboratório de Síntese: O Olhar Crítico")
    
    st.markdown("""
    <div class='alert-box'>
        <strong>Provocação do Professor:</strong> 
        "Se o lucro é uma opinião e o caixa é um fato, por que o mercado ainda dá tanta importância ao Lucro Líquido e ao ROE?"
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_discursiva_m13"):
        st.write("Responda às questões para debate em sala:")
        
        resp_1 = st.text_area(
            "1. Explique por que a venda de uma sede administrativa gera um lucro que 'distorce' a análise operacional da empresa.",
            placeholder="Pense em sustentabilidade e recorrência..."
        )
        
        resp_2 = st.text_area(
            "2. Como um analista deve reagir ao descobrir que uma empresa reduziu sua taxa de depreciação para aumentar o lucro líquido sem alterar nada na operação?",
            placeholder="Fale sobre ceticismo profissional e ajustes de análise..."
        )
        
        submit_final = st.form_submit_button("Submeter Análises para Revisão")
        
        if submit_final:
            if len(resp_1) > 30 and len(resp_2) > 30:
                st.success("Análises registradas! Seu ceticismo profissional é sua melhor ferramenta.")
                st.info("""
                **Comentários Pedagógicos:**
                - Questão 1: Lucros com venda de ativos são 'uma vez só'. Eles não pagam contas no futuro.
                - Questão 2: O analista deve 'normalizar' o lucro, revertendo o efeito dessa mudança para comparar com o histórico.
                """)
            else:
                st.warning("Por favor, desenvolva mais suas respostas antes de submeter.")

if __name__ == "__main__":
    run()