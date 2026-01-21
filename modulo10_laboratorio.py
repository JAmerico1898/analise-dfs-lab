"""
Módulo 10 - Análise de Rentabilidade (ROE, ROA, Dupont)
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Exercícios numéricos completos
- Comparação entre duas empresas com ROE semelhante
- Interpretação econômica dos resultados
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📈 Módulo 10 - Análise de Rentabilidade</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Calcular e interpretar ROE, ROA e seus componentes</li>
                <li>Aplicar a análise DuPont para decompor a rentabilidade</li>
                <li>Comparar empresas com ROE semelhante identificando diferenças estratégicas</li>
                <li>Interpretar economicamente os drivers de rentabilidade</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Exercícios Numéricos",
        "🔄 Comparativo de Empresas",
        "💡 Interpretação Econômica"
    ])
    
    with tab1:
        renderizar_exercicios_numericos()
    
    with tab2:
        renderizar_comparativo_empresas()
    
    with tab3:
        renderizar_interpretacao_economica()


def renderizar_exercicios_numericos():
    """Exercícios numéricos completos de rentabilidade."""
    
    st.markdown("### 📊 Exercícios Numéricos: ROE, ROA e Análise DuPont")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Revisão: Fórmulas Fundamentais</strong><br><br>
            <strong>ROE</strong> = Lucro Líquido / Patrimônio Líquido<br>
            <strong>ROA</strong> = Lucro Líquido / Ativo Total<br>
            <strong>ROIC</strong> = NOPAT / Capital Investido<br><br>
            <strong>Análise DuPont (3 fatores):</strong><br>
            ROE = Margem Líquida × Giro do Ativo × Multiplicador de Alavancagem<br>
            ROE = (LL/Receita) × (Receita/Ativo) × (Ativo/PL)
        </div>
    """, unsafe_allow_html=True)
    
    # Simulador DuPont
    st.markdown("#### 🧮 Simulador: Análise DuPont Interativa")
    
    st.markdown("Insira os dados para calcular o ROE decomposto:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Dados da DRE**")
        receita = st.number_input("Receita Líquida (R$)", min_value=0, value=5000000, step=100000, key="dp_rec")
        lucro_liquido = st.number_input("Lucro Líquido (R$)", min_value=-1000000, value=400000, step=50000, key="dp_ll")
    
    with col2:
        st.markdown("**Dados do Balanço**")
        ativo_total = st.number_input("Ativo Total (R$)", min_value=1, value=4000000, step=100000, key="dp_at")
        pl = st.number_input("Patrimônio Líquido (R$)", min_value=1, value=1600000, step=100000, key="dp_pl")
    
    with col3:
        st.markdown("**Dados Adicionais**")
        ebit = st.number_input("EBIT (R$)", min_value=0, value=600000, step=50000, key="dp_ebit")
        divida = ativo_total - pl
        st.metric("Dívida Total (calculada)", f"R$ {divida:,.0f}")
    
    # Cálculos
    margem_liquida = (lucro_liquido / receita * 100) if receita > 0 else 0
    giro_ativo = (receita / ativo_total) if ativo_total > 0 else 0
    multiplicador = (ativo_total / pl) if pl > 0 else 0
    
    roe = (lucro_liquido / pl * 100) if pl > 0 else 0
    roa = (lucro_liquido / ativo_total * 100) if ativo_total > 0 else 0
    
    # ROE via DuPont
    roe_dupont = (margem_liquida / 100) * giro_ativo * multiplicador * 100
    
    st.markdown("---")
    st.markdown("#### 📈 Resultados da Análise DuPont")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Margem Líquida</h4>
                <h2>{margem_liquida:.2f}%</h2>
                <p>LL / Receita</p>
                <small>Eficiência em converter vendas em lucro</small>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Giro do Ativo</h4>
                <h2>{giro_ativo:.2f}x</h2>
                <p>Receita / Ativo</p>
                <small>Eficiência no uso dos ativos</small>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Multiplicador (Alavancagem)</h4>
                <h2>{multiplicador:.2f}x</h2>
                <p>Ativo / PL</p>
                <small>Uso de capital de terceiros</small>
            </div>
        """, unsafe_allow_html=True)
    
    # Resultado final
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        cor_roe = "#22c55e" if roe > 15 else "#f97316" if roe > 8 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_roe}20; padding: 25px; border-radius: 15px; 
                        text-align: center; border: 3px solid {cor_roe};'>
                <h3>ROE = Margem × Giro × Alavancagem</h3>
                <h2>{margem_liquida:.2f}% × {giro_ativo:.2f} × {multiplicador:.2f} = <span style='color: {cor_roe};'>{roe_dupont:.2f}%</span></h2>
                <p>ROE direto (LL/PL): <strong>{roe:.2f}%</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    # Gráfico de decomposição
    st.markdown("#### 📊 Visualização da Decomposição")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras dos componentes
        fig1 = go.Figure()
        
        fig1.add_trace(go.Bar(
            x=['Margem Líquida (%)', 'Giro do Ativo (x)', 'Multiplicador (x)'],
            y=[margem_liquida, giro_ativo, multiplicador],
            marker_color=['#3b82f6', '#22c55e', '#f97316'],
            text=[f'{margem_liquida:.1f}%', f'{giro_ativo:.2f}x', f'{multiplicador:.2f}x'],
            textposition='outside'
        ))
        
        fig1.update_layout(title="Componentes do ROE (DuPont)", height=350, showlegend=False)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Gráfico de contribuição
        # Normalizar para mostrar contribuição relativa (usando log)
        contrib_margem = np.log(margem_liquida/100 + 0.01) if margem_liquida > 0 else -2
        contrib_giro = np.log(giro_ativo + 0.01)
        contrib_alav = np.log(multiplicador + 0.01)
        
        fig2 = go.Figure(go.Waterfall(
            name="Construção do ROE",
            orientation="v",
            measure=["absolute", "relative", "relative", "total"],
            x=["ROA Base", "Efeito Giro", "Efeito Alavancagem", "ROE Final"],
            y=[roa, (roe - roa) * 0.4, (roe - roa) * 0.6, roe],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#ef4444"}},
            increasing={"marker": {"color": "#22c55e"}},
            totals={"marker": {"color": "#3b82f6"}}
        ))
        
        fig2.update_layout(title="Do ROA ao ROE", height=350)
        st.plotly_chart(fig2, use_container_width=True)
    
    # ROA e ROIC
    st.markdown("---")
    st.markdown("#### 📊 Indicadores Complementares")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("ROA", f"{roa:.2f}%", help="Lucro Líquido / Ativo Total")
    
    with col2:
        margem_ebit = (ebit / receita * 100) if receita > 0 else 0
        st.metric("Margem EBIT", f"{margem_ebit:.2f}%", help="EBIT / Receita")
    
    with col3:
        # ROIC simplificado
        nopat = ebit * 0.66  # EBIT * (1 - 34%)
        capital_investido = pl + divida * 0.7  # Simplificação
        roic = (nopat / capital_investido * 100) if capital_investido > 0 else 0
        st.metric("ROIC (aprox.)", f"{roic:.2f}%", help="NOPAT / Capital Investido")
    
    with col4:
        gaf = roe / roa if roa > 0 else 0
        st.metric("GAF", f"{gaf:.2f}x", help="ROE / ROA")
    
    # Exercício prático
    st.markdown("---")
    st.markdown("#### ✏️ Exercício de Fixação")
    
    st.markdown("""
        **Dados da Empresa XYZ:**
        - Receita Líquida: R$ 8.000.000
        - Lucro Líquido: R$ 480.000
        - Ativo Total: R$ 6.000.000
        - Patrimônio Líquido: R$ 2.000.000
        
        **Calcule:**
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        resp_margem = st.number_input("Margem Líquida (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ex_marg")
    with col2:
        resp_giro = st.number_input("Giro do Ativo (x):", min_value=0.0, max_value=10.0, value=0.0, step=0.01, key="ex_giro")
    with col3:
        resp_roe = st.number_input("ROE (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ex_roe")
    
    if st.button("Verificar Respostas", key="btn_verif_ex"):
        # Gabarito
        marg_correta = 6.0
        giro_correto = 1.33
        roe_correto = 24.0
        
        acertos = 0
        
        if abs(resp_margem - marg_correta) < 0.2:
            st.success(f"✅ Margem Líquida: {marg_correta}% - Correto!")
            acertos += 1
        else:
            st.error(f"❌ Margem Líquida: Sua {resp_margem}% | Correta: {marg_correta}%")
            st.caption("   480.000 / 8.000.000 = 6%")
        
        if abs(resp_giro - giro_correto) < 0.05:
            st.success(f"✅ Giro do Ativo: {giro_correto}x - Correto!")
            acertos += 1
        else:
            st.error(f"❌ Giro do Ativo: Sua {resp_giro}x | Correto: {giro_correto}x")
            st.caption("   8.000.000 / 6.000.000 = 1,33x")
        
        if abs(resp_roe - roe_correto) < 0.5:
            st.success(f"✅ ROE: {roe_correto}% - Correto!")
            acertos += 1
        else:
            st.error(f"❌ ROE: Sua {resp_roe}% | Correto: {roe_correto}%")
            st.caption("   480.000 / 2.000.000 = 24% (ou 6% × 1,33 × 3 = 24%)")
        
        if acertos == 3:
            st.balloons()


