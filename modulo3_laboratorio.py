import streamlit as st

def run():
    """
    Função principal do Módulo 3.
    Foco: Princípios Contábeis e Qualidade da Informação.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .case-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #b45309;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .reflective-box {
            background-color: #1e293b;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border-right: 5px solid #b45309;
            margin: 20px 0;
        }
        .debate-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 03: Princípios e Qualidade da Informação</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, desafiamos a objetividade dos números e exploramos como as escolhas contábeis moldam a percepção da realidade financeira.")

    st.divider()

    # --- 1. ESTUDO DE CASO CURTO: O IMPACTO DA DEPRECIAÇÃO ---
    st.subheader("1. Estudo de Caso: O Peso das Estimativas")
    st.markdown("""
    Imagine uma empresa que adquiriu uma máquina por **R$ 100.000**. Ela precisa decidir a vida útil estimada 
    para fins de depreciação. Veja como essa decisão "subjetiva" altera o lucro reportado.
    """)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("<div class='case-card'>", unsafe_allow_html=True)
        st.write("🔧 **Configuração da Estimativa**")
        vida_util = st.slider("Vida útil estimada (anos):", 2, 20, 5)
        valor_residual = st.number_input("Valor residual estimado (R$):", 0, 50000, 10000, step=1000)
        
        depreciacao_anual = (100000 - valor_residual) / vida_util
        st.markdown(f"**Depreciação Anual:** R$ {depreciacao_anual:,.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.write("📊 **Impacto no Resultado (DRE)**")
        lucro_antes_dep = 50000
        lucro_liquido = lucro_antes_dep - depreciacao_anual
        margem_liquida = (lucro_liquido / 200000) * 100 # Assumindo receita de 200k
        
        st.metric("Lucro Líquido Estimado", f"R$ {lucro_liquido:,.2f}", delta=f"{-depreciacao_anual:,.2f} de gasto não-caixa")
        st.progress(max(0, min(100, int(margem_liquida))))
        st.caption(f"Margem Líquida estimada sobre receita de R$ 200k: {margem_liquida:.1f}%")

    st.info("**Reflexão:** A máquina é a mesma, o trabalho é o mesmo, mas o lucro muda apenas com uma canetada sobre o tempo estimado de uso.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. EXERCÍCIO REFLEXIVO ---
    st.subheader("2. Exercício Reflexivo: Verdade vs. Utilidade")
    
    st.markdown("""
    <div class='reflective-box'>
        <p style='font-size: 1.2rem; font-style: italic; text-align: center;'>
            “O lucro pode ser tecnicamente verdadeiro (dentro das normas) e, ainda assim, ser enganoso para um investidor?”
        </p>
    </div>
    """, unsafe_allow_html=True)

    reflexao_user = st.text_area("Com base no que discutimos sobre 'Qualidade do Lucro', escreva sua percepção:", 
                                  placeholder="Considere itens como resultados não recorrentes ou manobras de competência...")

    if st.button("Validar Reflexão"):
        if len(reflexao_user) > 20:
            st.success("Excelente análise! Lembre-se: o lucro é uma 'opinião' baseada em normas, enquanto o caixa é um fato. Lucros inflados por reversões de provisões ou estimativas agressivas de vida útil são 'verdadeiros' contábilmente, mas perigosos para projeções futuras.")
        else:
            st.warning("Desenvolva um pouco mais sua resposta. Pense no conflito entre o Regime de Competência e a Geração de Caixa.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. QUESTÕES DISCURSIVAS PARA DEBATE ---
    st.subheader("3. Painel de Debate: Sala de Aula")
    st.write("Utilize os tópicos abaixo para orientar a discussão com seus colegas:")

    with st.form("debate_form"):
        st.markdown("<div class='debate-header'>Tópico A: Conservadorismo</div>", unsafe_allow_html=True)
        st.write("Até que ponto o princípio da prudência (conservadorismo) ajuda ou atrapalha a fidedignidade da informação para um investidor otimista?")
        
        st.markdown("<div class='debate-header'>Tópico B: Comparabilidade</div>", unsafe_allow_html=True)
        st.write("Se duas empresas do mesmo setor usam métodos de depreciação opostos, como o analista deve proceder para compará-las de forma justa?")
        
        st.markdown("<div class='debate-header'>Tópico C: Competência vs. Caixa</div>", unsafe_allow_html=True)
        st.write("Qual informação é mais 'nobre' para avaliar a sobrevivência de uma startup: o lucro contábil ou o fluxo de caixa operacional?")

        debate_notes = st.text_input("Anotações do grupo para entrega:", placeholder="Resuma aqui os principais pontos levantados pelo grupo...")
        
        submit_debate = st.form_submit_button("Registrar Participação no Debate")
        
        if submit_debate:
            if debate_notes:
                st.balloons()
                st.success("Participação registrada! Estes pontos serão essenciais para nossa revisão de prova.")
            else:
                st.error("Por favor, insira um resumo das conclusões do grupo antes de enviar.")

if __name__ == "__main__":
    run()