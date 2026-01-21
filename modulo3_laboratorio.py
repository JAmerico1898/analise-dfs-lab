"""
Módulo 3 - Princípios e Qualidade da Informação
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Estudo de caso: impacto de diferentes métodos de depreciação no lucro
- Exercício reflexivo: "Lucro pode ser verdadeiro e ainda assim enganoso?"
- Questões discursivas para debate em sala
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📋 Módulo 3 - Princípios e Qualidade da Informação</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Compreender como escolhas contábeis afetam os números reportados</li>
                <li>Avaliar o impacto de diferentes métodos de depreciação no lucro</li>
                <li>Desenvolver senso crítico sobre a qualidade da informação contábil</li>
                <li>Identificar situações em que lucros "verdadeiros" podem ser enganosos</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Estudo de Caso: Depreciação",
        "🤔 Exercício Reflexivo",
        "💬 Questões para Debate"
    ])
    
    with tab1:
        renderizar_estudo_caso_depreciacao()
    
    with tab2:
        renderizar_exercicio_reflexivo()
    
    with tab3:
        renderizar_questoes_debate()


def calcular_depreciacao_linear(valor_ativo, valor_residual, vida_util, ano):
    """Calcula depreciação pelo método linear."""
    depreciacao_anual = (valor_ativo - valor_residual) / vida_util
    return depreciacao_anual


def calcular_depreciacao_acelerada(valor_ativo, valor_residual, vida_util, ano):
    """Calcula depreciação pelo método da soma dos dígitos (acelerada)."""
    soma_digitos = sum(range(1, vida_util + 1))
    fator = (vida_util - ano + 1) / soma_digitos
    depreciacao_anual = (valor_ativo - valor_residual) * fator
    return depreciacao_anual


def calcular_depreciacao_unidades(valor_ativo, valor_residual, producao_total, producao_ano):
    """Calcula depreciação pelo método de unidades produzidas."""
    taxa = (valor_ativo - valor_residual) / producao_total
    depreciacao_anual = taxa * producao_ano
    return depreciacao_anual


def renderizar_estudo_caso_depreciacao():
    """Estudo de caso sobre impacto dos métodos de depreciação no lucro."""
    
    st.markdown("### 📊 Estudo de Caso: Impacto dos Métodos de Depreciação no Lucro")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Cenário:</strong><br>
            <em>A Indústria Alfa adquiriu uma máquina por R$ 500.000 com vida útil estimada de 5 anos 
            e valor residual de R$ 50.000. A empresa precisa escolher o método de depreciação. 
            Como essa escolha afeta o lucro reportado?</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### ⚙️ Parâmetros do Ativo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        valor_ativo = st.number_input(
            "Valor do Ativo (R$)",
            min_value=100000,
            max_value=2000000,
            value=500000,
            step=50000,
            key="valor_ativo"
        )
    
    with col2:
        valor_residual = st.number_input(
            "Valor Residual (R$)",
            min_value=0,
            max_value=int(valor_ativo * 0.3),
            value=50000,
            step=10000,
            key="valor_residual"
        )
    
    with col3:
        vida_util = st.slider(
            "Vida Útil (anos)",
            min_value=3,
            max_value=10,
            value=5,
            key="vida_util"
        )
    
    # Produção para método de unidades
    st.markdown("##### Produção Estimada (para método de unidades produzidas)")
    
    producao_total = vida_util * 10000  # Total estimado
    producao_por_ano = []
    
    cols = st.columns(vida_util)
    for i, col in enumerate(cols):
        with col:
            prod = st.number_input(
                f"Ano {i+1}",
                min_value=1000,
                max_value=20000,
                value=12000 - i * 1000 if i < 5 else 8000,
                step=500,
                key=f"prod_{i}"
            )
            producao_por_ano.append(prod)
    
    producao_total = sum(producao_por_ano)
    
    st.markdown("---")
    
    # Cálculos
    anos = list(range(1, vida_util + 1))
    
    # Método Linear
    dep_linear = [calcular_depreciacao_linear(valor_ativo, valor_residual, vida_util, ano) for ano in anos]
    
    # Método Acelerado (Soma dos Dígitos)
    dep_acelerada = [calcular_depreciacao_acelerada(valor_ativo, valor_residual, vida_util, ano) for ano in anos]
    
    # Método Unidades Produzidas
    dep_unidades = [calcular_depreciacao_unidades(valor_ativo, valor_residual, producao_total, prod) for prod in producao_por_ano]
    
    # DataFrame comparativo
    df_depreciacao = pd.DataFrame({
        'Ano': anos,
        'Linear': dep_linear,
        'Acelerada': dep_acelerada,
        'Unidades Produzidas': dep_unidades
    })
    
    # Valores contábeis líquidos
    vcl_linear = [valor_ativo - sum(dep_linear[:i+1]) for i in range(vida_util)]
    vcl_acelerada = [valor_ativo - sum(dep_acelerada[:i+1]) for i in range(vida_util)]
    vcl_unidades = [valor_ativo - sum(dep_unidades[:i+1]) for i in range(vida_util)]
    
    st.markdown("#### 📈 Comparativo dos Métodos de Depreciação")
    
    tab_tabela, tab_grafico, tab_lucro = st.tabs(["📋 Tabela", "📊 Gráfico", "💰 Impacto no Lucro"])
    
    with tab_tabela:
        st.markdown("##### Despesa de Depreciação por Ano (R$)")
        
        df_display = df_depreciacao.copy()
        df_display['Linear'] = df_display['Linear'].apply(lambda x: f"R$ {x:,.0f}")
        df_display['Acelerada'] = df_display['Acelerada'].apply(lambda x: f"R$ {x:,.0f}")
        df_display['Unidades Produzidas'] = df_display['Unidades Produzidas'].apply(lambda x: f"R$ {x:,.0f}")
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Totais
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Linear", f"R$ {sum(dep_linear):,.0f}")
        with col2:
            st.metric("Total Acelerada", f"R$ {sum(dep_acelerada):,.0f}")
        with col3:
            st.metric("Total Unidades", f"R$ {sum(dep_unidades):,.0f}")
        
        st.info("💡 **Observe:** O total depreciado é igual em todos os métodos! A diferença está na **distribuição ao longo do tempo**.")
    
    with tab_grafico:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Despesa de Depreciação por Ano")
            
            fig1 = go.Figure()
            fig1.add_trace(go.Bar(name='Linear', x=anos, y=dep_linear, marker_color='#3b82f6'))
            fig1.add_trace(go.Bar(name='Acelerada', x=anos, y=dep_acelerada, marker_color='#ef4444'))
            fig1.add_trace(go.Bar(name='Unidades', x=anos, y=dep_unidades, marker_color='#22c55e'))
            
            fig1.update_layout(
                barmode='group',
                xaxis_title='Ano',
                yaxis_title='Depreciação (R$)',
                height=350,
                legend=dict(orientation="h", yanchor="bottom", y=1.02)
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            st.markdown("##### Valor Contábil Líquido do Ativo")
            
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(name='Linear', x=anos, y=vcl_linear, mode='lines+markers', line=dict(color='#3b82f6', width=2)))
            fig2.add_trace(go.Scatter(name='Acelerada', x=anos, y=vcl_acelerada, mode='lines+markers', line=dict(color='#ef4444', width=2)))
            fig2.add_trace(go.Scatter(name='Unidades', x=anos, y=vcl_unidades, mode='lines+markers', line=dict(color='#22c55e', width=2)))
            
            fig2.update_layout(
                xaxis_title='Ano',
                yaxis_title='Valor Contábil (R$)',
                height=350,
                legend=dict(orientation="h", yanchor="bottom", y=1.02)
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab_lucro:
        st.markdown("##### Simulação: Impacto no Lucro Operacional")
        
        receita_anual = st.number_input(
            "Receita Operacional Anual (R$)",
            min_value=100000,
            max_value=5000000,
            value=800000,
            step=50000,
            key="receita_anual"
        )
        
        outros_custos = st.number_input(
            "Outros Custos e Despesas (R$)",
            min_value=50000,
            max_value=3000000,
            value=500000,
            step=25000,
            key="outros_custos"
        )
        
        # Calcular lucro por método
        lucro_linear = [receita_anual - outros_custos - dep for dep in dep_linear]
        lucro_acelerado = [receita_anual - outros_custos - dep for dep in dep_acelerada]
        lucro_unidades = [receita_anual - outros_custos - dep for dep in dep_unidades]
        
        st.markdown("##### Lucro Operacional por Ano e Método")
        
        df_lucro = pd.DataFrame({
            'Ano': anos,
            'Lucro (Linear)': [f"R$ {l:,.0f}" for l in lucro_linear],
            'Lucro (Acelerada)': [f"R$ {l:,.0f}" for l in lucro_acelerado],
            'Lucro (Unidades)': [f"R$ {l:,.0f}" for l in lucro_unidades]
        })
        
        st.dataframe(df_lucro, use_container_width=True, hide_index=True)
        
        # Gráfico de lucros
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(name='Linear', x=anos, y=lucro_linear, mode='lines+markers', fill='tozeroy', line=dict(color='#3b82f6')))
        fig3.add_trace(go.Scatter(name='Acelerada', x=anos, y=lucro_acelerado, mode='lines+markers', line=dict(color='#ef4444')))
        fig3.add_trace(go.Scatter(name='Unidades', x=anos, y=lucro_unidades, mode='lines+markers', line=dict(color='#22c55e')))
        
        fig3.update_layout(
            xaxis_title='Ano',
            yaxis_title='Lucro Operacional (R$)',
            height=350
        )
        st.plotly_chart(fig3, use_container_width=True)
        
        # Análise
        diferenca_ano1 = lucro_linear[0] - lucro_acelerado[0]
        
        st.markdown(f"""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; margin-top: 15px;'>
                <strong>⚠️ Impacto no Ano 1:</strong><br>
                A diferença de lucro entre o método Linear e Acelerado no primeiro ano é de 
                <strong>R$ {diferenca_ano1:,.0f}</strong>.<br>
                Isso representa uma variação de <strong>{(diferenca_ano1/lucro_linear[0])*100:.1f}%</strong> no lucro reportado!
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Perguntas reflexivas
    st.markdown("#### 🤔 Questões para Reflexão")
    
    with st.expander("1. Qual método você recomendaria para uma empresa que quer mostrar lucros crescentes?"):
        resposta1 = st.text_area("Sua análise:", key="resp_dep_1", height=80)
        if st.button("Ver Comentário", key="btn_dep_1"):
            st.info("""
                **Comentário:** O método **acelerado** resultaria em lucros crescentes ao longo do tempo, 
                pois a despesa de depreciação diminui a cada ano. Já o método **linear** mantém o lucro 
                mais estável. Porém, a escolha deve refletir a realidade econômica do uso do ativo, 
                não apenas objetivos de apresentação.
            """)
    
    with st.expander("2. Se a empresa vender o ativo no Ano 3, qual método resultaria em maior ganho na venda?"):
        resposta2 = st.text_area("Sua análise:", key="resp_dep_2", height=80)
        if st.button("Ver Comentário", key="btn_dep_2"):
            st.info(f"""
                **Comentário:** O método **acelerado** resultaria em maior ganho na venda, pois o valor 
                contábil líquido seria menor (R$ {vcl_acelerada[2]:,.0f}) comparado ao linear 
                (R$ {vcl_linear[2]:,.0f}). Se vendido pelo mesmo preço, o ganho seria maior na depreciação 
                acelerada. Porém, isso é apenas uma questão de timing do reconhecimento!
            """)
    
    with st.expander("3. Por que a norma contábil permite diferentes métodos se o resultado total é igual?"):
        resposta3 = st.text_area("Sua análise:", key="resp_dep_3", height=80)
        if st.button("Ver Comentário", key="btn_dep_3"):
            st.info("""
                **Comentário:** A norma permite diferentes métodos porque cada um pode refletir melhor 
                o padrão de consumo dos benefícios econômicos do ativo:
                - **Linear:** quando o uso é constante ao longo do tempo
                - **Acelerada:** quando o ativo é mais produtivo nos primeiros anos
                - **Unidades:** quando o desgaste depende diretamente da produção
                
                O princípio da **essência sobre a forma** orienta que a contabilidade deve refletir 
                a realidade econômica.
            """)


