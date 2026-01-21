"""
Módulo 6 - Demonstração dos Fluxos de Caixa
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Exercício guiado: reconstrução do fluxo de caixa a partir da DRE e balanço
- Caso prático: empresa lucrativa com caixa negativo
- Questionário aplicado (formativo)
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>💵 Módulo 6 - Demonstração dos Fluxos de Caixa</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Reconstruir a DFC a partir da DRE e variações do Balanço</li>
                <li>Compreender a diferença entre lucro e geração de caixa</li>
                <li>Analisar os três componentes do fluxo de caixa (operacional, investimento, financiamento)</li>
                <li>Identificar situações de empresas lucrativas com problemas de caixa</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🔧 Reconstrução da DFC",
        "📉 Caso: Lucro sem Caixa",
        "📝 Questionário Formativo"
    ])
    
    with tab1:
        renderizar_reconstrucao_dfc()
    
    with tab2:
        renderizar_caso_lucro_sem_caixa()
    
    with tab3:
        renderizar_questionario()


def get_dados_empresa():
    """Retorna os dados da empresa exemplo para reconstrução da DFC."""
    
    dados = {
        "empresa": "Tech Solutions Ltda.",
        "balanco": {
            "2022": {
                "Caixa": 150000,
                "Clientes": 280000,
                "Estoques": 120000,
                "Despesas Antecipadas": 15000,
                "Imobilizado Bruto": 500000,
                "Depreciação Acumulada": -150000,
                "Total Ativo": 915000,
                "Fornecedores": 95000,
                "Salários a Pagar": 45000,
                "Impostos a Pagar": 35000,
                "Empréstimos CP": 80000,
                "Empréstimos LP": 200000,
                "Capital Social": 300000,
                "Reservas de Lucros": 160000,
                "Total Passivo + PL": 915000
            },
            "2023": {
                "Caixa": 85000,
                "Clientes": 420000,
                "Estoques": 180000,
                "Despesas Antecipadas": 20000,
                "Imobilizado Bruto": 650000,
                "Depreciação Acumulada": -200000,
                "Total Ativo": 1155000,
                "Fornecedores": 110000,
                "Salários a Pagar": 55000,
                "Impostos a Pagar": 40000,
                "Empréstimos CP": 120000,
                "Empréstimos LP": 280000,
                "Capital Social": 350000,
                "Reservas de Lucros": 200000,
                "Total Passivo + PL": 1155000
            }
        },
        "dre_2023": {
            "Receita Líquida": 1200000,
            "CMV": -720000,
            "Lucro Bruto": 480000,
            "Despesas Operacionais": -280000,
            "Depreciação": -50000,
            "EBIT": 150000,
            "Despesas Financeiras": -45000,
            "LAIR": 105000,
            "IR/CS": -35700,
            "Lucro Líquido": 69300
        },
        "info_adicional": {
            "Dividendos Pagos": 29300,
            "Aquisição Imobilizado": 150000,
            "Aumento Capital": 50000
        }
    }
    return dados


def renderizar_reconstrucao_dfc():
    """Exercício guiado de reconstrução da DFC."""
    
    st.markdown("### 🔧 Exercício Guiado: Reconstrução da DFC")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Aprender a reconstruir a Demonstração dos Fluxos de Caixa (método indireto) 
            a partir da DRE e das variações do Balanço Patrimonial.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_empresa()
    
    st.markdown(f"**Empresa:** {dados['empresa']}")
    
    # Exibir demonstrações base
    st.markdown("#### 📋 Dados Base para Análise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Balanço Patrimonial")
        
        df_balanco = pd.DataFrame({
            "Conta": list(dados['balanco']['2022'].keys()),
            "2022": [f"R$ {v:,.0f}" for v in dados['balanco']['2022'].values()],
            "2023": [f"R$ {v:,.0f}" for v in dados['balanco']['2023'].values()]
        })
        st.dataframe(df_balanco, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("##### DRE 2023")
        
        df_dre = pd.DataFrame({
            "Conta": list(dados['dre_2023'].keys()),
            "Valor": [f"R$ {v:,.0f}" for v in dados['dre_2023'].values()]
        })
        st.dataframe(df_dre, use_container_width=True, hide_index=True)
        
        st.markdown("##### Informações Adicionais")
        for info, valor in dados['info_adicional'].items():
            st.markdown(f"- {info}: R$ {valor:,.0f}")
    
    st.markdown("---")
    
    # Método Indireto - Passo a passo
    st.markdown("#### 🔄 Método Indireto: Passo a Passo")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            <strong>O Método Indireto parte do Lucro Líquido e faz ajustes:</strong>
            <ol>
                <li>Adiciona despesas não-caixa (depreciação, amortização)</li>
                <li>Ajusta variações de ativos e passivos operacionais</li>
                <li>Resultado = Caixa Gerado pelas Operações</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    # Calculando variações
    var = {}
    for conta in dados['balanco']['2022'].keys():
        var[conta] = dados['balanco']['2023'][conta] - dados['balanco']['2022'][conta]
    
    # FLUXO OPERACIONAL
    st.markdown("##### 1️⃣ Fluxo de Caixa Operacional")
    
    with st.expander("Passo 1: Partir do Lucro Líquido", expanded=True):
        lucro_liquido = dados['dre_2023']['Lucro Líquido']
        st.metric("Lucro Líquido", f"R$ {lucro_liquido:,.0f}")
        st.info("Este é o ponto de partida do método indireto.")
    
    with st.expander("Passo 2: Adicionar Despesas Não-Caixa"):
        depreciacao = abs(dados['dre_2023']['Depreciação'])
        st.metric("(+) Depreciação", f"R$ {depreciacao:,.0f}")
        st.info("Depreciação reduz o lucro mas não sai do caixa. Devemos adicionar de volta.")
    
    with st.expander("Passo 3: Ajustar Variações de Ativos Operacionais"):
        st.markdown("**Regra:** ↑ Ativo = Uso de caixa (subtrai) | ↓ Ativo = Fonte de caixa (soma)")
        
        var_clientes = var['Clientes']
        var_estoques = var['Estoques']
        var_desp_antec = var['Despesas Antecipadas']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            sinal = "-" if var_clientes > 0 else "+"
            st.metric("Δ Clientes", f"{sinal} R$ {abs(var_clientes):,.0f}")
        with col2:
            sinal = "-" if var_estoques > 0 else "+"
            st.metric("Δ Estoques", f"{sinal} R$ {abs(var_estoques):,.0f}")
        with col3:
            sinal = "-" if var_desp_antec > 0 else "+"
            st.metric("Δ Desp. Antecipadas", f"{sinal} R$ {abs(var_desp_antec):,.0f}")
        
        st.warning(f"""
            **Interpretação:**
            - Clientes aumentou R$ {var_clientes:,.0f} → vendeu a prazo, não recebeu em caixa
            - Estoques aumentou R$ {var_estoques:,.0f} → comprou mais do que vendeu
            - Desp. Antecipadas aumentou R$ {var_desp_antec:,.0f} → pagou adiantado
        """)
    
    with st.expander("Passo 4: Ajustar Variações de Passivos Operacionais"):
        st.markdown("**Regra:** ↑ Passivo = Fonte de caixa (soma) | ↓ Passivo = Uso de caixa (subtrai)")
        
        var_fornec = var['Fornecedores']
        var_salarios = var['Salários a Pagar']
        var_impostos = var['Impostos a Pagar']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            sinal = "+" if var_fornec > 0 else "-"
            st.metric("Δ Fornecedores", f"{sinal} R$ {abs(var_fornec):,.0f}")
        with col2:
            sinal = "+" if var_salarios > 0 else "-"
            st.metric("Δ Salários a Pagar", f"{sinal} R$ {abs(var_salarios):,.0f}")
        with col3:
            sinal = "+" if var_impostos > 0 else "-"
            st.metric("Δ Impostos a Pagar", f"{sinal} R$ {abs(var_impostos):,.0f}")
        
        st.success(f"""
            **Interpretação:**
            - Fornecedores aumentou R$ {var_fornec:,.0f} → comprou a prazo, não pagou
            - Salários aumentou R$ {var_salarios:,.0f} → deve mais salários
            - Impostos aumentou R$ {var_impostos:,.0f} → deve mais impostos
        """)
    
    # Cálculo do Fluxo Operacional
    fluxo_operacional = (lucro_liquido + depreciacao 
                        - var_clientes - var_estoques - var_desp_antec
                        + var_fornec + var_salarios + var_impostos)
    
    st.markdown(f"""
        <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; margin-top: 15px;'>
            <strong>📊 Fluxo de Caixa Operacional:</strong><br>
            {lucro_liquido:,.0f} + {depreciacao:,.0f} - {var_clientes:,.0f} - {var_estoques:,.0f} - {var_desp_antec:,.0f} 
            + {var_fornec:,.0f} + {var_salarios:,.0f} + {var_impostos:,.0f} = <strong>R$ {fluxo_operacional:,.0f}</strong>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FLUXO DE INVESTIMENTO
    st.markdown("##### 2️⃣ Fluxo de Caixa de Investimento")
    
    with st.expander("Atividades de Investimento"):
        aquisicao_imob = dados['info_adicional']['Aquisição Imobilizado']
        
        st.metric("(-) Aquisição de Imobilizado", f"R$ {aquisicao_imob:,.0f}")
        st.info("Compra de ativos fixos representa saída de caixa para investimento.")
        
        fluxo_investimento = -aquisicao_imob
        
        st.markdown(f"""
            <div style='background-color: #fce7f3; padding: 15px; border-radius: 10px;'>
                <strong>📊 Fluxo de Caixa de Investimento: R$ {fluxo_investimento:,.0f}</strong>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # FLUXO DE FINANCIAMENTO
    st.markdown("##### 3️⃣ Fluxo de Caixa de Financiamento")
    
    with st.expander("Atividades de Financiamento"):
        var_emprest_cp = var['Empréstimos CP']
        var_emprest_lp = var['Empréstimos LP']
        aumento_capital = dados['info_adicional']['Aumento Capital']
        dividendos = dados['info_adicional']['Dividendos Pagos']
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("(+) Novos Empréstimos CP", f"R$ {var_emprest_cp:,.0f}")
            st.metric("(+) Novos Empréstimos LP", f"R$ {var_emprest_lp:,.0f}")
        with col2:
            st.metric("(+) Aumento de Capital", f"R$ {aumento_capital:,.0f}")
            st.metric("(-) Dividendos Pagos", f"R$ {dividendos:,.0f}")
        
        fluxo_financiamento = var_emprest_cp + var_emprest_lp + aumento_capital - dividendos
        
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <strong>📊 Fluxo de Caixa de Financiamento: R$ {fluxo_financiamento:,.0f}</strong>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # RESUMO FINAL
    st.markdown("#### 📋 DFC Reconstruída - Resumo")
    
    variacao_caixa = fluxo_operacional + fluxo_investimento + fluxo_financiamento
    caixa_inicial = dados['balanco']['2022']['Caixa']
    caixa_final = caixa_inicial + variacao_caixa
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        df_dfc = pd.DataFrame({
            "Componente": [
                "Fluxo de Caixa Operacional",
                "Fluxo de Caixa de Investimento",
                "Fluxo de Caixa de Financiamento",
                "= Variação Líquida do Caixa",
                "Caixa Inicial",
                "= Caixa Final"
            ],
            "Valor (R$)": [
                f"{fluxo_operacional:,.0f}",
                f"{fluxo_investimento:,.0f}",
                f"{fluxo_financiamento:,.0f}",
                f"{variacao_caixa:,.0f}",
                f"{caixa_inicial:,.0f}",
                f"{caixa_final:,.0f}"
            ]
        })
        st.dataframe(df_dfc, use_container_width=True, hide_index=True)
    
    with col2:
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(
                x=['Operacional', 'Investimento', 'Financiamento'],
                y=[fluxo_operacional, fluxo_investimento, fluxo_financiamento],
                marker_color=['#22c55e' if fluxo_operacional > 0 else '#ef4444',
                             '#22c55e' if fluxo_investimento > 0 else '#ef4444',
                             '#22c55e' if fluxo_financiamento > 0 else '#ef4444']
            )
        ])
        fig.update_layout(title="Componentes da DFC", height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Verificação
    caixa_real = dados['balanco']['2023']['Caixa']
    if abs(caixa_final - caixa_real) < 1:
        st.success(f"✅ Verificação: Caixa Final calculado (R$ {caixa_final:,.0f}) = Caixa no Balanço (R$ {caixa_real:,.0f})")
    else:
        st.error(f"❌ Diferença encontrada: Calculado R$ {caixa_final:,.0f} vs Balanço R$ {caixa_real:,.0f}")


def renderizar_caso_lucro_sem_caixa():
    """Caso prático: empresa lucrativa com caixa negativo."""
    
    st.markdown("### 📉 Caso Prático: Empresa Lucrativa com Caixa Negativo")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>🔍 Caso: Crescimento Acelerado S.A.</strong><br>
            <em>A empresa reportou lucro líquido de R$ 2 milhões, mas encerrou o ano com saldo 
            negativo na conta bancária e precisou de empréstimo emergencial. Como isso é possível?</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados do caso
    st.markdown("#### 📊 Demonstrações da Empresa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### DRE do Período")
        dre_caso = {
            "Receita Líquida": 15000000,
            "(-) CMV": -9000000,
            "= Lucro Bruto": 6000000,
            "(-) Despesas Operacionais": -3200000,
            "(-) Depreciação": -300000,
            "= EBIT": 2500000,
            "(-) Despesas Financeiras": -200000,
            "= LAIR": 2300000,
            "(-) IR/CS": -300000,
            "= Lucro Líquido": 2000000
        }
        
        for conta, valor in dre_caso.items():
            if conta.startswith("="):
                st.markdown(f"**{conta}: R$ {valor/1000:,.0f} mil**")
            else:
                st.markdown(f"{conta}: R$ {valor/1000:,.0f} mil")
    
    with col2:
        st.markdown("##### Variações do Balanço")
        variacoes = {
            "Δ Clientes": 4500000,
            "Δ Estoques": 2800000,
            "Δ Fornecedores": 800000,
            "Δ Salários/Impostos": 200000,
            "Investimentos (CAPEX)": -3500000,
            "Dividendos Pagos": -1200000,
            "Novos Empréstimos": 1500000,
        }
        
        for item, valor in variacoes.items():
            cor = "#22c55e" if valor > 0 else "#ef4444"
            sinal = "+" if valor > 0 else ""
            st.markdown(f"{item}: <span style='color:{cor}'>{sinal}R$ {valor/1000:,.0f} mil</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Reconstrução da DFC
    st.markdown("#### 🔄 Reconstruindo o Fluxo de Caixa")
    
    # Fluxo Operacional
    st.markdown("##### Fluxo Operacional")
    
    lucro = 2000000
    depreciacao = 300000
    var_clientes = -4500000  # Aumento de ativo = uso de caixa
    var_estoques = -2800000
    var_fornec = 800000  # Aumento de passivo = fonte de caixa
    var_outros = 200000
    
    fco = lucro + depreciacao + var_clientes + var_estoques + var_fornec + var_outros
    
    df_fco = pd.DataFrame({
        "Item": ["Lucro Líquido", "(+) Depreciação", "(−) Δ Clientes", "(−) Δ Estoques", 
                "(+) Δ Fornecedores", "(+) Δ Outros Passivos", "= FCO"],
        "Valor (R$ mil)": [2000, 300, -4500, -2800, 800, 200, fco/1000]
    })
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.dataframe(df_fco, use_container_width=True, hide_index=True)
    
    with col2:
        cor_fco = "#22c55e" if fco > 0 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_fco}20; padding: 20px; border-radius: 10px; text-align: center;'>
                <h3 style='color: {cor_fco};'>FCO</h3>
                <h2 style='color: {cor_fco};'>R$ {fco/1000:,.0f} mil</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # Fluxo de Investimento e Financiamento
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Fluxo de Investimento")
        fci = -3500000
        st.metric("CAPEX (Investimentos)", f"R$ {fci/1000:,.0f} mil")
    
    with col2:
        st.markdown("##### Fluxo de Financiamento")
        fcf = 1500000 - 1200000  # Empréstimos - Dividendos
        st.metric("Empréstimos - Dividendos", f"R$ {fcf/1000:,.0f} mil")
    
    # Resultado Final
    variacao_total = fco + fci + fcf
    
    st.markdown("---")
    st.markdown("#### 📋 Resumo da Situação")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Lucro Líquido", "R$ 2.000 mil", delta="Positivo")
    with col2:
        st.metric("FCO", f"R$ {fco/1000:,.0f} mil", delta="Negativo!", delta_color="inverse")
    with col3:
        st.metric("FCI", f"R$ {fci/1000:,.0f} mil", delta="Investindo")
    with col4:
        st.metric("Variação Caixa", f"R$ {variacao_total/1000:,.0f} mil", delta="Queimando Caixa!", delta_color="inverse")
    
    # Gráfico Waterfall
    fig = go.Figure(go.Waterfall(
        name="DFC",
        orientation="v",
        measure=["absolute", "relative", "relative", "relative", "relative", "relative", "total"],
        x=["Lucro Líq.", "Deprec.", "Δ Clientes", "Δ Estoques", "Δ Passivos Op.", "Invest./Financ.", "Var. Caixa"],
        y=[2000, 300, -4500, -2800, 1000, -3200, variacao_total/1000],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#ef4444"}},
        increasing={"marker": {"color": "#22c55e"}},
        totals={"marker": {"color": "#3b82f6"}}
    ))
    
    fig.update_layout(title="Do Lucro à Variação de Caixa (R$ mil)", height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Análise das causas
    st.markdown("#### 🔍 Análise: Por que lucro não virou caixa?")
    
    causas = [
        {
            "causa": "Crescimento Acelerado de Vendas a Prazo",
            "impacto": "R$ 4,5 milhões",
            "explicacao": "A empresa cresceu vendas em 50%, mas 90% foi a prazo. Reconheceu receita (lucro) mas não recebeu em caixa.",
            "cor": "#fee2e2"
        },
        {
            "causa": "Acúmulo de Estoques",
            "impacto": "R$ 2,8 milhões",
            "explicacao": "Para suportar o crescimento, aumentou estoques significativamente. Pagou fornecedores mas não vendeu tudo.",
            "cor": "#fef3c7"
        },
        {
            "causa": "Investimentos Pesados (CAPEX)",
            "impacto": "R$ 3,5 milhões",
            "explicacao": "Expandiu capacidade produtiva. Investimento necessário, mas consome caixa no curto prazo.",
            "cor": "#e0e7ff"
        },
        {
            "causa": "Distribuição de Dividendos",
            "impacto": "R$ 1,2 milhões",
            "explicacao": "Distribuiu dividendos mesmo sem geração de caixa operacional positiva. Decisão questionável.",
            "cor": "#fce7f3"
        }
    ]
    
    for causa in causas:
        st.markdown(f"""
            <div style='background-color: {causa["cor"]}; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <strong>{causa["causa"]}</strong> - Impacto: {causa["impacto"]}<br>
                <small>{causa["explicacao"]}</small>
            </div>
        """, unsafe_allow_html=True)
    
    # Lições
    st.markdown("---")
    st.markdown("#### 📝 Sua Análise do Caso")
    
    q1 = st.text_area(
        "1. A empresa deveria ter distribuído dividendos nessa situação? Justifique.",
        placeholder="Desenvolva sua análise...",
        height=80,
        key="caso_q1"
    )
    
    q2 = st.text_area(
        "2. Quais indicadores de alerta deveriam ter sido monitorados?",
        placeholder="Liste os indicadores...",
        height=80,
        key="caso_q2"
    )
    
    q3 = st.text_area(
        "3. O que a empresa deveria fazer para sair dessa situação?",
        placeholder="Suas recomendações...",
        height=80,
        key="caso_q3"
    )
    
    if st.button("Ver Análise do Professor", key="btn_caso_prof"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Dividendos:</strong> NÃO deveria ter distribuído. Com FCO negativo, os dividendos 
                foram pagos com empréstimo. Isso é insustentável e aumenta o risco financeiro.</p>
                
                <p><strong>2. Indicadores de Alerta:</strong></p>
                <ul>
                    <li>Ciclo de Conversão de Caixa (CCC) - estava aumentando</li>
                    <li>Prazo Médio de Recebimento (PMR) - acima do setor</li>
                    <li>FCO/Lucro Líquido - deveria ser > 1, estava negativo</li>
                    <li>Cobertura de Dívida - deteriorando</li>
                </ul>
                
                <p><strong>3. Recomendações:</strong></p>
                <ul>
                    <li>Reduzir prazo de recebimento ou oferecer desconto para antecipação</li>
                    <li>Otimizar níveis de estoque (just-in-time)</li>
                    <li>Suspender dividendos até normalização do FCO</li>
                    <li>Revisar plano de CAPEX - priorizar investimentos essenciais</li>
                    <li>Renegociar prazos com fornecedores</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def renderizar_questionario():
    """Questionário aplicado (formativo)."""
    
    st.markdown("### 📝 Questionário Formativo")
    
    st.markdown("""
        <div style='background-color: #f0fdf4; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #22c55e; margin-bottom: 20px;'>
            <strong>Instruções:</strong><br>
            <em>Este questionário tem caráter formativo. Responda todas as questões e verifique 
            seu aprendizado sobre a Demonstração dos Fluxos de Caixa.</em>
        </div>
    """, unsafe_allow_html=True)
    
    if 'respostas_m6' not in st.session_state:
        st.session_state.respostas_m6 = {}
    if 'verificado_m6' not in st.session_state:
        st.session_state.verificado_m6 = False
    
    questoes = [
        {
            "id": 1,
            "pergunta": "No método indireto de elaboração da DFC, o ponto de partida é:",
            "opcoes": [
                "A) O saldo inicial de caixa",
                "B) A receita líquida de vendas",
                "C) O lucro líquido do exercício",
                "D) O EBITDA"
            ],
            "correta": "C",
            "explicacao": "O método indireto parte do lucro líquido e faz ajustes para chegar ao caixa gerado pelas operações."
        },
        {
            "id": 2,
            "pergunta": "Um aumento nas contas a receber (Clientes) representa, na DFC pelo método indireto:",
            "opcoes": [
                "A) Adição ao lucro líquido",
                "B) Subtração do lucro líquido",
                "C) Não afeta o fluxo operacional",
                "D) Fluxo de investimento"
            ],
            "correta": "B",
            "explicacao": "Aumento de Clientes significa que houve venda (receita/lucro) sem recebimento em caixa. Logo, deve ser subtraído."
        },
        {
            "id": 3,
            "pergunta": "A depreciação é adicionada ao lucro líquido na DFC porque:",
            "opcoes": [
                "A) Representa entrada de caixa",
                "B) É uma despesa que não representa saída de caixa",
                "C) Aumenta o valor dos ativos",
                "D) É um investimento da empresa"
            ],
            "correta": "B",
            "explicacao": "A depreciação reduz o lucro contábil mas não representa desembolso de caixa. Por isso, deve ser adicionada de volta."
        },
        {
            "id": 4,
            "pergunta": "O pagamento de dividendos é classificado na DFC como:",
            "opcoes": [
                "A) Fluxo de Caixa Operacional",
                "B) Fluxo de Caixa de Investimento",
                "C) Fluxo de Caixa de Financiamento",
                "D) Não aparece na DFC"
            ],
            "correta": "C",
            "explicacao": "Dividendos representam remuneração aos acionistas (financiadores), portanto são classificados como atividade de financiamento."
        },
        {
            "id": 5,
            "pergunta": "A compra de um equipamento à vista é classificada como:",
            "opcoes": [
                "A) Fluxo de Caixa Operacional",
                "B) Fluxo de Caixa de Investimento",
                "C) Fluxo de Caixa de Financiamento",
                "D) Não afeta a DFC"
            ],
            "correta": "B",
            "explicacao": "Aquisição de ativos imobilizados é atividade de investimento - a empresa está investindo em sua capacidade produtiva."
        },
        {
            "id": 6,
            "pergunta": "Uma empresa com lucro líquido positivo pode ter fluxo de caixa operacional negativo?",
            "opcoes": [
                "A) Não, é impossível",
                "B) Sim, se houver aumento significativo de ativos operacionais",
                "C) Sim, apenas se tiver prejuízos acumulados",
                "D) Não, pois lucro sempre gera caixa"
            ],
            "correta": "B",
            "explicacao": "Sim! Se a empresa aumentar muito seus recebíveis e estoques (vendas a prazo, acúmulo de estoque), o lucro não se converte em caixa."
        },
        {
            "id": 7,
            "pergunta": "Um aumento no saldo de Fornecedores representa, no fluxo operacional:",
            "opcoes": [
                "A) Uso de caixa (subtração)",
                "B) Fonte de caixa (adição)",
                "C) Não afeta o caixa operacional",
                "D) Atividade de financiamento"
            ],
            "correta": "B",
            "explicacao": "Aumento de fornecedores significa que a empresa comprou mas não pagou - economizou caixa. É uma fonte de recursos operacionais."
        },
        {
            "id": 8,
            "pergunta": "O indicador 'FCO / Lucro Líquido' serve para avaliar:",
            "opcoes": [
                "A) A rentabilidade da empresa",
                "B) A qualidade do lucro em termos de geração de caixa",
                "C) O nível de endividamento",
                "D) A liquidez corrente"
            ],
            "correta": "B",
            "explicacao": "Este índice mostra quanto do lucro contábil está se convertendo em caixa real. Valores baixos ou negativos indicam lucro de baixa qualidade."
        },
        {
            "id": 9,
            "pergunta": "O recebimento de empréstimo bancário é classificado como:",
            "opcoes": [
                "A) Fluxo de Caixa Operacional",
                "B) Fluxo de Caixa de Investimento",
                "C) Fluxo de Caixa de Financiamento",
                "D) Equivalente de caixa"
            ],
            "correta": "C",
            "explicacao": "Empréstimos são captação de recursos de terceiros, portanto classificados como atividade de financiamento."
        },
        {
            "id": 10,
            "pergunta": "Uma empresa saudável geralmente apresenta:",
            "opcoes": [
                "A) FCO negativo e FCI positivo",
                "B) FCO positivo, FCI negativo (investindo) e FCF variável",
                "C) Todos os fluxos positivos",
                "D) Todos os fluxos negativos"
            ],
            "correta": "B",
            "explicacao": "Empresas saudáveis geram caixa operacional (FCO+), investem no negócio (FCI-) e têm financiamento variável conforme a estratégia."
        }
    ]
    
    st.markdown("---")
    
    for q in questoes:
        st.markdown(f"**Questão {q['id']}:** {q['pergunta']}")
        st.session_state.respostas_m6[f"q{q['id']}"] = st.radio(
            f"Resposta {q['id']}",
            options=q['opcoes'],
            key=f"m6_q{q['id']}",
            label_visibility="collapsed"
        )
        st.markdown("---")
    
    if st.button("📊 Verificar Respostas", type="primary"):
        st.session_state.verificado_m6 = True
    
    if st.session_state.verificado_m6:
        st.markdown("### 📋 Resultado")
        
        acertos = 0
        for q in questoes:
            resp = st.session_state.respostas_m6.get(f"q{q['id']}", "")
            correta = [o for o in q['opcoes'] if o.startswith(q['correta'])][0]
            
            if resp and resp[0] == q['correta']:
                st.success(f"✅ Questão {q['id']}: Correta!")
                acertos += 1
            else:
                st.error(f"❌ Questão {q['id']}: Resposta correta: {q['correta']}")
                st.caption(f"   💡 {q['explicacao']}")
        
        # Resultado final
        pct = (acertos / len(questoes)) * 100
        
        cor = "#dcfce7" if pct >= 70 else "#fef3c7" if pct >= 50 else "#fee2e2"
        
        if pct >= 90:
            msg = "🏆 Excelente! Domínio completo do conteúdo!"
        elif pct >= 70:
            msg = "🌟 Muito bom! Conhecimento sólido."
        elif pct >= 50:
            msg = "👍 Bom, mas revise alguns conceitos."
        else:
            msg = "📚 Recomendamos revisar o material teórico."
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;'>
                <h2>Resultado: {acertos}/{len(questoes)} ({pct:.0f}%)</h2>
                <p>{msg}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Gráfico de desempenho por tema
        st.markdown("#### 📊 Análise por Tema")
        
        temas = {
            "Método Indireto": [1, 2, 3],
            "Classificação de Fluxos": [4, 5, 9],
            "Interpretação": [6, 7, 8, 10]
        }
        
        desempenho_tema = {}
        for tema, questoes_tema in temas.items():
            acertos_tema = sum(1 for qid in questoes_tema 
                             if st.session_state.respostas_m6.get(f"q{qid}", "")[0:1] == 
                             questoes[qid-1]['correta'])
            desempenho_tema[tema] = (acertos_tema / len(questoes_tema)) * 100
        
        fig = go.Figure(data=[
            go.Bar(
                x=list(desempenho_tema.keys()),
                y=list(desempenho_tema.values()),
                marker_color=['#22c55e' if v >= 70 else '#f97316' if v >= 50 else '#ef4444' 
                             for v in desempenho_tema.values()]
            )
        ])
        fig.update_layout(
            title="Desempenho por Tema (%)",
            yaxis_range=[0, 100],
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Síntese final
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Lucro ≠ Caixa:</strong> A DFC revela o que o lucro contábil esconde</li>
                <li><strong>Método Indireto:</strong> Parte do lucro e ajusta por variações de balanço</li>
                <li><strong>FCO positivo:</strong> Essencial para sustentabilidade do negócio</li>
                <li><strong>Crescimento consome caixa:</strong> Empresas em expansão precisam financiar capital de giro</li>
                <li><strong>Análise integrada:</strong> DRE + BP + DFC = visão completa da empresa</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()