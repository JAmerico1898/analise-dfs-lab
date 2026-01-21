"""
Módulo 8 - Indicadores de Liquidez e Ciclo Financeiro
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Cálculo e interpretação de índices
- Estudo de caso: empresa em crescimento com crise de caixa
- Exercício aplicado de ciclo financeiro
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>💧 Módulo 8 - Indicadores de Liquidez e Ciclo Financeiro</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Calcular e interpretar os principais índices de liquidez</li>
                <li>Compreender o ciclo operacional e o ciclo financeiro (de caixa)</li>
                <li>Identificar situações de crise de liquidez em empresas em crescimento</li>
                <li>Propor soluções para problemas de capital de giro</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Índices de Liquidez",
        "📉 Caso: Crise de Caixa",
        "🔄 Ciclo Financeiro"
    ])
    
    with tab1:
        renderizar_indices_liquidez()
    
    with tab2:
        renderizar_caso_crise_caixa()
    
    with tab3:
        renderizar_ciclo_financeiro()


def renderizar_indices_liquidez():
    """Cálculo e interpretação de índices de liquidez."""
    
    st.markdown("### 📊 Cálculo e Interpretação de Índices de Liquidez")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Conceito:</strong><br>
            <em>Os índices de liquidez medem a capacidade da empresa de honrar suas obrigações 
            de curto e longo prazo, relacionando os recursos disponíveis com as dívidas.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Revisão dos Índices
    st.markdown("#### 📚 Os Quatro Índices de Liquidez")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>💧 Liquidez Corrente (LC)</h4>
                <p><strong>Fórmula:</strong> AC / PC</p>
                <p><strong>Indica:</strong> Capacidade de pagar dívidas de curto prazo com ativos circulantes</p>
                <p><strong>Referência:</strong> > 1,0 é desejável</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>🔥 Liquidez Seca (LS)</h4>
                <p><strong>Fórmula:</strong> (AC - Estoques) / PC</p>
                <p><strong>Indica:</strong> Capacidade de pagar sem depender da venda de estoques</p>
                <p><strong>Referência:</strong> > 0,8 é desejável</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>⚡ Liquidez Imediata (LI)</h4>
                <p><strong>Fórmula:</strong> Disponível / PC</p>
                <p><strong>Indica:</strong> Capacidade de pagar imediatamente com caixa</p>
                <p><strong>Referência:</strong> Varia muito por setor</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fce7f3; padding: 15px; border-radius: 10px;'>
                <h4>🏦 Liquidez Geral (LG)</h4>
                <p><strong>Fórmula:</strong> (AC + RLP) / (PC + PNC)</p>
                <p><strong>Indica:</strong> Capacidade de pagar todas as dívidas</p>
                <p><strong>Referência:</strong> > 1,0 indica solvência</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simulador
    st.markdown("#### 🧮 Simulador de Índices de Liquidez")
    
    st.markdown("Insira os dados do Balanço para calcular os índices:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Ativo Circulante**")
        caixa = st.number_input("Caixa e Equivalentes", min_value=0, value=50000, step=5000, key="liq_caixa")
        aplicacoes = st.number_input("Aplicações Financeiras", min_value=0, value=80000, step=5000, key="liq_aplic")
        clientes = st.number_input("Contas a Receber", min_value=0, value=150000, step=10000, key="liq_clientes")
        estoques = st.number_input("Estoques", min_value=0, value=120000, step=10000, key="liq_estoques")
        outros_ac = st.number_input("Outros AC", min_value=0, value=20000, step=5000, key="liq_outros_ac")
    
    with col2:
        st.markdown("**Ativo Não Circulante**")
        rlp = st.number_input("Realizável LP", min_value=0, value=45000, step=5000, key="liq_rlp")
        
        st.markdown("**Passivo Circulante**")
        fornecedores = st.number_input("Fornecedores", min_value=0, value=95000, step=5000, key="liq_fornec")
        emprest_cp = st.number_input("Empréstimos CP", min_value=0, value=85000, step=5000, key="liq_emp_cp")
        outros_pc = st.number_input("Outros PC", min_value=0, value=70000, step=5000, key="liq_outros_pc")
    
    with col3:
        st.markdown("**Passivo Não Circulante**")
        emprest_lp = st.number_input("Empréstimos LP", min_value=0, value=180000, step=10000, key="liq_emp_lp")
        outros_pnc = st.number_input("Outros PNC", min_value=0, value=50000, step=5000, key="liq_outros_pnc")
    
    # Cálculos
    ac = caixa + aplicacoes + clientes + estoques + outros_ac
    pc = fornecedores + emprest_cp + outros_pc
    pnc = emprest_lp + outros_pnc
    disponivel = caixa + aplicacoes
    
    lc = ac / pc if pc > 0 else 0
    ls = (ac - estoques) / pc if pc > 0 else 0
    li = disponivel / pc if pc > 0 else 0
    lg = (ac + rlp) / (pc + pnc) if (pc + pnc) > 0 else 0
    
    st.markdown("---")
    
    # Resultados
    st.markdown("#### 📈 Resultados Calculados")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        cor_lc = "#22c55e" if lc >= 1.0 else "#f97316" if lc >= 0.8 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_lc}20; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {cor_lc};'>
                <h4>Liquidez Corrente</h4>
                <h2 style='color: {cor_lc};'>{lc:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        cor_ls = "#22c55e" if ls >= 0.8 else "#f97316" if ls >= 0.5 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_ls}20; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {cor_ls};'>
                <h4>Liquidez Seca</h4>
                <h2 style='color: {cor_ls};'>{ls:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        cor_li = "#22c55e" if li >= 0.3 else "#f97316" if li >= 0.1 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_li}20; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {cor_li};'>
                <h4>Liquidez Imediata</h4>
                <h2 style='color: {cor_li};'>{li:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        cor_lg = "#22c55e" if lg >= 1.0 else "#f97316" if lg >= 0.8 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_lg}20; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {cor_lg};'>
                <h4>Liquidez Geral</h4>
                <h2 style='color: {cor_lg};'>{lg:.2f}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # Gráfico
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=['Liq. Corrente', 'Liq. Seca', 'Liq. Imediata', 'Liq. Geral'],
        y=[lc, ls, li, lg],
        marker_color=[cor_lc, cor_ls, cor_li, cor_lg],
        text=[f'{lc:.2f}', f'{ls:.2f}', f'{li:.2f}', f'{lg:.2f}'],
        textposition='outside'
    ))
    
    # Linha de referência
    fig.add_hline(y=1.0, line_dash="dash", line_color="gray", annotation_text="Referência = 1,0")
    
    fig.update_layout(title="Índices de Liquidez", height=350, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Interpretação automática
    st.markdown("#### 💡 Interpretação Automática")
    
    interpretacoes = []
    
    if lc >= 1.5:
        interpretacoes.append(("✅", "Liquidez Corrente confortável - empresa tem folga para pagar obrigações CP.", "#dcfce7"))
    elif lc >= 1.0:
        interpretacoes.append(("⚠️", "Liquidez Corrente adequada, mas com pouca margem de segurança.", "#fef3c7"))
    else:
        interpretacoes.append(("❌", "Liquidez Corrente insuficiente - risco de dificuldades no curto prazo.", "#fee2e2"))
    
    if ls >= 0.8:
        interpretacoes.append(("✅", "Liquidez Seca adequada - não depende criticamente da venda de estoques.", "#dcfce7"))
    elif ls >= 0.5:
        interpretacoes.append(("⚠️", "Liquidez Seca moderada - alguma dependência dos estoques.", "#fef3c7"))
    else:
        interpretacoes.append(("❌", "Liquidez Seca baixa - alta dependência da conversão de estoques em caixa.", "#fee2e2"))
    
    if lc - ls > 0.5:
        interpretacoes.append(("📦", f"Diferença LC - LS = {lc-ls:.2f} indica peso significativo dos estoques no AC.", "#e0e7ff"))
    
    if lg < 1.0:
        interpretacoes.append(("⚠️", "Liquidez Geral < 1 indica que dívidas totais superam ativos realizáveis.", "#fee2e2"))
    
    for emoji, texto, cor in interpretacoes:
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>
                {emoji} {texto}
            </div>
        """, unsafe_allow_html=True)


