import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 5.
    Foco: Análise da Demonstração do Resultado (DRE).
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .performance-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #b45309;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .metric-label {
            color: #1e293b;
            font-weight: bold;
            font-size: 1rem;
        }
        .interpret-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 15px;
        }
        .warning-box {
            background-color: #fffbeb;
            color: #92400e;
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #f59e0b;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 05: Análise da Demonstração do Resultado (DRE)</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, exploramos a eficiência econômica da empresa. Vamos além do lucro líquido para entender como as margens revelam a qualidade da operação.")

    st.divider()

    # --- 1. EXERCÍCIO PRÁTICO: CÁLCULO E INTERPRETAÇÃO DE MARGENS ---
    st.subheader("1. Simulador de Margens: Estrutura da DRE")
    st.write("Ajuste os valores abaixo para observar como a eficiência operacional impacta as margens bruta e líquida.")

    with st.container():
        col_inp1, col_inp2, col_inp3 = st.columns(3)
        
        with col_inp1:
            receita = st.number_input("Receita Líquida (R$)", min_value=1000, value=100000, step=5000)
        with col_inp2:
            cpv = st.number_input("Custo Prod. Vendidos - CPV (R$)", min_value=0, value=60000, step=5000)
        with col_inp3:
            despesas = st.number_input("Despesas Operacionais (R$)", min_value=0, value=25000, step=2000)

        # Cálculos
        lucro_bruto = receita - cpv
        margem_bruta = (lucro_bruto / receita) * 100 if receita > 0 else 0
        
        ebit = lucro_bruto - despesas
        margem_operacional = (ebit / receita) * 100 if receita > 0 else 0

        st.markdown("<br>", unsafe_allow_html=True)
        
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("Margem Bruta", f"{margem_bruta:.1f}%", help="Revela a eficiência da produção/compra antes das despesas fixas.")
        with res_col2:
            st.metric("Margem Operacional", f"{margem_operacional:.1f}%", help="Mede a eficiência da gestão e controle de despesas administrativas/vendas.")

    with st.expander("Análise Pedagógica das Margens"):
        if margem_bruta < 30:
            st.warning("A Margem Bruta está baixa. Verifique se os custos de produção estão subindo ou se a empresa perdeu poder de precificação.")
        else:
            st.success("A Margem Bruta está saudável, indicando uma boa vantagem competitiva no produto.")
        
        if (margem_bruta - margem_operacional) > 25:
            st.error("Alerta: Há um 'degrau' muito grande entre a margem bruta e a operacional. As despesas de estrutura podem estar corroendo o lucro.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. ESTUDO DE CASO: EMPRESA COM LUCRO CRESCENTE E MARGEM DECRESCENTE ---
    st.subheader("2. Estudo de Caso: O Paradoxo da 'Tech-Varejo'")
    st.markdown("""
    Analise os dados comparativos da **Tech-Varejo S.A.** abaixo. A empresa comemora um aumento no lucro líquido, mas será que a saúde econômica melhorou?
    """)

    dados_caso = {
        "Indicador": ["Receita Líquida", "Lucro Líquido", "Margem Líquida %"],
        "Ano Anterior (R$)": [1000000, 100000, 10.0],
        "Ano Atual (R$)": [1800000, 126000, 7.0]
    }
    df_caso = pd.DataFrame(dados_caso)
    st.table(df_caso)

    st.markdown("<div class='interpret-header'>Desafio do Analista</div>", unsafe_allow_html=True)
    
    escolha_caso = st.radio(
        "Como você interpreta esse cenário?",
        [
            "A empresa está melhor, pois o lucro absoluto cresceu 26%.",
            "A empresa está em declínio de eficiência, pois a margem caiu de 10% para 7%.",
            "O crescimento de 80% na receita não foi acompanhado pela eficiência nos custos/despesas."
        ]
    )

    if st.button("Validar Diagnóstico"):
        if "eficiência" in escolha_caso.lower() or "acompanhado" in escolha_caso.lower():
            st.success("Exato! Embora o lucro absoluto tenha subido, a queda na margem indica que para vender muito mais, a empresa teve que sacrificar rentabilidade de forma desproporcional. Isso pode ser um sinal de 'guerra de preços' ou descontrole de custos.")
        else:
            st.warning("Cuidado: Lucro absoluto pode ser vaidade. Analistas focam na rentabilidade relativa (margem).")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. DISCUSSÃO: LUCRO CONTÁBIL VS. DESEMPENHO ECONÔMICO ---
    st.subheader("3. Painel de Debate: Lucro vs. Realidade")
    
    st.markdown("""
    <div class='warning-box'>
        <strong>Provocação:</strong> Uma empresa pode reportar lucro contábil e estar destruindo valor econômico?
    </div>
    """, unsafe_allow_html=True)

    with st.form("debate_m5"):
        topico = st.selectbox("Escolha um tópico para debater:", 
                                ["EBITDA vs. Lucro Líquido", 
                                 "Resultados Não Recorrentes (Venda de Ativos)", 
                                 "Impacto da Inflação nos Custos"])
        
        contribuicao = st.text_area("Sua análise sobre como este tópico afeta a interpretação da DRE:", 
                                    placeholder="Ex: 'Um lucro gerado pela venda da sede da empresa não reflete a operação...'")

        submit_debate = st.form_submit_button("Registrar Contribuição")
        
        if submit_debate:
            if len(contribuicao) > 15:
                st.balloons()
                st.success("Sua contribuição foi registrada! Lembre-se: O lucro operacional (EBITDA) costuma ser mais fiel ao desempenho do 'core business' do que o lucro líquido final.")
            else:
                st.error("Por favor, desenvolva mais seu raciocínio antes de submeter.")

if __name__ == "__main__":
    run()