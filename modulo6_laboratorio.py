import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 7.
    Foco: Análise Horizontal e Vertical (AV/AH).
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .analysis-card {
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
            font-size: 1.1rem;
            margin-top: 20px;
        }
        .highlight-text {
            color: #b45309;
            font-weight: bold;
        }
        .stTable {
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 07: Análise Horizontal e Vertical</h1>", unsafe_allow_html=True)
    st.write("Nesta etapa, transformamos valores absolutos em percentuais para identificar tendências de crescimento e mudanças na estrutura de gastos da empresa.")

    st.divider()

    # --- 1. APLICAÇÃO PRÁTICA EM DADOS REAIS (DRE COMPARATIVA) ---
    st.subheader("1. Laboratório de Dados: DRE Comparativa")
    st.markdown("""
    Analise a Demonstração de Resultado da **Varejo Total S.A.** para os anos de 2023 e 2024. 
    Sua missão é calcular os indicadores de estrutura (AV) e crescimento (AH).
    """)

    # Dados Fictícios Realistas
    data = {
        "Conta": ["Receita Líquida", "Custo das Vendas (CPV)", "Lucro Bruto", "Despesas Operacionais", "EBIT", "Resultado Financeiro", "Lucro Líquido"],
        "2023 (R$)": [500000, 300000, 200000, 120000, 80000, -10000, 70000],
        "2024 (R$)": [650000, 420000, 230000, 130000, 100000, -15000, 85000]
    }
    df = pd.DataFrame(data)

    st.write("**Dados Brutos da Empresa (Extraídos do Sistema):**")
    st.table(df.style.format({"2023 (R$)": "{:,.0f}", "2024 (R$)": "{:,.0f}"}))

    # --- 2. COMPARAÇÃO E PROCESSAMENTO ---
    st.markdown("<div class='metric-header'>Ferramenta de Processamento Financeiro</div>", unsafe_allow_html=True)
    
    if st.button("Gerar Análise Vertical (AV) e Horizontal (AH)"):
        # Cálculos AV (Base: Receita Líquida)
        df["AV 2023 (%)"] = (df["2023 (R$)"] / df.iloc[0, 1]) * 100
        df["AV 2024 (%)"] = (df["2024 (R$)"] / df.iloc[0, 2]) * 100
        
        # Cálculo AH (Ano Atual / Ano Anterior - 1)
        df["AH 24/23 (%)"] = ((df["2024 (R$)"] / df["2023 (R$)"]) - 1) * 100

        # Exibição da Tabela Processada
        st.success("Análise processada com sucesso!")
        st.dataframe(
            df.style.format({
                "2023 (R$)": "{:,.0f}", 
                "2024 (R$)": "{:,.0f}",
                "AV 2023 (%)": "{:.1f}%",
                "AV 2024 (%)": "{:.1f}%",
                "AH 24/23 (%)": "{:+.1f}%"
            }),
            use_container_width=True
        )

        # Insights Automáticos para o Aluno
        st.markdown("<div class='analysis-card'>", unsafe_allow_html=True)
        st.markdown("🔍 **Principais Achados Estruturais:**")
        st.write(f"- A Receita cresceu <span class='highlight-text'>{df.iloc[0, 5]:.1f}%</span> na Análise Horizontal.", unsafe_allow_html=True)
        st.write(f"- O Custo (CPV) subiu de {df.iloc[1, 3]:.1f}% para <span class='highlight-text'>{df.iloc[1, 4]:.1f}%</span> da receita (AV), indicando perda de margem bruta.", unsafe_allow_html=True)
        st.write("- As despesas operacionais foram diluídas, caindo de 24% para 20% na Análise Vertical.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. INTERPRETAÇÃO ESCRITA (ATIVIDADE AVALIATIVA) ---
    st.subheader("3. Relatório de Interpretação")
    st.info("Com base nos dados processados acima, redija sua conclusão técnica sobre o desempenho da empresa.")

    with st.form("interpretacao_m7"):
        pergunta_1 = st.text_area("1. O crescimento do Lucro Líquido (AH) acompanhou o crescimento da Receita? Explique o porquê.", 
                                  placeholder="Dica: Compare a AH da Receita com a AH do Lucro...")
        
        pergunta_2 = st.text_area("2. Qual conta da DRE apresentou a variação mais preocupante na Análise Vertical?",
                                  placeholder="Considere se os custos ou despesas estão 'comendo' uma fatia maior do bolo...")

        st.markdown("<div class='metric-header'>Checklist de Qualidade da Análise</div>", unsafe_allow_html=True)
        check_1 = st.checkbox("Mencionei a variação da Margem Bruta (AV do CPV).")
        check_2 = st.checkbox("Citei a diluição de despesas fixas.")
        check_3 = st.checkbox("Analisei o impacto do resultado financeiro.")

        submit_relatorio = st.form_submit_button("Submeter Relatório para o Professor")

        if submit_relatorio:
            if len(pergunta_1) > 20 and len(pergunta_2) > 20:
                st.balloons()
                st.success("Relatório enviado com sucesso! Sua capacidade analítica está evoluindo.")
                
                # Feedback Pedagógico Gabarito
                with st.expander("Clique para ver o comentário do Professor sobre este caso"):
                    st.write("""
                    **Gabarito Sugerido:** 
                    Embora a receita tenha crescido 30%, o Lucro Líquido cresceu apenas 21.4%. 
                    O principal motivo foi o aumento do CPV na Análise Vertical (subiu de 60% para 64.6%), o que indica que a empresa 
                    pode estar enfrentando inflação de insumos ou dificuldade de repasse de preços. 
                    Por outro lado, houve eficiência administrativa, já que as despesas operacionais pesaram menos na estrutura final.
                    """)
            else:
                st.error("Por favor, preencha as análises com mais profundidade antes de enviar.")

if __name__ == "__main__":
    run()