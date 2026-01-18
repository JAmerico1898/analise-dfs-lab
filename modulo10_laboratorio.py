import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 10.
    Foco: Análise de Rentabilidade (ROE, ROA e ROI).
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .profitability-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #b45309;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .metric-header {
            color: #1e293b;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 15px;
        }
        .comparison-table {
            background-color: #f8fafc;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #e2e8f0;
        }
        .interpretation-box {
            background-color: #1e293b;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border-right: 5px solid #b45309;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 10: Análise de Rentabilidade e Retorno</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, aprendemos a medir a eficiência final da gestão: a capacidade de transformar ativos e capital próprio em lucro real.")

    st.divider()

    # --- 1. EXERCÍCIOS NUMÉRICOS COMPLETOS ---
    st.subheader("1. Desafio de Cálculo: ROE e ROA")
    st.markdown("""
    Utilize os dados extraídos das demonstrações financeiras para calcular os índices de rentabilidade. 
    Lembre-se de usar os valores médios (início + fim do período / 2) quando disponíveis.
    """)

    with st.container():
        col_inp1, col_inp2 = st.columns(2)
        with col_inp1:
            receita_liquida = st.number_input("Receita Líquida (R$):", min_value=1, value=500000)
            lucro_liquido = st.number_input("Lucro Líquido (R$):", min_value=0, value=65000)
        with col_inp2:
            ativo_medio = st.number_input("Ativo Total Médio (R$):", min_value=1, value=400000)
            pl_medio = st.number_input("Patrimônio Líquido Médio (R$):", min_value=1, value=250000)

        # Cálculos de Rentabilidade
        margem_liquida = (lucro_liquido / receita_liquida) * 100
        roa = (lucro_liquido / ativo_medio) * 100
        roe = (lucro_liquido / pl_medio) * 100

        st.markdown("<br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("Margem Líquida", f"{margem_liquida:.1f}%")
        with m_col2:
            st.metric("ROA (Retorno Ativo)", f"{roa:.1f}%")
        with m_col3:
            st.metric("ROE (Retorno Acionista)", f"{roe:.1f}%")

    with st.expander("Ver Análise Pedagógica"):
        st.write(f"**Interpretação:** Para cada R$ 100 investidos pelos sócios, a empresa gera **R$ {roe/100 * 100:.2f}** de lucro.")
        if roe > roa:
            st.info("O ROE é maior que o ROA. Isso indica que a empresa está utilizando alavancagem financeira de forma positiva para turbinar o retorno do acionista.")
        else:
            st.warning("O ROE está muito próximo ou abaixo do ROA. A estrutura de capital pode não estar otimizada.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. COMPARAÇÃO: O PARADOXO DO ROE ---
    st.subheader("2. Comparação Executiva: Empresa A vs. Empresa B")
    st.markdown("""
    Analise o caso de duas empresas com o **mesmo ROE de 20%**. Elas são igualmente boas?
    """)

    dados_comp = {
        "Indicador": ["Lucro Líquido", "Patrimônio Líquido", "Dívida Total", "Margem Líquida", "Giro do Ativo", "ROE Final"],
        "Empresa Eficiência (A)": ["R$ 100k", "R$ 500k", "R$ 100k", "15%", "1.5x", "20%"],
        "Empresa Alavancada (B)": ["R$ 100k", "R$ 500k", "R$ 800k", "4%", "0.5x", "20%"]
    }
    st.table(pd.DataFrame(dados_comp))

    st.markdown("""
    <div class="profitability-card">
        <p><strong>Cenário:</strong> Ambas entregam 20% ao sócio. 
        Contudo, a <strong>Empresa A</strong> foca em margem e eficiência operacional, 
        enquanto a <strong>Empresa B</strong> possui margens baixas e está pesadamente endividada.</p>
    </div>
    """, unsafe_allow_html=True)

    escolha_diagnostico = st.radio(
        "Como analista, qual empresa apresenta o retorno de maior 'qualidade'?",
        [
            "Empresa A: O retorno vem da eficiência operacional e margens sólidas.",
            "Empresa B: O retorno é alto devido ao uso agressivo de capital de terceiros.",
            "Ambas são idênticas, pois o que importa para o investidor é o ROE de 20%."
        ]
    )

    if st.button("Validar Diagnóstico"):
        if "Empresa A" in escolha_diagnostico:
            st.balloons()
            st.success("Correto! O retorno da Empresa A é mais sustentável. A Empresa B corre um alto risco financeiro; qualquer queda na receita pode tornar o custo da dívida maior que o lucro operacional, destruindo o ROE rapidamente.")
        else:
            st.error("Cuidado! O analista deve olhar 'atrás' do ROE. Rentabilidade via dívida excessiva é muito mais arriscada que via margem operacional.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. INTERPRETAÇÃO ECONÔMICA ---
    st.subheader("3. Interpretação Econômica dos Resultados")
    
    st.markdown("""
    <div class="interpretation-box">
        <p style="text-align: center; font-style: italic;">
            "Um ROE de 15% em um país com juros de 2% é excelente. O mesmo ROE em um país com juros de 13,75% pode significar destruição de valor."
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_interpretacao_m10"):
        st.write("Reflexão Final:")
        pergunta = st.text_area(
            "Por que o analista deve comparar o ROE da empresa com a taxa básica de juros (Selic) e com o custo de capital próprio (Ke)?",
            placeholder="Discuta o conceito de Custo de Oportunidade..."
        )
        
        submit = st.form_submit_button("Submeter para Debate")
        
        if submit:
            if len(pergunta) > 30:
                st.info("""
                **Análise do Professor:**
                Excelente ponto. Se o ROE for menor que a taxa livre de risco, o acionista está perdendo dinheiro em termos relativos, 
                pois teria um retorno maior com risco zero no Tesouro Direto. A rentabilidade deve sempre premiar o risco do negócio.
                """)
                st.success("Reflexão registrada para nossa discussão em sala!")
            else:
                st.warning("Desenvolva um pouco mais sua resposta sobre o risco e o prêmio exigido pelo acionista.")

if __name__ == "__main__":
    run()