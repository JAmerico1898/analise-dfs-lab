"""
Módulo 11 - Modelo DuPont Expandido e Diagnóstico Integrado
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Aplicação completa do modelo DuPont
- Diagnóstico comparativo entre empresas
- Exercício interpretativo escrito
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>🔬 Módulo 11 - Modelo DuPont Expandido</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Aplicar o modelo DuPont expandido (5 fatores) de forma completa</li>
                <li>Realizar diagnóstico comparativo entre múltiplas empresas</li>
                <li>Identificar os drivers específicos de rentabilidade de cada negócio</li>
                <li>Elaborar relatórios interpretativos com recomendações</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🔬 DuPont Expandido",
        "📊 Diagnóstico Comparativo",
        "✍️ Exercício Interpretativo"
    ])
    
    with tab1:
        renderizar_dupont_expandido()
    
    with tab2:
        renderizar_diagnostico_comparativo()
    
    with tab3:
        renderizar_exercicio_interpretativo()


def renderizar_dupont_expandido():
    """Aplicação completa do modelo DuPont expandido (5 fatores)."""
    
    st.markdown("### 🔬 Modelo DuPont Expandido (5 Fatores)")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Evolução do Modelo DuPont:</strong><br><br>
            <strong>DuPont Clássico (3 fatores):</strong><br>
            ROE = Margem Líquida × Giro do Ativo × Multiplicador<br><br>
            <strong>DuPont Expandido (5 fatores):</strong><br>
            ROE = Carga Tributária × Carga de Juros × Margem EBIT × Giro do Ativo × Multiplicador<br><br>
            <em>O modelo expandido separa os efeitos de impostos, juros e operações.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Fórmulas detalhadas
    st.markdown("#### 📐 Decomposição dos 5 Fatores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>1️⃣ Carga Tributária</h4>
                <p><strong>Fórmula:</strong> Lucro Líquido / LAIR</p>
                <p><strong>Indica:</strong> Quanto sobra após impostos (1 - alíquota efetiva)</p>
                <p><strong>Ideal:</strong> Quanto maior, melhor (menos impostos)</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>2️⃣ Carga de Juros</h4>
                <p><strong>Fórmula:</strong> LAIR / EBIT</p>
                <p><strong>Indica:</strong> Quanto sobra após despesas financeiras</p>
                <p><strong>Ideal:</strong> Quanto maior, melhor (menos juros)</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>3️⃣ Margem EBIT (Operacional)</h4>
                <p><strong>Fórmula:</strong> EBIT / Receita Líquida</p>
                <p><strong>Indica:</strong> Eficiência operacional pura</p>
                <p><strong>Ideal:</strong> Depende do setor</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>4️⃣ Giro do Ativo</h4>
                <p><strong>Fórmula:</strong> Receita Líquida / Ativo Total</p>
                <p><strong>Indica:</strong> Eficiência no uso dos ativos</p>
                <p><strong>Ideal:</strong> Depende do modelo de negócio</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fce7f3; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>5️⃣ Multiplicador de Alavancagem</h4>
                <p><strong>Fórmula:</strong> Ativo Total / Patrimônio Líquido</p>
                <p><strong>Indica:</strong> Uso de capital de terceiros</p>
                <p><strong>Ideal:</strong> Equilíbrio risco-retorno</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.latex(r"ROE = \frac{LL}{LAIR} \times \frac{LAIR}{EBIT} \times \frac{EBIT}{Rec} \times \frac{Rec}{AT} \times \frac{AT}{PL}")
    
    st.markdown("---")
    
    # Simulador Completo
    st.markdown("#### 🧮 Simulador DuPont Expandido")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**DRE**")
        receita = st.number_input("Receita Líquida", min_value=0, value=10000000, step=500000, key="exp_rec")
        ebit = st.number_input("EBIT", min_value=0, value=1500000, step=100000, key="exp_ebit")
        desp_fin = st.number_input("Despesas Financeiras", min_value=0, value=300000, step=50000, key="exp_fin")
        rec_fin = st.number_input("Receitas Financeiras", min_value=0, value=50000, step=10000, key="exp_recfin")
    
    with col2:
        st.markdown("**Impostos**")
        lair = ebit - desp_fin + rec_fin
        st.metric("LAIR (calculado)", f"R$ {lair:,.0f}")
        ir_cs = st.number_input("IR/CS", min_value=0, value=int(lair * 0.34) if lair > 0 else 0, step=50000, key="exp_ir")
        ll = lair - ir_cs
        st.metric("Lucro Líquido", f"R$ {ll:,.0f}")
    
    with col3:
        st.markdown("**Balanço**")
        ativo = st.number_input("Ativo Total", min_value=1, value=8000000, step=500000, key="exp_at")
        pl = st.number_input("Patrimônio Líquido", min_value=1, value=3200000, step=200000, key="exp_pl")
    
    # Cálculos dos 5 fatores
    carga_trib = (ll / lair) if lair > 0 else 0
    carga_juros = (lair / ebit) if ebit > 0 else 0
    margem_ebit = (ebit / receita) if receita > 0 else 0
    giro_ativo = (receita / ativo) if ativo > 0 else 0
    multiplicador = (ativo / pl) if pl > 0 else 0
    
    roe_5fatores = carga_trib * carga_juros * margem_ebit * giro_ativo * multiplicador * 100
    roe_direto = (ll / pl * 100) if pl > 0 else 0
    
    st.markdown("---")
    st.markdown("#### 📊 Resultados da Decomposição")
    
    # Cards dos 5 fatores
    col1, col2, col3, col4, col5 = st.columns(5)
    
    fatores = [
        ("Carga Tributária", carga_trib, "#fee2e2", "LL/LAIR"),
        ("Carga de Juros", carga_juros, "#fef3c7", "LAIR/EBIT"),
        ("Margem EBIT", margem_ebit, "#dcfce7", "EBIT/Rec"),
        ("Giro Ativo", giro_ativo, "#dbeafe", "Rec/AT"),
        ("Multiplicador", multiplicador, "#fce7f3", "AT/PL")
    ]
    
    cols = [col1, col2, col3, col4, col5]
    
    for col, (nome, valor, cor, formula) in zip(cols, fatores):
        with col:
            if nome in ["Carga Tributária", "Carga de Juros", "Margem EBIT"]:
                valor_fmt = f"{valor*100:.1f}%"
            else:
                valor_fmt = f"{valor:.2f}x"
            
            st.markdown(f"""
                <div style='background-color: {cor}; padding: 10px; border-radius: 10px; text-align: center;'>
                    <small>{nome}</small>
                    <h3>{valor_fmt}</h3>
                    <small>{formula}</small>
                </div>
            """, unsafe_allow_html=True)
    
    # Resultado ROE
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        cor_roe = "#22c55e" if roe_5fatores > 15 else "#f97316" if roe_5fatores > 8 else "#ef4444"
        st.markdown(f"""
            <div style='background-color: {cor_roe}20; padding: 25px; border-radius: 15px; 
                        text-align: center; border: 3px solid {cor_roe};'>
                <h3>ROE (5 Fatores)</h3>
                <h2>{carga_trib*100:.1f}% × {carga_juros*100:.1f}% × {margem_ebit*100:.1f}% × {giro_ativo:.2f} × {multiplicador:.2f}</h2>
                <h1 style='color: {cor_roe};'>{roe_5fatores:.2f}%</h1>
                <p>Verificação (LL/PL): {roe_direto:.2f}%</p>
            </div>
        """, unsafe_allow_html=True)
    
    # Gráfico de contribuição
    st.markdown("#### 📈 Análise de Contribuição de Cada Fator")
    
    # Calcular contribuição marginal de cada fator
    # Usando log para linearizar a multiplicação
    log_fatores = {
        'Carga Tributária': np.log(carga_trib) if carga_trib > 0 else -5,
        'Carga de Juros': np.log(carga_juros) if carga_juros > 0 else -5,
        'Margem EBIT': np.log(margem_ebit) if margem_ebit > 0 else -5,
        'Giro do Ativo': np.log(giro_ativo) if giro_ativo > 0 else -5,
        'Multiplicador': np.log(multiplicador) if multiplicador > 0 else -5
    }
    
    # Normalizar para mostrar contribuição percentual
    total_log = sum(log_fatores.values())
    contrib_pct = {k: (v/total_log)*100 if total_log != 0 else 20 for k, v in log_fatores.items()}
    
    fig = go.Figure(data=[
        go.Bar(
            x=list(contrib_pct.keys()),
            y=list(contrib_pct.values()),
            marker_color=['#ef4444', '#f97316', '#22c55e', '#3b82f6', '#ec4899'],
            text=[f'{v:.1f}%' for v in contrib_pct.values()],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title="Contribuição Relativa de Cada Fator para o ROE",
        yaxis_title="Contribuição (%)",
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Interpretação automática
    st.markdown("#### 💡 Diagnóstico Automático")
    
    diagnosticos = []
    
    # Carga tributária
    aliquota_efetiva = (1 - carga_trib) * 100
    if aliquota_efetiva < 25:
        diagnosticos.append(("✅", f"Carga tributária efetiva baixa ({aliquota_efetiva:.1f}%) - possíveis incentivos fiscais", "#dcfce7"))
    elif aliquota_efetiva > 40:
        diagnosticos.append(("⚠️", f"Carga tributária elevada ({aliquota_efetiva:.1f}%) - verificar planejamento tributário", "#fee2e2"))
    
    # Carga de juros
    if carga_juros > 0.9:
        diagnosticos.append(("✅", "Baixo impacto dos juros - estrutura de capital conservadora", "#dcfce7"))
    elif carga_juros < 0.7:
        diagnosticos.append(("⚠️", f"Alto impacto dos juros (apenas {carga_juros*100:.1f}% do EBIT sobra após juros) - risco financeiro", "#fee2e2"))
    
    # Margem EBIT
    if margem_ebit > 0.15:
        diagnosticos.append(("✅", f"Margem operacional sólida ({margem_ebit*100:.1f}%) - boa eficiência", "#dcfce7"))
    elif margem_ebit < 0.08:
        diagnosticos.append(("⚠️", f"Margem operacional apertada ({margem_ebit*100:.1f}%) - vulnerável a pressões de custo", "#fee2e2"))
    
    # Giro do ativo
    if giro_ativo > 1.5:
        diagnosticos.append(("✅", f"Alto giro do ativo ({giro_ativo:.2f}x) - uso eficiente dos recursos", "#dcfce7"))
    elif giro_ativo < 0.5:
        diagnosticos.append(("⚠️", f"Baixo giro do ativo ({giro_ativo:.2f}x) - possível capacidade ociosa", "#fef3c7"))
    
    # Multiplicador
    if multiplicador > 3:
        diagnosticos.append(("⚠️", f"Alta alavancagem ({multiplicador:.2f}x) - ROE amplificado mas com risco", "#fef3c7"))
    elif multiplicador < 1.5:
        diagnosticos.append(("ℹ️", f"Baixa alavancagem ({multiplicador:.2f}x) - estrutura conservadora, possível subotimização", "#dbeafe"))
    
    for emoji, texto, cor in diagnosticos:
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 10px; border-radius: 10px; margin-bottom: 5px;'>
                {emoji} {texto}
            </div>
        """, unsafe_allow_html=True)