def renderizar_comparativo_empresas():
    """Comparação entre duas empresas com ROE semelhante."""
    
    st.markdown("### 🔄 Comparativo: Mesmo ROE, Estratégias Diferentes")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Duas empresas podem ter ROE semelhante, mas alcançá-lo de formas completamente 
            diferentes. A análise DuPont revela essas diferenças estratégicas.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados das empresas
    st.markdown("#### 📊 Dados das Empresas")
    
    empresas = {
        "Indicador": [
            "Receita Líquida (R$ mi)", "Lucro Líquido (R$ mi)", "Ativo Total (R$ mi)",
            "Patrimônio Líquido (R$ mi)", "Dívida Total (R$ mi)", "EBIT (R$ mi)"
        ],
        "Luxo Premium S.A.": [500, 60, 400, 200, 200, 90],
        "Varejo Popular Ltda.": [3000, 60, 750, 200, 550, 100]
    }
    
    df_empresas = pd.DataFrame(empresas)
    st.dataframe(df_empresas, use_container_width=True, hide_index=True)
    
    # Cálculos
    # Luxo Premium
    rec_luxo, ll_luxo, at_luxo, pl_luxo, div_luxo, ebit_luxo = 500, 60, 400, 200, 200, 90
    margem_luxo = ll_luxo / rec_luxo * 100
    giro_luxo = rec_luxo / at_luxo
    mult_luxo = at_luxo / pl_luxo
    roe_luxo = ll_luxo / pl_luxo * 100
    roa_luxo = ll_luxo / at_luxo * 100
    
    # Varejo Popular
    rec_var, ll_var, at_var, pl_var, div_var, ebit_var = 3000, 60, 750, 200, 550, 100
    margem_var = ll_var / rec_var * 100
    giro_var = rec_var / at_var
    mult_var = at_var / pl_var
    roe_var = ll_var / pl_var * 100
    roa_var = ll_var / at_var * 100
    
    st.markdown("---")
    st.markdown("#### 📈 Análise DuPont Comparativa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px;'>
                <h3>🏆 Luxo Premium S.A.</h3>
                <p><em>Joalheria de alto padrão</em></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("Margem Líquida", f"{margem_luxo:.1f}%", delta="Alta margem")
        st.metric("Giro do Ativo", f"{giro_luxo:.2f}x", delta="Baixo giro")
        st.metric("Multiplicador", f"{mult_luxo:.2f}x", delta="Baixa alavancagem")
        st.metric("ROE", f"{roe_luxo:.1f}%")
        st.metric("ROA", f"{roa_luxo:.1f}%")
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
                <h3>🛒 Varejo Popular Ltda.</h3>
                <p><em>Rede de lojas de R$ 1,99</em></p>
            </div>
        """, unsafe_allow_html=True)
        
        st.metric("Margem Líquida", f"{margem_var:.1f}%", delta="Baixa margem", delta_color="inverse")
        st.metric("Giro do Ativo", f"{giro_var:.2f}x", delta="Alto giro")
        st.metric("Multiplicador", f"{mult_var:.2f}x", delta="Alta alavancagem")
        st.metric("ROE", f"{roe_var:.1f}%")
        st.metric("ROA", f"{roa_var:.1f}%")
    
    # Gráfico radar
    st.markdown("---")
    st.markdown("#### 📊 Visualização Comparativa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar chart
        categorias = ['Margem Líq. (norm)', 'Giro Ativo (norm)', 'Alavancagem (norm)', 'ROA (norm)']
        
        # Normalizar para escala 0-100
        valores_luxo = [
            margem_luxo * 5,  # Normalizado
            giro_luxo * 25,
            mult_luxo * 20,
            roa_luxo * 5
        ]
        
        valores_var = [
            margem_var * 5,
            giro_var * 25,
            mult_var * 20,
            roa_var * 5
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=valores_luxo + [valores_luxo[0]],
            theta=categorias + [categorias[0]],
            fill='toself',
            name='Luxo Premium',
            line_color='#3b82f6'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=valores_var + [valores_var[0]],
            theta=categorias + [categorias[0]],
            fill='toself',
            name='Varejo Popular',
            line_color='#22c55e'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Perfil Estratégico (Radar)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Barras comparativas
        fig2 = go.Figure()
        
        indicadores = ['Margem (%)', 'Giro (x)', 'Multiplicador (x)', 'ROE (%)']
        valores_luxo_bar = [margem_luxo, giro_luxo, mult_luxo, roe_luxo]
        valores_var_bar = [margem_var, giro_var, mult_var, roe_var]
        
        fig2.add_trace(go.Bar(name='Luxo Premium', x=indicadores, y=valores_luxo_bar, marker_color='#3b82f6'))
        fig2.add_trace(go.Bar(name='Varejo Popular', x=indicadores, y=valores_var_bar, marker_color='#22c55e'))
        
        fig2.update_layout(barmode='group', title="Indicadores Lado a Lado", height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Fórmula DuPont visual
    st.markdown("---")
    st.markdown("#### 🔢 Decomposição DuPont")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>Luxo Premium</h4>
                <h3>{margem_luxo:.1f}% × {giro_luxo:.2f} × {mult_luxo:.2f} = {roe_luxo:.1f}%</h3>
                <p><strong>Estratégia: Alta Margem</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; text-align: center;'>
                <h4>Varejo Popular</h4>
                <h3>{margem_var:.1f}% × {giro_var:.2f} × {mult_var:.2f} = {roe_var:.1f}%</h3>
                <p><strong>Estratégia: Alto Giro + Alavancagem</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    # Análise das estratégias
    st.markdown("---")
    st.markdown("#### 💡 Análise das Estratégias")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #eff6ff; padding: 15px; border-radius: 10px;'>
                <h4>🏆 Luxo Premium - Estratégia de Diferenciação</h4>
                <ul>
                    <li><strong>Margem alta (12%):</strong> Produtos exclusivos com markup elevado</li>
                    <li><strong>Giro baixo (1,25x):</strong> Estoques de alto valor, vendas menos frequentes</li>
                    <li><strong>Baixa alavancagem (2x):</strong> Negócio conservador, menor risco</li>
                    <li><strong>ROA alto (15%):</strong> Ativos geram bom retorno</li>
                </ul>
                <p><strong>Risco:</strong> Sensível a crises econômicas (demanda por luxo cai)</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #f0fdf4; padding: 15px; border-radius: 10px;'>
                <h4>🛒 Varejo Popular - Estratégia de Volume</h4>
                <ul>
                    <li><strong>Margem baixa (2%):</strong> Preços competitivos, margens apertadas</li>
                    <li><strong>Giro alto (4x):</strong> Estoque gira rapidamente, alta eficiência</li>
                    <li><strong>Alta alavancagem (3,75x):</strong> Uso intensivo de capital de terceiros</li>
                    <li><strong>ROA baixo (8%):</strong> Compensa com escala e alavancagem</li>
                </ul>
                <p><strong>Risco:</strong> Margens apertadas + dívida alta = pouca margem para erros</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Exercício
    st.markdown("---")
    st.markdown("#### 📝 Exercício de Análise")
    
    q1 = st.text_area(
        "1. Qual empresa você considera mais arriscada? Por quê?",
        placeholder="Analise os riscos de cada estratégia...",
        height=80,
        key="comp_q1"
    )
    
    q2 = st.text_area(
        "2. Se a economia entrar em recessão, qual empresa sofreria mais? Por quê?",
        placeholder="Considere os componentes do ROE...",
        height=80,
        key="comp_q2"
    )
    
    if st.button("Ver Análise do Professor", key="btn_comp"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Qual é mais arriscada?</strong></p>
                <p>O <strong>Varejo Popular</strong> é mais arriscado porque:</p>
                <ul>
                    <li>Margem muito baixa (2%) - qualquer aumento de custo elimina o lucro</li>
                    <li>Alta alavancagem (3,75x) - obrigações fixas com juros</li>
                    <li>ROA baixo (8%) - se custo da dívida subir, ROE despenca</li>
                    <li>Cobertura de juros provavelmente apertada</li>
                </ul>
                
                <p><strong>2. Impacto da recessão:</strong></p>
                <p>Paradoxalmente, <strong>ambas sofreriam, mas de formas diferentes:</strong></p>
                <ul>
                    <li><strong>Luxo Premium:</strong> Queda de demanda (consumo de luxo é cortado primeiro), 
                    mas tem margem para absorver e baixa dívida para sobreviver</li>
                    <li><strong>Varejo Popular:</strong> Demanda pode até aumentar (trade-down), 
                    MAS se margens já apertadas forem comprimidas, pode não conseguir pagar dívidas</li>
                </ul>
                <p><strong>Conclusão:</strong> Luxo sofre mais na receita, mas sobrevive. Varejo pode 
                manter receita mas quebrar por falta de margem para cobrir juros.</p>
            </div>
        """, unsafe_allow_html=True)


