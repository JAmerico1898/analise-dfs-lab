"""
Módulo 7 - Análise Horizontal e Vertical
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Aplicação prática em dados reais (planilha)
- Comparação de dois períodos consecutivos
- Interpretação escrita dos principais achados
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📊 Módulo 7 - Análise Horizontal e Vertical</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Aplicar análise horizontal (evolução temporal) em demonstrações reais</li>
                <li>Aplicar análise vertical (estrutura percentual) em BP e DRE</li>
                <li>Comparar dois períodos consecutivos identificando tendências</li>
                <li>Redigir interpretações analíticas dos principais achados</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📈 Análise Prática",
        "🔄 Comparativo de Períodos",
        "✍️ Interpretação dos Achados"
    ])
    
    with tab1:
        renderizar_analise_pratica()
    
    with tab2:
        renderizar_comparativo_periodos()
    
    with tab3:
        renderizar_interpretacao_achados()


def get_dados_empresa_real():
    """Retorna dados simulando uma empresa real para análise."""
    
    dados = {
        "empresa": "Varejista Nacional S.A.",
        "setor": "Comércio Varejista",
        "balanco": {
            2022: {
                "ATIVO": {
                    "Circulante": {
                        "Caixa e Equivalentes": 245000,
                        "Aplicações Financeiras": 180000,
                        "Contas a Receber": 520000,
                        "Estoques": 680000,
                        "Impostos a Recuperar": 95000,
                        "Outros Ativos Circulantes": 45000,
                    },
                    "Não Circulante": {
                        "Realizável LP": 85000,
                        "Investimentos": 120000,
                        "Imobilizado Líquido": 1450000,
                        "Intangível": 280000,
                    }
                },
                "PASSIVO": {
                    "Circulante": {
                        "Fornecedores": 485000,
                        "Empréstimos CP": 220000,
                        "Salários e Encargos": 125000,
                        "Impostos a Pagar": 98000,
                        "Outras Obrigações CP": 67000,
                    },
                    "Não Circulante": {
                        "Empréstimos LP": 680000,
                        "Debêntures": 350000,
                        "Provisões LP": 145000,
                    },
                    "Patrimônio Líquido": {
                        "Capital Social": 800000,
                        "Reservas de Capital": 95000,
                        "Reservas de Lucros": 535000,
                    }
                }
            },
            2023: {
                "ATIVO": {
                    "Circulante": {
                        "Caixa e Equivalentes": 185000,
                        "Aplicações Financeiras": 220000,
                        "Contas a Receber": 695000,
                        "Estoques": 820000,
                        "Impostos a Recuperar": 115000,
                        "Outros Ativos Circulantes": 55000,
                    },
                    "Não Circulante": {
                        "Realizável LP": 95000,
                        "Investimentos": 150000,
                        "Imobilizado Líquido": 1680000,
                        "Intangível": 310000,
                    }
                },
                "PASSIVO": {
                    "Circulante": {
                        "Fornecedores": 545000,
                        "Empréstimos CP": 385000,
                        "Salários e Encargos": 145000,
                        "Impostos a Pagar": 88000,
                        "Outras Obrigações CP": 82000,
                    },
                    "Não Circulante": {
                        "Empréstimos LP": 820000,
                        "Debêntures": 450000,
                        "Provisões LP": 175000,
                    },
                    "Patrimônio Líquido": {
                        "Capital Social": 800000,
                        "Reservas de Capital": 95000,
                        "Reservas de Lucros": 635000,
                    }
                }
            }
        },
        "dre": {
            2022: {
                "Receita Bruta": 4850000,
                "(-) Deduções": -728000,
                "Receita Líquida": 4122000,
                "(-) CMV": -2679000,
                "Lucro Bruto": 1443000,
                "(-) Despesas com Vendas": -535000,
                "(-) Despesas Administrativas": -412000,
                "(-) Outras Despesas Operacionais": -86000,
                "EBIT": 410000,
                "(-) Despesas Financeiras": -185000,
                "(+) Receitas Financeiras": 42000,
                "LAIR": 267000,
                "(-) IR/CS": -90780,
                "Lucro Líquido": 176220
            },
            2023: {
                "Receita Bruta": 5820000,
                "(-) Deduções": -873000,
                "Receita Líquida": 4947000,
                "(-) CMV": -3265000,
                "Lucro Bruto": 1682000,
                "(-) Despesas com Vendas": -692000,
                "(-) Despesas Administrativas": -485000,
                "(-) Outras Despesas Operacionais": -125000,
                "EBIT": 380000,
                "(-) Despesas Financeiras": -268000,
                "(+) Receitas Financeiras": 55000,
                "LAIR": 167000,
                "(-) IR/CS": -56780,
                "Lucro Líquido": 110220
            }
        }
    }
    return dados


def calcular_totais_balanco(balanco_ano):
    """Calcula totais do balanço para um ano."""
    
    ac = sum(balanco_ano['ATIVO']['Circulante'].values())
    anc = sum(balanco_ano['ATIVO']['Não Circulante'].values())
    ativo_total = ac + anc
    
    pc = sum(balanco_ano['PASSIVO']['Circulante'].values())
    pnc = sum(balanco_ano['PASSIVO']['Não Circulante'].values())
    pl = sum(balanco_ano['PASSIVO']['Patrimônio Líquido'].values())
    passivo_total = pc + pnc + pl
    
    return {
        'AC': ac, 'ANC': anc, 'Ativo Total': ativo_total,
        'PC': pc, 'PNC': pnc, 'PL': pl, 'Passivo Total': passivo_total
    }


def renderizar_analise_pratica():
    """Aplicação prática em dados reais."""
    
    st.markdown("### 📈 Aplicação Prática: Análise Horizontal e Vertical")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Conceitos-Chave:</strong><br>
            <ul>
                <li><strong>Análise Horizontal (AH):</strong> Compara a evolução das contas ao longo do tempo (variação %)</li>
                <li><strong>Análise Vertical (AV):</strong> Mostra a participação de cada conta no total (estrutura %)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_empresa_real()
    
    st.markdown(f"**Empresa:** {dados['empresa']} | **Setor:** {dados['setor']}")
    
    # Seleção de demonstração
    demo_selecionada = st.radio(
        "Selecione a demonstração para análise:",
        ["Balanço Patrimonial", "Demonstração do Resultado (DRE)"],
        horizontal=True,
        key="demo_pratica"
    )
    
    st.markdown("---")
    
    if demo_selecionada == "Balanço Patrimonial":
        renderizar_analise_balanco(dados)
    else:
        renderizar_analise_dre(dados)


def renderizar_analise_balanco(dados):
    """Renderiza análise H e V do Balanço."""
    
    st.markdown("#### 📊 Análise do Balanço Patrimonial")
    
    # Preparar dados
    totais_2022 = calcular_totais_balanco(dados['balanco'][2022])
    totais_2023 = calcular_totais_balanco(dados['balanco'][2023])
    
    # ATIVO
    st.markdown("##### ATIVO")
    
    linhas_ativo = []
    
    # Circulante
    linhas_ativo.append({
        "Conta": "**ATIVO CIRCULANTE**",
        "2022": totais_2022['AC'],
        "AV 2022": (totais_2022['AC'] / totais_2022['Ativo Total']) * 100,
        "2023": totais_2023['AC'],
        "AV 2023": (totais_2023['AC'] / totais_2023['Ativo Total']) * 100,
        "AH %": ((totais_2023['AC'] / totais_2022['AC']) - 1) * 100
    })
    
    for conta, valor_2022 in dados['balanco'][2022]['ATIVO']['Circulante'].items():
        valor_2023 = dados['balanco'][2023]['ATIVO']['Circulante'][conta]
        linhas_ativo.append({
            "Conta": f"  {conta}",
            "2022": valor_2022,
            "AV 2022": (valor_2022 / totais_2022['Ativo Total']) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / totais_2023['Ativo Total']) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    # Não Circulante
    linhas_ativo.append({
        "Conta": "**ATIVO NÃO CIRCULANTE**",
        "2022": totais_2022['ANC'],
        "AV 2022": (totais_2022['ANC'] / totais_2022['Ativo Total']) * 100,
        "2023": totais_2023['ANC'],
        "AV 2023": (totais_2023['ANC'] / totais_2023['Ativo Total']) * 100,
        "AH %": ((totais_2023['ANC'] / totais_2022['ANC']) - 1) * 100
    })
    
    for conta, valor_2022 in dados['balanco'][2022]['ATIVO']['Não Circulante'].items():
        valor_2023 = dados['balanco'][2023]['ATIVO']['Não Circulante'][conta]
        linhas_ativo.append({
            "Conta": f"  {conta}",
            "2022": valor_2022,
            "AV 2022": (valor_2022 / totais_2022['Ativo Total']) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / totais_2023['Ativo Total']) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    # Total
    linhas_ativo.append({
        "Conta": "**ATIVO TOTAL**",
        "2022": totais_2022['Ativo Total'],
        "AV 2022": 100.0,
        "2023": totais_2023['Ativo Total'],
        "AV 2023": 100.0,
        "AH %": ((totais_2023['Ativo Total'] / totais_2022['Ativo Total']) - 1) * 100
    })
    
    df_ativo = pd.DataFrame(linhas_ativo)
    
    # Formatar para exibição
    df_ativo_display = df_ativo.copy()
    df_ativo_display['2022'] = df_ativo_display['2022'].apply(lambda x: f"R$ {x:,.0f}")
    df_ativo_display['2023'] = df_ativo_display['2023'].apply(lambda x: f"R$ {x:,.0f}")
    df_ativo_display['AV 2022'] = df_ativo_display['AV 2022'].apply(lambda x: f"{x:.1f}%")
    df_ativo_display['AV 2023'] = df_ativo_display['AV 2023'].apply(lambda x: f"{x:.1f}%")
    df_ativo_display['AH %'] = df_ativo_display['AH %'].apply(lambda x: f"{x:+.1f}%")
    
    st.dataframe(df_ativo_display, use_container_width=True, hide_index=True)
    
    # PASSIVO + PL
    st.markdown("##### PASSIVO + PATRIMÔNIO LÍQUIDO")
    
    linhas_passivo = []
    
    # Circulante
    linhas_passivo.append({
        "Conta": "**PASSIVO CIRCULANTE**",
        "2022": totais_2022['PC'],
        "AV 2022": (totais_2022['PC'] / totais_2022['Passivo Total']) * 100,
        "2023": totais_2023['PC'],
        "AV 2023": (totais_2023['PC'] / totais_2023['Passivo Total']) * 100,
        "AH %": ((totais_2023['PC'] / totais_2022['PC']) - 1) * 100
    })
    
    for conta, valor_2022 in dados['balanco'][2022]['PASSIVO']['Circulante'].items():
        valor_2023 = dados['balanco'][2023]['PASSIVO']['Circulante'][conta]
        linhas_passivo.append({
            "Conta": f"  {conta}",
            "2022": valor_2022,
            "AV 2022": (valor_2022 / totais_2022['Passivo Total']) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / totais_2023['Passivo Total']) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    # Não Circulante
    linhas_passivo.append({
        "Conta": "**PASSIVO NÃO CIRCULANTE**",
        "2022": totais_2022['PNC'],
        "AV 2022": (totais_2022['PNC'] / totais_2022['Passivo Total']) * 100,
        "2023": totais_2023['PNC'],
        "AV 2023": (totais_2023['PNC'] / totais_2023['Passivo Total']) * 100,
        "AH %": ((totais_2023['PNC'] / totais_2022['PNC']) - 1) * 100
    })
    
    for conta, valor_2022 in dados['balanco'][2022]['PASSIVO']['Não Circulante'].items():
        valor_2023 = dados['balanco'][2023]['PASSIVO']['Não Circulante'][conta]
        linhas_passivo.append({
            "Conta": f"  {conta}",
            "2022": valor_2022,
            "AV 2022": (valor_2022 / totais_2022['Passivo Total']) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / totais_2023['Passivo Total']) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    # PL
    linhas_passivo.append({
        "Conta": "**PATRIMÔNIO LÍQUIDO**",
        "2022": totais_2022['PL'],
        "AV 2022": (totais_2022['PL'] / totais_2022['Passivo Total']) * 100,
        "2023": totais_2023['PL'],
        "AV 2023": (totais_2023['PL'] / totais_2023['Passivo Total']) * 100,
        "AH %": ((totais_2023['PL'] / totais_2022['PL']) - 1) * 100
    })
    
    for conta, valor_2022 in dados['balanco'][2022]['PASSIVO']['Patrimônio Líquido'].items():
        valor_2023 = dados['balanco'][2023]['PASSIVO']['Patrimônio Líquido'][conta]
        linhas_passivo.append({
            "Conta": f"  {conta}",
            "2022": valor_2022,
            "AV 2022": (valor_2022 / totais_2022['Passivo Total']) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / totais_2023['Passivo Total']) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    # Total
    linhas_passivo.append({
        "Conta": "**PASSIVO + PL TOTAL**",
        "2022": totais_2022['Passivo Total'],
        "AV 2022": 100.0,
        "2023": totais_2023['Passivo Total'],
        "AV 2023": 100.0,
        "AH %": ((totais_2023['Passivo Total'] / totais_2022['Passivo Total']) - 1) * 100
    })
    
    df_passivo = pd.DataFrame(linhas_passivo)
    
    df_passivo_display = df_passivo.copy()
    df_passivo_display['2022'] = df_passivo_display['2022'].apply(lambda x: f"R$ {x:,.0f}")
    df_passivo_display['2023'] = df_passivo_display['2023'].apply(lambda x: f"R$ {x:,.0f}")
    df_passivo_display['AV 2022'] = df_passivo_display['AV 2022'].apply(lambda x: f"{x:.1f}%")
    df_passivo_display['AV 2023'] = df_passivo_display['AV 2023'].apply(lambda x: f"{x:.1f}%")
    df_passivo_display['AH %'] = df_passivo_display['AH %'].apply(lambda x: f"{x:+.1f}%")
    
    st.dataframe(df_passivo_display, use_container_width=True, hide_index=True)
    
    # Gráficos
    st.markdown("#### 📊 Visualização da Estrutura")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Estrutura do Ativo
        fig1 = make_subplots(rows=1, cols=2, specs=[[{'type':'pie'}, {'type':'pie'}]],
                           subplot_titles=['2022', '2023'])
        
        fig1.add_trace(go.Pie(
            labels=['AC', 'ANC'],
            values=[totais_2022['AC'], totais_2022['ANC']],
            marker_colors=['#3b82f6', '#1e40af'],
            hole=0.4
        ), row=1, col=1)
        
        fig1.add_trace(go.Pie(
            labels=['AC', 'ANC'],
            values=[totais_2023['AC'], totais_2023['ANC']],
            marker_colors=['#3b82f6', '#1e40af'],
            hole=0.4
        ), row=1, col=2)
        
        fig1.update_layout(title="Estrutura do Ativo", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Estrutura do Passivo
        fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'pie'}, {'type':'pie'}]],
                           subplot_titles=['2022', '2023'])
        
        fig2.add_trace(go.Pie(
            labels=['PC', 'PNC', 'PL'],
            values=[totais_2022['PC'], totais_2022['PNC'], totais_2022['PL']],
            marker_colors=['#ef4444', '#f97316', '#22c55e'],
            hole=0.4
        ), row=1, col=1)
        
        fig2.add_trace(go.Pie(
            labels=['PC', 'PNC', 'PL'],
            values=[totais_2023['PC'], totais_2023['PNC'], totais_2023['PL']],
            marker_colors=['#ef4444', '#f97316', '#22c55e'],
            hole=0.4
        ), row=1, col=2)
        
        fig2.update_layout(title="Estrutura das Fontes", height=300)
        st.plotly_chart(fig2, use_container_width=True)


def renderizar_analise_dre(dados):
    """Renderiza análise H e V da DRE."""
    
    st.markdown("#### 📊 Análise da DRE")
    
    # Preparar dados
    rl_2022 = dados['dre'][2022]['Receita Líquida']
    rl_2023 = dados['dre'][2023]['Receita Líquida']
    
    linhas_dre = []
    
    for conta in dados['dre'][2022].keys():
        valor_2022 = dados['dre'][2022][conta]
        valor_2023 = dados['dre'][2023][conta]
        
        linhas_dre.append({
            "Conta": conta,
            "2022": valor_2022,
            "AV 2022": (valor_2022 / rl_2022) * 100,
            "2023": valor_2023,
            "AV 2023": (valor_2023 / rl_2023) * 100,
            "AH %": ((valor_2023 / valor_2022) - 1) * 100 if valor_2022 != 0 else 0
        })
    
    df_dre = pd.DataFrame(linhas_dre)
    
    # Formatar para exibição
    df_dre_display = df_dre.copy()
    df_dre_display['2022'] = df_dre_display['2022'].apply(lambda x: f"R$ {x:,.0f}")
    df_dre_display['2023'] = df_dre_display['2023'].apply(lambda x: f"R$ {x:,.0f}")
    df_dre_display['AV 2022'] = df_dre_display['AV 2022'].apply(lambda x: f"{x:.1f}%")
    df_dre_display['AV 2023'] = df_dre_display['AV 2023'].apply(lambda x: f"{x:.1f}%")
    df_dre_display['AH %'] = df_dre_display['AH %'].apply(lambda x: f"{x:+.1f}%")
    
    st.dataframe(df_dre_display, use_container_width=True, hide_index=True)
    
    # Gráfico de Margens
    st.markdown("#### 📈 Evolução das Margens")
    
    margens_2022 = {
        'Margem Bruta': (dados['dre'][2022]['Lucro Bruto'] / rl_2022) * 100,
        'Margem EBIT': (dados['dre'][2022]['EBIT'] / rl_2022) * 100,
        'Margem Líquida': (dados['dre'][2022]['Lucro Líquido'] / rl_2022) * 100
    }
    
    margens_2023 = {
        'Margem Bruta': (dados['dre'][2023]['Lucro Bruto'] / rl_2023) * 100,
        'Margem EBIT': (dados['dre'][2023]['EBIT'] / rl_2023) * 100,
        'Margem Líquida': (dados['dre'][2023]['Lucro Líquido'] / rl_2023) * 100
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='2022',
            x=list(margens_2022.keys()),
            y=list(margens_2022.values()),
            marker_color='#3b82f6'
        ))
        fig.add_trace(go.Bar(
            name='2023',
            x=list(margens_2023.keys()),
            y=list(margens_2023.values()),
            marker_color='#22c55e'
        ))
        
        fig.update_layout(
            title="Comparativo de Margens (%)",
            barmode='group',
            height=350
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Métricas de variação
        for margem in margens_2022.keys():
            var = margens_2023[margem] - margens_2022[margem]
            delta_color = "normal" if var > 0 else "inverse"
            st.metric(
                margem,
                f"{margens_2023[margem]:.1f}%",
                delta=f"{var:+.1f}pp",
                delta_color=delta_color
            )


def renderizar_comparativo_periodos():
    """Comparação detalhada de dois períodos consecutivos."""
    
    st.markdown("### 🔄 Comparativo de Períodos: 2022 vs 2023")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Identificar as principais mudanças entre os dois períodos e avaliar 
            se representam melhoria ou deterioração da situação financeira.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_empresa_real()
    totais_2022 = calcular_totais_balanco(dados['balanco'][2022])
    totais_2023 = calcular_totais_balanco(dados['balanco'][2023])
    
    # Dashboard de Indicadores
    st.markdown("#### 📊 Dashboard Comparativo")
    
    # Indicadores de Liquidez
    st.markdown("##### 💧 Liquidez")
    
    lc_2022 = totais_2022['AC'] / totais_2022['PC']
    lc_2023 = totais_2023['AC'] / totais_2023['PC']
    
    ls_2022 = (totais_2022['AC'] - dados['balanco'][2022]['ATIVO']['Circulante']['Estoques']) / totais_2022['PC']
    ls_2023 = (totais_2023['AC'] - dados['balanco'][2023]['ATIVO']['Circulante']['Estoques']) / totais_2023['PC']
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        var_lc = lc_2023 - lc_2022
        st.metric("Liquidez Corrente 2022", f"{lc_2022:.2f}")
    with col2:
        st.metric("Liquidez Corrente 2023", f"{lc_2023:.2f}", 
                 delta=f"{var_lc:+.2f}", delta_color="normal" if var_lc > 0 else "inverse")
    with col3:
        st.metric("Liquidez Seca 2022", f"{ls_2022:.2f}")
    with col4:
        var_ls = ls_2023 - ls_2022
        st.metric("Liquidez Seca 2023", f"{ls_2023:.2f}",
                 delta=f"{var_ls:+.2f}", delta_color="normal" if var_ls > 0 else "inverse")
    
    # Indicadores de Endividamento
    st.markdown("##### 📊 Endividamento")
    
    endiv_2022 = ((totais_2022['PC'] + totais_2022['PNC']) / totais_2022['Ativo Total']) * 100
    endiv_2023 = ((totais_2023['PC'] + totais_2023['PNC']) / totais_2023['Ativo Total']) * 100
    
    comp_2022 = (totais_2022['PC'] / (totais_2022['PC'] + totais_2022['PNC'])) * 100
    comp_2023 = (totais_2023['PC'] / (totais_2023['PC'] + totais_2023['PNC'])) * 100
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Endividamento 2022", f"{endiv_2022:.1f}%")
    with col2:
        var_end = endiv_2023 - endiv_2022
        st.metric("Endividamento 2023", f"{endiv_2023:.1f}%",
                 delta=f"{var_end:+.1f}pp", delta_color="inverse" if var_end > 0 else "normal")
    with col3:
        st.metric("Dívida CP 2022", f"{comp_2022:.1f}%")
    with col4:
        var_comp = comp_2023 - comp_2022
        st.metric("Dívida CP 2023", f"{comp_2023:.1f}%",
                 delta=f"{var_comp:+.1f}pp", delta_color="inverse" if var_comp > 0 else "normal")
    
    # Indicadores de Rentabilidade
    st.markdown("##### 💰 Rentabilidade")
    
    rl_2022 = dados['dre'][2022]['Receita Líquida']
    rl_2023 = dados['dre'][2023]['Receita Líquida']
    ll_2022 = dados['dre'][2022]['Lucro Líquido']
    ll_2023 = dados['dre'][2023]['Lucro Líquido']
    
    ml_2022 = (ll_2022 / rl_2022) * 100
    ml_2023 = (ll_2023 / rl_2023) * 100
    
    roe_2022 = (ll_2022 / totais_2022['PL']) * 100
    roe_2023 = (ll_2023 / totais_2023['PL']) * 100
    
    roa_2022 = (ll_2022 / totais_2022['Ativo Total']) * 100
    roa_2023 = (ll_2023 / totais_2023['Ativo Total']) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        var_ml = ml_2023 - ml_2022
        st.metric("Margem Líquida", f"{ml_2023:.1f}%",
                 delta=f"{var_ml:+.1f}pp", delta_color="normal" if var_ml > 0 else "inverse")
    with col2:
        var_roe = roe_2023 - roe_2022
        st.metric("ROE", f"{roe_2023:.1f}%",
                 delta=f"{var_roe:+.1f}pp", delta_color="normal" if var_roe > 0 else "inverse")
    with col3:
        var_roa = roa_2023 - roa_2022
        st.metric("ROA", f"{roa_2023:.1f}%",
                 delta=f"{var_roa:+.1f}pp", delta_color="normal" if var_roa > 0 else "inverse")
    
    st.markdown("---")
    
    # Análise das Principais Variações
    st.markdown("#### 🔍 Principais Variações Identificadas")
    
    variacoes = [
        {
            "item": "Contas a Receber",
            "2022": dados['balanco'][2022]['ATIVO']['Circulante']['Contas a Receber'],
            "2023": dados['balanco'][2023]['ATIVO']['Circulante']['Contas a Receber'],
            "tipo": "preocupante"
        },
        {
            "item": "Estoques",
            "2022": dados['balanco'][2022]['ATIVO']['Circulante']['Estoques'],
            "2023": dados['balanco'][2023]['ATIVO']['Circulante']['Estoques'],
            "tipo": "preocupante"
        },
        {
            "item": "Empréstimos CP",
            "2022": dados['balanco'][2022]['PASSIVO']['Circulante']['Empréstimos CP'],
            "2023": dados['balanco'][2023]['PASSIVO']['Circulante']['Empréstimos CP'],
            "tipo": "alerta"
        },
        {
            "item": "Empréstimos LP",
            "2022": dados['balanco'][2022]['PASSIVO']['Não Circulante']['Empréstimos LP'],
            "2023": dados['balanco'][2023]['PASSIVO']['Não Circulante']['Empréstimos LP'],
            "tipo": "alerta"
        },
        {
            "item": "Receita Líquida",
            "2022": rl_2022,
            "2023": rl_2023,
            "tipo": "positivo"
        },
        {
            "item": "Lucro Líquido",
            "2022": ll_2022,
            "2023": ll_2023,
            "tipo": "preocupante"
        }
    ]
    
    for v in variacoes:
        var_pct = ((v['2023'] / v['2022']) - 1) * 100
        var_abs = v['2023'] - v['2022']
        
        if v['tipo'] == 'positivo':
            cor = "#dcfce7"
        elif v['tipo'] == 'alerta':
            cor = "#fef3c7"
        else:
            cor = "#fee2e2"
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <strong>{v['item']}</strong><br>
                2022: R$ {v['2022']:,.0f} → 2023: R$ {v['2023']:,.0f}<br>
                Variação: <strong>{var_pct:+.1f}%</strong> (R$ {var_abs:+,.0f})
            </div>
        """, unsafe_allow_html=True)
    
    # Gráfico Radar
    st.markdown("#### 📊 Radar Comparativo")
    
    categorias = ['Liquidez', 'Endividamento', 'Margem', 'ROE', 'ROA']
    
    # Normalizar valores para escala 0-100
    valores_2022 = [
        min(lc_2022 * 50, 100),  # Liquidez
        100 - endiv_2022,  # Menor endividamento = melhor
        ml_2022 * 10,  # Margem
        roe_2022 * 5,  # ROE
        roa_2022 * 10  # ROA
    ]
    
    valores_2023 = [
        min(lc_2023 * 50, 100),
        100 - endiv_2023,
        ml_2023 * 10,
        roe_2023 * 5,
        roa_2023 * 10
    ]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=valores_2022,
        theta=categorias,
        fill='toself',
        name='2022',
        line_color='#3b82f6'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=valores_2023,
        theta=categorias,
        fill='toself',
        name='2023',
        line_color='#ef4444'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)


