import streamlit as st

def run():
    """
    Função principal do Módulo 2.
    Foco: Estrutura e Lógica das Demonstrações Financeiras.
    """
    
    # Estilização CSS local para consistência visual
    st.markdown("""
        <style>
        .logic-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #1e293b;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .equation-highlight {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-size: 1.5rem;
            text-align: center;
            font-weight: bold;
            margin: 20px 0;
        }
        .connection-tag {
            background-color: #f1f5f9;
            color: #b45309;
            padding: 4px 10px;
            border-radius: 5px;
            font-weight: bold;
            font-size: 0.8rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 02: Estrutura e Lógica das Demonstrações</h1>", unsafe_allow_html=True)
    st.write("Nesta etapa, vamos entender a mecânica por trás dos números e como as demonstrações financeiras conversam entre si.")

    st.divider()

    # --- 1. EXERCÍCIO GUIADO: MAPEAMENTO DE EVENTOS ---
    st.subheader("1. Exercício Guiado: O Caminho do Fato Econômico")
    st.markdown("""
    Analise os eventos abaixo e selecione o impacto correto nas contas do **Balanço Patrimonial (BP)** 
    e da **Demonstração do Resultado (DRE)**.
    """)

    with st.expander("Evento A: Venda de mercadoria a prazo por R$ 1.000 (Custo: R$ 600)"):
        impacto_a = st.selectbox("Qual o impacto combinado?", [
            "Selecione...",
            "Aumento no Ativo (Clientes) e Aumento no PL (Lucro) apenas.",
            "Aumento no Ativo (Clientes), Redução no Ativo (Estoques) e Aumento no PL (Lucro via DRE).",
            "Aumento no Passivo (Fornecedores) e Redução no PL."
        ], key="ev_a")
        
        if st.button("Mapear Evento A"):
            if "Redução no Ativo (Estoques)" in impacto_a:
                st.success("Perfeito! Você captou a essência: a venda a prazo cria um direito (Ativo), retira a mercadoria (estoque) e a diferença gera lucro, que flui para o Patrimônio Líquido.")
            else:
                st.error("Tente novamente. Lembre-se que o estoque precisa sair do balanço para que o custo seja reconhecido.")

    with st.expander("Evento B: Captação de Empréstimo Bancário de R$ 50.000"):
        impacto_b = st.selectbox("Como as contas se movimentam?", [
            "Selecione...",
            "Aumento do Ativo (Caixa) e Aumento do Passivo (Empréstimos).",
            "Aumento do Ativo (Caixa) e Aumento da Receita na DRE.",
            "Aumento do Passivo e Redução do Patrimônio Líquido."
        ], key="ev_b")
        
        if st.button("Mapear Evento B"):
            if "Aumento do Passivo" in impacto_b and "Ativo (Caixa)" in impacto_b:
                st.success("Correto! Empréstimos não são receitas (DRE), são origens de recursos de terceiros que aumentam o Passivo e o Disponível.")
            else:
                st.error("Cuidado: Empréstimo não é lucro! É uma obrigação.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. ATIVIDADE EM DUPLA: INTERCONECTIVIDADE ---
    st.subheader("2. Atividade: Onde está o número?")
    st.info("Trabalhe com sua dupla: Identifiquem onde um mesmo fato aparece em demonstrações diferentes.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="logic-card">
            <span class="connection-tag">CONEXÃO 1</span>
            <h4>O Lucro Líquido do Exercício</h4>
            <p>Aparece como a linha final da <b>DRE</b> e flui diretamente para...</p>
        </div>
        """, unsafe_allow_html=True)
        resp_con1 = st.text_input("Destino no Balanço Patrimonial:", placeholder="Ex: Reservas de Lucro no PL")
        
    with col2:
        st.markdown("""
        <div class="logic-card">
            <span class="connection-tag">CONEXÃO 2</span>
            <h4>O Saldo Final de Caixa</h4>
            <p>É o resultado da <b>DFC</b> (Demonstração dos Fluxos de Caixa) e deve ser igual ao...</p>
        </div>
        """, unsafe_allow_html=True)
        resp_con2 = st.text_input("Conta correspondente no Ativo:", placeholder="Ex: Conta Caixa/Bancos")

    if st.button("Validar Conexões"):
        if "pl" in resp_con1.lower() or "lucro" in resp_con1.lower():
            st.write("✅ Conexão 1: Correta! O lucro é o elo entre o desempenho (DRE) e a riqueza dos sócios (PL).")
        if "caixa" in resp_con2.lower() or "banco" in resp_con2.lower() or "disponível" in resp_con2.lower():
            st.write("✅ Conexão 2: Correta! A DFC detalha a variação da conta Caixa que está no Ativo Circulante.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. LISTA ESTRUTURAL (ENTREGÁVEL) ---
    st.subheader("3. Quiz Estrutural: A Lógica Econômica")
    st.write("Responda às questões abaixo para gerar seu relatório de progresso.")

    with st.form("quiz_m2"):
        st.markdown("<div class='equation-highlight'>A = P + PL</div>", unsafe_allow_html=True)
        
        q1 = st.radio(
            "1. Se uma empresa compra uma máquina à vista, o que acontece com o Ativo Total?",
            ["O Ativo Total aumenta.", "O Ativo Total diminui.", "O Ativo Total permanece o mesmo (Permutação).", "O Passivo aumenta."]
        )
        
        q2 = st.radio(
            "2. Qual demonstração financeira explica a variação da riqueza líquida dos sócios entre dois períodos?",
            ["DRE (Resultado)", "DMPL (Mutações do PL)", "DFC (Fluxo de Caixa)", "Notas Explicativas"]
        )
        
        q3 = st.radio(
            "3. O pagamento de um dividendo aos sócios impacta quais demonstrações?",
            ["Apenas a DRE.", "Apenas o Balanço Patrimonial.", "O Balanço Patrimonial (reduz caixa e PL) e a DFC (saída financeira).", "Não impacta as demonstrações."]
        )

        q4 = st.radio(
            "4. A depreciação é uma despesa na DRE que não consome caixa. Onde ela é ajustada na DFC?",
            ["No Fluxo de Investimento.", "No Fluxo de Financiamento.", "No Fluxo Operacional (Método Indireto).", "Ela não aparece na DFC."]
        )

        q5 = st.radio(
            "5. Se o Passivo é maior que o Ativo, dizemos que a empresa possui:",
            ["Lucro acumulado alto.", "Passivo a Descoberto (Patrimônio Líquido Negativo).", "Excesso de liquidez.", "Ativo Imobilizado."]
        )

        submit_btn = st.form_submit_button("Submeter Respostas para o Professor")
        
        if submit_btn:
            # Gabarito: 2, 1, 2, 2, 1 (índices)
            score = 0
            if q1 == "O Ativo Total permanece o mesmo (Permutação).": score += 1
            if q2 == "DMPL (Mutações do PL)": score += 1
            if q3 == "O Balanço Patrimonial (reduz caixa e PL) e a DFC (saída financeira).": score += 1
            if q4 == "No Fluxo Operacional (Método Indireto).": score += 1
            if q5 == "Passivo a Descoberto (Patrimônio Líquido Negativo).": score += 1
            
            st.metric("Desempenho", f"{score}/5")
            if score >= 4:
                st.balloons()
                st.success("Excelente! Você compreende a estrutura e a lógica das demonstrações.")
            else:
                st.warning("Bom esforço. Sugerimos revisar as Notas Explicativas e as conexões entre BP e DRE.")

if __name__ == "__main__":
    run()