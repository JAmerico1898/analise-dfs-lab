import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 14.
    Foco: Tomada de Decisão (Crédito vs. Investimento).
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .decision-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #1e293b;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .role-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.4rem;
            margin-bottom: 10px;
        }
        .indicator-box {
            background-color: #f8fafc;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-align: center;
        }
        .highlight-navy {
            color: #1e293b;
            font-weight: bold;
        }
        .status-badge {
            background-color: #b45309;
            color: white;
            padding: 3px 12px;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 14: Análise para Tomada de Decisão</h1>", unsafe_allow_html=True)
    st.write("Chegou a hora de converter diagnóstico em ação. Nesta simulação, você assumirá um papel executivo e decidirá o futuro financeiro de uma organização.")

    st.divider()

    # --- 1. SIMULAÇÃO: O CENÁRIO DA "LOGÍSTICA GLOBAL S.A." ---
    st.subheader("1. Simulação: O Comitê de Decisão")
    st.markdown("""
    Analise os indicadores consolidados da **Logística Global S.A.** abaixo. A empresa solicita um novo empréstimo 
    e, ao mesmo tempo, busca atrair novos acionistas para um projeto de expansão.
    """)

    # Dados Consolidados para Decisão
    dados_kpi = {
        "Dimensão": ["Liquidez", "Endividamento", "Rentabilidade", "Qualidade"],
        "Indicador Chave": ["Liquidez Corrente", "Dívida Líquida / EBITDA", "ROE", "Fluxo de Caixa Op. / Lucro Líquido"],
        "Valor Atual": ["1.15", "3.9x", "24.5%", "0.55"],
        "Média Setor": ["1.60", "2.5x", "18.0%", "0.90"]
    }
    st.table(pd.DataFrame(dados_kpi))

    st.markdown("<div class='decision-card'>", unsafe_allow_html=True)
    st.markdown("<p class='role-header'>Escolha o seu Papel:</p>", unsafe_allow_html=True)
    
    papel = st.selectbox(
        "Como você deseja analisar este caso?",
        ["Selecione...", "🏦 Analista de Risco de Crédito (Banco)", "📈 Gestor de Fundo de Investimento (Equity)"]
    )
    
    if papel != "Selecione...":
        st.markdown(f"**Contexto do {papel}:**")
        if "Crédito" in papel:
            st.warning("Seu foco é a **Segurança**. Você quer saber se a empresa tem margem para pagar os juros e o principal, mesmo se o lucro cair.")
        else:
            st.info("Seu foco é o **Retorno**. Você busca crescimento e dividendos, mas está atento ao risco de insolvência que pode zerar seu capital.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. JUSTIFICATIVA ESCRITA E DECISÃO ---
    st.subheader("2. O Veredito Financeiro")
    
    if papel != "Selecione...":
        with st.form("form_decisao_m14"):
            st.markdown(f"<span class='status-badge'>DECISÃO PARA {papel.upper()}</span>", unsafe_allow_html=True)
            
            if "Crédito" in papel:
                decisao = st.radio("Sua decisão final sobre o empréstimo:", ["Aprovar", "Reprovar", "Aprovar com Garantias Extras"])
            else:
                decisao = st.radio("Sua decisão final sobre a compra de ações:", ["Comprar", "Manter", "Vender / Não Investir"])
            
            justificativa = st.text_area(
                "Justificativa Técnica (Mencione ao menos 2 indicadores da tabela):",
                placeholder="Ex: 'Reprovo o crédito devido à baixa liquidez (1.15) e à alavancagem perigosa (3.9x)...'"
            )
            
            submit_decisao = st.form_submit_button("Submeter Decisão ao Comitê")
            
            if submit_decisao:
                if len(justificativa) > 50:
                    st.balloons()
                    st.success("Decisão registrada com sucesso! Prepare sua defesa para a discussão em grupo.")
                    
                    # Feedback Pedagógico (Dica do Professor)
                    with st.expander("Clique para ver a 'Provocação' do Professor sobre este caso"):
                        st.write("""
                        **Ponto de Reflexão:** 
                        A Logística Global é um caso clássico de 'Rentabilidade vs. Risco'. 
                        O ROE de 24.5% é sedutor para o investidor, mas a qualidade do lucro (0.55) indica que o caixa não 
                        está acompanhando o resultado. Para o banco, a alavancagem de 3.9x está muito acima da média setorial (2.5x), 
                        o que torna o empréstimo altamente arriscado sem garantias reais sólidas.
                        """)
                else:
                    st.error("Sua justificativa está muito curta. Um analista precisa de argumentos robustos.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. DISCUSSÃO EM GRUPO: DEFESA DA DECISÃO ---
    st.subheader("3. Atividade de Sala: O Grande Debate")
    
    st.markdown("""
    <div class='decision-card' style='border-left: 5px solid #b45309;'>
        <p class='indicator-box'><strong>Dinâmica de Grupo:</strong></p>
        <ol>
            <li>Reúna-se com colegas que escolheram <strong>papéis opostos</strong> ao seu.</li>
            <li>Defenda sua decisão utilizando os indicadores de <strong>Qualidade do Lucro</strong> (Aula 13) e <strong>Modelo DuPont</strong> (Aula 11).</li>
            <li>Tentem chegar a um consenso: É possível a empresa ser um bom investimento, mas um péssimo risco de crédito ao mesmo tempo?</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("A ata da discussão e o consenso do grupo devem ser entregues via portal ao final desta aula.")

if __name__ == "__main__":
    run()