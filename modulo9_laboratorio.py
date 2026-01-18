import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 9.
    Foco: Endividamento, Alavancagem e Estrutura de Capital.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .leverage-card {
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
        .formula-box {
            background-color: #f8fafc;
            padding: 15px;
            border-radius: 8px;
            border: 1px dashed #1e293b;
            text-align: center;
            font-family: 'Merriweather', serif;
            margin: 15px 0;
        }
        .debate-box {
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
    st.markdown("<h1>Módulo 09: Endividamento e Estrutura de Capital</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, exploramos como a dívida impacta a rentabilidade do acionista e qual o limite saudável para a alavancagem financeira.")

    st.divider()

    # --- 1. EXERCÍCIO PRÁTICO: CÁLCULO DE ALAVANCAGEM ---
    st.subheader("1. Simulador de Alavancagem Financeira")
    st.markdown("""
    A alavancagem ocorre quando o retorno sobre o capital total (ROA) é maior que o custo da dívida. 
    Ajuste os parâmetros abaixo para ver o **Efeito Alavanca** no ROE.
    """)

    with st.container():
        col_inp1, col_inp2 = st.columns(2)
        with col_inp1:
            ativo_total = st.number_input("Ativo Total (R$):", min_value=1000, value=100000, step=10000)
            patrimonio_liquido = st.slider("Patrimônio Líquido (R$):", 10000, int(ativo_total), 60000)
            divida_total = ativo_total - patrimonio_liquido
            st.caption(f"Dívida Calculada: R$ {divida_total:,.2f}")
            
        with col_inp2:
            lucro_operacional = st.number_input("EBIT (Lucro Operacional R$):", min_value=0, value=15000, step=1000)
            taxa_juros = st.slider("Taxa de Juros da Dívida (% a.a.):", 0.0, 30.0, 10.0) / 100

        # Cálculos
        despesa_financeira = divida_total * taxa_juros
        lucro_antes_ir = lucro_operacional - despesa_financeira
        
        # Simplificando sem IR para foco didático na alavancagem
        roa = (lucro_operacional / ativo_total) * 100
        roe = (lucro_antes_ir / patrimonio_liquido) * 100 if patrimonio_liquido > 0 else 0
        gaf = roe / roa if roa > 0 else 0

        st.markdown("<br>", unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric("ROA (Retorno Ativo)", f"{roa:.1f}%", help="EBIT / Ativo Total")
        with m_col2:
            st.metric("ROE (Retorno Acionista)", f"{roe:.1f}%", help="Lucro Líquido / PL")
        with m_col3:
            status_gaf = "Positiva" if gaf > 1 else "Negativa"
            st.metric("Grau de Alavancagem (GAF)", f"{gaf:.2f}", delta=status_gaf, delta_color="normal" if gaf > 1 else "inverse")

    with st.expander("Ver Explicação Técnica"):
        if gaf > 1:
            st.success(f"**Alavancagem Favorável:** O retorno gerado pelos ativos ({roa:.1f}%) é maior que o custo da dívida ({taxa_juros*100:.1f}%). A dívida está TRABALHANDO para o acionista.")
        else:
            st.error(f"**Alavancagem Desfavorável:** O custo da dívida ({taxa_juros*100:.1f}%) está consumindo a rentabilidade operacional. O acionista estaria melhor se a empresa não tivesse dívidas.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. ESTUDO DE CASO: EMPRESA ALFA (LUCRO VS. DÍVIDA) ---
    st.subheader("2. Estudo de Caso: O Risco da 'Siderúrgica Forte'")
    st.markdown("""
    Analise os indicadores da **Siderúrgica Forte S.A.**, uma empresa com margens excelentes, mas um endividamento pesado.
    """)

    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        st.metric("Margem EBITDA", "35%", delta="Alta Eficiência")
    with col_c2:
        st.metric("Dívida Líquida / EBITDA", "4.5x", delta="Risco Alto", delta_color="inverse")
    with col_c3:
        st.metric("Índice de Cobertura de Juros", "1.2x", delta="Margem Curta", delta_color="inverse")

    st.markdown("""
    <div class='leverage-card'>
        <p><strong>Diagnóstico:</strong> A empresa gera muito caixa operacional (EBITDA), mas gasta quase tudo para pagar os juros da dívida. 
        Uma queda de 10% nas vendas pode tornar a empresa incapaz de honrar seus compromissos financeiros.</p>
    </div>
    """, unsafe_allow_html=True)

    pergunta_caso = st.radio(
        "Qual a recomendação estratégica mais prudente para a Siderúrgica Forte?",
        [
            "Aumentar o endividamento para aproveitar a margem alta e crescer.",
            "Realizar um aumento de capital (Follow-on) para reduzir a dívida e os juros.",
            "Manter a estrutura atual, pois o ROE é de 25%."
        ]
    )

    if st.button("Validar Diagnóstico"):
        if "aumento de capital" in pergunta_caso.lower():
            st.balloons()
            st.success("Correto! Com uma cobertura de juros tão baixa (1.2x), a empresa está vulnerável. Trocar dívida por capital próprio (desalavancagem) reduz o risco financeiro e garante a sobrevivência em ciclos de baixa.")
        else:
            st.error("Resposta Arriscada! O retorno alto (ROE) não justifica o risco de insolvência iminente.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. DEBATE ORIENTADO: QUANDO A DÍVIDA É POSITIVA? ---
    st.subheader("3. Debate Orientado: A Dívida como Ferramenta")
    
    st.markdown("""
    <div class='debate-box'>
        <p style='font-style: italic; text-align: center; font-size: 1.1rem;'>
            “O endividamento é o combustível do capitalismo. Sem ele, o crescimento seria lento demais. O problema não é a dívida, mas o custo e o prazo.”
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_debate_m9"):
        st.write("Reflita e responda para debate em sala:")
        pergunta_debate = st.text_area("Em quais condições específicas você considera que uma empresa DEVE se endividar, mesmo já tendo capital próprio disponível?",
                                       placeholder="Pense em benefícios fiscais, expansão acelerada e custo de oportunidade...")
        
        submit_debate = st.form_submit_button("Enviar para Discussão")
        
        if submit_debate:
            if len(pergunta_debate) > 20:
                st.info("""
                **Pontos para nossa discussão em sala:**
                1. **Benefício Fiscal:** Os juros da dívida reduzem o lucro tributável (Economia de IR).
                2. **ROE:** Quando o custo da dívida < ROA, o retorno do acionista é turbinado.
                3. **Custo de Oportunidade:** Preservar o caixa para projetos mais rentáveis no futuro.
                """)
                st.success("Sua reflexão foi registrada!")
            else:
                st.warning("Por favor, elabore mais sua resposta antes de submeter.")

if __name__ == "__main__":
    run()