import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 8.
    Foco: Análise de Liquidez e Capital de Giro.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .liquidity-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #1e293b;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .metric-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        .cycle-box {
            background-color: #f8fafc;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-align: center;
        }
        .highlight-number {
            font-size: 2rem;
            font-weight: 700;
            color: #b45309;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 08: Análise de Liquidez e Capital de Giro</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, avaliamos a solvência de curto prazo e a eficiência da empresa em gerir seu 'oxigênio' financeiro: o caixa.")

    st.divider()

    # --- 1. CÁLCULO E INTERPRETAÇÃO DE ÍNDICES ---
    st.subheader("1. Laboratório de Índices de Liquidez")
    st.markdown("""
    Insira os dados do Balanço Patrimonial para calcular automaticamente os índices de liquidez. 
    Analise como a exclusão de ativos menos líquidos impacta a margem de segurança.
    """)

    with st.container():
        col_inp1, col_inp2 = st.columns(2)
        with col_inp1:
            ac = st.number_input("Ativo Circulante (R$):", min_value=0, value=150000, step=5000)
            estoques = st.number_input("Estoques (R$):", min_value=0, value=60000, step=5000)
        with col_inp2:
            pc = st.number_input("Passivo Circulante (R$):", min_value=1, value=100000, step=5000)
            caixa_imediato = st.number_input("Caixa e Equivalentes (R$):", min_value=0, value=15000, step=1000)

        # Cálculos
        liq_corrente = ac / pc
        liq_seca = (ac - estoques) / pc
        liq_imediata = caixa_imediato / pc

        st.markdown("<br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("Liquidez Corrente", f"{liq_corrente:.2f}", help="AC / PC")
        with m_col2:
            st.metric("Liquidez Seca", f"{liq_seca:.2f}", help="(AC - Estoques) / PC")
        with m_col3:
            st.metric("Liquidez Imediata", f"{liq_imediata:.2f}", help="Caixa / PC")

    with st.expander("Ver Diagnóstico Pedagógico"):
        if liq_corrente > 1.5:
            st.success("A Liquidez Corrente indica uma folga confortável. A empresa possui R$ {:.2f} para cada R$ 1,00 de dívida.".format(liq_corrente))
        elif liq_corrente >= 1.0:
            st.warning("A liquidez está no limite. Qualquer atraso em recebimentos pode pressionar o caixa.")
        else:
            st.error("Risco de Insolvência! O Ativo Circulante não cobre as obrigações de curto prazo.")
        
        st.info(f"Nota: A diferença entre a Liquidez Corrente e a Seca ({liq_corrente-liq_seca:.2f}) mostra que os estoques representam uma fatia significativa da solvência. Se os estoques não girarem, a empresa terá problemas.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. ESTUDO DE CASO: O PARADOXO DO CRESCIMENTO (OVERTRADING) ---
    st.subheader("2. Estudo de Caso: Expansão vs. Crise de Caixa")
    st.markdown("""
    A **FastGrowth S.A.** dobrou seu faturamento no último ano. Contudo, o CFO está preocupado com o aumento 
    nos pedidos de empréstimos bancários para pagar salários.
    """)

    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        st.metric("Vendas", "+100%", delta="Crescimento")
    with col_c2:
        st.metric("Lucro Líquido", "R$ 200k", delta="Saudável")
    with col_c3:
        st.metric("Saldo de Caixa", "R$ -50k", delta="Crítico", delta_color="inverse")

    st.markdown("""
    <div class='liquidity-card'>
        <strong>Cenário:</strong> Para vender mais, a FastGrowth deu prazos maiores aos clientes (de 30 para 90 dias) 
        e precisou triplicar o estoque.
    </div>
    """, unsafe_allow_html=True)

    pergunta_caso = st.radio(
        "Como analista, qual sua recomendação principal para evitar a quebra por falta de caixa?",
        [
            "Aumentar ainda mais as vendas para gerar mais lucro.",
            "Reduzir o prazo médio de recebimento e otimizar o giro de estoque.",
            "Distribuir mais dividendos para atrair investidores."
        ]
    )

    if st.button("Validar Recomendação"):
        if "prazo médio" in pergunta_caso.lower():
            st.balloons()
            st.success("Exato! O problema é o 'Capital de Giro'. O crescimento acelerado consumiu todo o caixa operacional (Overtrading). É necessário trazer o dinheiro dos clientes mais rápido para o bolso.")
        else:
            st.error("Cuidado! Vender mais pode piorar a situação se o ciclo financeiro estiver descasado.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. EXERCÍCIO APLICADO DE CICLO FINANCEIRO ---
    st.subheader("3. Simulador de Ciclo Financeiro")
    st.write("Ajuste os prazos médios operacionais e observe o impacto no 'Gap de Caixa' da empresa.")

    with st.container():
        s_col1, s_col2, s_col3 = st.columns(3)
        with s_col1:
            pmre = st.slider("Prazo Médio Estoques (dias):", 10, 120, 45)
        with s_col2:
            pmrv = st.slider("Prazo Médio Recebimento (dias):", 10, 120, 30)
        with s_col3:
            pmpf = st.slider("Prazo Médio Pagamento (dias):", 10, 120, 40)

        # Cálculos de Ciclo
        ciclo_operacional = pmre + pmrv
        ciclo_financeiro = ciclo_operacional - pmpf

        st.markdown("<br>", unsafe_allow_html=True)
        
        res_c1, res_c2 = st.columns(2)
        with res_c1:
            st.markdown(f"<div class='cycle-box'>Ciclo Operacional<br><span class='highlight-number'>{ciclo_operacional} dias</span></div>", unsafe_allow_html=True)
        with res_c2:
            color = "#ef4444" if ciclo_financeiro > 0 else "#22c55e"
            st.markdown(f"<div class='cycle-box'>Ciclo Financeiro (Gap de Caixa)<br><span class='highlight-number' style='color: {color}'>{ciclo_financeiro} dias</span></div>", unsafe_allow_html=True)

    st.info("""
    **Interpretação:**
    - **Ciclo Operacional:** Tempo total desde a compra da matéria-prima até o recebimento do cliente.
    - **Ciclo Financeiro:** Tempo que a empresa precisa financiar com recursos próprios ou bancos. 
    Quanto **menor** (ou mais negativo), melhor para o caixa!
    """)

if __name__ == "__main__":
    run()