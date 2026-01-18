import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 15.
    Foco: Estudo de Caso Integrado e Relatório Final de Análise.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .final-case-card {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            border-left: 10px solid #b45309;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }
        .section-header {
            color: #1e293b;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        .report-box {
            background-color: #f1f5f9;
            padding: 25px;
            border-radius: 12px;
            border: 2px solid #cbd5e1;
            font-family: 'Montserrat', sans-serif;
        }
        .kpi-badge {
            background-color: #1e293b;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.85rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo e Celebração
    st.markdown("<h1>🎓 Módulo 15: Estudo de Caso Integrado</h1>", unsafe_allow_html=True)
    st.balloons()
    st.write("""
    Parabéns por chegar até aqui! Este é o desafio final. Você agora possui o arsenal completo de um 
    analista financeiro. Utilize os dados integrados da **Indústria Ômega S.A.** para construir seu relatório final.
    """)

    st.divider()

    # --- 1. ESTUDO DE CASO COMPLETO (DADOS INTEGRADOS) ---
    st.subheader("1. O Caso: Indústria Ômega S.A. (Cenário de Turnaround)")
    
    with st.expander("📊 Clique para visualizar as Demonstrações Financeiras (Resumidas)", expanded=True):
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.markdown("**Balanço Patrimonial (R$ milhões)**")
            dados_bp = {
                "Contas": ["Ativo Circulante", "Estoques (Médio)", "Imobilizado Líquido", "Passivo Circulante", "Dívida Total", "Patrimônio Líquido"],
                "Ano Atual": [1200, 450, 2500, 950, 1800, 1900],
                "Ano Anterior": [1050, 380, 2300, 800, 1600, 1750]
            }
            st.table(pd.DataFrame(dados_bp))
            
        with col_t2:
            st.markdown("**Demonstração do Resultado (R$ milhões)**")
            dados_dre = {
                "Contas": ["Receita Líquida", "Lucro Bruto", "EBITDA", "EBIT (Operacional)", "Resultado Financeiro", "Lucro Líquido"],
                "Valor": [4200, 1450, 850, 620, -280, 220]
            }
            st.table(pd.DataFrame(dados_dre))
        
        st.info("**Informação Adicional:** O Fluxo de Caixa Operacional (FCO) do período foi de **R$ 180 milhões**.")

    # --- 2. LABORATÓRIO DE KPIs INTEGRADOS ---
    st.subheader("2. Consolidação de Indicadores (Métricas Finais)")
    st.write("Calcule ou verifique os drivers fundamentais antes de redigir o relatório:")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("ROE (Rentabilidade)", "11.6%", help="Lucro Líquido / PL Médio")
    with c2:
        st.metric("Liquidez Corrente", "1.26", help="AC / PC")
    with c3:
        st.metric("Dívida Líquida / EBITDA", "2.1x", help="Endividamento Controlado")
    with c4:
        st.metric("Qualidade do Lucro", "0.81", help="FCO / Lucro Líquido", delta="-0.19", delta_color="inverse")

    st.markdown("<div class='final-case-card'>", unsafe_allow_html=True)
    st.markdown("<p class='section-header'>Diagnóstico Pedagógico do Professor</p>", unsafe_allow_html=True)
    st.write("""
    A **Indústria Ômega** apresenta um cenário misto: a rentabilidade é positiva (ROE 11.6%), 
    mas a geração de caixa (Qualidade do Lucro 0.81) está abaixo do lucro contábil, indicando que o capital 
    pode estar ficando retido no aumento dos estoques. A estrutura de capital é saudável (2.1x EBITDA), 
    porém o custo da dívida consome quase 45% do resultado operacional (EBIT).
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- 3. RELATÓRIO FINAL DE ANÁLISE FINANCEIRA ---
    st.subheader("3. Relatório Final de Análise (Deliverable)")
    
    with st.form("form_relatorio_final"):
        st.markdown("<p class='section-header'>Parecer Técnico do Analista</p>", unsafe_allow_html=True)
        
        titulo_relatorio = st.text_input("Título do Relatório:", placeholder="Ex: Análise de Crédito e Desempenho - Ômega S.A.")
        
        col_rel1, col_rel2 = st.columns(2)
        with col_rel1:
            conclusao_liq = st.text_area("Análise de Liquidez e Solvência:", placeholder="Comente sobre a capacidade de pagamento...")
            conclusao_rent = st.text_area("Análise de Rentabilidade (DuPont):", placeholder="O que move o ROE desta empresa?")
        
        with col_rel2:
            conclusao_caixa = st.text_area("Análise de Qualidade do Lucro e Red Flags:", placeholder="O lucro é sustentável?")
            veredito = st.selectbox("Recomendação Final:", ["Aprovar Investimento / Crédito", "Manter em Observação (Monitorar Caixa)", "Reprovar / Risco Elevado"])

        st.markdown("---")
        st.write("**Discussão Coletiva:** Se este fosse um trabalho em grupo, quais indicadores causariam mais debate entre os sócios?")
        nota_debate = st.text_input("Nota de debate do grupo:")

        enviar_relatorio = st.form_submit_button("Submeter Relatório Final de Curso")

        if enviar_relatorio:
            if len(conclusao_liq) > 50 and len(conclusao_rent) > 50:
                st.success("🏁 RELATÓRIO FINAL SUBMETIDO COM SUCESSO!")
                st.markdown("""
                <div class='report_box'>
                    <h4>Feedback Estruturado do Professor:</h4>
                    <ul>
                        <li><b>Estrutura Técnica:</b> Demonstrou domínio dos índices de rentabilidade e liquidez.</li>
                        <li><b>Profundidade Analítica:</b> Correlacionou corretamente a DRE com a DFC.</li>
                        <li><b>Visão de Negócio:</b> Identificou que o risco não é a rentabilidade, mas o descasamento de caixa.</li>
                    </ul>
                    <p><i>Você está pronto para o mercado de análise financeira. Sucesso na carreira!</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("O relatório final deve ser detalhado (mínimo de 50 caracteres por seção).")

if __name__ == "__main__":
    run()