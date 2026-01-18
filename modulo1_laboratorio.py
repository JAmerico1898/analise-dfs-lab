import streamlit as st

def run():
    """
    Função principal do Módulo 1.
    Executada dinamicamente pelo Hub Central.
    """
    
    # Estilização CSS local para manter o padrão "Boutique Académica"
    st.markdown("""
        <style>
        .card-discussao {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #b45309;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            min-height: 180px;
        }
        .user-tag {
            color: #b45309;
            font-weight: 700;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            display: block;
        }
        .decision-highlight {
            color: #1e293b;
            font-weight: 600;
            font-style: italic;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 01: Introdução à Análise Financeira</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, exploramos o papel da contabilidade como sistema de informação e os diferentes utilizadores das demonstrações.")

    st.divider()

    # --- 1. DISCUSSÃO ORIENTADA ---
    st.subheader("1. Discussão Orientada")
    st.markdown("**Provocação:** Como é que um investidor, um banco e um gestor tomam decisões a partir das mesmas demonstrações?")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="card-discussao">
                <span class="user-tag">📈 Investidor</span>
                <p class="decision-highlight">"Vale a pena comprar esta ação?"</p>
                <p><small>Foco: Rentabilidade (ROE), potencial de dividendos e crescimento futuro do valor da empresa.</small></p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="card-discussao">
                <span class="user-tag">🏦 Banco</span>
                <p class="decision-highlight">"Eles vão conseguir pagar o empréstimo?"</p>
                <p><small>Foco: Liquidez de curto prazo, garantias reais e risco de incumprimento ou insolvência.</small></p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="card-discussao">
                <span class="user-tag">👔 Gestor</span>
                <p class="decision-highlight">"Onde podemos ser mais eficientes?"</p>
                <p><small>Foco: Eficiência operacional, margens de lucro por produto e controlo rigoroso de custos.</small></p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. EXERCÍCIO DIAGNÓSTICO ---
    st.subheader("2. Exercício Diagnóstico")
    st.info("Classifique as decisões abaixo conforme o utilizador da informação predominante (não avaliativo).")

    cenarios = [
        {
            "pergunta": "Avaliar se a empresa tem ativos suficientes para dar como garantia num financiamento de 10 anos.",
            "opcoes": ["Investidor", "Banco", "Gestor"],
            "correta": "Banco",
            "feedback": "Exato! O banco (credor) foca na solvência e nas garantias para mitigar o risco do empréstimo."
        },
        {
            "pergunta": "Decidir se o preço de venda deve ser aumentado para recuperar a margem bruta que caiu no último trimestre.",
            "opcoes": ["Investidor", "Banco", "Gestor"],
            "correta": "Gestor",
            "feedback": "Correto! O gestor utiliza a contabilidade para decisões operacionais internas e correção de rotas."
        },
        {
            "pergunta": "Analisar se o lucro líquido gerado justifica o risco de manter o capital aplicado nesta empresa em vez de no Tesouro.",
            "opcoes": ["Investidor", "Banco", "Gestor"],
            "correta": "Investidor",
            "feedback": "Muito bem! O investidor foca no custo de oportunidade e no retorno sobre o capital próprio (ROE)."
        }
    ]

    for i, c in enumerate(cenarios):
        with st.expander(f"Cenário {i+1}: {c['pergunta']}"):
            resp = st.radio("Selecione o utilizador:", c["opcoes"], key=f"ex_diag_{i}")
            if st.button("Validar Cenário", key=f"btn_ex_{i}"):
                if resp == c["correta"]:
                    st.success(c["feedback"])
                else:
                    st.error("Resposta incorreta. Analise o objetivo principal da decisão.")

    st.divider()

    # --- 3. MINI-QUIZ DE FIXAÇÃO ---
    st.subheader("3. Mini-Quiz de Fixação")
    st.write("Teste os seus conhecimentos sobre os conceitos base da Aula 1.")

    questoes = [
        {
            "pergunta": "1. Qual a principal característica da Contabilidade Financeira?",
            "opcoes": [
                "É voltada para utilizadores internos e não segue padrões fixos.",
                "Foca em utilizadores externos e segue normas padronizadas (IFRS/CPC).",
                "Serve apenas para calcular o bónus dos diretores.",
                "Não utiliza o regime de competência."
            ],
            "correta": 1
        },
        {
            "pergunta": "2. Por que razão a subjetividade é uma limitação da informação contábil?",
            "opcoes": [
                "Porque os números são inventados mensalmente.",
                "Porque o uso de estimativas (ex: vida útil) depende do julgamento profissional.",
                "Porque a contabilidade não utiliza matemática.",
                "Porque os impostos mudam todos os dias."
            ],
            "correta": 1
        },
        {
            "pergunta": "3. O Regime de Competência dita que uma despesa deve ser registada:",
            "opcoes": [
                "Apenas quando o dinheiro sai da conta bancária.",
                "Quando o facto económico ocorre, independentemente do pagamento.",
                "Somente se houver lucro no final do ano.",
                "Quando o fornecedor envia um brinde."
            ],
            "correta": 1
        },
        {
            "pergunta": "4. Um lucro crescente acompanhado de um caixa operacional negativo persistente é:",
            "opcoes": [
                "Um excelente indicador de eficiência.",
                "Uma 'Red Flag' (sinal de alerta) sobre a qualidade do lucro.",
                "Impossível de acontecer na contabilidade real.",
                "O objetivo de todo o gestor financeiro."
            ],
            "correta": 1
        },
        {
            "pergunta": "5. O utilizador que foca primordialmente na 'Liquidez' e 'Solvência' é:",
            "opcoes": [
                "O Analista de Marketing.",
                "O Banco ou Credor Financeiro.",
                "O Cliente do retalho.",
                "O Estagiário de RH."
            ],
            "correta": 1
        }
    ]

    score = 0
    with st.form("quiz_fixacao_m1"):
        for i, q in enumerate(questoes):
            escolha = st.radio(q["pergunta"], q["opcoes"], key=f"q_quiz_{i}")
            if escolha == q["opcoes"][q["correta"]]:
                score += 1
        
        finalizar = st.form_submit_button("Submeter Quiz")
        if finalizar:
            st.metric("Pontuação Final", f"{score} / {len(questoes)}")
            if score == len(questoes):
                st.balloons()
                st.success("Excelente! Domina os conceitos básicos da análise financeira.")
            elif score >= 3:
                st.info("Bom trabalho! Mas reveja os pontos onde teve dúvidas.")
            else:
                st.warning("Recomendamos rever os slides da Aula 1 antes de avançar.")

if __name__ == "__main__":
    # Permite a execução isolada para testes
    run()