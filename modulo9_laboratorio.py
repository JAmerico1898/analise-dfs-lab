"""
Módulo 9 - Estrutura de Capital e Alavancagem
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Exercício prático de cálculo de alavancagem
- Caso: empresa altamente lucrativa, porém muito endividada
- Debate orientado: quando a dívida é positiva?
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>⚖️ Módulo 9 - Estrutura de Capital e Alavancagem</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Calcular e interpretar indicadores de endividamento e alavancagem</li>
                <li>Compreender o efeito da alavancagem financeira sobre o ROE</li>
                <li>Analisar os riscos de estruturas de capital altamente alavancadas</li>
                <li>Avaliar quando o endividamento cria ou destrói valor</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Cálculo de Alavancagem",
        "📉 Caso: Lucrativa e Endividada",
        "💬 Debate: Quando Dívida é Positiva?"
    ])
    
    with tab1:
        renderizar_calculo_alavancagem()
    
    with tab2:
        renderizar_caso_endividamento()
    
    with tab3:
        renderizar_debate_divida()


def renderizar_calculo_alavancagem():
    """Exercício prático de cálculo de alavancagem."""
    
    st.markdown("### 📊 Exercício Prático: Cálculo de Alavancagem")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Conceito-Chave:</strong><br>
            <em>Alavancagem financeira é o uso de capital de terceiros (dívida) para amplificar 
            os retornos sobre o capital próprio. Pode magnificar tanto ganhos quanto perdas.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Indicadores de Estrutura de Capital
    st.markdown("#### 📚 Indicadores de Estrutura de Capital")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>📊 Endividamento Geral</h4>
                <p><strong>Fórmula:</strong> (PC + PNC) / Ativo Total</p>
                <p><strong>Indica:</strong> % do ativo financiado por terceiros</p>
                <p><strong>Referência:</strong> < 60% é conservador</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>🔢 Participação de Terceiros</h4>
                <p><strong>Fórmula:</strong> (PC + PNC) / PL</p>
                <p><strong>Indica:</strong> Quanto de dívida para cada R$ de capital próprio</p>
                <p><strong>Referência:</strong> < 1,5 é moderado</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>⚡ Grau de Alavancagem Financeira (GAF)</h4>
                <p><strong>Fórmula:</strong> ROE / ROA ou LAIR / EBIT</p>
                <p><strong>Indica:</strong> Multiplicação do retorno pela dívida</p>
                <p><strong>Referência:</strong> > 1 indica alavancagem positiva</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px;'>
                <h4>🛡️ Cobertura de Juros</h4>
                <p><strong>Fórmula:</strong> EBIT / Despesas Financeiras</p>
                <p><strong>Indica:</strong> Quantas vezes o lucro cobre os juros</p>
                <p><strong>Referência:</strong> > 3x é seguro</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simulador
    st.markdown("#### 🧮 Simulador de Alavancagem Financeira")
    
    st.markdown("**Compare duas empresas com mesmo Ativo Total mas estruturas de capital diferentes:**")
    
    ativo_total = st.number_input("Ativo Total (igual para ambas)", min_value=100000, value=1000000, step=100000, key="ativo_total")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🏢 Empresa A (Conservadora)")
        pct_divida_a = st.slider("% de Dívida", 0, 100, 30, key="div_a")
        taxa_juros_a = st.slider("Taxa de Juros (%)", 0.0, 30.0, 12.0, key="juros_a")
    
    with col2:
        st.markdown("##### 🏭 Empresa B (Alavancada)")
        pct_divida_b = st.slider("% de Dívida", 0, 100, 70, key="div_b")
        taxa_juros_b = st.slider("Taxa de Juros (%)", 0.0, 30.0, 15.0, key="juros_b")
    
    roa = st.slider("ROA (Retorno sobre Ativo) - igual para ambas (%)", 0.0, 30.0, 15.0, key="roa_sim")
    
    # Cálculos Empresa A
    divida_a = ativo_total * (pct_divida_a / 100)
    pl_a = ativo_total - divida_a
    ebit_a = ativo_total * (roa / 100)
    juros_a = divida_a * (taxa_juros_a / 100)
    lair_a = ebit_a - juros_a
    ir_a = lair_a * 0.34 if lair_a > 0 else 0
    ll_a = lair_a - ir_a
    roe_a = (ll_a / pl_a * 100) if pl_a > 0 else 0
    gaf_a = (roe_a / roa) if roa > 0 else 0
    cobertura_a = (ebit_a / juros_a) if juros_a > 0 else float('inf')
    
    # Cálculos Empresa B
    divida_b = ativo_total * (pct_divida_b / 100)
    pl_b = ativo_total - divida_b
    ebit_b = ativo_total * (roa / 100)
    juros_b = divida_b * (taxa_juros_b / 100)
    lair_b = ebit_b - juros_b
    ir_b = lair_b * 0.34 if lair_b > 0 else 0
    ll_b = lair_b - ir_b
    roe_b = (ll_b / pl_b * 100) if pl_b > 0 else 0
    gaf_b = (roe_b / roa) if roa > 0 else 0
    cobertura_b = (ebit_b / juros_b) if juros_b > 0 else float('inf')
    
    st.markdown("---")
    st.markdown("#### 📊 Comparativo de Resultados")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("**Indicador**")
        st.markdown("Dívida Total")
        st.markdown("Patrimônio Líquido")
        st.markdown("EBIT")
        st.markdown("Despesas Financeiras")
        st.markdown("Lucro Líquido")
        st.markdown("**ROE**")
        st.markdown("**GAF**")
        st.markdown("Cobertura de Juros")
    
    with col2:
        st.markdown("**Empresa A**")
        st.markdown(f"R$ {divida_a:,.0f}")
        st.markdown(f"R$ {pl_a:,.0f}")
        st.markdown(f"R$ {ebit_a:,.0f}")
        st.markdown(f"R$ {juros_a:,.0f}")
        st.markdown(f"R$ {ll_a:,.0f}")
        st.markdown(f"**{roe_a:.1f}%**")
        st.markdown(f"**{gaf_a:.2f}x**")
        st.markdown(f"{cobertura_a:.1f}x" if cobertura_a != float('inf') else "∞")
    
    with col3:
        st.markdown("**Empresa B**")
        st.markdown(f"R$ {divida_b:,.0f}")
        st.markdown(f"R$ {pl_b:,.0f}")
        st.markdown(f"R$ {ebit_b:,.0f}")
        st.markdown(f"R$ {juros_b:,.0f}")
        st.markdown(f"R$ {ll_b:,.0f}")
        delta_roe = roe_b - roe_a
        st.markdown(f"**{roe_b:.1f}%** ({delta_roe:+.1f}pp)")
        st.markdown(f"**{gaf_b:.2f}x**")
        cob_txt = f"{cobertura_b:.1f}x" if cobertura_b != float('inf') else "∞"
        st.markdown(cob_txt)
    
    # Gráfico comparativo
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure(data=[
            go.Bar(name='Empresa A', x=['ROE', 'GAF'], y=[roe_a, gaf_a], marker_color='#3b82f6'),
            go.Bar(name='Empresa B', x=['ROE', 'GAF'], y=[roe_b, gaf_b], marker_color='#ef4444')
        ])
        fig1.update_layout(title="ROE e GAF", barmode='group', height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Estrutura de capital
        fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'pie'}, {'type':'pie'}]],
                           subplot_titles=['Empresa A', 'Empresa B'])
        
        fig2.add_trace(go.Pie(labels=['Dívida', 'PL'], values=[divida_a, pl_a],
                             marker_colors=['#ef4444', '#22c55e'], hole=0.4), row=1, col=1)
        fig2.add_trace(go.Pie(labels=['Dívida', 'PL'], values=[divida_b, pl_b],
                             marker_colors=['#ef4444', '#22c55e'], hole=0.4), row=1, col=2)
        
        fig2.update_layout(title="Estrutura de Capital", height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Interpretação
    st.markdown("#### 💡 Interpretação")
    
    if roe_b > roe_a and cobertura_b > 2:
        st.success(f"""
            ✅ **Alavancagem Positiva na Empresa B**
            
            O ROE da Empresa B ({roe_b:.1f}%) é maior que o da Empresa A ({roe_a:.1f}%) porque:
            - O ROA ({roa}%) é MAIOR que o custo da dívida após impostos
            - A alavancagem está amplificando os retornos
            - Cobertura de juros de {cobertura_b:.1f}x ainda é razoável
            
            **GAF > 1 indica que a dívida está criando valor para o acionista.**
        """)
    elif roe_b < roe_a:
        st.error(f"""
            ❌ **Alavancagem Negativa na Empresa B**
            
            O ROE da Empresa B ({roe_b:.1f}%) é MENOR que o da Empresa A ({roe_a:.1f}%) porque:
            - O custo da dívida ({taxa_juros_b}%) é muito alto em relação ao ROA ({roa}%)
            - A alavancagem está destruindo valor
            - A dívida está consumindo o lucro operacional
            
            **GAF < 1 indica que seria melhor operar sem dívida!**
        """)
    elif cobertura_b < 2:
        st.warning(f"""
            ⚠️ **Alavancagem Arriscada na Empresa B**
            
            Embora o ROE seja maior, a cobertura de juros de {cobertura_b:.1f}x é perigosa:
            - Pouca margem para quedas no EBIT
            - Risco de insolvência em cenários adversos
            - Dificuldade de obter novos financiamentos
            
            **O retorno maior vem com risco desproporcional.**
        """)
    
    # Sensibilidade ao ROA
    st.markdown("---")
    st.markdown("#### 📈 Análise de Sensibilidade: E se o ROA cair?")
    
    roas = np.arange(5, 25, 1)
    roes_a = []
    roes_b = []
    
    for r in roas:
        ebit = ativo_total * (r / 100)
        
        # Empresa A
        lair = ebit - juros_a
        ll = lair * 0.66 if lair > 0 else lair
        roe = (ll / pl_a * 100) if pl_a > 0 else 0
        roes_a.append(roe)
        
        # Empresa B
        lair = ebit - juros_b
        ll = lair * 0.66 if lair > 0 else lair
        roe = (ll / pl_b * 100) if pl_b > 0 else 0
        roes_b.append(roe)
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=roas, y=roes_a, name='Empresa A (Conservadora)', 
                             line=dict(color='#3b82f6', width=3)))
    fig3.add_trace(go.Scatter(x=roas, y=roes_b, name='Empresa B (Alavancada)', 
                             line=dict(color='#ef4444', width=3)))
    fig3.add_vline(x=roa, line_dash="dash", line_color="gray", annotation_text="ROA atual")
    fig3.add_hline(y=0, line_color="black", line_width=1)
    
    fig3.update_layout(
        title="Sensibilidade do ROE ao ROA",
        xaxis_title="ROA (%)",
        yaxis_title="ROE (%)",
        height=400
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.info("""
        📊 **Observe no gráfico:**
        - A linha da Empresa B é mais inclinada (maior sensibilidade)
        - Em ROAs altos, B tem ROE muito maior
        - Em ROAs baixos, B pode ter ROE negativo enquanto A ainda é positivo
        - O ponto onde as linhas se cruzam é o "break-even" da alavancagem
    """)


def renderizar_caso_endividamento():
    """Caso: empresa altamente lucrativa, porém muito endividada."""
    
    st.markdown("### 📉 Caso: Altamente Lucrativa, Altamente Endividada")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>🔍 Caso: AeroTech Indústria S.A.</strong><br>
            <em>A empresa é líder de mercado, com margens invejáveis e crescimento consistente. 
            Os acionistas estão felizes com o ROE de 35%. Mas os analistas de crédito estão 
            preocupados. Por quê?</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados da empresa
    st.markdown("#### 📊 Dados Financeiros da AeroTech")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Balanço Patrimonial (R$ milhões)")
        bp_data = {
            "Conta": ["Ativo Total", "Passivo Circulante", "Passivo Não Circulante", 
                     "Patrimônio Líquido", "Dívida Financeira Total"],
            "Valor": ["2.500", "450", "1.550", "500", "1.600"]
        }
        st.dataframe(pd.DataFrame(bp_data), use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("##### DRE Anual (R$ milhões)")
        dre_data = {
            "Conta": ["Receita Líquida", "EBITDA", "EBIT", "Despesas Financeiras", 
                     "LAIR", "Lucro Líquido"],
            "Valor": ["1.800", "450", "350", "200", "150", "100"]
        }
        st.dataframe(pd.DataFrame(dre_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Indicadores
    st.markdown("#### 📈 Indicadores Calculados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>Margem EBITDA</h4>
                <h2 style='color: #22c55e;'>25%</h2>
                <p>Excelente</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>ROE</h4>
                <h2 style='color: #22c55e;'>20%</h2>
                <p>Muito Bom</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>Dívida/EBITDA</h4>
                <h2 style='color: #ef4444;'>3,6x</h2>
                <p>Elevado</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>Cobertura Juros</h4>
                <h2 style='color: #f97316;'>1,75x</h2>
                <p>Baixo</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Segunda linha de indicadores
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Endividamento", "80%", delta="Alto", delta_color="inverse")
    with col2:
        st.metric("Dívida/PL", "3,2x", delta="Muito Alto", delta_color="inverse")
    with col3:
        st.metric("ROA", "4%", delta="Baixo")
    with col4:
        st.metric("GAF", "5,0x", delta="Muito Alavancado")
    
    st.markdown("---")
    
    # O paradoxo
    st.markdown("#### 🤔 O Paradoxo da AeroTech")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>👍 O Que Está Bom</h4>
                <ul>
                    <li>Líder de mercado com 35% de market share</li>
                    <li>Margem EBITDA de 25% - acima do setor</li>
                    <li>ROE de 20% - atrativo para investidores</li>
                    <li>Crescimento de receita de 15% a.a.</li>
                    <li>Contratos de longo prazo com clientes</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px;'>
                <h4>👎 O Que Preocupa</h4>
                <ul>
                    <li>Dívida de R$ 1,6 bilhão = 3,6x EBITDA</li>
                    <li>Cobertura de juros de apenas 1,75x</li>
                    <li>80% do ativo financiado por terceiros</li>
                    <li>Vencimentos concentrados em 2 anos</li>
                    <li>Taxa de juros média de 12,5% a.a.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Cenário de estresse
    st.markdown("---")
    st.markdown("#### 📉 Análise de Cenários de Estresse")
    
    st.markdown("**O que acontece se o EBITDA cair?**")
    
    cenarios = {
        "Cenário": ["Base", "Queda 10%", "Queda 20%", "Queda 30%"],
        "EBITDA": [450, 405, 360, 315],
        "EBIT": [350, 305, 260, 215],
        "Desp. Financeiras": [200, 200, 200, 200],
        "LAIR": [150, 105, 60, 15],
        "Lucro Líquido": [100, 69, 40, 10],
        "Cobertura Juros": [1.75, 1.53, 1.30, 1.08],
        "Dívida/EBITDA": [3.6, 4.0, 4.4, 5.1]
    }
    
    df_cenarios = pd.DataFrame(cenarios)
    st.dataframe(df_cenarios, use_container_width=True, hide_index=True)
    
    # Gráfico de cenários
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Lucro Líquido',
        x=cenarios['Cenário'],
        y=cenarios['Lucro Líquido'],
        marker_color=['#22c55e', '#84cc16', '#f97316', '#ef4444']
    ))
    
    fig.add_trace(go.Scatter(
        name='Cobertura de Juros',
        x=cenarios['Cenário'],
        y=cenarios['Cobertura Juros'],
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='#3b82f6', width=3)
    ))
    
    fig.add_hline(y=1.5, line_dash="dash", line_color="red", 
                 annotation_text="Cobertura Mínima", yref='y2')
    
    fig.update_layout(
        title="Sensibilidade do Lucro e Cobertura de Juros",
        yaxis=dict(title='Lucro Líquido (R$ mi)'),
        yaxis2=dict(title='Cobertura de Juros (x)', overlaying='y', side='right'),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.error("""
        ⚠️ **Risco Crítico Identificado:**
        
        Com queda de apenas 30% no EBITDA (possível em uma recessão):
        - Cobertura de juros cai para 1,08x (quase não sobra para pagar juros!)
        - Dívida/EBITDA sobe para 5,1x (covenant típico é 3,5x)
        - Lucro líquido cai 90%
        - Empresa pode entrar em default técnico dos covenants
    """)
    
    # Covenants
    st.markdown("---")
    st.markdown("#### 📜 Análise de Covenants Bancários")
    
    covenants = {
        "Covenant": ["Dívida/EBITDA", "Cobertura de Juros", "Endividamento Máximo"],
        "Limite": ["≤ 3,5x", "≥ 2,0x", "≤ 75%"],
        "Atual": ["3,6x", "1,75x", "80%"],
        "Status": ["❌ Violado", "❌ Violado", "❌ Violado"]
    }
    
    df_cov = pd.DataFrame(covenants)
    st.dataframe(df_cov, use_container_width=True, hide_index=True)
    
    st.warning("""
        🚨 **Situação dos Covenants:**
        
        A empresa JÁ está violando os três principais covenants! Isso significa:
        - Bancos podem exigir pagamento antecipado
        - Novas linhas de crédito serão negadas ou muito caras
        - Risco de renegociação forçada com perda de controle
    """)
    
    # Exercício
    st.markdown("---")
    st.markdown("#### 📝 Sua Análise")
    
    q1 = st.text_area(
        "1. Você investiria nas ações da AeroTech? Por quê?",
        placeholder="Considere o ROE alto vs o risco financeiro...",
        height=80,
        key="caso9_q1"
    )
    
    q2 = st.text_area(
        "2. Se você fosse o CFO, o que faria para melhorar a situação?",
        placeholder="Liste medidas concretas...",
        height=100,
        key="caso9_q2"
    )
    
    if st.button("Ver Análise do Professor", key="btn_caso9"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Investir nas ações?</strong></p>
                <p>Depende do perfil de risco, mas há sérias preocupações:</p>
                <ul>
                    <li>O ROE de 20% é bom, MAS é amplificado por alavancagem extrema</li>
                    <li>Em caso de dificuldades, acionistas são os últimos a receber</li>
                    <li>Violação de covenants pode levar à diluição ou falência</li>
                    <li>O upside é limitado vs downside significativo</li>
                </ul>
                <p><strong>Recomendação:</strong> Evitar ou posição pequena com stop loss.</p>
                
                <p><strong>2. Ações do CFO:</strong></p>
                <ul>
                    <li><strong>Imediato:</strong>
                        <ul>
                            <li>Renegociar covenants com bancos (waiver)</li>
                            <li>Vender ativos não-core para reduzir dívida</li>
                            <li>Cortar dividendos e direcionar caixa para dívida</li>
                        </ul>
                    </li>
                    <li><strong>Curto prazo:</strong>
                        <ul>
                            <li>Fazer aumento de capital (follow-on)</li>
                            <li>Trocar dívida cara por mais barata/longa</li>
                            <li>Implementar programa de eficiência</li>
                        </ul>
                    </li>
                    <li><strong>Estrutural:</strong>
                        <ul>
                            <li>Definir meta de Dívida/EBITDA ≤ 2,5x</li>
                            <li>Criar política de hedge de juros</li>
                            <li>Diversificar fontes de financiamento</li>
                        </ul>
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def renderizar_debate_divida():
    """Debate orientado: quando a dívida é positiva?"""
    
    st.markdown("### 💬 Debate: Quando a Dívida é Positiva?")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Questão Central do Debate:</strong><br>
            <em>"Dívida é sempre ruim? Em quais situações o endividamento pode criar valor 
            para os acionistas? Quais são os limites?"</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Argumentos
    st.markdown("#### ⚖️ Argumentos Pró e Contra Endividamento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>👍 Argumentos a Favor da Dívida</h4>
                <ol>
                    <li><strong>Benefício Fiscal:</strong> Juros são dedutíveis do IR, reduzindo custo efetivo</li>
                    <li><strong>Alavancagem do ROE:</strong> Amplifica retornos quando ROA > custo dívida</li>
                    <li><strong>Disciplina Gerencial:</strong> Obrigação de pagar juros força eficiência</li>
                    <li><strong>Preserva Controle:</strong> Não dilui participação dos acionistas</li>
                    <li><strong>Custo Menor:</strong> Dívida geralmente é mais barata que capital próprio</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px;'>
                <h4>👎 Argumentos Contra a Dívida</h4>
                <ol>
                    <li><strong>Risco de Insolvência:</strong> Obrigação fixa mesmo em crises</li>
                    <li><strong>Perda de Flexibilidade:</strong> Covenants limitam decisões estratégicas</li>
                    <li><strong>Custo do Financial Distress:</strong> Empresas em dificuldades pagam mais</li>
                    <li><strong>Risco de Expropriação:</strong> Credores podem tomar controle</li>
                    <li><strong>Volatilidade do ROE:</strong> Amplifica perdas em momentos ruins</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Teoria do Trade-off
    st.markdown("#### 📚 Teoria do Trade-off da Estrutura de Capital")
    
    st.markdown("""
        A teoria do trade-off sugere que existe um nível **ótimo** de endividamento que maximiza 
        o valor da empresa, balanceando:
    """)
    
    # Gráfico do Trade-off
    dividas = np.linspace(0, 100, 100)
    beneficio_fiscal = 0.1 * dividas  # Benefício crescente
    custo_distress = 0.0001 * (dividas ** 2.5)  # Custo crescente exponencial
    valor_empresa = 100 + beneficio_fiscal - custo_distress
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dividas, y=100 + beneficio_fiscal,
        name='Com Benefício Fiscal',
        line=dict(color='#22c55e', width=2, dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=dividas, y=valor_empresa,
        name='Valor Líquido (com custos de distress)',
        line=dict(color='#3b82f6', width=3)
    ))
    
    # Ponto ótimo
    idx_max = np.argmax(valor_empresa)
    divida_otima = dividas[idx_max]
    
    fig.add_vline(x=divida_otima, line_dash="dash", line_color="gray",
                 annotation_text=f"Dívida Ótima: {divida_otima:.0f}%")
    
    fig.update_layout(
        title="Trade-off: Benefício Fiscal vs Custo de Distress",
        xaxis_title="Nível de Endividamento (%)",
        yaxis_title="Valor da Empresa",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info(f"""
        📊 **Interpretação do Gráfico:**
        - A linha verde tracejada mostra o valor com benefício fiscal (sem considerar riscos)
        - A linha azul mostra o valor real, considerando custos de dificuldade financeira
        - O ponto ótimo está em torno de {divida_otima:.0f}% de endividamento
        - Após esse ponto, os custos superam os benefícios
    """)
    
    st.markdown("---")
    
    # Quando dívida é positiva
    st.markdown("#### ✅ Quando a Dívida Tende a Ser Positiva?")
    
    situacoes_positivas = [
        {
            "situacao": "Empresa com fluxo de caixa estável e previsível",
            "exemplo": "Concessionárias de energia, empresas de saneamento",
            "motivo": "Capacidade de honrar compromissos mesmo em crises"
        },
        {
            "situacao": "ROA consistentemente acima do custo da dívida",
            "exemplo": "Empresas com vantagens competitivas duráveis",
            "motivo": "Alavancagem amplifica retornos positivos"
        },
        {
            "situacao": "Ativos tangíveis que servem como garantia",
            "exemplo": "Indústrias, empresas imobiliárias",
            "motivo": "Reduz custo e aumenta acesso a crédito"
        },
        {
            "situacao": "Taxa de juros baixa e acesso fácil a crédito",
            "exemplo": "Empresas em países desenvolvidos, investment grade",
            "motivo": "Custo de oportunidade de não usar dívida é alto"
        }
    ]
    
    for sit in situacoes_positivas:
        with st.expander(f"✅ {sit['situacao']}"):
            st.markdown(f"**Exemplo:** {sit['exemplo']}")
            st.markdown(f"**Por quê:** {sit['motivo']}")
    
    st.markdown("#### ❌ Quando a Dívida Tende a Ser Negativa?")
    
    situacoes_negativas = [
        {
            "situacao": "Empresa com receitas voláteis ou cíclicas",
            "exemplo": "Construtoras, commodities, startups",
            "motivo": "Risco de não conseguir pagar em momentos de baixa"
        },
        {
            "situacao": "Setor em transformação ou disrupção",
            "exemplo": "Mídia tradicional, varejo físico",
            "motivo": "Incerteza sobre viabilidade futura do negócio"
        },
        {
            "situacao": "Empresa com poucos ativos tangíveis",
            "exemplo": "Empresas de tecnologia, serviços",
            "motivo": "Dificuldade de oferecer garantias, custo alto"
        },
        {
            "situacao": "Custo da dívida próximo ou acima do ROA",
            "exemplo": "Empresas de baixa rentabilidade",
            "motivo": "Alavancagem destrói valor"
        }
    ]
    
    for sit in situacoes_negativas:
        with st.expander(f"❌ {sit['situacao']}"):
            st.markdown(f"**Exemplo:** {sit['exemplo']}")
            st.markdown(f"**Por quê:** {sit['motivo']}")
    
    st.markdown("---")
    
    # Exercício de debate
    st.markdown("#### 📝 Exercício de Debate em Grupo")
    
    casos_debate = [
        {
            "caso": "Caso 1: Startup de Tecnologia",
            "contexto": "Startup de software SaaS, sem lucro ainda, crescendo 100% a.a., queimando caixa.",
            "pergunta": "Deve usar dívida para financiar crescimento ou apenas equity?"
        },
        {
            "caso": "Caso 2: Rede de Supermercados",
            "contexto": "Rede regional lucrativa, margens estáveis, quer dobrar de tamanho em 3 anos.",
            "pergunta": "Qual a estrutura de capital ideal para financiar a expansão?"
        },
        {
            "caso": "Caso 3: Petroleira",
            "contexto": "Grande petroleira, muito lucrativa, petróleo a US$ 80/barril, previsão de queda.",
            "pergunta": "Deve aumentar dívida para recomprar ações ou manter caixa?"
        }
    ]
    
    for caso in casos_debate:
        with st.expander(f"💬 {caso['caso']}"):
            st.markdown(f"**Contexto:** {caso['contexto']}")
            st.markdown(f"**Pergunta para debate:** {caso['pergunta']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.text_area("Argumentos a favor de mais dívida:", key=f"favor_{caso['caso'][:10]}", height=80)
            with col2:
                st.text_area("Argumentos contra mais dívida:", key=f"contra_{caso['caso'][:10]}", height=80)
    
    # Quiz final
    st.markdown("---")
    st.markdown("#### ✅ Verificação de Aprendizado")
    
    quiz = st.radio(
        "Qual afirmação sobre alavancagem financeira está CORRETA?",
        options=[
            "A) Alavancagem sempre aumenta o ROE da empresa",
            "B) Empresas mais alavancadas são sempre mais arriscadas, mas também mais rentáveis",
            "C) A alavancagem aumenta o ROE quando o ROA supera o custo da dívida após impostos",
            "D) O nível ótimo de dívida é o mesmo para todas as empresas"
        ],
        key="quiz_m9"
    )
    
    if st.button("Verificar", key="btn_quiz_m9"):
        if "C)" in quiz:
            st.success("""
                ✅ **Correto!** A alavancagem só é positiva (aumenta ROE) quando o retorno 
                gerado pelos ativos (ROA) é maior que o custo da dívida. Se o custo da dívida 
                for maior que o ROA, a alavancagem REDUZ o ROE e destrói valor.
            """)
        else:
            st.error("""
                ❌ **Incorreto.** A resposta correta é C. A alavancagem financeira não é 
                automaticamente boa ou ruim - depende da relação entre ROA e custo da dívida. 
                Quando ROA > custo da dívida, alavancagem cria valor. Caso contrário, destrói.
            """)
    
    # Síntese
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Alavancagem é uma faca de dois gumes:</strong> Amplifica ganhos E perdas</li>
                <li><strong>GAF > 1:</strong> Dívida está criando valor (ROA > custo da dívida)</li>
                <li><strong>Cobertura de Juros:</strong> Indicador crítico de risco - mínimo 2x-3x</li>
                <li><strong>Trade-off:</strong> Existe um nível ótimo que balanceia benefícios e riscos</li>
                <li><strong>Contexto importa:</strong> O que é bom para uma empresa pode ser ruim para outra</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()