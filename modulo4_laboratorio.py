import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 4.
    Foco: Leitura e Interpretação do Balanço Patrimonial.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .analysis-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #1e293b;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .strength-box {
            background-color: #f0fdf4;
            color: #166534;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #22c55e;
            margin-bottom: 10px;
        }
        .weakness-box {
            background-color: #fef2f2;
            color: #991b1b;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #ef4444;
            margin-bottom: 10px;
        }
        .interpret-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 04: Leitura e Interpretação do Balanço Patrimonial</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, saímos da mecânica básica para a interpretação estratégica. O objetivo é 'ouvir' o que os ativos e passivos dizem sobre a saúde da empresa.")

    st.divider()

    # --- 1. ANÁLISE DIRIGIDA DE UM BALANÇO REAL SIMPLIFICADO ---
    st.subheader("1. Análise Dirigida: O Balanço da 'Indústria Alpha'")
    st.markdown("""
    Abaixo, apresentamos o Balanço Patrimonial simplificado da **Indústria Alpha S.A.** referente ao último exercício. 
    Analise os números antes de responder às perguntas interpretativas.
    """)

    # Dados do Balanço
    dados_ativo = {
        "Contas do Ativo": ["Caixa e Equivalentes", "Contas a Receber", "Estoques", "Realizável a Longo Prazo", "Imobilizado Líquido", "Intangível"],
        "Valor (R$)": [45000, 120000, 180000, 30000, 450000, 75000]
    }
    dados_passivo = {
        "Contas do Passivo e PL": ["Fornecedores", "Empréstimos CP", "Salários e Encargos", "Empréstimos LP", "Capital Social", "Lucros Acumulados"],
        "Valor (R$)": [95000, 150000, 35000, 220000, 350000, 50000]
    }

    df_ativo = pd.DataFrame(dados_ativo)
    df_passivo = pd.DataFrame(dados_passivo)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Ativo (Aplicações)**")
        st.table(df_ativo)
        ativo_total = df_ativo["Valor (R$)"].sum()
        st.metric("Ativo Total", f"R$ {ativo_total:,.2f}")

    with col2:
        st.write("**Passivo e PL (Origens)**")
        st.table(df_passivo)
        passivo_pl_total = df_passivo["Valor (R$)"].sum()
        st.metric("Total Passivo + PL", f"R$ {passivo_pl_total:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Perguntas dirigidas
    st.markdown("<div class='interpret-header'>Desafio de Leitura Rápida</div>", unsafe_allow_html=True)
    
    with st.expander("Clique para responder: Qual o valor do Capital de Giro (Ativo Circulante)?"):
        # AC = Caixa + Receber + Estoques = 45+120+180 = 345
        resp_ac = st.number_input("Insira o valor do Ativo Circulante (R$):", step=1000)
        if st.button("Validar AC"):
            if resp_ac == 345000:
                st.success("Correto! O Ativo Circulante totaliza R$ 345.000,00.")
            else:
                st.error("Incorreto. Some as contas de curto prazo (Caixa, Receber e Estoques).")

    with st.expander("Clique para responder: Qual a situação do Capital de Giro Líquido (CCL)?"):
        # PC = Fornecedores + Emp CP + Salários = 95+150+35 = 280
        # CCL = 345 - 280 = 65
        st.write("CCL = Ativo Circulante - Passivo Circulante")
        resp_ccl = st.radio("A situação da empresa é:", ["CCL Positivo (Folga)", "CCL Negativo (Risco de Liquidez)"])
        if st.button("Validar CCL"):
            if resp_ccl == "CCL Positivo (Folga)":
                st.success("Excelente! O CCL é de R$ 65.000,00. A empresa possui recursos de curto prazo suficientes para cobrir as obrigações imediatas.")
            else:
                st.error("Reveja os cálculos. O AC (345k) é maior que o PC (280k).")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. IDENTIFICAÇÃO DE PONTOS FORTES E FRAGILIDADES ---
    st.subheader("2. Diagnóstico: Pontos Fortes e Fragilidades")
    st.write("Com base nos números da Indústria Alpha, arraste seu julgamento para os pontos identificados:")

    diag_col1, diag_col2 = st.columns(2)

    with diag_col1:
        st.markdown("<div class='strength-box'><strong>Ponto Forte 1:</strong> Baixo Intangível comparado ao Imobilizado.</div>", unsafe_allow_html=True)
        st.markdown("<div class='strength-box'><strong>Ponto Forte 2:</strong> Ativo Circulante financia todo o Passivo Circulante.</div>", unsafe_allow_html=True)
    
    with diag_col2:
        st.markdown("<div class='weakness-box'><strong>Fragilidade 1:</strong> Alta dependência de Empréstimos de Curto Prazo (R$ 150k).</div>", unsafe_allow_html=True)
        st.markdown("<div class='weakness-box'><strong>Fragilidade 2:</strong> Baixo volume de Lucros Acumulados em relação ao Capital Social.</div>", unsafe_allow_html=True)

    st.info("**Análise do Professor:** Note que embora a empresa tenha liquidez (CCL positivo), a estrutura de empréstimos no curto prazo é pesada, o que pode pressionar o caixa operacional em momentos de queda nas vendas.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. EXERCÍCIO INDIVIDUAL: CLASSIFICAÇÃO E INTERPRETAÇÃO ---
    st.subheader("3. Exercício Individual: Classificação e Lógica")
    
    with st.form("exercicio_individual_m4"):
        st.markdown("<div class='interpret-header'>Classificação de Contas</div>", unsafe_allow_html=True)
        
        c1 = st.selectbox("A conta 'Adiantamento a Fornecedores (entrega em 18 meses)' é:", 
                          ["Ativo Circulante", "Ativo Não Circulante (Realizável LP)", "Passivo Circulante", "Patrimônio Líquido"])
        
        c2 = st.selectbox("A conta 'Reserva de Lucros' pertence ao:", 
                          ["Passivo Circulante", "Passivo Não Circulante", "Patrimônio Líquido", "Ativo Intangível"])

        st.markdown("<div class='interpret-header'>Interpretação Econômica</div>", unsafe_allow_html=True)
        
        pergunta_desc = st.text_area("Se a empresa decidisse vender metade do seu Imobilizado para quitar empréstimos de Longo Prazo, o que aconteceria com o Índice de Liquidez Corrente?", 
                                     placeholder="Pense no impacto nas contas de curto prazo...")

        submit_btn = st.form_submit_button("Submeter para Avaliação")
        
        if submit_btn:
            # Validação simples
            erros = 0
            if c1 != "Ativo Não Circulante (Realizável LP)": erros += 1
            if c2 != "Patrimônio Líquido": erros += 1
            
            if erros == 0:
                st.balloons()
                st.success("Classificações perfeitas! Sua interpretação econômica foi registrada para debate em sala.")
                st.write("**Nota sobre sua resposta aberta:** Vender imobilizado (Não Circulante) para quitar dívida de Longo Prazo (Não Circulante) não altera a Liquidez Corrente diretamente, mas melhora a Solvência Geral. Excelente reflexão!")
            else:
                st.error(f"Você teve {erros} erro(s) de classificação. Revise o conceito de segregação por prazo (12 meses).")

if __name__ == "__main__":
    run()