def renderizar_exercicio_reflexivo():
    """Exercício reflexivo sobre lucro verdadeiro vs enganoso."""
    
    st.markdown("### 🤔 Exercício Reflexivo: Lucro Verdadeiro, Porém Enganoso?")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Questão Central:</strong><br>
            <em>"Um lucro pode ser tecnicamente verdadeiro e ainda assim ser enganoso para os usuários 
            das demonstrações financeiras?"</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📚 Casos para Análise")
    
    casos = [
        {
            "id": 1,
            "titulo": "Caso 1: Receita de Venda de Ativo",
            "descricao": """A Empresa Beta reportou lucro de R$ 10 milhões no trimestre. 
            Porém, R$ 8 milhões vieram da venda de um imóvel da sede (ganho não recorrente). 
            O lucro operacional foi de apenas R$ 2 milhões, 60% menor que o trimestre anterior.""",
            "pergunta": "O lucro de R$ 10 milhões é verdadeiro? É uma representação fiel da performance?",
            "analise": """**Análise:** O lucro é tecnicamente verdadeiro - foi corretamente calculado conforme 
            as normas. Porém, pode ser enganoso porque:
            - Mistura resultado recorrente (operações) com não recorrente (venda de ativo)
            - Investidores podem projetar lucros futuros com base em um número inflado
            - A qualidade do lucro é baixa (não sustentável)
            
            **Lição:** Sempre analise a composição do lucro, não apenas o número final."""
        },
        {
            "id": 2,
            "titulo": "Caso 2: Mudança de Estimativa Contábil",
            "descricao": """A Empresa Gama aumentou a vida útil estimada de suas máquinas de 10 para 15 anos. 
            Isso reduziu a despesa de depreciação em R$ 5 milhões por ano, aumentando o lucro reportado 
            em 25%. A justificativa: "reavaliação técnica da durabilidade".""",
            "pergunta": "A empresa manipulou o resultado ou fez um ajuste legítimo?",
            "analise": """**Análise:** Mudanças de estimativa são permitidas e às vezes necessárias. Porém:
            - O momento da mudança é suspeito? (perto de meta de bônus, covenant bancário?)
            - A justificativa técnica é sólida e documentada?
            - Há consistência com práticas do setor?
            
            **Sinais de alerta:**
            - Mudanças frequentes de estimativas
            - Sempre na direção que favorece o lucro
            - Timing conveniente
            
            **Lição:** Mudanças de estimativa merecem ceticismo profissional."""
        },
        {
            "id": 3,
            "titulo": "Caso 3: Reconhecimento Agressivo de Receita",
            "descricao": """A Construtora Delta reconhece receita pelo método POC (Percentage of Completion). 
            No trimestre, reportou 40% de avanço físico em uma obra, reconhecendo R$ 40 milhões de receita. 
            Porém, auditores independentes estimaram o avanço real em apenas 25%.""",
            "pergunta": "Qual o impacto dessa superestimativa? Quem é prejudicado?",
            "analise": """**Análise:** A superestimativa de 15 pontos percentuais resulta em:
            - Receita antecipada de R$ 15 milhões
            - Lucro inflado no período atual
            - Lucros menores em períodos futuros (quando a "conta chegar")
            
            **Prejudicados:**
            - Investidores que compram ações com base em lucros inflados
            - Credores que concedem crédito com base em indicadores distorcidos
            - Gestores futuros que herdarão resultados deprimidos
            
            **Lição:** O reconhecimento de receita é uma das áreas de maior risco de manipulação."""
        },
        {
            "id": 4,
            "titulo": "Caso 4: Provisões Insuficientes",
            "descricao": """O Banco Épsilon tem carteira de crédito de R$ 10 bilhões. A provisão para 
            devedores duvidosos (PCLD) representa 2% da carteira (R$ 200 milhões). Bancos similares 
            provisionam em média 4%. O banco alega que sua carteira é de "melhor qualidade".""",
            "pergunta": "Como avaliar se a provisão é adequada ou se o lucro está inflado?",
            "analise": """**Análise:** Provisão menor = despesa menor = lucro maior. Para avaliar:
            
            **Verificar:**
            - Histórico de perdas efetivas vs provisões passadas
            - Composição da carteira (garantias, rating, setores)
            - Tendência de inadimplência no mercado
            - Comparação com peers (concorrentes similares)
            
            **Sinais de alerta:**
            - Provisão muito abaixo do setor sem justificativa clara
            - Reversões frequentes de provisões
            - Crescimento da carteira acima do mercado (pode indicar menor seletividade)
            
            **Lição:** Provisões subjetivas são terreno fértil para gerenciamento de resultados."""
        }
    ]
    
    for caso in casos:
        with st.expander(f"📌 {caso['titulo']}", expanded=(caso['id'] == 1)):
            st.markdown(f"""
                <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    {caso['descricao']}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**❓ {caso['pergunta']}**")
            
            resposta = st.text_area(
                "Sua análise:",
                placeholder="Desenvolva seu raciocínio...",
                height=100,
                key=f"reflexivo_{caso['id']}"
            )
            
            if st.button("Ver Análise do Professor", key=f"btn_reflexivo_{caso['id']}"):
                st.markdown(f"""
                    <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                        {caso['analise']}
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Síntese
    st.markdown("#### 📝 Síntese: Qualidade da Informação Contábil")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px;'>
            <h4>Características da Informação de Qualidade (CPC 00)</h4>
            
            <p><strong>Características Fundamentais:</strong></p>
            <ul>
                <li><strong>Relevância:</strong> Capaz de fazer diferença nas decisões</li>
                <li><strong>Representação Fidedigna:</strong> Completa, neutra e livre de erros</li>
            </ul>
            
            <p><strong>Características de Melhoria:</strong></p>
            <ul>
                <li><strong>Comparabilidade:</strong> Permite comparação entre entidades e períodos</li>
                <li><strong>Verificabilidade:</strong> Observadores independentes chegam ao mesmo resultado</li>
                <li><strong>Tempestividade:</strong> Disponível a tempo de influenciar decisões</li>
                <li><strong>Compreensibilidade:</strong> Clara e concisa</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Quiz rápido
    st.markdown("#### ✅ Verificação de Aprendizado")
    
    quiz_reflexivo = st.radio(
        "Qual das situações abaixo NÃO representa necessariamente um problema de qualidade da informação?",
        options=[
            "A) Empresa muda método de depreciação para aumentar lucro antes de IPO",
            "B) Empresa revisa estimativa de vida útil com base em laudo técnico independente",
            "C) Empresa reconhece receita antes da entrega do produto",
            "D) Empresa não provisiona processos trabalhistas em andamento"
        ],
        key="quiz_reflexivo"
    )
    
    if st.button("Verificar Resposta", key="btn_quiz_reflexivo"):
        if "B)" in quiz_reflexivo:
            st.success("""
                ✅ **Correto!** A alternativa B descreve uma mudança de estimativa legítima, baseada em 
                evidência técnica independente. Mudanças de estimativa são normais e esperadas quando 
                há novas informações. As demais alternativas descrevem situações potencialmente 
                problemáticas (timing suspeito, receita antecipada, ausência de provisão).
            """)
        else:
            st.error("""
                ❌ **Incorreto.** A resposta correta é B. Mudanças de estimativa baseadas em laudos 
                técnicos independentes são procedimentos normais e representam melhoria na qualidade 
                da informação, não manipulação.
            """)


def renderizar_questoes_debate():
    """Questões discursivas para debate em sala."""
    
    st.markdown("### 💬 Questões para Debate em Sala")
    
    st.markdown("""
        <div style='background-color: #f0fdf4; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #22c55e; margin-bottom: 20px;'>
            <strong>Instruções:</strong><br>
            <em>As questões abaixo devem ser discutidas em grupos ou com toda a turma. 
            Não há respostas únicas corretas - o objetivo é desenvolver pensamento crítico 
            sobre a qualidade da informação contábil.</em>
        </div>
    """, unsafe_allow_html=True)
    
    questoes = [
        {
            "numero": 1,
            "tema": "Essência vs Forma",
            "questao": """Uma empresa de tecnologia "vende" equipamentos para uma financeira 
            e simultaneamente assina contrato de leasing para usar os mesmos equipamentos 
            por 5 anos. No final, tem opção de recompra por valor simbólico. 
            
            **Debate:** Isso é uma venda real ou um financiamento disfarçado? 
            Como deveria ser contabilizado?""",
            "pontos": [
                "Qual a essência econômica da transação?",
                "Quem assume os riscos e benefícios do ativo?",
                "Como as normas IFRS 16 tratam essa situação?",
                "Quais os incentivos para estruturar a transação dessa forma?"
            ]
        },
        {
            "numero": 2,
            "tema": "Conservadorismo vs Neutralidade",
            "questao": """Historicamente, a contabilidade seguia o princípio do conservadorismo: 
            "na dúvida, seja pessimista". As normas atuais (IFRS/CPC) substituíram isso pela 
            neutralidade: "não seja nem otimista nem pessimista".
            
            **Debate:** Qual abordagem protege melhor os usuários das demonstrações?""",
            "pontos": [
                "Conservadorismo pode gerar reservas ocultas?",
                "Neutralidade pode abrir espaço para otimismo excessivo?",
                "Qual o papel do auditor em cada abordagem?",
                "Como isso afeta decisões de crédito e investimento?"
            ]
        },
        {
            "numero": 3,
            "tema": "Valor Justo vs Custo Histórico",
            "questao": """Um fundo imobiliário possui edifícios comerciais adquiridos há 10 anos 
            por R$ 100 milhões. Avaliação a valor justo indica R$ 300 milhões. O mercado 
            imobiliário está em alta, mas há sinais de bolha.
            
            **Debate:** Deve-se reconhecer o ganho de R$ 200 milhões mesmo sem vender os imóveis?""",
            "pontos": [
                "Valor justo é mais relevante ou menos confiável?",
                "Como lidar com a volatilidade nos resultados?",
                "O ganho não realizado deveria poder ser distribuído como dividendo?",
                "Como a crise de 2008 mostrou os riscos do valor justo?"
            ]
        },
        {
            "numero": 4,
            "tema": "Responsabilidade da Administração vs Auditor",
            "questao": """A Empresa Zeta apresentou demonstrações com parecer limpo do auditor. 
            Seis meses depois, descobriu-se fraude contábil de R$ 500 milhões. Investidores 
            processam tanto a empresa quanto a firma de auditoria.
            
            **Debate:** Até onde vai a responsabilidade do auditor?""",
            "pontos": [
                "Auditoria é garantia de ausência de fraude?",
                "Qual a diferença entre erros e fraudes na perspectiva da auditoria?",
                "O que significa 'segurança razoável'?",
                "Como alinhar expectativas dos usuários com o trabalho real do auditor?"
            ]
        },
        {
            "numero": 5,
            "tema": "Informação Prospectiva",
            "questao": """Algumas empresas divulgam projeções de lucro (guidance) junto com 
            as demonstrações financeiras históricas. Quando não atingem as projeções, 
            frequentemente culpam "fatores externos imprevisíveis".
            
            **Debate:** Projeções da administração deveriam ser auditadas?""",
            "pontos": [
                "Projeções são informação relevante para investidores?",
                "É possível auditar previsões sobre o futuro?",
                "Guidance cria incentivos perversos (gerenciar para atingir meta)?",
                "Como outros países tratam essa questão?"
            ]
        }
    ]
    
    for q in questoes:
        with st.expander(f"📌 Questão {q['numero']}: {q['tema']}", expanded=(q['numero'] == 1)):
            st.markdown(f"""
                <div style='background-color: #ffffff; padding: 15px; border-radius: 10px; 
                            border: 1px solid #e2e8f0; margin-bottom: 15px;'>
                    {q['questao']}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Pontos para discussão:**")
            for ponto in q['pontos']:
                st.markdown(f"- {ponto}")
            
            st.markdown("---")
            
            st.markdown("**📝 Registro da Discussão do Grupo:**")
            
            argumentos_favor = st.text_area(
                "Principais argumentos a favor:",
                placeholder="Registre os argumentos levantados...",
                height=80,
                key=f"favor_{q['numero']}"
            )
            
            argumentos_contra = st.text_area(
                "Principais argumentos contra:",
                placeholder="Registre os contra-argumentos...",
                height=80,
                key=f"contra_{q['numero']}"
            )
            
            conclusao = st.text_area(
                "Conclusão ou consenso do grupo:",
                placeholder="Qual foi a posição majoritária?",
                height=60,
                key=f"conclusao_{q['numero']}"
            )
    
    st.markdown("---")
    
    # Reflexão final
    st.markdown("#### 🎯 Reflexão Final Individual")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            <strong>📌 Exercício Avaliativo (Individual)</strong><br>
            Escolha uma das questões debatidas e elabore um texto de 10-15 linhas apresentando 
            sua posição pessoal fundamentada.
        </div>
    """, unsafe_allow_html=True)
    
    questao_escolhida = st.selectbox(
        "Selecione a questão para sua reflexão:",
        options=[f"Questão {q['numero']}: {q['tema']}" for q in questoes],
        key="questao_reflexao_final"
    )
    
    reflexao_final = st.text_area(
        "Sua reflexão fundamentada:",
        placeholder="Desenvolva sua argumentação com base nos debates realizados...",
        height=200,
        key="reflexao_final_texto"
    )
    
    if reflexao_final:
        palavras = len(reflexao_final.split())
        st.caption(f"Palavras: {palavras} (recomendado: 100-150)")
        
        if palavras < 50:
            st.warning("⚠️ Desenvolva mais sua argumentação.")
        elif palavras > 200:
            st.info("💡 Considere ser mais conciso.")
        else:
            st.success("✅ Extensão adequada.")
    
    st.markdown("""
        <div style='background-color: #f0f9ff; padding: 15px; border-radius: 10px; margin-top: 20px;'>
            <strong>📝 Critérios de Avaliação:</strong>
            <ul style='margin-bottom: 0;'>
                <li>Clareza na exposição do argumento principal</li>
                <li>Fundamentação com conceitos estudados</li>
                <li>Consideração de perspectivas diferentes</li>
                <li>Conclusão coerente com a argumentação</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()