def renderizar_caso_crise_caixa():
    """Estudo de caso: empresa em crescimento com crise de caixa."""
    
    st.markdown("### 📉 Estudo de Caso: Crescimento com Crise de Caixa")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>🔍 Caso: TechGrow Comércio Eletrônico Ltda.</strong><br>
            <em>A empresa cresceu 80% em faturamento em 2 anos, mas agora enfrenta dificuldades 
            para pagar fornecedores e está à beira da insolvência. Como uma empresa que só cresce 
            pode estar quebrada?</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Evolução histórica
    st.markdown("#### 📊 Evolução Histórica (3 anos)")
    
    dados_historico = {
        "Indicador": [
            "Receita Líquida (R$ mil)", "Lucro Líquido (R$ mil)", "Margem Líquida (%)",
            "Ativo Circulante (R$ mil)", "Passivo Circulante (R$ mil)", "Liquidez Corrente",
            "Contas a Receber (R$ mil)", "Estoques (R$ mil)", "Fornecedores (R$ mil)",
            "Caixa (R$ mil)", "Empréstimos CP (R$ mil)"
        ],
        "2021": [2500, 125, 5.0, 850, 620, 1.37, 380, 320, 285, 95, 180],
        "2022": [3500, 140, 4.0, 1380, 1150, 1.20, 620, 520, 385, 65, 480],
        "2023": [4500, 135, 3.0, 1920, 2150, 0.89, 950, 780, 495, 25, 1250],
    }
    
    df_hist = pd.DataFrame(dados_historico)
    
    # Colorir células problemáticas
    st.dataframe(df_hist, use_container_width=True, hide_index=True)
    
    # Métricas de destaque
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Crescimento Receita", "+80%", delta="2 anos", delta_color="normal")
    with col2:
        st.metric("Lucro Líquido", "R$ 135 mil", delta="+8%", delta_color="normal")
    with col3:
        st.metric("Liquidez Corrente", "0,89", delta="-35%", delta_color="inverse")
    with col4:
        st.metric("Caixa", "R$ 25 mil", delta="-74%", delta_color="inverse")
    
    st.markdown("---")
    
    # Análise Gráfica
    st.markdown("#### 📈 Visualização do Problema")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de evolução
        anos = [2021, 2022, 2023]
        
        fig1 = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig1.add_trace(
            go.Bar(name='Receita', x=anos, y=[2500, 3500, 4500], marker_color='#3b82f6'),
            secondary_y=False
        )
        
        fig1.add_trace(
            go.Scatter(name='Liquidez Corrente', x=anos, y=[1.37, 1.20, 0.89], 
                      mode='lines+markers', line=dict(color='#ef4444', width=3)),
            secondary_y=True
        )
        
        fig1.add_hline(y=1.0, line_dash="dash", line_color="gray", secondary_y=True)
        
        fig1.update_layout(title="Receita vs Liquidez", height=350)
        fig1.update_yaxes(title_text="Receita (R$ mil)", secondary_y=False)
        fig1.update_yaxes(title_text="Liquidez Corrente", secondary_y=True)
        
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Composição do AC vs PC
        fig2 = go.Figure()
        
        fig2.add_trace(go.Bar(
            name='Ativo Circulante',
            x=anos,
            y=[850, 1380, 1920],
            marker_color='#22c55e'
        ))
        
        fig2.add_trace(go.Bar(
            name='Passivo Circulante',
            x=anos,
            y=[620, 1150, 2150],
            marker_color='#ef4444'
        ))
        
        fig2.update_layout(title="AC vs PC", barmode='group', height=350)
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Diagnóstico
    st.markdown("#### 🔍 Diagnóstico: Onde Está o Problema?")
    
    with st.expander("1️⃣ Análise do Capital de Giro", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Necessidade de Capital de Giro (NCG)**")
            
            ncg_2021 = (380 + 320) - 285
            ncg_2022 = (620 + 520) - 385
            ncg_2023 = (950 + 780) - 495
            
            st.markdown(f"""
                | Ano | Clientes + Estoques | Fornecedores | NCG |
                |-----|---------------------|--------------|-----|
                | 2021 | R$ 700 mil | R$ 285 mil | **R$ {ncg_2021} mil** |
                | 2022 | R$ 1.140 mil | R$ 385 mil | **R$ {ncg_2022} mil** |
                | 2023 | R$ 1.730 mil | R$ 495 mil | **R$ {ncg_2023} mil** |
            """)
        
        with col2:
            var_ncg = ncg_2023 - ncg_2021
            st.error(f"""
                **Problema Identificado:**
                
                A NCG aumentou **R$ {var_ncg} mil** em 2 anos (+197%)!
                
                A empresa precisou de R$ {var_ncg} mil ADICIONAIS só para 
                financiar seu capital de giro, mas não gerou esse caixa.
            """)
    
    with st.expander("2️⃣ De Onde Veio o Dinheiro?"):
        st.markdown("""
            **Fontes de Financiamento do Crescimento:**
            
            | Fonte | 2021 | 2023 | Variação |
            |-------|------|------|----------|
            | Fornecedores | R$ 285 mil | R$ 495 mil | +R$ 210 mil |
            | Empréstimos CP | R$ 180 mil | R$ 1.250 mil | **+R$ 1.070 mil** |
            | Caixa consumido | R$ 95 mil | R$ 25 mil | -R$ 70 mil |
            
            **Conclusão:** O crescimento foi financiado com dívida de curto prazo cara, 
            não com geração de caixa operacional!
        """)
    
    with st.expander("3️⃣ O Ciclo Vicioso"):
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>🔄 O Ciclo do Efeito Tesoura</h4>
                <ol>
                    <li>Empresa cresce vendas → Precisa de mais estoque e concede mais prazo</li>
                    <li>NCG aumenta → Precisa de financiamento</li>
                    <li>Toma empréstimo caro de curto prazo → Despesa financeira sobe</li>
                    <li>Margem cai → Menos geração de caixa</li>
                    <li>Precisa de mais empréstimo → Ciclo se repete</li>
                    <li>Até que... não consegue mais crédito = CRISE!</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
        
        # Gráfico do Efeito Tesoura
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=[2021, 2022, 2023],
            y=[ncg_2021, ncg_2022, ncg_2023],
            name='NCG',
            line=dict(color='#ef4444', width=3),
            mode='lines+markers'
        ))
        
        fig.add_trace(go.Scatter(
            x=[2021, 2022, 2023],
            y=[95-180, 65-480, 25-1250],  # CDG = Caixa - Empréstimos CP
            name='CDG (simplificado)',
            line=dict(color='#3b82f6', width=3),
            mode='lines+markers'
        ))
        
        fig.update_layout(
            title="Efeito Tesoura: NCG crescendo, CDG caindo",
            height=300,
            yaxis_title="R$ mil"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Exercício
    st.markdown("#### 📝 Sua Análise")
    
    q1 = st.text_area(
        "1. Por que uma empresa lucrativa pode ter crise de caixa?",
        placeholder="Explique o paradoxo...",
        height=80,
        key="crise_q1"
    )
    
    q2 = st.text_area(
        "2. Quais medidas você recomendaria para a TechGrow sair dessa situação?",
        placeholder="Liste suas recomendações...",
        height=100,
        key="crise_q2"
    )
    
    if st.button("Ver Análise do Professor", key="btn_crise"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Por que lucro não significa caixa:</strong></p>
                <ul>
                    <li>Lucro é regime de competência; caixa é regime de caixa</li>
                    <li>Vender a prazo gera lucro mas não gera caixa imediato</li>
                    <li>Crescimento rápido exige investimento em capital de giro ANTES de gerar retorno</li>
                    <li>A margem líquida caindo (5% → 3%) não gera caixa suficiente para financiar o crescimento</li>
                </ul>
                
                <p><strong>2. Recomendações para TechGrow:</strong></p>
                <ul>
                    <li><strong>Curto prazo:</strong>
                        <ul>
                            <li>Renegociar dívidas - alongar perfil</li>
                            <li>Vender ativos não essenciais</li>
                            <li>Antecipar recebíveis (factoring/FIDC)</li>
                            <li>Buscar aporte de capital</li>
                        </ul>
                    </li>
                    <li><strong>Médio prazo:</strong>
                        <ul>
                            <li>Reduzir prazos de recebimento</li>
                            <li>Otimizar níveis de estoque</li>
                            <li>Negociar prazos maiores com fornecedores</li>
                            <li>Desacelerar crescimento até normalizar capital de giro</li>
                        </ul>
                    </li>
                    <li><strong>Estrutural:</strong>
                        <ul>
                            <li>Melhorar margens (revisar preços e custos)</li>
                            <li>Financiar crescimento com capital próprio ou dívida LP</li>
                            <li>Monitorar NCG como indicador-chave</li>
                        </ul>
                    </li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def renderizar_ciclo_financeiro():
    """Exercício aplicado de ciclo financeiro."""
    
    st.markdown("### 🔄 Exercício Aplicado: Ciclo Operacional e Financeiro")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Conceitos-Chave:</strong><br>
            <ul>
                <li><strong>PME (Prazo Médio de Estocagem):</strong> Tempo que mercadoria fica em estoque</li>
                <li><strong>PMR (Prazo Médio de Recebimento):</strong> Tempo para receber dos clientes</li>
                <li><strong>PMP (Prazo Médio de Pagamento):</strong> Tempo para pagar fornecedores</li>
                <li><strong>Ciclo Operacional:</strong> PME + PMR (compra até recebimento)</li>
                <li><strong>Ciclo Financeiro:</strong> PME + PMR - PMP (necessidade de financiamento)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Fórmulas
    st.markdown("#### 📐 Fórmulas de Cálculo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.latex(r"PME = \frac{Estoques}{CMV} \times 360")
    with col2:
        st.latex(r"PMR = \frac{Clientes}{Receita} \times 360")
    with col3:
        st.latex(r"PMP = \frac{Fornecedores}{Compras} \times 360")
    
    st.markdown("---")
    
    # Simulador
    st.markdown("#### 🧮 Simulador de Ciclo Financeiro")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Dados do Balanço (saldos médios)**")
        estoques = st.number_input("Estoques (R$)", min_value=0, value=500000, step=50000, key="cf_est")
        clientes = st.number_input("Contas a Receber (R$)", min_value=0, value=600000, step=50000, key="cf_cli")
        fornecedores = st.number_input("Fornecedores (R$)", min_value=0, value=350000, step=50000, key="cf_forn")
    
    with col2:
        st.markdown("**Dados da DRE (anuais)**")
        receita = st.number_input("Receita Líquida (R$)", min_value=0, value=4800000, step=100000, key="cf_rec")
        cmv = st.number_input("CMV (R$)", min_value=0, value=3200000, step=100000, key="cf_cmv")
        compras = st.number_input("Compras (R$)", min_value=0, value=3400000, step=100000, key="cf_comp")
    
    # Cálculos
    pme = (estoques / cmv * 360) if cmv > 0 else 0
    pmr = (clientes / receita * 360) if receita > 0 else 0
    pmp = (fornecedores / compras * 360) if compras > 0 else 0
    
    ciclo_operacional = pme + pmr
    ciclo_financeiro = pme + pmr - pmp
    
    st.markdown("---")
    
    # Resultados
    st.markdown("#### 📊 Resultados")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("PME (Estocagem)", f"{pme:.0f} dias")
        st.metric("PMR (Recebimento)", f"{pmr:.0f} dias")
        st.metric("PMP (Pagamento)", f"{pmp:.0f} dias")
    
    with col2:
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Ciclo Operacional</h4>
                <h2>{ciclo_operacional:.0f} dias</h2>
                <p>PME + PMR</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        cor_cf = "#22c55e" if ciclo_financeiro < 30 else "#f97316" if ciclo_financeiro < 60 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_cf}20; padding: 20px; border-radius: 10px; text-align: center; border: 2px solid {cor_cf};'>
                <h4>Ciclo Financeiro</h4>
                <h2 style='color: {cor_cf};'>{ciclo_financeiro:.0f} dias</h2>
                <p>PME + PMR - PMP</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Visualização do Ciclo
    st.markdown("#### 📈 Visualização do Ciclo")
    
    # Diagrama de tempo
    fig = go.Figure()
    
    # PME (Estocagem)
    fig.add_trace(go.Bar(
        y=['Ciclo'],
        x=[pme],
        name=f'PME: {pme:.0f} dias',
        orientation='h',
        marker_color='#f97316',
        text=f'Estocagem: {pme:.0f}d',
        textposition='inside'
    ))
    
    # PMR (Recebimento)
    fig.add_trace(go.Bar(
        y=['Ciclo'],
        x=[pmr],
        name=f'PMR: {pmr:.0f} dias',
        orientation='h',
        marker_color='#3b82f6',
        text=f'Recebimento: {pmr:.0f}d',
        textposition='inside'
    ))
    
    # PMP (Pagamento) - como desconto
    fig.add_trace(go.Bar(
        y=['Ciclo'],
        x=[-pmp],
        name=f'PMP: {pmp:.0f} dias',
        orientation='h',
        marker_color='#22c55e',
        text=f'Pagamento: {pmp:.0f}d',
        textposition='inside'
    ))
    
    fig.update_layout(
        barmode='relative',
        title=f"Linha do Tempo do Ciclo (Ciclo Financeiro = {ciclo_financeiro:.0f} dias)",
        xaxis_title="Dias",
        height=200,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Interpretação
    st.markdown("#### 💡 Interpretação")
    
    if ciclo_financeiro < 0:
        st.success(f"""
            ✅ **Ciclo Financeiro Negativo ({ciclo_financeiro:.0f} dias)**
            
            A empresa recebe dos clientes ANTES de pagar os fornecedores!
            Isso significa que ela é financiada pelos fornecedores - situação ideal.
            Comum em supermercados e varejo de conveniência.
        """)
    elif ciclo_financeiro < 30:
        st.success(f"""
            ✅ **Ciclo Financeiro Curto ({ciclo_financeiro:.0f} dias)**
            
            A empresa precisa financiar apenas {ciclo_financeiro:.0f} dias de operação.
            Necessidade de capital de giro relativamente baixa.
        """)
    elif ciclo_financeiro < 60:
        st.warning(f"""
            ⚠️ **Ciclo Financeiro Moderado ({ciclo_financeiro:.0f} dias)**
            
            A empresa precisa financiar {ciclo_financeiro:.0f} dias de operação.
            Necessidade relevante de capital de giro - monitorar.
        """)
    else:
        st.error(f"""
            ❌ **Ciclo Financeiro Longo ({ciclo_financeiro:.0f} dias)**
            
            A empresa precisa financiar {ciclo_financeiro:.0f} dias de operação!
            Alta necessidade de capital de giro - risco de liquidez.
            Recomenda-se ação para reduzir PME/PMR ou aumentar PMP.
        """)
    
    st.markdown("---")
    
    # Exercício prático
    st.markdown("#### 📝 Exercício: Simulação de Melhorias")
    
    st.markdown("""
        A diretoria quer reduzir o ciclo financeiro. Simule o impacto das seguintes ações:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        reducao_pme = st.slider("Reduzir PME em (dias):", 0, 30, 0, key="red_pme")
    with col2:
        reducao_pmr = st.slider("Reduzir PMR em (dias):", 0, 30, 0, key="red_pmr")
    with col3:
        aumento_pmp = st.slider("Aumentar PMP em (dias):", 0, 30, 0, key="aum_pmp")
    
    novo_cf = ciclo_financeiro - reducao_pme - reducao_pmr - aumento_pmp
    melhoria = ciclo_financeiro - novo_cf
    
    # Cálculo da liberação de caixa
    receita_diaria = receita / 360
    liberacao_caixa = melhoria * receita_diaria
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Ciclo Financeiro Atual", f"{ciclo_financeiro:.0f} dias")
        st.metric("Novo Ciclo Financeiro", f"{novo_cf:.0f} dias", delta=f"-{melhoria:.0f} dias")
    
    with col2:
        st.metric("Melhoria Total", f"{melhoria:.0f} dias")
        st.metric("Liberação de Caixa Estimada", f"R$ {liberacao_caixa:,.0f}")
    
    if melhoria > 0:
        st.success(f"""
            💰 **Impacto Estimado:**
            
            Reduzindo o ciclo financeiro em {melhoria:.0f} dias, a empresa liberaria 
            aproximadamente **R$ {liberacao_caixa:,.0f}** em capital de giro, que poderia 
            ser usado para reduzir dívidas ou investir no crescimento.
        """)
    
    # Síntese
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Liquidez ≠ Rentabilidade:</strong> Empresa lucrativa pode ter crise de caixa</li>
                <li><strong>Crescimento consome caixa:</strong> NCG aumenta com o faturamento</li>
                <li><strong>Ciclo Financeiro:</strong> Quanto menor, menor a necessidade de financiamento</li>
                <li><strong>Efeito Tesoura:</strong> NCG crescendo mais que CDG = caminho para insolvência</li>
                <li><strong>Gestão de Capital de Giro:</strong> Essencial para sustentabilidade do negócio</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()