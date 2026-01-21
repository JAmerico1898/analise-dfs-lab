"""
Módulo 1 - Introdução à Análise Financeira
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Discussão orientada sobre usuários da informação contábil
- Exercício diagnóstico de classificação de decisões
- Mini-quiz conceitual de fixação (5 questões)
"""

import streamlit as st


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    # =========================================================================
    # CABEÇALHO DO MÓDULO
    # =========================================================================
    st.markdown("<h1>📊 Módulo 1 - Introdução à Análise Financeira</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Identificar os principais usuários das demonstrações financeiras</li>
                <li>Compreender como diferentes stakeholders utilizam a mesma informação</li>
                <li>Classificar decisões empresariais segundo o tipo de usuário</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # =========================================================================
    # NAVEGAÇÃO POR ABAS
    # =========================================================================
    tab1, tab2, tab3 = st.tabs([
        "💬 Discussão Orientada", 
        "🔍 Exercício Diagnóstico", 
        "📝 Mini-Quiz"
    ])
    
    # =========================================================================
    # ABA 1: DISCUSSÃO ORIENTADA
    # =========================================================================
    with tab1:
        renderizar_discussao_orientada()
    
    # =========================================================================
    # ABA 2: EXERCÍCIO DIAGNÓSTICO
    # =========================================================================
    with tab2:
        renderizar_exercicio_diagnostico()
    
    # =========================================================================
    # ABA 3: MINI-QUIZ
    # =========================================================================
    with tab3:
        renderizar_mini_quiz()


def renderizar_discussao_orientada():
    """Renderiza a seção de discussão orientada."""
    
    st.markdown("### 💬 Discussão Orientada")
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Questão Central:</strong><br>
            <em>"Quais decisões um investidor, um banco e um gestor tomam a partir das mesmas demonstrações financeiras?"</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Apresentação dos três perfis de usuários
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px; 
                        text-align: center; height: 280px;'>
                <h4>📈 Investidor</h4>
                <p style='font-size: 0.9rem;'>Busca maximizar retorno sobre o capital investido</p>
                <hr>
                <p style='font-size: 0.85rem; text-align: left;'>
                    <strong>Foco principal:</strong><br>
                    • Rentabilidade<br>
                    • Potencial de valorização<br>
                    • Política de dividendos<br>
                    • Risco do negócio
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px; 
                        text-align: center; height: 280px;'>
                <h4>🏦 Banco / Credor</h4>
                <p style='font-size: 0.9rem;'>Avalia capacidade de pagamento e garantias</p>
                <hr>
                <p style='font-size: 0.85rem; text-align: left;'>
                    <strong>Foco principal:</strong><br>
                    • Liquidez<br>
                    • Endividamento<br>
                    • Geração de caixa<br>
                    • Garantias reais
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background-color: #fce7f3; padding: 20px; border-radius: 10px; 
                        text-align: center; height: 280px;'>
                <h4>👔 Gestor Interno</h4>
                <p style='font-size: 0.9rem;'>Monitora performance e planeja operações</p>
                <hr>
                <p style='font-size: 0.85rem; text-align: left;'>
                    <strong>Foco principal:</strong><br>
                    • Eficiência operacional<br>
                    • Margens de lucro<br>
                    • Ciclo operacional<br>
                    • Metas e orçamento
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Seção interativa de reflexão
    st.markdown("### 🤔 Reflexão Individual")
    st.info("Antes de prosseguir, reflita sobre a questão central e registre suas ideias abaixo.")
    
    with st.expander("📝 Espaço para suas anotações", expanded=False):
        col_inv, col_ban, col_ges = st.columns(3)
        
        with col_inv:
            st.text_area(
                "Decisões do Investidor:",
                placeholder="Ex: Comprar ou vender ações...",
                height=120,
                key="notas_investidor"
            )
        
        with col_ban:
            st.text_area(
                "Decisões do Banco:",
                placeholder="Ex: Aprovar linha de crédito...",
                height=120,
                key="notas_banco"
            )
        
        with col_ges:
            st.text_area(
                "Decisões do Gestor:",
                placeholder="Ex: Reduzir custos operacionais...",
                height=120,
                key="notas_gestor"
            )
    
    # Revelação das respostas sugeridas
    with st.expander("✅ Ver Respostas Sugeridas", expanded=False):
        st.markdown("""
        #### Decisões típicas de cada usuário:
        
        **📈 Investidor:**
        - Comprar, manter ou vender ações da empresa
        - Participar de ofertas públicas (IPO, follow-on)
        - Comparar retorno com outras oportunidades de investimento
        - Avaliar se a política de dividendos atende suas expectativas
        
        **🏦 Banco / Credor:**
        - Aprovar ou negar pedidos de empréstimo
        - Definir limite de crédito e taxa de juros
        - Exigir garantias adicionais
        - Monitorar covenants (cláusulas restritivas)
        - Renegociar prazos e condições
        
        **👔 Gestor Interno:**
        - Ajustar preços de produtos/serviços
        - Decidir sobre expansão ou redução de operações
        - Alocar recursos entre departamentos
        - Definir política de estoques
        - Negociar prazos com fornecedores e clientes
        """)
    
    st.markdown("---")
    st.caption("💡 Dica: A mesma demonstração financeira conta histórias diferentes para cada usuário!")


def renderizar_exercicio_diagnostico():
    """Renderiza o exercício diagnóstico de classificação."""
    
    st.markdown("### 🔍 Exercício Diagnóstico")
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
            <strong>Instrução:</strong> Classifique cada decisão empresarial abaixo de acordo com o 
            principal usuário da informação contábil que a tomaria. Este exercício não é avaliativo 
            e serve para você testar sua compreensão inicial do conteúdo.
        </div>
    """, unsafe_allow_html=True)
    
    # Definição das decisões e gabaritos
    decisoes = [
        {
            "id": 1,
            "texto": "Aumentar a participação acionária na empresa após análise do ROE",
            "resposta_correta": "Investidor",
            "explicacao": "O ROE (Retorno sobre Patrimônio Líquido) é um indicador fundamental para investidores avaliarem se vale a pena aumentar sua participação."
        },
        {
            "id": 2,
            "texto": "Reduzir o prazo de pagamento a fornecedores para melhorar o índice de liquidez",
            "resposta_correta": "Gestor",
            "explicacao": "Decisões sobre prazos operacionais são tipicamente tomadas pela gestão interna da empresa."
        },
        {
            "id": 3,
            "texto": "Exigir garantia real adicional após constatar aumento do endividamento",
            "resposta_correta": "Banco/Credor",
            "explicacao": "Credores monitoram o endividamento e podem exigir garantias adicionais para proteger seus empréstimos."
        },
        {
            "id": 4,
            "texto": "Aprovar o orçamento de marketing com base na margem de contribuição",
            "resposta_correta": "Gestor",
            "explicacao": "A alocação de recursos internos é uma decisão gerencial baseada em indicadores de performance."
        },
        {
            "id": 5,
            "texto": "Vender as ações antes da divulgação de resultados fracos esperados",
            "resposta_correta": "Investidor",
            "explicacao": "Decisões de compra e venda de ações são típicas de investidores (atenção: venda com informação privilegiada é ilegal!)."
        },
        {
            "id": 6,
            "texto": "Incluir cláusula de covenant exigindo liquidez corrente mínima de 1,5",
            "resposta_correta": "Banco/Credor",
            "explicacao": "Covenants são cláusulas restritivas impostas por credores em contratos de empréstimo."
        },
        {
            "id": 7,
            "texto": "Renegociar o prazo médio de recebimento de clientes",
            "resposta_correta": "Gestor",
            "explicacao": "A gestão do ciclo operacional e capital de giro é responsabilidade da administração."
        },
        {
            "id": 8,
            "texto": "Comparar o dividend yield com outras empresas do setor",
            "resposta_correta": "Investidor",
            "explicacao": "Investidores comparam retornos de dividendos para decidir onde alocar seu capital."
        }
    ]
    
    opcoes = ["Selecione...", "Investidor", "Banco/Credor", "Gestor"]
    
    # Inicializar estado das respostas
    if 'respostas_exercicio' not in st.session_state:
        st.session_state.respostas_exercicio = {d['id']: None for d in decisoes}
    
    if 'mostrar_resultado_exercicio' not in st.session_state:
        st.session_state.mostrar_resultado_exercicio = False
    
    # Renderizar cada decisão
    st.markdown("#### Classifique as decisões:")
    
    for decisao in decisoes:
        col_texto, col_select = st.columns([3, 1])
        
        with col_texto:
            st.markdown(f"**{decisao['id']}.** {decisao['texto']}")
        
        with col_select:
            resposta = st.selectbox(
                f"Usuário {decisao['id']}",
                options=opcoes,
                key=f"decisao_{decisao['id']}",
                label_visibility="collapsed"
            )
            st.session_state.respostas_exercicio[decisao['id']] = resposta
        
        st.markdown("---")
    
    # Botão de verificação
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    
    with col_btn2:
        if st.button("🎯 Verificar Respostas", use_container_width=True, type="primary"):
            st.session_state.mostrar_resultado_exercicio = True
    
    # Exibir resultados
    if st.session_state.mostrar_resultado_exercicio:
        st.markdown("### 📊 Resultado do Exercício")
        
        acertos = 0
        total = len(decisoes)
        
        for decisao in decisoes:
            resposta_usuario = st.session_state.respostas_exercicio[decisao['id']]
            correta = resposta_usuario == decisao['resposta_correta']
            
            if correta:
                acertos += 1
                icone = "✅"
                cor = "#dcfce7"
            elif resposta_usuario == "Selecione...":
                icone = "⚪"
                cor = "#f3f4f6"
            else:
                icone = "❌"
                cor = "#fee2e2"
            
            st.markdown(f"""
                <div style='background-color: {cor}; padding: 10px; border-radius: 8px; margin-bottom: 8px;'>
                    <strong>{icone} Decisão {decisao['id']}:</strong> 
                    Sua resposta: <em>{resposta_usuario}</em> | 
                    Correta: <strong>{decisao['resposta_correta']}</strong>
                    <br><small style='color: #64748b;'>{decisao['explicacao']}</small>
                </div>
            """, unsafe_allow_html=True)
        
        # Resumo
        percentual = (acertos / total) * 100
        
        if percentual >= 80:
            msg = "🌟 Excelente! Você demonstra ótima compreensão dos usuários da informação contábil!"
            cor_msg = "#dcfce7"
        elif percentual >= 60:
            msg = "👍 Bom trabalho! Revise os conceitos das questões erradas."
            cor_msg = "#fef3c7"
        else:
            msg = "📚 Recomendamos revisar o material teórico sobre usuários da informação contábil."
            cor_msg = "#fee2e2"
        
        st.markdown(f"""
            <div style='background-color: {cor_msg}; padding: 20px; border-radius: 10px; 
                        text-align: center; margin-top: 20px;'>
                <h3>Pontuação: {acertos}/{total} ({percentual:.0f}%)</h3>
                <p>{msg}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Botão para reiniciar
        if st.button("🔄 Refazer Exercício"):
            st.session_state.respostas_exercicio = {d['id']: None for d in decisoes}
            st.session_state.mostrar_resultado_exercicio = False
            st.rerun()


def renderizar_mini_quiz():
    """Renderiza o mini-quiz de fixação com 5 questões objetivas."""
    
    st.markdown("### 📝 Mini-Quiz de Fixação")
    st.markdown("""
        <div style='background-color: #f0fdf4; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
            <strong>Instrução:</strong> Responda às 5 questões objetivas abaixo para testar sua 
            compreensão dos conceitos fundamentais da análise de demonstrações financeiras.
        </div>
    """, unsafe_allow_html=True)
    
    # Banco de questões
    questoes = [
        {
            "id": 1,
            "pergunta": "Qual é o principal objetivo da análise de demonstrações financeiras?",
            "alternativas": [
                "a) Calcular impostos devidos pela empresa",
                "b) Extrair informações para tomada de decisões econômicas",
                "c) Registrar transações contábeis",
                "d) Elaborar o orçamento empresarial"
            ],
            "correta": "b",
            "explicacao": "A análise de demonstrações financeiras visa extrair informações relevantes dos relatórios contábeis para subsidiar decisões de investimento, crédito e gestão."
        },
        {
            "id": 2,
            "pergunta": "Um banco, ao analisar as demonstrações de uma empresa solicitante de crédito, estará principalmente interessado em avaliar:",
            "alternativas": [
                "a) O potencial de valorização das ações",
                "b) A eficiência da gestão de marketing",
                "c) A capacidade de pagamento e as garantias disponíveis",
                "d) A política de distribuição de dividendos"
            ],
            "correta": "c",
            "explicacao": "Credores focam em liquidez, endividamento e capacidade de geração de caixa para avaliar se a empresa conseguirá honrar seus compromissos."
        },
        {
            "id": 3,
            "pergunta": "Qual das seguintes NÃO é uma demonstração financeira obrigatória para sociedades anônimas de capital aberto no Brasil?",
            "alternativas": [
                "a) Balanço Patrimonial",
                "b) Demonstração do Resultado do Exercício",
                "c) Demonstração do Fluxo de Caixa",
                "d) Demonstração do Orçamento Realizado"
            ],
            "correta": "d",
            "explicacao": "A Demonstração do Orçamento Realizado não faz parte das demonstrações obrigatórias. As obrigatórias incluem: BP, DRE, DFC, DVA, DMPL e Notas Explicativas."
        },
        {
            "id": 4,
            "pergunta": "O conceito de 'usuário externo' da informação contábil inclui:",
            "alternativas": [
                "a) Apenas os acionistas majoritários",
                "b) Investidores, credores, governo e sociedade em geral",
                "c) Apenas os funcionários da empresa",
                "d) Exclusivamente os órgãos reguladores"
            ],
            "correta": "b",
            "explicacao": "Usuários externos são todos aqueles que não participam da gestão direta da empresa, incluindo investidores, credores, fornecedores, clientes, governo e a sociedade."
        },
        {
            "id": 5,
            "pergunta": "A análise de demonstrações financeiras é considerada uma ferramenta de apoio à decisão porque:",
            "alternativas": [
                "a) Substitui completamente o julgamento do analista",
                "b) Garante retornos positivos nos investimentos",
                "c) Transforma dados contábeis em informações úteis para avaliação",
                "d) Elimina todos os riscos do negócio"
            ],
            "correta": "c",
            "explicacao": "A análise financeira processa e interpreta os dados contábeis, transformando-os em informações que auxiliam (mas não substituem) o julgamento na tomada de decisões."
        }
    ]
    
    # Inicializar estado do quiz
    if 'respostas_quiz' not in st.session_state:
        st.session_state.respostas_quiz = {q['id']: None for q in questoes}
    
    if 'quiz_submetido' not in st.session_state:
        st.session_state.quiz_submetido = False
    
    # Renderizar questões
    for i, questao in enumerate(questoes):
        st.markdown(f"""
            <div style='background-color: #ffffff; padding: 15px; border-radius: 10px; 
                        border: 1px solid #e2e8f0; margin-bottom: 15px;'>
                <strong>Questão {questao['id']}:</strong> {questao['pergunta']}
            </div>
        """, unsafe_allow_html=True)
        
        resposta = st.radio(
            f"Selecione a alternativa para a questão {questao['id']}:",
            options=questao['alternativas'],
            key=f"quiz_q{questao['id']}",
            label_visibility="collapsed"
        )
        
        # Armazenar apenas a letra da resposta
        if resposta:
            st.session_state.respostas_quiz[questao['id']] = resposta[0]
        
        st.markdown("---")
    
    # Botão de submissão
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("📨 Enviar Quiz", use_container_width=True, type="primary"):
            st.session_state.quiz_submetido = True
    
    # Exibir resultado do quiz
    if st.session_state.quiz_submetido:
        st.markdown("### 🏆 Resultado do Quiz")
        
        acertos = 0
        
        for questao in questoes:
            resposta_usuario = st.session_state.respostas_quiz[questao['id']]
            correta = resposta_usuario == questao['correta']
            
            if correta:
                acertos += 1
                st.success(f"✅ **Questão {questao['id']}:** Correta!")
            else:
                st.error(f"❌ **Questão {questao['id']}:** Incorreta. Resposta correta: **{questao['correta']})**")
            
            with st.expander(f"📖 Ver explicação da Questão {questao['id']}"):
                st.info(questao['explicacao'])
        
        # Resumo final
        percentual = (acertos / len(questoes)) * 100
        
        st.markdown("---")
        
        if percentual == 100:
            st.balloons()
            msg = "🎉 Parabéns! Você acertou todas as questões!"
            cor = "#dcfce7"
        elif percentual >= 80:
            msg = "🌟 Excelente desempenho! Você está bem preparado!"
            cor = "#dcfce7"
        elif percentual >= 60:
            msg = "👍 Bom resultado! Revise os pontos que errou."
            cor = "#fef3c7"
        else:
            msg = "📚 Recomendamos revisar o conteúdo teórico antes de prosseguir."
            cor = "#fee2e2"
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 25px; border-radius: 15px; 
                        text-align: center; margin-top: 20px;'>
                <h2>Sua Pontuação: {acertos}/{len(questoes)}</h2>
                <h3>{percentual:.0f}%</h3>
                <p style='font-size: 1.1rem;'>{msg}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Botão para refazer
        st.markdown("")
        col_a, col_b, col_c = st.columns([1, 1, 1])
        with col_b:
            if st.button("🔄 Refazer Quiz", use_container_width=True):
                st.session_state.respostas_quiz = {q['id']: None for q in questoes}
                st.session_state.quiz_submetido = False
                st.rerun()


# Execução standalone para testes
if __name__ == "__main__":
    run()