def renderizar_interpretacao_economica():
    """Interpretação econômica dos resultados de rentabilidade."""
    
    st.markdown("### 💡 Interpretação Econômica dos Resultados")
    
    st.markdown("""
        <div style='background-color: #f0fdf4; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #22c55e; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Ir além dos números e entender o que os indicadores de rentabilidade 
            revelam sobre a estratégia, eficiência e riscos do negócio.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # O que cada componente revela
    st.markdown("#### 📚 O Que Cada Componente do ROE Revela")
    
    componentes = [
        {
            "componente": "Margem Líquida",
            "formula": "Lucro Líquido / Receita",
            "revela": "Poder de precificação e controle de custos",
            "alta": "Produtos diferenciados, marca forte, poder de mercado, eficiência operacional",
            "baixa": "Commodities, concorrência intensa, custos mal controlados, setor competitivo",
            "cor": "#dbeafe"
        },
        {
            "componente": "Giro do Ativo",
            "formula": "Receita / Ativo Total",
            "revela": "Eficiência no uso dos recursos",
            "alta": "Ativos bem utilizados, operação enxuta, modelo asset-light",
            "baixa": "Capacidade ociosa, ativos improdutivos, modelo capital-intensivo",
            "cor": "#dcfce7"
        },
        {
            "componente": "Multiplicador de Alavancagem",
            "formula": "Ativo / Patrimônio Líquido",
            "revela": "Estrutura de financiamento e apetite a risco",
            "alta": "Uso intensivo de dívida, amplificação de retornos (e riscos)",
            "baixa": "Estrutura conservadora, menor risco financeiro, possível subutilização",
            "cor": "#fef3c7"
        }
    ]
    
    for comp in componentes:
        with st.expander(f"📊 {comp['componente']}: {comp['formula']}", expanded=True):
            st.markdown(f"""
                <div style='background-color: {comp["cor"]}; padding: 15px; border-radius: 10px;'>
                    <p><strong>O que revela:</strong> {comp['revela']}</p>
                    <p>✅ <strong>Quando é alta:</strong> {comp['alta']}</p>
                    <p>⚠️ <strong>Quando é baixa:</strong> {comp['baixa']}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Casos de interpretação
    st.markdown("#### 🔍 Casos para Interpretação")
    
    casos = [
        {
            "titulo": "Caso 1: ROE caiu, mas empresa melhorou?",
            "dados": {
                "Indicador": ["Margem Líquida", "Giro do Ativo", "Multiplicador", "ROE"],
                "2022": ["8%", "1,5x", "3,0x", "36%"],
                "2023": ["10%", "1,8x", "2,0x", "36%"]
            },
            "pergunta": "O ROE ficou igual. A empresa melhorou ou piorou?",
            "analise": """
                **A empresa MELHOROU significativamente:**
                - Margem subiu de 8% para 10% (melhor eficiência operacional)
                - Giro subiu de 1,5x para 1,8x (melhor uso dos ativos)
                - Alavancagem caiu de 3,0x para 2,0x (reduziu risco)
                - O ROE se manteve, mas agora é de melhor QUALIDADE
                - Antes: ROE dependia de dívida | Agora: ROE vem de operação
            """
        },
        {
            "titulo": "Caso 2: ROE subiu, mas é sustentável?",
            "dados": {
                "Indicador": ["Margem Líquida", "Giro do Ativo", "Multiplicador", "ROE"],
                "2022": ["5%", "2,0x", "2,5x", "25%"],
                "2023": ["4%", "1,8x", "4,2x", "30%"]
            },
            "pergunta": "O ROE subiu de 25% para 30%. Isso é bom?",
            "analise": """
                **ALERTA: ROE subiu, mas de forma INSUSTENTÁVEL:**
                - Margem CAIU de 5% para 4% (pior eficiência)
                - Giro CAIU de 2,0x para 1,8x (pior uso de ativos)
                - O aumento do ROE veio 100% da alavancagem (2,5x → 4,2x)
                - Empresa está mais arriscada
                - ROE de menor qualidade - depende de dívida
            """
        },
        {
            "titulo": "Caso 3: Comparando setores diferentes",
            "dados": {
                "Indicador": ["Margem Líquida", "Giro do Ativo", "Multiplicador", "ROE"],
                "Software": ["25%", "0,8x", "1,5x", "30%"],
                "Supermercado": ["2%", "3,5x", "4,3x", "30%"]
            },
            "pergunta": "Ambos têm ROE de 30%. Qual é melhor negócio?",
            "analise": """
                **São modelos de negócio completamente diferentes:**
                
                **Software:**
                - Alta margem (25%) - produto escalável, baixo custo marginal
                - Baixo giro (0,8x) - ativos intangíveis valiosos
                - Baixa alavancagem (1,5x) - não precisa de dívida
                - ROE vem da margem (qualidade alta)
                
                **Supermercado:**
                - Baixa margem (2%) - competição intensa, produtos commoditizados
                - Alto giro (3,5x) - estoque gira rápido, operação eficiente
                - Alta alavancagem (4,3x) - precisa de escala
                - ROE vem de giro e alavancagem (maior risco)
                
                **Conclusão:** Não existe "melhor" - são estratégias válidas para seus setores.
                O importante é comparar com peers do mesmo setor.
            """
        }
    ]
    
    for caso in casos:
        with st.expander(f"📌 {caso['titulo']}"):
            st.dataframe(pd.DataFrame(caso['dados']), use_container_width=True, hide_index=True)
            st.markdown(f"**❓ {caso['pergunta']}**")
            
            resposta = st.text_area("Sua interpretação:", key=f"interp_{caso['titulo'][:10]}", height=80)
            
            if st.button(f"Ver Análise", key=f"btn_{caso['titulo'][:10]}"):
                st.markdown(f"""
                    <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                        {caso['analise']}
                    </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Framework de análise
    st.markdown("#### 🎯 Framework de Interpretação")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px;'>
            <h4>Checklist para Interpretar Rentabilidade</h4>
            <ol>
                <li><strong>Qual é o nível do ROE?</strong> Compare com custo de capital e setor</li>
                <li><strong>De onde vem o ROE?</strong> Use DuPont para decompor</li>
                <li><strong>O ROE é sustentável?</strong> Verifique se vem de operação ou alavancagem</li>
                <li><strong>Como evoluiu?</strong> Analise tendência dos componentes</li>
                <li><strong>Faz sentido para o setor?</strong> Compare com modelo de negócio</li>
                <li><strong>Qual o risco associado?</strong> Maior ROE pode significar maior risco</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    # Quiz final
    st.markdown("---")
    st.markdown("#### ✅ Verificação de Aprendizado")
    
    quiz = st.radio(
        "Uma empresa teve aumento de ROE de 20% para 28%. A margem caiu de 10% para 8%, o giro ficou estável em 2x, e o multiplicador subiu de 1,0 para 1,75. Qual a interpretação correta?",
        options=[
            "A) Excelente! ROE subiu 40% - empresa está mais rentável",
            "B) O aumento do ROE veio exclusivamente da melhora operacional",
            "C) O ROE subiu, mas às custas de maior risco financeiro - qualidade piorou",
            "D) A empresa está mais eficiente no uso dos ativos"
        ],
        key="quiz_m10"
    )
    
    if st.button("Verificar", key="btn_quiz_m10"):
        if "C)" in quiz:
            st.success("""
                ✅ **Correto!** O ROE subiu, mas a análise DuPont revela que:
                - A margem PIOROU (10% → 8%)
                - O giro ficou igual (2x)
                - Todo o aumento veio da ALAVANCAGEM (1,0 → 1,75)
                
                Isso significa ROE de menor qualidade e maior risco. Se a dívida ficar 
                mais cara ou o EBIT cair, o ROE pode despencar rapidamente.
            """)
        else:
            st.error("""
                ❌ **Incorreto.** A resposta correta é C. 
                
                Veja a decomposição:
                - 2022: 10% × 2,0 × 1,0 = 20%
                - 2023: 8% × 2,0 × 1,75 = 28%
                
                O aumento de 8pp no ROE veio APENAS do maior endividamento, 
                enquanto a operação (margem) piorou. Isso é um sinal de alerta!
            """)
    
    # Síntese
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>ROE = Margem × Giro × Alavancagem:</strong> Cada componente conta uma história</li>
                <li><strong>Mesmo ROE, estratégias diferentes:</strong> DuPont revela o "como"</li>
                <li><strong>Qualidade importa:</strong> ROE de margem > ROE de alavancagem</li>
                <li><strong>Tendência importa:</strong> Analise evolução, não só foto</li>
                <li><strong>Contexto importa:</strong> Compare com setor e modelo de negócio</li>
                <li><strong>Risco importa:</strong> Maior ROE pode significar maior risco</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()