def renderizar_diagnostico_comparativo():
    """Diagnóstico comparativo entre múltiplas empresas."""
    
    st.markdown("### 📊 Diagnóstico Comparativo: 3 Empresas do Mesmo Setor")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Contexto:</strong><br>
            <em>Três empresas do setor de alimentos industrializados competem no mesmo mercado. 
            Todas têm capital aberto e divulgaram seus resultados anuais. 
            Seu desafio é identificar qual tem o melhor modelo de rentabilidade.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados das empresas
    empresas_data = {
        "Nutri Foods S.A.": {
            "receita": 5200, "ebit": 520, "desp_fin": 80, "lair": 470, "ll": 310,
            "ativo": 3200, "pl": 1600, "setor": "Alimentos", "perfil": "Líder de Mercado"
        },
        "Sabor Brasil Ltda.": {
            "receita": 2800, "ebit": 392, "desp_fin": 140, "lair": 280, "ll": 185,
            "ativo": 2100, "pl": 700, "setor": "Alimentos", "perfil": "Challenger"
        },
        "AgroNut Ind. S.A.": {
            "receita": 4100, "ebit": 287, "desp_fin": 45, "lair": 262, "ll": 173,
            "ativo": 4500, "pl": 2250, "setor": "Alimentos", "perfil": "Conservadora"
        }
    }
    
    st.markdown("#### 📋 Dados Financeiros (R$ milhões)")
    
    # Tabela de dados
    dados_tabela = {
        "Indicador": ["Receita Líquida", "EBIT", "Despesas Financeiras", "LAIR", "Lucro Líquido", 
                     "Ativo Total", "Patrimônio Líquido"],
        "Nutri Foods": [5200, 520, 80, 470, 310, 3200, 1600],
        "Sabor Brasil": [2800, 392, 140, 280, 185, 2100, 700],
        "AgroNut": [4100, 287, 45, 262, 173, 4500, 2250]
    }
    
    df_dados = pd.DataFrame(dados_tabela)
    st.dataframe(df_dados, use_container_width=True, hide_index=True)
    
    # Calcular indicadores para cada empresa
    def calcular_dupont(dados):
        carga_trib = dados['ll'] / dados['lair'] if dados['lair'] > 0 else 0
        carga_juros = dados['lair'] / dados['ebit'] if dados['ebit'] > 0 else 0
        margem_ebit = dados['ebit'] / dados['receita'] if dados['receita'] > 0 else 0
        giro_ativo = dados['receita'] / dados['ativo'] if dados['ativo'] > 0 else 0
        multiplicador = dados['ativo'] / dados['pl'] if dados['pl'] > 0 else 0
        roe = dados['ll'] / dados['pl'] * 100 if dados['pl'] > 0 else 0
        roa = dados['ll'] / dados['ativo'] * 100 if dados['ativo'] > 0 else 0
        
        return {
            'carga_trib': carga_trib,
            'carga_juros': carga_juros,
            'margem_ebit': margem_ebit,
            'giro_ativo': giro_ativo,
            'multiplicador': multiplicador,
            'roe': roe,
            'roa': roa
        }
    
    indicadores = {nome: calcular_dupont(dados) for nome, dados in empresas_data.items()}
    
    st.markdown("---")
    st.markdown("#### 📈 Análise DuPont Comparativa (5 Fatores)")
    
    # Tabela de indicadores
    ind_tabela = {
        "Fator": ["Carga Tributária", "Carga de Juros", "Margem EBIT", "Giro do Ativo", 
                 "Multiplicador", "ROE", "ROA"],
        "Nutri Foods": [
            f"{indicadores['Nutri Foods S.A.']['carga_trib']*100:.1f}%",
            f"{indicadores['Nutri Foods S.A.']['carga_juros']*100:.1f}%",
            f"{indicadores['Nutri Foods S.A.']['margem_ebit']*100:.1f}%",
            f"{indicadores['Nutri Foods S.A.']['giro_ativo']:.2f}x",
            f"{indicadores['Nutri Foods S.A.']['multiplicador']:.2f}x",
            f"{indicadores['Nutri Foods S.A.']['roe']:.1f}%",
            f"{indicadores['Nutri Foods S.A.']['roa']:.1f}%"
        ],
        "Sabor Brasil": [
            f"{indicadores['Sabor Brasil Ltda.']['carga_trib']*100:.1f}%",
            f"{indicadores['Sabor Brasil Ltda.']['carga_juros']*100:.1f}%",
            f"{indicadores['Sabor Brasil Ltda.']['margem_ebit']*100:.1f}%",
            f"{indicadores['Sabor Brasil Ltda.']['giro_ativo']:.2f}x",
            f"{indicadores['Sabor Brasil Ltda.']['multiplicador']:.2f}x",
            f"{indicadores['Sabor Brasil Ltda.']['roe']:.1f}%",
            f"{indicadores['Sabor Brasil Ltda.']['roa']:.1f}%"
        ],
        "AgroNut": [
            f"{indicadores['AgroNut Ind. S.A.']['carga_trib']*100:.1f}%",
            f"{indicadores['AgroNut Ind. S.A.']['carga_juros']*100:.1f}%",
            f"{indicadores['AgroNut Ind. S.A.']['margem_ebit']*100:.1f}%",
            f"{indicadores['AgroNut Ind. S.A.']['giro_ativo']:.2f}x",
            f"{indicadores['AgroNut Ind. S.A.']['multiplicador']:.2f}x",
            f"{indicadores['AgroNut Ind. S.A.']['roe']:.1f}%",
            f"{indicadores['AgroNut Ind. S.A.']['roa']:.1f}%"
        ]
    }
    
    df_ind = pd.DataFrame(ind_tabela)
    st.dataframe(df_ind, use_container_width=True, hide_index=True)
    
    # Métricas de destaque
    st.markdown("---")
    st.markdown("#### 🏆 Comparativo de ROE")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        roe_nutri = indicadores['Nutri Foods S.A.']['roe']
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>🏭 Nutri Foods</h4>
                <h2 style='color: #3b82f6;'>{roe_nutri:.1f}%</h2>
                <p>Líder de Mercado</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        roe_sabor = indicadores['Sabor Brasil Ltda.']['roe']
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>🌟 Sabor Brasil</h4>
                <h2 style='color: #22c55e;'>{roe_sabor:.1f}%</h2>
                <p>Challenger Agressivo</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        roe_agro = indicadores['AgroNut Ind. S.A.']['roe']
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>🌾 AgroNut</h4>
                <h2 style='color: #f97316;'>{roe_agro:.1f}%</h2>
                <p>Conservadora</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráficos comparativos
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar comparativo
        categorias = ['Carga Trib.', 'Carga Juros', 'Margem EBIT', 'Giro Ativo', 'Alavancagem']
        
        fig = go.Figure()
        
        cores = ['#3b82f6', '#22c55e', '#f97316']
        empresas_nomes = ['Nutri Foods S.A.', 'Sabor Brasil Ltda.', 'AgroNut Ind. S.A.']
        
        for i, (nome, cor) in enumerate(zip(empresas_nomes, cores)):
            ind = indicadores[nome]
            valores = [
                ind['carga_trib'] * 100,
                ind['carga_juros'] * 100,
                ind['margem_ebit'] * 100 * 5,  # Escalar para visualização
                ind['giro_ativo'] * 50,
                ind['multiplicador'] * 20
            ]
            
            fig.add_trace(go.Scatterpolar(
                r=valores + [valores[0]],
                theta=categorias + [categorias[0]],
                fill='toself',
                name=nome.split()[0],
                line_color=cor,
                opacity=0.6
            ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Radar: Perfil DuPont",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Barras empilhadas conceituais
        fig2 = go.Figure()
        
        empresas_curtos = ['Nutri Foods', 'Sabor Brasil', 'AgroNut']
        
        fig2.add_trace(go.Bar(
            name='Margem EBIT',
            x=empresas_curtos,
            y=[indicadores[e]['margem_ebit']*100 for e in empresas_nomes],
            marker_color='#22c55e'
        ))
        
        fig2.add_trace(go.Bar(
            name='Giro do Ativo',
            x=empresas_curtos,
            y=[indicadores[e]['giro_ativo']*10 for e in empresas_nomes],
            marker_color='#3b82f6'
        ))
        
        fig2.add_trace(go.Bar(
            name='Multiplicador',
            x=empresas_curtos,
            y=[indicadores[e]['multiplicador']*5 for e in empresas_nomes],
            marker_color='#f97316'
        ))
        
        fig2.update_layout(
            title="Componentes do ROE (normalizado)",
            barmode='group',
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Análise qualitativa
    st.markdown("---")
    st.markdown("#### 🔍 Diagnóstico Qualitativo")
    
    analises = [
        {
            "empresa": "Nutri Foods S.A.",
            "cor": "#dbeafe",
            "pontos_fortes": [
                "Melhor ROA do grupo (9,7%) - eficiência operacional",
                "Margem EBIT de 10% - poder de precificação",
                "Baixo impacto de juros - estrutura financeira saudável"
            ],
            "pontos_fracos": [
                "Giro moderado (1,63x) - pode haver espaço para otimização",
                "Alavancagem moderada (2x) - poderia usar mais dívida barata"
            ],
            "estrategia": "Foco em qualidade e marca, pricing premium"
        },
        {
            "empresa": "Sabor Brasil Ltda.",
            "cor": "#dcfce7",
            "pontos_fortes": [
                "Maior ROE do grupo (26,4%) - retorno atrativo",
                "Excelente margem EBIT (14%) - operação muito eficiente",
                "Bom giro (1,33x) - gestão de ativos adequada"
            ],
            "pontos_fracos": [
                "Alta alavancagem (3x) - risco financeiro elevado",
                "Carga de juros alta (71,4%) - vulnerável a taxas",
                "ROE muito dependente de dívida"
            ],
            "estrategia": "Crescimento agressivo com alavancagem, aposta no scale"
        },
        {
            "empresa": "AgroNut Ind. S.A.",
            "cor": "#fef3c7",
            "pontos_fortes": [
                "Estrutura conservadora - baixo risco financeiro",
                "Carga de juros mínima (91,3%) - praticamente sem impacto",
                "Baixa alavancagem (2x) - solidez patrimonial"
            ],
            "pontos_fracos": [
                "Menor ROE (7,7%) - retorno abaixo do custo de capital?",
                "Menor margem EBIT (7%) - eficiência operacional a melhorar",
                "Baixo giro (0,91x) - ativos subutilizados"
            ],
            "estrategia": "Conservadora, prioriza segurança sobre retorno"
        }
    ]
    
    for analise in analises:
        with st.expander(f"📌 {analise['empresa']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**✅ Pontos Fortes:**")
                for ponto in analise['pontos_fortes']:
                    st.markdown(f"- {ponto}")
            
            with col2:
                st.markdown("**⚠️ Pontos Fracos:**")
                for ponto in analise['pontos_fracos']:
                    st.markdown(f"- {ponto}")
            
            st.info(f"**Estratégia identificada:** {analise['estrategia']}")
    
    # Recomendação
    st.markdown("---")
    st.markdown("#### 🎯 Qual Empresa Você Escolheria?")
    
    escolha = st.radio(
        "Se você fosse um investidor, qual empresa escolheria?",
        options=["Nutri Foods (ROE 19,4%, moderado)", 
                "Sabor Brasil (ROE 26,4%, agressivo)", 
                "AgroNut (ROE 7,7%, conservador)"],
        key="escolha_empresa"
    )
    
    justificativa = st.text_area(
        "Justifique sua escolha considerando risco e retorno:",
        placeholder="Considere os componentes do ROE e os riscos de cada estratégia...",
        height=80,
        key="justif_escolha"
    )


def renderizar_exercicio_interpretativo():
    """Exercício interpretativo escrito completo."""
    
    st.markdown("### ✍️ Exercício Interpretativo: Relatório de Análise")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>📋 ATIVIDADE AVALIATIVA</strong><br>
            <em>Você é analista de uma gestora de investimentos e precisa elaborar um relatório 
            sobre a empresa MegaIndústria S.A. com base nos dados apresentados.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Dados da empresa
    st.markdown("#### 📊 Dados da MegaIndústria S.A. (3 anos)")
    
    dados_historico = {
        "Indicador": ["Receita Líquida (R$ mi)", "EBIT (R$ mi)", "Desp. Financeiras (R$ mi)",
                     "LAIR (R$ mi)", "Lucro Líquido (R$ mi)", "Ativo Total (R$ mi)",
                     "Patrimônio Líquido (R$ mi)"],
        "2021": [3500, 525, 120, 430, 284, 2800, 1400],
        "2022": [4200, 546, 180, 400, 264, 3500, 1500],
        "2023": [5040, 504, 270, 280, 185, 4200, 1550]
    }
    
    df_hist = pd.DataFrame(dados_historico)
    st.dataframe(df_hist, use_container_width=True, hide_index=True)
    
    # Calcular indicadores para cada ano
    def calc_ano(rec, ebit, fin, lair, ll, ativo, pl):
        return {
            'carga_trib': ll/lair if lair > 0 else 0,
            'carga_juros': lair/ebit if ebit > 0 else 0,
            'margem_ebit': ebit/rec if rec > 0 else 0,
            'giro_ativo': rec/ativo if ativo > 0 else 0,
            'multiplicador': ativo/pl if pl > 0 else 0,
            'roe': ll/pl*100 if pl > 0 else 0,
            'roa': ll/ativo*100 if ativo > 0 else 0
        }
    
    ind_2021 = calc_ano(3500, 525, 120, 430, 284, 2800, 1400)
    ind_2022 = calc_ano(4200, 546, 180, 400, 264, 3500, 1500)
    ind_2023 = calc_ano(5040, 504, 270, 280, 185, 4200, 1550)
    
    # Tabela de indicadores calculados
    st.markdown("#### 📈 Evolução dos Indicadores DuPont")
    
    ind_evolucao = {
        "Indicador": ["Carga Tributária", "Carga de Juros", "Margem EBIT", 
                     "Giro do Ativo", "Multiplicador", "ROE", "ROA"],
        "2021": [
            f"{ind_2021['carga_trib']*100:.1f}%",
            f"{ind_2021['carga_juros']*100:.1f}%",
            f"{ind_2021['margem_ebit']*100:.1f}%",
            f"{ind_2021['giro_ativo']:.2f}x",
            f"{ind_2021['multiplicador']:.2f}x",
            f"{ind_2021['roe']:.1f}%",
            f"{ind_2021['roa']:.1f}%"
        ],
        "2022": [
            f"{ind_2022['carga_trib']*100:.1f}%",
            f"{ind_2022['carga_juros']*100:.1f}%",
            f"{ind_2022['margem_ebit']*100:.1f}%",
            f"{ind_2022['giro_ativo']:.2f}x",
            f"{ind_2022['multiplicador']:.2f}x",
            f"{ind_2022['roe']:.1f}%",
            f"{ind_2022['roa']:.1f}%"
        ],
        "2023": [
            f"{ind_2023['carga_trib']*100:.1f}%",
            f"{ind_2023['carga_juros']*100:.1f}%",
            f"{ind_2023['margem_ebit']*100:.1f}%",
            f"{ind_2023['giro_ativo']:.2f}x",
            f"{ind_2023['multiplicador']:.2f}x",
            f"{ind_2023['roe']:.1f}%",
            f"{ind_2023['roa']:.1f}%"
        ],
        "Tendência": ["↔️", "↘️ Piora", "↘️ Piora", "↔️", "↗️ Sobe", "↘️ Piora", "↘️ Piora"]
    }
    
    df_evolucao = pd.DataFrame(ind_evolucao)
    st.dataframe(df_evolucao, use_container_width=True, hide_index=True)
    
    # Gráfico de evolução
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        anos = [2021, 2022, 2023]
        
        fig1.add_trace(go.Scatter(
            x=anos, y=[ind_2021['roe'], ind_2022['roe'], ind_2023['roe']],
            name='ROE', line=dict(color='#3b82f6', width=3), mode='lines+markers'
        ))
        
        fig1.add_trace(go.Scatter(
            x=anos, y=[ind_2021['roa'], ind_2022['roa'], ind_2023['roa']],
            name='ROA', line=dict(color='#22c55e', width=3), mode='lines+markers'
        ))
        
        fig1.update_layout(title="Evolução ROE e ROA (%)", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        
        fig2.add_trace(go.Bar(
            x=['2021', '2022', '2023'],
            y=[ind_2021['carga_juros']*100, ind_2022['carga_juros']*100, ind_2023['carga_juros']*100],
            name='Carga de Juros',
            marker_color='#f97316'
        ))
        
        fig2.update_layout(title="Deterioração da Carga de Juros (%)", height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Exercícios de redação
    st.markdown("#### ✏️ Elabore seu Relatório de Análise")
    
    st.markdown("**Parte 1: Diagnóstico (análise dos dados)**")
    
    diag1 = st.text_area(
        "1. Analise a evolução da receita e do lucro. O que você observa?",
        placeholder="Descreva o que os números mostram (receita cresceu X%, lucro caiu Y%...)",
        height=100,
        key="diag1"
    )
    
    diag2 = st.text_area(
        "2. Usando o modelo DuPont expandido, identifique qual(is) fator(es) explicam a queda do ROE.",
        placeholder="Analise cada um dos 5 fatores e identifique o(s) responsável(is)...",
        height=120,
        key="diag2"
    )
    
    st.markdown("**Parte 2: Interpretação Econômica**")
    
    interp1 = st.text_area(
        "3. Por que a Carga de Juros deteriorou tão rapidamente? Relacione com a estratégia da empresa.",
        placeholder="Considere: crescimento da receita, aumento dos ativos, fonte de financiamento...",
        height=100,
        key="interp1"
    )
    
    interp2 = st.text_area(
        "4. O crescimento da empresa foi sustentável do ponto de vista financeiro? Justifique.",
        placeholder="Analise se o modelo de crescimento é viável no longo prazo...",
        height=100,
        key="interp2"
    )
    
    st.markdown("**Parte 3: Recomendações**")
    
    recom = st.text_area(
        "5. Quais medidas você recomendaria à administração para reverter a tendência de queda do ROE?",
        placeholder="Liste pelo menos 3 recomendações concretas e justificadas...",
        height=120,
        key="recom"
    )
    
    conclusao = st.text_area(
        "6. Como investidor, você compraria, manteria ou venderia as ações? Por quê?",
        placeholder="Dê sua recomendação final considerando risco e retorno...",
        height=100,
        key="conclusao"
    )
    
    # Contagem de palavras
    total_palavras = sum(len(t.split()) for t in [diag1, diag2, interp1, interp2, recom, conclusao])
    st.caption(f"Total de palavras escritas: {total_palavras}")
    
    if total_palavras < 200:
        st.warning("Seu relatório está curto. Recomendamos pelo menos 300 palavras para uma análise completa.")
    elif total_palavras >= 300:
        st.success("Boa extensão! Relatório com profundidade adequada.")
    
    st.markdown("---")
    
    # Gabarito
    if st.button("📖 Ver Gabarito Comentado", type="primary"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
                <h4>📋 Gabarito Comentado</h4>
                
                <p><strong>1. Evolução Receita vs Lucro:</strong></p>
                <ul>
                    <li>Receita cresceu 44% em 2 anos (R$ 3.500 → R$ 5.040 mi)</li>
                    <li>Lucro Líquido CAIU 35% (R$ 284 → R$ 185 mi)</li>
                    <li>Típico caso de "crescimento que destrói valor"</li>
                </ul>
                
                <p><strong>2. Fatores DuPont responsáveis:</strong></p>
                <ul>
                    <li><strong>Carga Tributária:</strong> Estável (~66%) - NÃO é o problema</li>
                    <li><strong>Carga de Juros:</strong> CAIU de 81,9% para 55,6% - PRINCIPAL VILÃO</li>
                    <li><strong>Margem EBIT:</strong> Caiu de 15% para 10% - deterioração operacional</li>
                    <li><strong>Giro do Ativo:</strong> Estável (~1,2x) - neutro</li>
                    <li><strong>Multiplicador:</strong> Subiu de 2x para 2,7x - mais dívida</li>
                </ul>
                <p><strong>Conclusão:</strong> ROE caiu porque margem operacional piorou E custo financeiro explodiu.</p>
                
                <p><strong>3. Por que Carga de Juros deteriorou:</strong></p>
                <ul>
                    <li>Empresa financiou crescimento com DÍVIDA (ativo +50%, PL +11%)</li>
                    <li>Despesas financeiras mais que dobraram (R$ 120 → R$ 270 mi)</li>
                    <li>EBIT não acompanhou o custo da dívida</li>
                    <li>Alavancagem subiu em momento de taxa de juros alta</li>
                </ul>
                
                <p><strong>4. Sustentabilidade do crescimento:</strong></p>
                <p><strong>NÃO foi sustentável porque:</strong></p>
                <ul>
                    <li>Crescimento veio 100% de dívida cara</li>
                    <li>Margem operacional comprimida (menor poder de precificação ou custos maiores)</li>
                    <li>ROA caiu de 10,1% para 4,4% - ativos novos não geram retorno adequado</li>
                    <li>Alavancagem está destruindo valor (ROA < custo da dívida)</li>
                </ul>
                
                <p><strong>5. Recomendações à administração:</strong></p>
                <ol>
                    <li><strong>Reduzir dívida:</strong> Vender ativos não-core, fazer aumento de capital</li>
                    <li><strong>Melhorar margem:</strong> Revisar preços, cortar custos, focar em produtos rentáveis</li>
                    <li><strong>Desacelerar crescimento:</strong> Não expandir até normalizar rentabilidade</li>
                    <li><strong>Renegociar dívidas:</strong> Alongar prazo, buscar taxas menores</li>
                    <li><strong>Melhorar giro:</strong> Otimizar capital de giro, reduzir ativos improdutivos</li>
                </ol>
                
                <p><strong>6. Recomendação de investimento:</strong></p>
                <p><strong>VENDER</strong> - A empresa está em trajetória de destruição de valor:</p>
                <ul>
                    <li>ROE caindo (20,3% → 11,9%) apesar do crescimento de receita</li>
                    <li>Risco financeiro aumentando (alavancagem e juros)</li>
                    <li>Sem sinais de reversão da tendência</li>
                    <li>Reevaliar após plano de reestruturação concreto</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Síntese
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>DuPont Expandido:</strong> 5 fatores permitem diagnóstico mais preciso</li>
                <li><strong>Carga de Juros:</strong> Revela o impacto da estrutura de capital no lucro</li>
                <li><strong>Crescimento nem sempre é bom:</strong> Se destrói rentabilidade, destrói valor</li>
                <li><strong>Diagnóstico comparativo:</strong> Revela estratégias diferentes para mesmo ROE</li>
                <li><strong>Análise de tendência:</strong> Mais importante que foto é o filme</li>
                <li><strong>Recomendação fundamentada:</strong> Basear em dados, não em intuição</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()