def renderizar_interpretacao_achados():
    """Interpretação escrita dos principais achados."""
    
    st.markdown("### ✍️ Interpretação dos Principais Achados")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>📌 EXERCÍCIO AVALIATIVO</strong><br>
            <em>Com base nas análises realizadas, elabore interpretações escritas 
            para os principais achados identificados.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_empresa_real()
    
    # Resumo dos dados
    st.markdown("#### 📋 Resumo dos Dados para Análise")
    
    with st.expander("Ver Resumo dos Indicadores"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                **Variações Principais (2022→2023):**
                - Receita Líquida: +20,0%
                - Lucro Líquido: -37,5%
                - Contas a Receber: +33,7%
                - Estoques: +20,6%
                - Empréstimos CP: +75,0%
                - Empréstimos LP: +20,6%
            """)
        
        with col2:
            st.markdown("""
                **Indicadores 2023:**
                - Liquidez Corrente: 1,68
                - Endividamento: 63,5%
                - Margem Líquida: 2,2%
                - ROE: 7,2%
                - ROA: 2,6%
            """)
    
    st.markdown("---")
    
    # Exercícios de interpretação
    st.markdown("#### 📝 Exercícios de Interpretação")
    
    exercicios = [
        {
            "numero": 1,
            "titulo": "Análise da Liquidez",
            "contexto": "A liquidez corrente caiu de 1,77 para 1,68, enquanto a liquidez seca caiu de 1,09 para 0,99.",
            "pergunta": "Interprete essa variação. A empresa está com problemas de liquidez? Justifique.",
            "dica": "Considere a composição do ativo circulante e o perfil das obrigações."
        },
        {
            "numero": 2,
            "titulo": "Análise do Endividamento",
            "contexto": "O endividamento total subiu de 59,0% para 63,5%, com aumento de 75% nos empréstimos de curto prazo.",
            "pergunta": "Avalie a evolução da estrutura de capital. Quais os riscos dessa mudança?",
            "dica": "Analise a composição da dívida (CP vs LP) e relacione com a liquidez."
        },
        {
            "numero": 3,
            "titulo": "Análise da Rentabilidade",
            "contexto": "A receita cresceu 20%, mas o lucro líquido caiu 37,5%. A margem líquida caiu de 4,3% para 2,2%.",
            "pergunta": "Explique por que o crescimento de receita não se traduziu em crescimento de lucro.",
            "dica": "Analise a evolução das despesas operacionais e financeiras em relação à receita."
        },
        {
            "numero": 4,
            "titulo": "Análise do Capital de Giro",
            "contexto": "Contas a receber cresceram 33,7% e estoques 20,6%, enquanto fornecedores cresceram apenas 12,4%.",
            "pergunta": "Qual o impacto dessa evolução no capital de giro? A empresa está gerenciando bem seu ciclo operacional?",
            "dica": "Relacione com a necessidade de financiamento adicional observada."
        },
        {
            "numero": 5,
            "titulo": "Diagnóstico Geral",
            "contexto": "Considerando todas as análises realizadas neste módulo.",
            "pergunta": "Elabore um diagnóstico geral da situação financeira da empresa, destacando pontos fortes, fragilidades e recomendações.",
            "dica": "Estruture sua resposta em: Pontos Fortes, Pontos Fracos, Riscos e Recomendações."
        }
    ]
    
    respostas = {}
    
    for ex in exercicios:
        with st.expander(f"📌 Exercício {ex['numero']}: {ex['titulo']}", expanded=(ex['numero'] == 1)):
            st.markdown(f"""
                <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    <strong>Contexto:</strong> {ex['contexto']}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**❓ {ex['pergunta']}**")
            
            st.caption(f"💡 Dica: {ex['dica']}")
            
            respostas[ex['numero']] = st.text_area(
                f"Sua interpretação:",
                placeholder="Desenvolva sua análise de forma estruturada...",
                height=150,
                key=f"interp_{ex['numero']}"
            )
            
            if respostas[ex['numero']]:
                palavras = len(respostas[ex['numero']].split())
                st.caption(f"Palavras: {palavras}")
    
    st.markdown("---")
    
    # Gabarito
    if st.button("📖 Ver Gabarito Comentado", type="primary"):
        st.markdown("### 📋 Gabarito Comentado")
        
        gabaritos = [
            {
                "numero": 1,
                "resposta": """
                **Interpretação da Liquidez:**
                
                A queda na liquidez corrente de 1,77 para 1,68 indica leve deterioração, porém o índice 
                ainda está acima de 1, sinalizando capacidade de honrar compromissos de curto prazo.
                
                A liquidez seca abaixo de 1 (0,99) é mais preocupante: sem considerar os estoques, a 
                empresa não consegue cobrir integralmente suas obrigações de curto prazo. Isso indica:
                
                1. Dependência dos estoques para equilibrar o capital de giro
                2. Risco se houver dificuldade de venda ou obsolescência
                3. Necessidade de monitorar o giro dos estoques
                
                **Conclusão:** Não há crise de liquidez imediata, mas a tendência é preocupante e 
                merece atenção da administração.
                """
            },
            {
                "numero": 2,
                "resposta": """
                **Avaliação do Endividamento:**
                
                O aumento do endividamento de 59% para 63,5% representa deterioração da estrutura de capital.
                Mais preocupante é a composição: empréstimos de curto prazo cresceram 75%, pressionando o caixa.
                
                **Riscos identificados:**
                1. Maior pressão sobre o fluxo de caixa no curto prazo
                2. Vulnerabilidade a aumento de taxas de juros
                3. Redução da flexibilidade financeira
                4. Possível dificuldade de refinanciamento
                
                **Relação com liquidez:** O aumento de dívidas CP explica parte da queda na liquidez, 
                criando um ciclo vicioso onde a empresa pode precisar de mais dívida para cobrir vencimentos.
                
                **Conclusão:** Estrutura de capital deteriorando. Recomenda-se alongamento do perfil 
                da dívida e redução do endividamento total.
                """
            },
            {
                "numero": 3,
                "resposta": """
                **Por que receita cresceu mas lucro caiu:**
                
                Analisando a DRE verticalmente:
                
                | Item | 2022 (% RL) | 2023 (% RL) | Variação |
                |------|-------------|-------------|----------|
                | CMV | 65,0% | 66,0% | +1,0pp |
                | Desp. Vendas | 13,0% | 14,0% | +1,0pp |
                | Desp. Admin. | 10,0% | 9,8% | -0,2pp |
                | Desp. Financ. | 4,5% | 5,4% | +0,9pp |
                
                **Conclusão:** O crescimento foi "comprado" com:
                1. Margem bruta menor (possivelmente preços menores ou custos maiores)
                2. Maior esforço comercial (despesas de vendas)
                3. Maior custo financeiro (para financiar o crescimento)
                
                A empresa cresceu vendas sacrificando rentabilidade - clássico caso de crescimento 
                não lucrativo que merece revisão estratégica.
                """
            },
            {
                "numero": 4,
                "resposta": """
                **Impacto no Capital de Giro:**
                
                O descasamento entre ativos e passivos operacionais criou Necessidade de Capital de 
                Giro (NCG) adicional:
                
                - Δ Clientes: +R$ 175.000 (mais dinheiro "preso" em recebíveis)
                - Δ Estoques: +R$ 140.000 (mais dinheiro "preso" em mercadorias)
                - Δ Fornecedores: +R$ 60.000 (financiamento espontâneo)
                
                **NCG adicional = 175 + 140 - 60 = R$ 255.000**
                
                Este valor precisou ser financiado com empréstimos (daí o aumento de 75% na dívida CP).
                
                **Diagnóstico:** A empresa NÃO está gerenciando bem seu ciclo operacional:
                - Prazo de recebimento aumentou (clientes cresceram mais que vendas)
                - Giro de estoques piorou
                - Não conseguiu alongar prazo com fornecedores proporcionalmente
                
                **Recomendações:** Revisar política de crédito, otimizar níveis de estoque, 
                renegociar prazos com fornecedores.
                """
            },
            {
                "numero": 5,
                "resposta": """
                **DIAGNÓSTICO GERAL - VAREJISTA NACIONAL S.A.**
                
                **PONTOS FORTES:**
                - Crescimento de receita de 20% (demonstra capacidade comercial)
                - Liquidez corrente ainda acima de 1
                - Aumento do imobilizado (+15,9%) indica investimento em capacidade
                
                **PONTOS FRACOS:**
                - Rentabilidade em queda acentuada (ROE caiu de 12,3% para 7,2%)
                - Margens comprimidas em todos os níveis
                - Gestão de capital de giro ineficiente
                - Endividamento crescente com perfil de curto prazo
                
                **RISCOS:**
                - Continuidade da deterioração pode levar a problemas de liquidez
                - Aumento de taxas de juros agravaria situação
                - Dependência de refinanciamento constante
                - Possível obsolescência de estoques
                
                **RECOMENDAÇÕES:**
                1. **Curto prazo:** Alongar perfil da dívida, melhorar gestão de recebíveis
                2. **Médio prazo:** Revisar política de preços, otimizar mix de produtos
                3. **Longo prazo:** Avaliar se modelo de crescimento é sustentável
                
                **CONCLUSÃO:** Empresa em situação de atenção. Não há crise imediata, mas as 
                tendências são negativas e exigem ação corretiva da administração.
                """
            }
        ]
        
        for g in gabaritos:
            st.markdown(f"""
                <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    <strong>Exercício {g['numero']}:</strong>
                    {g['resposta']}
                </div>
            """, unsafe_allow_html=True)
    
    # Síntese final
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Análise Horizontal:</strong> Revela tendências e evolução temporal</li>
                <li><strong>Análise Vertical:</strong> Mostra estrutura e composição percentual</li>
                <li><strong>Combinação AH + AV:</strong> Permite diagnóstico completo</li>
                <li><strong>Interpretação:</strong> Números precisam ser traduzidos em insights de negócio</li>
                <li><strong>Contexto importa:</strong> Mesmos números podem ter interpretações diferentes conforme o setor</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()