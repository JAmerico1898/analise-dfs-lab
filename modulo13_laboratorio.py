"""
Módulo 13 - Qualidade dos Lucros e Red Flags
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Estudo de caso: empresa com crescimento artificial de lucro
- Checklist de sinais de alerta financeiro
- Questões discursivas analíticas
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>🚨 Módulo 13 - Qualidade dos Lucros e Red Flags</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Identificar sinais de manipulação ou baixa qualidade dos lucros</li>
                <li>Distinguir entre crescimento sustentável e artificial</li>
                <li>Aplicar um checklist de red flags em análises financeiras</li>
                <li>Desenvolver ceticismo profissional na análise de demonstrações</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📉 Caso: Lucro Artificial",
        "🚩 Checklist de Red Flags",
        "✍️ Questões Analíticas"
    ])
    
    with tab1:
        renderizar_caso_lucro_artificial()
    
    with tab2:
        renderizar_checklist_red_flags()
    
    with tab3:
        renderizar_questoes_analiticas()


def renderizar_caso_lucro_artificial():
    """Estudo de caso: empresa com crescimento artificial de lucro."""
    
    st.markdown("### 📉 Estudo de Caso: O Milagre da Contabilidade Criativa")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>🔍 Caso: TechVision Sistemas S.A.</strong><br>
            <em>A empresa apresentou 5 anos consecutivos de crescimento de lucro, encantando investidores 
            e recebendo prêmios de "melhor gestão". Mas um analista atento descobriu que algo não batia. 
            Você consegue identificar os problemas?</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados históricos da empresa
    st.markdown("#### 📊 Evolução Financeira (5 anos)")
    
    dados_historico = {
        "Indicador (R$ milhões)": [
            "Receita Líquida", "Lucro Bruto", "EBIT", "Lucro Líquido",
            "Fluxo de Caixa Operacional", "Contas a Receber", "Estoques",
            "Contas a Pagar", "Ativo Total", "Patrimônio Líquido"
        ],
        "2019": [500, 200, 75, 50, 60, 80, 45, 40, 400, 200],
        "2020": [600, 240, 96, 65, 55, 120, 70, 45, 520, 250],
        "2021": [750, 300, 127, 88, 40, 180, 110, 50, 700, 320],
        "2022": [920, 368, 165, 115, 20, 275, 165, 55, 950, 410],
        "2023": [1100, 440, 209, 147, -15, 400, 240, 60, 1280, 530]
    }
    
    df_hist = pd.DataFrame(dados_historico)
    st.dataframe(df_hist, use_container_width=True, hide_index=True)
    
    # Métricas de crescimento
    st.markdown("#### 📈 Crescimento Reportado")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        cresc_receita = ((1100/500) - 1) * 100
        st.metric("Receita (5 anos)", f"+{cresc_receita:.0f}%", delta="Impressionante!")
    
    with col2:
        cresc_lucro = ((147/50) - 1) * 100
        st.metric("Lucro Líquido (5 anos)", f"+{cresc_lucro:.0f}%", delta="Fantástico!")
    
    with col3:
        cagr_receita = ((1100/500)**(1/4) - 1) * 100
        st.metric("CAGR Receita", f"{cagr_receita:.1f}%", delta="Acima do setor")
    
    with col4:
        cagr_lucro = ((147/50)**(1/4) - 1) * 100
        st.metric("CAGR Lucro", f"{cagr_lucro:.1f}%", delta="Excepcional")
    
    st.success("✨ À primeira vista, uma empresa de crescimento exemplar!")
    
    st.markdown("---")
    
    # Revelando os problemas
    st.markdown("#### 🔍 Mas um Analista Atento Observou...")
    
    # Gráfico: Lucro vs Caixa
    st.markdown("##### 1️⃣ Divergência entre Lucro e Caixa")
    
    anos = [2019, 2020, 2021, 2022, 2023]
    lucros = [50, 65, 88, 115, 147]
    fcos = [60, 55, 40, 20, -15]
    
    fig1 = go.Figure()
    
    fig1.add_trace(go.Bar(
        name='Lucro Líquido',
        x=anos,
        y=lucros,
        marker_color='#22c55e'
    ))
    
    fig1.add_trace(go.Bar(
        name='Fluxo de Caixa Operacional',
        x=anos,
        y=fcos,
        marker_color='#ef4444'
    ))
    
    fig1.update_layout(
        title="🚨 RED FLAG #1: Lucro Cresce, Caixa Desaparece",
        barmode='group',
        height=350
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.error("""
        **⚠️ Sinal de Alerta:** O lucro cresceu 194% enquanto o fluxo de caixa operacional 
        CAIU de R$ 60 milhões positivo para R$ 15 milhões NEGATIVO!
        
        **O que isso significa?** O lucro contábil não está se convertendo em dinheiro real. 
        Possíveis causas: reconhecimento agressivo de receitas, vendas fictícias, ou manipulação.
    """)
    
    # Gráfico: Contas a Receber vs Receita
    st.markdown("##### 2️⃣ Explosão das Contas a Receber")
    
    receitas = [500, 600, 750, 920, 1100]
    receber = [80, 120, 180, 275, 400]
    
    # Calcular PMR
    pmr = [r/rec*360 for r, rec in zip(receber, receitas)]
    
    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig2.add_trace(
        go.Scatter(name='Receita', x=anos, y=receitas, mode='lines+markers', 
                  line=dict(color='#3b82f6', width=3)),
        secondary_y=False
    )
    
    fig2.add_trace(
        go.Scatter(name='Contas a Receber', x=anos, y=receber, mode='lines+markers',
                  line=dict(color='#ef4444', width=3)),
        secondary_y=False
    )
    
    fig2.add_trace(
        go.Bar(name='PMR (dias)', x=anos, y=pmr, marker_color='#fbbf24', opacity=0.5),
        secondary_y=True
    )
    
    fig2.update_layout(
        title="🚨 RED FLAG #2: Contas a Receber Cresce Mais Rápido que Receita",
        height=400
    )
    fig2.update_yaxes(title_text="R$ milhões", secondary_y=False)
    fig2.update_yaxes(title_text="PMR (dias)", secondary_y=True)
    
    st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        cresc_receita_pct = (1100/500 - 1) * 100
        st.metric("Crescimento da Receita", f"+{cresc_receita_pct:.0f}%")
    with col2:
        cresc_receber_pct = (400/80 - 1) * 100
        st.metric("Crescimento de Recebíveis", f"+{cresc_receber_pct:.0f}%", delta="5x mais!", delta_color="inverse")
    
    st.error("""
        **⚠️ Sinal de Alerta:** Receita cresceu 120%, mas Contas a Receber cresceu 400%!
        
        **O que isso significa?** A empresa pode estar:
        - Vendendo para clientes que não vão pagar
        - Reconhecendo receitas antecipadamente
        - Estendendo prazos excessivamente para inflar vendas
        - Criando vendas fictícias (fraude)
    """)
    
    # Gráfico: Qualidade do Lucro
    st.markdown("##### 3️⃣ Índice de Qualidade do Lucro")
    
    qualidade = [fco/ll if ll > 0 else 0 for fco, ll in zip(fcos, lucros)]
    
    fig3 = go.Figure()
    
    fig3.add_trace(go.Scatter(
        x=anos,
        y=qualidade,
        mode='lines+markers+text',
        text=[f'{q:.2f}' for q in qualidade],
        textposition='top center',
        line=dict(color='#ef4444', width=3),
        marker=dict(size=12)
    ))
    
    fig3.add_hline(y=1.0, line_dash="dash", line_color="green", 
                  annotation_text="Qualidade Ideal (FCO = LL)")
    fig3.add_hline(y=0.8, line_dash="dot", line_color="orange",
                  annotation_text="Mínimo Aceitável")
    
    fig3.update_layout(
        title="🚨 RED FLAG #3: Qualidade do Lucro em Queda Livre",
        yaxis_title="FCO / Lucro Líquido",
        height=350
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.error("""
        **⚠️ Sinal de Alerta:** O índice FCO/LL caiu de 1,20 (saudável) para -0,10 (crítico)!
        
        **Interpretação:**
        - **> 1,0:** Lucro de alta qualidade (gera mais caixa do que reporta)
        - **0,8 - 1,0:** Aceitável
        - **< 0,8:** Preocupante
        - **< 0 ou negativo:** Grave - lucro é "fictício" em termos de caixa
    """)
    
    # Outros red flags
    st.markdown("---")
    st.markdown("##### 4️⃣ Outros Sinais Encontrados")
    
    outros_flags = [
        {
            "flag": "Estoques crescendo mais que vendas",
            "evidencia": f"Estoques +{((240/45)-1)*100:.0f}% vs Receita +{((1100/500)-1)*100:.0f}%",
            "risco": "Possível obsolescência ou superavaliação"
        },
        {
            "flag": "Fornecedores crescendo menos que compras",
            "evidencia": f"Fornecedores +{((60/40)-1)*100:.0f}% vs CMV implícito muito maior",
            "risco": "Perda de crédito comercial (fornecedores desconfiados?)"
        },
        {
            "flag": "Margem Bruta constante apesar de tudo",
            "evidencia": "Margem Bruta estável em 40% todos os anos",
            "risco": "Margem 'gerenciada' para parecer consistente"
        },
        {
            "flag": "Ausência de write-offs",
            "evidencia": "Nenhuma provisão para devedores duvidosos aumentada",
            "risco": "PCLD subdimensionada, lucro inflado"
        }
    ]
    
    for flag in outros_flags:
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <strong>🚩 {flag['flag']}</strong><br>
                <small><strong>Evidência:</strong> {flag['evidencia']}</small><br>
                <small><strong>Risco:</strong> {flag['risco']}</small>
            </div>
        """, unsafe_allow_html=True)
    
    # Desfecho do caso
    st.markdown("---")
    st.markdown("#### 📰 Desfecho do Caso")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px;'>
            <h4>🔴 O Que Aconteceu</h4>
            <p>Uma investigação revelou que a TechVision:</p>
            <ul>
                <li>Reconhecia receitas de contratos não assinados</li>
                <li>Vendia para empresas de fachada relacionadas a executivos</li>
                <li>Não provisionava adequadamente para perdas esperadas</li>
                <li>Capitalizava despesas que deveriam ser reconhecidas no resultado</li>
            </ul>
            <p><strong>Resultado:</strong> Republicação de 3 anos de balanços, queda de 80% no preço da ação, 
            CEO e CFO afastados, processo da CVM e investigação criminal.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Exercício
    st.markdown("---")
    st.markdown("#### 📝 Sua Análise do Caso")
    
    q1 = st.text_area(
        "1. Qual foi o principal indicador que deveria ter alertado os investidores desde 2020?",
        placeholder="Identifique o sinal mais claro...",
        height=80,
        key="caso13_q1"
    )
    
    q2 = st.text_area(
        "2. Por que auditores e analistas não perceberam antes?",
        placeholder="Reflita sobre as limitações da análise...",
        height=80,
        key="caso13_q2"
    )
    
    if st.button("Ver Análise do Professor", key="btn_caso13"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Principal indicador de alerta:</strong></p>
                <p>A <strong>divergência entre Lucro Líquido e Fluxo de Caixa Operacional</strong> era o 
                sinal mais claro. Já em 2020, o FCO começou a cair enquanto o lucro subia. Em 2023, 
                tinha-se lucro de R$ 147 milhões com FCO negativo de R$ 15 milhões - uma diferença 
                de R$ 162 milhões que não faz sentido operacional.</p>
                
                <p><strong>2. Por que não perceberam antes:</strong></p>
                <ul>
                    <li><strong>Viés de confirmação:</strong> Quando resultados são bons, questionamos menos</li>
                    <li><strong>Complexidade:</strong> Manipulações sofisticadas são difíceis de detectar</li>
                    <li><strong>Pressão por fees:</strong> Auditores têm incentivo para manter clientes</li>
                    <li><strong>Foco no DRE:</strong> Muitos analistas não analisam DFC com rigor</li>
                    <li><strong>Informação assimétrica:</strong> Empresa sabe mais que analistas externos</li>
                    <li><strong>Herd behavior:</strong> Se todos recomendam, difícil ser o único cético</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def renderizar_checklist_red_flags():
    """Checklist de sinais de alerta financeiro."""
    
    st.markdown("### 🚩 Checklist de Red Flags Financeiros")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>O que são Red Flags?</strong><br>
            <em>São sinais de alerta que indicam possíveis problemas na qualidade das demonstrações 
            financeiras, manipulação de resultados ou deterioração iminente da saúde financeira. 
            Não são provas de fraude, mas merecem investigação adicional.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Categorias de Red Flags
    st.markdown("#### 📋 Red Flags por Categoria")
    
    categorias = {
        "🔴 Qualidade dos Lucros": {
            "cor": "#fee2e2",
            "flags": [
                {"flag": "FCO significativamente menor que Lucro Líquido", "gravidade": "Alta", 
                 "como_detectar": "FCO/LL < 0,8 por mais de 2 anos consecutivos"},
                {"flag": "Lucro cresce mas caixa não acompanha", "gravidade": "Alta",
                 "como_detectar": "Comparar crescimento de LL vs crescimento de FCO"},
                {"flag": "Muitas receitas não-recorrentes ou extraordinárias", "gravidade": "Média",
                 "como_detectar": "Analisar composição do resultado, notas explicativas"},
                {"flag": "Mudanças frequentes de políticas contábeis", "gravidade": "Alta",
                 "como_detectar": "Verificar notas explicativas ano a ano"},
                {"flag": "Resultados sempre no limite das expectativas", "gravidade": "Média",
                 "como_detectar": "Comparar com consenso de mercado, padrão suspeito"}
            ]
        },
        "🟠 Capital de Giro": {
            "cor": "#fef3c7",
            "flags": [
                {"flag": "Contas a Receber crescendo mais que Receita", "gravidade": "Alta",
                 "como_detectar": "Calcular % crescimento de cada, comparar por 3+ anos"},
                {"flag": "Estoques crescendo mais que CMV", "gravidade": "Alta",
                 "como_detectar": "Verificar giro do estoque, comparar com setor"},
                {"flag": "PMR aumentando consistentemente", "gravidade": "Média",
                 "como_detectar": "Calcular PMR ano a ano, tendência de alta é ruim"},
                {"flag": "PCLD não acompanha crescimento de recebíveis", "gravidade": "Alta",
                 "como_detectar": "PCLD/Clientes deve se manter ou aumentar"},
                {"flag": "Ciclo financeiro deteriorando", "gravidade": "Média",
                 "como_detectar": "PME + PMR - PMP aumentando"}
            ]
        },
        "🟡 Estrutura e Endividamento": {
            "cor": "#fef9c3",
            "flags": [
                {"flag": "Cobertura de juros em queda consistente", "gravidade": "Alta",
                 "como_detectar": "EBIT/Despesas Financeiras caindo por 2+ anos"},
                {"flag": "Dívida/EBITDA acima de covenants", "gravidade": "Alta",
                 "como_detectar": "Verificar nas notas explicativas os limites"},
                {"flag": "Vencimentos concentrados no curto prazo", "gravidade": "Alta",
                 "como_detectar": "Analisar perfil de vencimento da dívida"},
                {"flag": "Refinanciamentos frequentes e cada vez mais caros", "gravidade": "Média",
                 "como_detectar": "Comparar taxas de novas dívidas com anteriores"},
                {"flag": "Patrimônio Líquido negativo ou próximo", "gravidade": "Crítica",
                 "como_detectar": "Verificar BP - passivo a descoberto"}
            ]
        },
        "🟢 Governança e Transparência": {
            "cor": "#dcfce7",
            "flags": [
                {"flag": "Troca de auditor sem explicação clara", "gravidade": "Alta",
                 "como_detectar": "Verificar histórico de auditores, ler parecer"},
                {"flag": "Ressalvas ou ênfases no parecer do auditor", "gravidade": "Alta",
                 "como_detectar": "Ler parecer de auditoria com atenção"},
                {"flag": "Transações com partes relacionadas significativas", "gravidade": "Média",
                 "como_detectar": "Nota explicativa de partes relacionadas"},
                {"flag": "Atrasos na divulgação de resultados", "gravidade": "Média",
                 "como_detectar": "Comparar datas com trimestres anteriores"},
                {"flag": "Executivos vendendo ações da empresa", "gravidade": "Média",
                 "como_detectar": "Verificar movimentações de insiders na CVM"}
            ]
        },
        "🔵 Operacionais e Setoriais": {
            "cor": "#dbeafe",
            "flags": [
                {"flag": "Margens muito acima dos concorrentes", "gravidade": "Média",
                 "como_detectar": "Benchmarking setorial - outlier positivo é suspeito"},
                {"flag": "Crescimento muito acima do mercado sem explicação", "gravidade": "Média",
                 "como_detectar": "Comparar com crescimento do setor"},
                {"flag": "Market share implausível", "gravidade": "Média",
                 "como_detectar": "Cruzar receita reportada com tamanho do mercado"},
                {"flag": "Capex muito baixo para o crescimento reportado", "gravidade": "Alta",
                 "como_detectar": "Crescer sem investir é difícil na maioria dos setores"},
                {"flag": "Funcionários ou lojas não crescem com receita", "gravidade": "Média",
                 "como_detectar": "Receita/funcionário implausível"}
            ]
        }
    }
    
    for categoria, dados in categorias.items():
        with st.expander(f"📌 {categoria}", expanded=False):
            for flag in dados['flags']:
                st.markdown(f"""
                    <div style='background-color: {dados["cor"]}; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
                        <strong>🚩 {flag['flag']}</strong><br>
                        <small>🎯 <strong>Gravidade:</strong> {flag['gravidade']}</small><br>
                        <small>🔍 <strong>Como detectar:</strong> {flag['como_detectar']}</small>
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Ferramenta interativa de checklist
    st.markdown("#### ✅ Ferramenta: Avalie uma Empresa")
    
    st.markdown("Marque os red flags identificados na empresa que você está analisando:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Qualidade dos Lucros**")
        rf1 = st.checkbox("FCO < 80% do Lucro Líquido", key="rf1")
        rf2 = st.checkbox("Lucro cresce, caixa não", key="rf2")
        rf3 = st.checkbox("Muitos itens não-recorrentes", key="rf3")
        rf4 = st.checkbox("Mudanças de política contábil", key="rf4")
        
        st.markdown("**Capital de Giro**")
        rf5 = st.checkbox("Recebíveis crescem mais que receita", key="rf5")
        rf6 = st.checkbox("Estoques crescem mais que CMV", key="rf6")
        rf7 = st.checkbox("PMR aumentando", key="rf7")
        rf8 = st.checkbox("PCLD insuficiente", key="rf8")
    
    with col2:
        st.markdown("**Estrutura de Capital**")
        rf9 = st.checkbox("Cobertura de juros em queda", key="rf9")
        rf10 = st.checkbox("Dívida/EBITDA elevado", key="rf10")
        rf11 = st.checkbox("Vencimentos concentrados", key="rf11")
        
        st.markdown("**Governança**")
        rf12 = st.checkbox("Troca de auditor", key="rf12")
        rf13 = st.checkbox("Ressalvas no parecer", key="rf13")
        rf14 = st.checkbox("Partes relacionadas relevantes", key="rf14")
        rf15 = st.checkbox("Insiders vendendo ações", key="rf15")
    
    # Calcular score
    flags = [rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8, rf9, rf10, rf11, rf12, rf13, rf14, rf15]
    total_flags = sum(flags)
    
    # Flags críticos (peso maior)
    flags_criticos = sum([rf1, rf2, rf5, rf8, rf12, rf13])
    
    st.markdown("---")
    st.markdown("#### 📊 Resultado da Avaliação")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Red Flags Totais", f"{total_flags}/15")
    
    with col2:
        st.metric("Red Flags Críticos", f"{flags_criticos}/6")
    
    with col3:
        if total_flags == 0:
            classificacao = "🟢 Sem Alertas"
            cor = "#dcfce7"
        elif total_flags <= 3 and flags_criticos == 0:
            classificacao = "🟡 Atenção Leve"
            cor = "#fef3c7"
        elif total_flags <= 6 and flags_criticos <= 2:
            classificacao = "🟠 Atenção Moderada"
            cor = "#fed7aa"
        else:
            classificacao = "🔴 Alerta Alto"
            cor = "#fee2e2"
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>{classificacao}</h4>
            </div>
        """, unsafe_allow_html=True)
    
    # Recomendação
    if total_flags > 6 or flags_criticos > 2:
        st.error("""
            **⚠️ Recomendação:** Análise aprofundada necessária antes de qualquer decisão de investimento. 
            Considere contatar RI, verificar notas explicativas detalhadamente, e comparar com concorrentes.
        """)
    elif total_flags > 3:
        st.warning("""
            **⚡ Recomendação:** Monitorar de perto os indicadores sinalizados. 
            Buscar explicações da administração para os pontos identificados.
        """)
    elif total_flags > 0:
        st.info("""
            **ℹ️ Recomendação:** Acompanhar a evolução nos próximos trimestres. 
            Manter atenção mas sem preocupação excessiva.
        """)
    else:
        st.success("""
            **✅ Recomendação:** Nenhum red flag identificado. Continuar acompanhamento normal.
        """)


def renderizar_questoes_analiticas():
    """Questões discursivas analíticas."""
    
    st.markdown("### ✍️ Questões Discursivas Analíticas")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>📋 ATIVIDADE AVALIATIVA</strong><br>
            <em>Responda às questões abaixo com profundidade analítica. 
            Estas questões avaliam sua capacidade de identificar e interpretar 
            sinais de problemas na qualidade das demonstrações financeiras.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Questão 1
    st.markdown("#### Questão 1: Análise de Cenário")
    
    st.markdown("""
        <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            <strong>Cenário:</strong> Uma empresa de varejo apresentou os seguintes dados nos últimos 3 anos:
            <ul>
                <li>Receita: R$ 100 → R$ 130 → R$ 170 milhões (+70% acumulado)</li>
                <li>Lucro Líquido: R$ 5 → R$ 8 → R$ 12 milhões (+140% acumulado)</li>
                <li>FCO: R$ 8 → R$ 4 → R$ -2 milhões (negativo no último ano)</li>
                <li>Contas a Receber: R$ 15 → R$ 30 → R$ 55 milhões (+267% acumulado)</li>
                <li>Número de lojas: 50 → 55 → 58 (+16% acumulado)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    q1 = st.text_area(
        "a) Identifique pelo menos 3 red flags nos dados acima e explique por que são preocupantes.",
        placeholder="Liste os red flags identificados e explique cada um...",
        height=120,
        key="quest1a"
    )
    
    q1b = st.text_area(
        "b) Como a receita pode ter crescido 70% com apenas 16% mais lojas? Isso é plausível?",
        placeholder="Analise a coerência entre crescimento de receita e capacidade operacional...",
        height=100,
        key="quest1b"
    )
    
    # Questão 2
    st.markdown("---")
    st.markdown("#### Questão 2: Comparação Crítica")
    
    st.markdown("""
        <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            Duas empresas do mesmo setor apresentaram os seguintes índices de qualidade do lucro (FCO/LL):
            <ul>
                <li><strong>Empresa A:</strong> 1,2 → 1,1 → 0,9 → 0,7 → 0,5</li>
                <li><strong>Empresa B:</strong> 0,8 → 0,9 → 1,0 → 1,1 → 1,2</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    q2 = st.text_area(
        "Analise a trajetória de cada empresa. Qual apresenta melhor qualidade de lucro? Por quê? O que pode explicar cada trajetória?",
        placeholder="Compare as duas trajetórias e interprete...",
        height=120,
        key="quest2"
    )
    
    # Questão 3
    st.markdown("---")
    st.markdown("#### Questão 3: Caso Prático")
    
    st.markdown("""
        <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            Uma empresa apresentou as seguintes informações em suas notas explicativas:
            <ul>
                <li>Mudança do método de depreciação de acelerado para linear</li>
                <li>Extensão da vida útil estimada de equipamentos de 10 para 15 anos</li>
                <li>Reclassificação de R$ 50 milhões de despesas para ativo intangível</li>
                <li>Reconhecimento de receita de contrato de 5 anos no primeiro ano</li>
            </ul>
            O lucro reportado foi de R$ 80 milhões, 20% acima do ano anterior.
        </div>
    """, unsafe_allow_html=True)
    
    q3a = st.text_area(
        "a) Estime o impacto aproximado de cada mudança no lucro reportado.",
        placeholder="Quantifique ou estime o efeito de cada item...",
        height=100,
        key="quest3a"
    )
    
    q3b = st.text_area(
        "b) O crescimento de 20% no lucro é real ou artificial? Justifique.",
        placeholder="Avalie a qualidade do crescimento reportado...",
        height=100,
        key="quest3b"
    )
    
    # Questão 4
    st.markdown("---")
    st.markdown("#### Questão 4: Reflexão Conceitual")
    
    q4 = st.text_area(
        "Por que uma empresa lucrativa pode quebrar? Relacione sua resposta com os conceitos de qualidade do lucro e gestão de caixa.",
        placeholder="Desenvolva sua reflexão sobre a relação entre lucro contábil e solvência...",
        height=120,
        key="quest4"
    )
    
    # Questão 5
    st.markdown("---")
    st.markdown("#### Questão 5: Aplicação Profissional")
    
    q5 = st.text_area(
        "Você é analista de crédito de um banco e precisa decidir sobre um empréstimo de R$ 50 milhões para a TechVision (do caso estudado). Baseado nos red flags identificados, qual seria sua decisão e quais condições você exigiria?",
        placeholder="Elabore sua análise de crédito e condições...",
        height=140,
        key="quest5"
    )
    
    # Contagem de palavras
    todas_respostas = [q1, q1b, q2, q3a, q3b, q4, q5]
    total_palavras = sum(len(r.split()) for r in todas_respostas if r)
    
    st.markdown("---")
    st.caption(f"Total de palavras escritas: {total_palavras}")
    
    if total_palavras < 300:
        st.warning("Suas respostas estão curtas. Recomendamos pelo menos 500 palavras no total para demonstrar profundidade de análise.")
    elif total_palavras >= 500:
        st.success("Boa profundidade! Continue desenvolvendo seus argumentos.")
    
    # Gabarito
    if st.button("📖 Ver Gabarito Comentado", type="primary"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
                <h4>📋 Gabarito Comentado</h4>
                
                <p><strong>Questão 1a - Red Flags:</strong></p>
                <ol>
                    <li><strong>Lucro cresceu mais que receita:</strong> +140% vs +70% - margem "melhorando" demais</li>
                    <li><strong>FCO negativo com lucro positivo:</strong> Divergência clássica de baixa qualidade</li>
                    <li><strong>Recebíveis cresceram 267% vs receita 70%:</strong> Quase 4x mais - fortíssimo red flag</li>
                    <li><strong>Receita/loja implausível:</strong> Receita +70% com lojas +16% = crescimento de 
                    ~47% por loja, muito acima do normal</li>
                </ol>
                
                <p><strong>Questão 1b - Plausibilidade:</strong></p>
                <p>Dificilmente plausível. Receita por loja teria que saltar de R$ 2 mi para R$ 2,93 mi (+47%). 
                Possíveis explicações legítimas: e-commerce, ticket médio muito maior, inflação. Mas combinado 
                com outros red flags, sugere reconhecimento agressivo de receita.</p>
                
                <p><strong>Questão 2 - Trajetórias:</strong></p>
                <ul>
                    <li><strong>Empresa A:</strong> Trajetória PREOCUPANTE - qualidade deteriorando consistentemente. 
                    Pode indicar: vendas a prazo crescentes, reconhecimento agressivo, problemas de cobrança.</li>
                    <li><strong>Empresa B:</strong> Trajetória POSITIVA - qualidade melhorando. Indica: melhor 
                    gestão de recebíveis, política de crédito mais conservadora, lucros mais "reais".</li>
                </ul>
                <p>Empresa B é claramente superior em qualidade, mesmo que Empresa A tenha lucros maiores.</p>
                
                <p><strong>Questão 3a - Impactos estimados:</strong></p>
                <ul>
                    <li>Mudança de depreciação: Pode adicionar R$ 5-15 mi ao lucro</li>
                    <li>Extensão de vida útil: Similar efeito, R$ 5-10 mi</li>
                    <li>Reclassificação de despesas: R$ 50 mi direto no resultado (!)
                    <li>Reconhecimento antecipado: Pode ser a maior parte do lucro reportado</li>
                </ul>
                
                <p><strong>Questão 3b - Qualidade do crescimento:</strong></p>
                <p>ARTIFICIAL. Os R$ 80 mi de lucro provavelmente incluem R$ 50 mi de reclassificação + 
                R$ 10-20 mi de mudanças de depreciação + receita antecipada. O lucro "real" comparável pode ser 
                negativo ou próximo de zero. O crescimento de 20% é ilusório.</p>
                
                <p><strong>Questão 4 - Empresa lucrativa pode quebrar:</strong></p>
                <p>Sim, porque lucro contábil ≠ caixa. Uma empresa pode ter lucro contábil (regime de competência) 
                mas não receber em dinheiro (regime de caixa). Se ela não consegue converter lucro em caixa para 
                pagar dívidas, fornecedores e funcionários, ela quebra. Casos clássicos: crescimento muito rápido 
                financiado por capital de giro, vendas a prazo para clientes duvidosos, estoques encalhados.</p>
                
                <p><strong>Questão 5 - Decisão de crédito:</strong></p>
                <p><strong>RECOMENDAÇÃO: NEGAR</strong> o crédito ou aprovar apenas com condições muito restritivas:</p>
                <ul>
                    <li>Garantias reais (imóveis, equipamentos)</li>
                    <li>Covenants apertados de FCO mínimo</li>
                    <li>Limite de dividendos enquanto empréstimo ativo</li>
                    <li>Auditoria independente trimestral</li>
                    <li>Cross-default com outras dívidas</li>
                    <li>Taxa de juros elevada pelo risco</li>
                </ul>
                <p>Na prática, os red flags são tão graves que a melhor decisão seria não emprestar.</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Síntese
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Lucro ≠ Caixa:</strong> A divergência entre LL e FCO é o principal indicador de qualidade</li>
                <li><strong>Crescimento pode ser ilusório:</strong> Verificar se cresce de forma sustentável</li>
                <li><strong>Red flags são sinais, não provas:</strong> Merecem investigação, não conclusão precipitada</li>
                <li><strong>Ceticismo profissional:</strong> Questionar números muito bons é prudente</li>
                <li><strong>Análise integrada:</strong> Um red flag isolado pode ser explicado; vários juntos são graves</li>
                <li><strong>DFC é seu amigo:</strong> Mais difícil de manipular que DRE</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()