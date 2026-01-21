"""
Módulo 5 - Análise da Performance (DRE)
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Exercício prático: cálculo e interpretação de margens
- Estudo de caso: empresa com lucro crescente e margem decrescente
- Discussão: lucro contábil vs. desempenho econômico
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📈 Módulo 5 - Análise da Performance (DRE)</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Calcular e interpretar as principais margens de lucro</li>
                <li>Analisar a evolução da performance ao longo do tempo</li>
                <li>Identificar situações de lucro crescente com margem decrescente</li>
                <li>Distinguir lucro contábil de desempenho econômico real</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Cálculo de Margens",
        "📉 Estudo de Caso",
        "💬 Lucro vs. Desempenho"
    ])
    
    with tab1:
        renderizar_calculo_margens()
    
    with tab2:
        renderizar_estudo_caso()
    
    with tab3:
        renderizar_discussao_lucro_desempenho()


def get_dre_exemplo():
    """Retorna DRE exemplo para análise."""
    
    dre = {
        "empresa": "Distribuidora Nacional S.A.",
        "setor": "Comércio Atacadista",
        "dados": {
            2021: {
                "Receita Bruta": 2500000,
                "(-) Deduções": -375000,
                "Receita Líquida": 2125000,
                "(-) CMV": -1487500,
                "Lucro Bruto": 637500,
                "(-) Despesas Operacionais": -382500,
                "    Vendas": -212500,
                "    Administrativas": -127500,
                "    Outras": -42500,
                "Resultado Operacional (EBIT)": 255000,
                "(-) Despesas Financeiras": -85000,
                "(+) Receitas Financeiras": 21250,
                "Resultado Antes IR/CS": 191250,
                "(-) IR/CS": -65025,
                "Lucro Líquido": 126225
            },
            2022: {
                "Receita Bruta": 3000000,
                "(-) Deduções": -450000,
                "Receita Líquida": 2550000,
                "(-) CMV": -1836000,
                "Lucro Bruto": 714000,
                "(-) Despesas Operacionais": -484500,
                "    Vendas": -280500,
                "    Administrativas": -153000,
                "    Outras": -51000,
                "Resultado Operacional (EBIT)": 229500,
                "(-) Despesas Financeiras": -114750,
                "(+) Receitas Financeiras": 25500,
                "Resultado Antes IR/CS": 140250,
                "(-) IR/CS": -47685,
                "Lucro Líquido": 92565
            },
            2023: {
                "Receita Bruta": 3750000,
                "(-) Deduções": -562500,
                "Receita Líquida": 3187500,
                "(-) CMV": -2358750,
                "Lucro Bruto": 828750,
                "(-) Despesas Operacionais": -606875,
                "    Vendas": -366563,
                "    Administrativas": -175313,
                "    Outras": -65000,
                "Resultado Operacional (EBIT)": 221875,
                "(-) Despesas Financeiras": -159375,
                "(+) Receitas Financeiras": 31875,
                "Resultado Antes IR/CS": 94375,
                "(-) IR/CS": -32088,
                "Lucro Líquido": 62288
            }
        }
    }
    return dre


def calcular_margens(dados_ano, receita_liquida):
    """Calcula todas as margens a partir dos dados da DRE."""
    
    return {
        "Margem Bruta": (dados_ano["Lucro Bruto"] / receita_liquida) * 100,
        "Margem Operacional (EBIT)": (dados_ano["Resultado Operacional (EBIT)"] / receita_liquida) * 100,
        "Margem Líquida": (dados_ano["Lucro Líquido"] / receita_liquida) * 100,
        "Margem EBITDA": ((dados_ano["Resultado Operacional (EBIT)"] + 50000) / receita_liquida) * 100  # Assumindo depreciação
    }


def renderizar_calculo_margens():
    """Exercício prático de cálculo e interpretação de margens."""
    
    st.markdown("### 📊 Exercício Prático: Cálculo e Interpretação de Margens")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Aprender a calcular e interpretar as principais margens de lucratividade 
            a partir de uma Demonstração do Resultado do Exercício (DRE).</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Revisão das Margens
    st.markdown("#### 📚 Revisão: As Principais Margens")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>📈 Margem Bruta</h4>
                <p><strong>Fórmula:</strong> (Lucro Bruto / Receita Líquida) × 100</p>
                <p><strong>Indica:</strong> Eficiência na produção/aquisição de mercadorias</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📊 Margem Operacional (EBIT)</h4>
                <p><strong>Fórmula:</strong> (EBIT / Receita Líquida) × 100</p>
                <p><strong>Indica:</strong> Eficiência operacional total do negócio</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #fce7f3; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>💰 Margem Líquida</h4>
                <p><strong>Fórmula:</strong> (Lucro Líquido / Receita Líquida) × 100</p>
                <p><strong>Indica:</strong> Quanto sobra para os acionistas de cada R$ vendido</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>⚡ Margem EBITDA</h4>
                <p><strong>Fórmula:</strong> (EBITDA / Receita Líquida) × 100</p>
                <p><strong>Indica:</strong> Geração de caixa operacional (proxy)</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simulador de DRE
    st.markdown("#### 🧮 Simulador: Monte sua DRE e Calcule as Margens")
    
    st.markdown("Insira os valores da DRE para calcular automaticamente as margens:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        receita_bruta = st.number_input("Receita Bruta (R$)", min_value=0, value=1000000, step=50000, key="rb")
        deducoes = st.number_input("(-) Deduções (R$)", min_value=0, value=150000, step=10000, key="ded")
        cmv = st.number_input("(-) CMV (R$)", min_value=0, value=500000, step=25000, key="cmv")
        desp_operacionais = st.number_input("(-) Despesas Operacionais (R$)", min_value=0, value=200000, step=10000, key="desp_op")
    
    with col2:
        desp_financeiras = st.number_input("(-) Despesas Financeiras (R$)", min_value=0, value=50000, step=5000, key="desp_fin")
        rec_financeiras = st.number_input("(+) Receitas Financeiras (R$)", min_value=0, value=10000, step=5000, key="rec_fin")
        depreciacao = st.number_input("Depreciação (inclusa nas desp. op.) (R$)", min_value=0, value=30000, step=5000, key="deprec")
        aliquota_ir = st.slider("Alíquota IR/CS (%)", min_value=0, max_value=50, value=34, key="ir")
    
    # Cálculos
    receita_liquida = receita_bruta - deducoes
    lucro_bruto = receita_liquida - cmv
    ebit = lucro_bruto - desp_operacionais
    ebitda = ebit + depreciacao
    resultado_financeiro = rec_financeiras - desp_financeiras
    lair = ebit + resultado_financeiro
    ir_cs = lair * (aliquota_ir / 100) if lair > 0 else 0
    lucro_liquido = lair - ir_cs
    
    st.markdown("---")
    
    # DRE Calculada
    st.markdown("#### 📋 DRE Calculada")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        dre_calc = pd.DataFrame({
            "Conta": [
                "Receita Bruta",
                "(-) Deduções",
                "= Receita Líquida",
                "(-) CMV",
                "= Lucro Bruto",
                "(-) Despesas Operacionais",
                "= EBIT",
                "(+/-) Resultado Financeiro",
                "= LAIR",
                "(-) IR/CS",
                "= Lucro Líquido"
            ],
            "Valor (R$)": [
                f"{receita_bruta:,.0f}",
                f"({deducoes:,.0f})",
                f"{receita_liquida:,.0f}",
                f"({cmv:,.0f})",
                f"{lucro_bruto:,.0f}",
                f"({desp_operacionais:,.0f})",
                f"{ebit:,.0f}",
                f"{resultado_financeiro:,.0f}",
                f"{lair:,.0f}",
                f"({ir_cs:,.0f})",
                f"{lucro_liquido:,.0f}"
            ]
        })
        st.dataframe(dre_calc, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("##### 📈 Margens Calculadas")
        
        if receita_liquida > 0:
            mg_bruta = (lucro_bruto / receita_liquida) * 100
            mg_ebit = (ebit / receita_liquida) * 100
            mg_ebitda = (ebitda / receita_liquida) * 100
            mg_liquida = (lucro_liquido / receita_liquida) * 100
            
            st.metric("Margem Bruta", f"{mg_bruta:.1f}%")
            st.metric("Margem EBIT", f"{mg_ebit:.1f}%")
            st.metric("Margem EBITDA", f"{mg_ebitda:.1f}%")
            st.metric("Margem Líquida", f"{mg_liquida:.1f}%")
        else:
            st.warning("Receita Líquida deve ser maior que zero")
    
    # Gráfico de Cascata
    if receita_liquida > 0:
        st.markdown("#### 📊 Visualização: Cascata de Lucratividade")
        
        fig = go.Figure(go.Waterfall(
            name="DRE",
            orientation="v",
            measure=["absolute", "relative", "relative", "relative", "relative", "total"],
            x=["Receita Líq.", "CMV", "Desp. Oper.", "Resultado Fin.", "IR/CS", "Lucro Líq."],
            y=[receita_liquida, -cmv, -desp_operacionais, resultado_financeiro, -ir_cs, lucro_liquido],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            decreasing={"marker": {"color": "#ef4444"}},
            increasing={"marker": {"color": "#22c55e"}},
            totals={"marker": {"color": "#3b82f6"}}
        ))
        
        fig.update_layout(
            title="Da Receita ao Lucro Líquido",
            showlegend=False,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Exercício de fixação
    st.markdown("#### ✏️ Exercício de Fixação")
    
    st.markdown("""
        **Dados:** Uma empresa apresentou Receita Líquida de R$ 800.000, CMV de R$ 480.000, 
        Despesas Operacionais de R$ 160.000, Resultado Financeiro de -R$ 40.000 e IR/CS de R$ 40.800.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        resp_mg_bruta = st.number_input("Margem Bruta (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ex_mgb")
    with col2:
        resp_mg_ebit = st.number_input("Margem EBIT (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ex_mge")
    with col3:
        resp_mg_liq = st.number_input("Margem Líquida (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1, key="ex_mgl")
    
    if st.button("Verificar Respostas", key="btn_verif_margens"):
        # Gabarito: LB=320.000, EBIT=160.000, LL=79.200
        mg_bruta_correta = 40.0
        mg_ebit_correta = 20.0
        mg_liq_correta = 9.9
        
        acertos = 0
        
        if abs(resp_mg_bruta - mg_bruta_correta) < 0.5:
            st.success(f"✅ Margem Bruta: {mg_bruta_correta}% - Correto!")
            acertos += 1
        else:
            st.error(f"❌ Margem Bruta: Sua resposta {resp_mg_bruta}% | Correta: {mg_bruta_correta}%")
            st.caption("   LB = 800.000 - 480.000 = 320.000 → MB = 320.000/800.000 = 40%")
        
        if abs(resp_mg_ebit - mg_ebit_correta) < 0.5:
            st.success(f"✅ Margem EBIT: {mg_ebit_correta}% - Correto!")
            acertos += 1
        else:
            st.error(f"❌ Margem EBIT: Sua resposta {resp_mg_ebit}% | Correta: {mg_ebit_correta}%")
            st.caption("   EBIT = 320.000 - 160.000 = 160.000 → ME = 160.000/800.000 = 20%")
        
        if abs(resp_mg_liq - mg_liq_correta) < 0.5:
            st.success(f"✅ Margem Líquida: {mg_liq_correta}% - Correto!")
            acertos += 1
        else:
            st.error(f"❌ Margem Líquida: Sua resposta {resp_mg_liq}% | Correta: {mg_liq_correta}%")
            st.caption("   LL = 160.000 - 40.000 - 40.800 = 79.200 → ML = 79.200/800.000 = 9,9%")
        
        if acertos == 3:
            st.balloons()


def renderizar_estudo_caso():
    """Estudo de caso: lucro crescente com margem decrescente."""
    
    st.markdown("### 📉 Estudo de Caso: O Paradoxo do Crescimento")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>🔍 Caso: Distribuidora Nacional S.A.</strong><br>
            <em>A empresa apresentou lucro crescente nos últimos 3 anos. O CEO comemora os resultados. 
            Mas os analistas estão preocupados. Por quê?</em>
        </div>
    """, unsafe_allow_html=True)
    
    dre = get_dre_exemplo()
    
    st.markdown(f"**Empresa:** {dre['empresa']} | **Setor:** {dre['setor']}")
    
    # Dados resumidos
    anos = [2021, 2022, 2023]
    
    receitas = [dre['dados'][ano]['Receita Líquida'] for ano in anos]
    lucros_brutos = [dre['dados'][ano]['Lucro Bruto'] for ano in anos]
    ebits = [dre['dados'][ano]['Resultado Operacional (EBIT)'] for ano in anos]
    lucros_liquidos = [dre['dados'][ano]['Lucro Líquido'] for ano in anos]
    
    margens_bruta = [(lb/rl)*100 for lb, rl in zip(lucros_brutos, receitas)]
    margens_ebit = [(ebit/rl)*100 for ebit, rl in zip(ebits, receitas)]
    margens_liquida = [(ll/rl)*100 for ll, rl in zip(lucros_liquidos, receitas)]
    
    # Tabela comparativa
    st.markdown("#### 📋 Evolução da DRE (em R$ mil)")
    
    df_evolucao = pd.DataFrame({
        "Conta": ["Receita Líquida", "Lucro Bruto", "EBIT", "Lucro Líquido"],
        "2021": [f"{receitas[0]/1000:,.0f}", f"{lucros_brutos[0]/1000:,.0f}", 
                f"{ebits[0]/1000:,.0f}", f"{lucros_liquidos[0]/1000:,.0f}"],
        "2022": [f"{receitas[1]/1000:,.0f}", f"{lucros_brutos[1]/1000:,.0f}", 
                f"{ebits[1]/1000:,.0f}", f"{lucros_liquidos[1]/1000:,.0f}"],
        "2023": [f"{receitas[2]/1000:,.0f}", f"{lucros_brutos[2]/1000:,.0f}", 
                f"{ebits[2]/1000:,.0f}", f"{lucros_liquidos[2]/1000:,.0f}"],
        "Var. 21-23": [
            f"+{((receitas[2]/receitas[0])-1)*100:.0f}%",
            f"+{((lucros_brutos[2]/lucros_brutos[0])-1)*100:.0f}%",
            f"{((ebits[2]/ebits[0])-1)*100:.0f}%",
            f"{((lucros_liquidos[2]/lucros_liquidos[0])-1)*100:.0f}%"
        ]
    })
    st.dataframe(df_evolucao, use_container_width=True, hide_index=True)
    
    # Métricas de destaque
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        var_receita = ((receitas[2]/receitas[0])-1)*100
        st.metric("Receita 21→23", f"+{var_receita:.0f}%", delta="Crescimento")
    with col2:
        var_lucro = ((lucros_liquidos[2]/lucros_liquidos[0])-1)*100
        st.metric("Lucro Líq. 21→23", f"{var_lucro:.0f}%", delta="Queda!", delta_color="inverse")
    with col3:
        st.metric("Margem Líq. 2021", f"{margens_liquida[0]:.1f}%")
    with col4:
        st.metric("Margem Líq. 2023", f"{margens_liquida[2]:.1f}%", 
                 delta=f"{margens_liquida[2]-margens_liquida[0]:.1f}pp", delta_color="inverse")
    
    st.markdown("---")
    
    # Gráficos
    st.markdown("#### 📊 Análise Visual")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de valores absolutos
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(name='Receita Líquida', x=anos, y=[r/1000 for r in receitas], marker_color='#3b82f6'))
        fig1.add_trace(go.Bar(name='Lucro Líquido', x=anos, y=[l/1000 for l in lucros_liquidos], marker_color='#22c55e'))
        
        fig1.update_layout(
            title="Evolução em Valores Absolutos (R$ mil)",
            barmode='group',
            height=350
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # Gráfico de margens
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(name='Margem Bruta', x=anos, y=margens_bruta, mode='lines+markers', line=dict(color='#3b82f6', width=2)))
        fig2.add_trace(go.Scatter(name='Margem EBIT', x=anos, y=margens_ebit, mode='lines+markers', line=dict(color='#f97316', width=2)))
        fig2.add_trace(go.Scatter(name='Margem Líquida', x=anos, y=margens_liquida, mode='lines+markers', line=dict(color='#22c55e', width=2)))
        
        fig2.update_layout(
            title="Evolução das Margens (%)",
            yaxis_title="Margem (%)",
            height=350
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Análise dirigida
    st.markdown("#### 🔍 Análise Dirigida: Identificando as Causas")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            <strong>❓ Questão Central:</strong> A receita cresceu 50% em 2 anos, mas o lucro CAIU 51%. 
            Onde está o problema?
        </div>
    """, unsafe_allow_html=True)
    
    # Análise do CMV
    with st.expander("1️⃣ Análise do Custo das Mercadorias Vendidas (CMV)"):
        cmvs = [dre['dados'][ano]['(-) CMV'] for ano in anos]
        pct_cmv = [abs(c)/r*100 for c, r in zip(cmvs, receitas)]
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
                | Ano | CMV (R$ mil) | % Receita |
                |-----|--------------|-----------|
                | 2021 | {abs(cmvs[0])/1000:,.0f} | {pct_cmv[0]:.1f}% |
                | 2022 | {abs(cmvs[1])/1000:,.0f} | {pct_cmv[1]:.1f}% |
                | 2023 | {abs(cmvs[2])/1000:,.0f} | {pct_cmv[2]:.1f}% |
            """)
        with col2:
            st.warning(f"""
                **Diagnóstico:** O CMV subiu de {pct_cmv[0]:.1f}% para {pct_cmv[2]:.1f}% da receita.
                
                **Possíveis causas:**
                - Aumento no custo de aquisição
                - Piora no poder de barganha
                - Mudança no mix de produtos
            """)
    
    # Análise das Despesas Operacionais
    with st.expander("2️⃣ Análise das Despesas Operacionais"):
        desp_ops = [abs(dre['dados'][ano]['(-) Despesas Operacionais']) for ano in anos]
        pct_desp = [d/r*100 for d, r in zip(desp_ops, receitas)]
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
                | Ano | Desp. Op. (R$ mil) | % Receita |
                |-----|-------------------|-----------|
                | 2021 | {desp_ops[0]/1000:,.0f} | {pct_desp[0]:.1f}% |
                | 2022 | {desp_ops[1]/1000:,.0f} | {pct_desp[1]:.1f}% |
                | 2023 | {desp_ops[2]/1000:,.0f} | {pct_desp[2]:.1f}% |
            """)
        with col2:
            st.warning(f"""
                **Diagnóstico:** Despesas cresceram de {pct_desp[0]:.1f}% para {pct_desp[2]:.1f}%.
                
                **Possíveis causas:**
                - Deseconomias de escala
                - Investimento em estrutura antecipado
                - Ineficiência administrativa
            """)
    
    # Análise das Despesas Financeiras
    with st.expander("3️⃣ Análise do Resultado Financeiro"):
        desp_fins = [abs(dre['dados'][ano]['(-) Despesas Financeiras']) for ano in anos]
        pct_fin = [d/r*100 for d, r in zip(desp_fins, receitas)]
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
                | Ano | Desp. Fin. (R$ mil) | % Receita |
                |-----|---------------------|-----------|
                | 2021 | {desp_fins[0]/1000:,.0f} | {pct_fin[0]:.1f}% |
                | 2022 | {desp_fins[1]/1000:,.0f} | {pct_fin[1]:.1f}% |
                | 2023 | {desp_fins[2]/1000:,.0f} | {pct_fin[2]:.1f}% |
            """)
        with col2:
            st.error(f"""
                **Diagnóstico:** Despesas financeiras DOBRARAM de {pct_fin[0]:.1f}% para {pct_fin[2]:.1f}%.
                
                **Possíveis causas:**
                - Crescimento financiado por dívida
                - Aumento das taxas de juros
                - Maior capital de giro necessário
            """)
    
    st.markdown("---")
    
    # Conclusão do caso
    st.markdown("#### 📝 Sua Análise do Caso")
    
    st.markdown("Com base nas informações analisadas, responda:")
    
    analise_caso = st.text_area(
        "1. Por que a empresa tem lucro crescente em valores absolutos mas margem decrescente?",
        placeholder="Desenvolva sua análise...",
        height=100,
        key="analise_caso_1"
    )
    
    recomendacao = st.text_area(
        "2. Se você fosse consultor, quais ações recomendaria para reverter essa tendência?",
        placeholder="Liste suas recomendações...",
        height=100,
        key="analise_caso_2"
    )
    
    if st.button("Ver Análise do Professor", key="btn_analise_prof"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>📋 Análise do Professor</h4>
                
                <p><strong>1. Diagnóstico:</strong></p>
                <p>A empresa está em um ciclo de <strong>"crescimento não lucrativo"</strong>:</p>
                <ul>
                    <li>Cresceu receita sacrificando margens (possível guerra de preços)</li>
                    <li>CMV aumentou proporcionalmente mais que receita (perda de eficiência ou poder de compra)</li>
                    <li>Despesas operacionais não escalam (estrutura cresceu antes da receita)</li>
                    <li>Crescimento foi financiado com dívida cara (juros consomem resultado)</li>
                </ul>
                
                <p><strong>2. Recomendações:</strong></p>
                <ul>
                    <li>Revisar política de preços - margem bruta é prioridade</li>
                    <li>Renegociar com fornecedores ou buscar alternativas</li>
                    <li>Implementar programa de eficiência operacional</li>
                    <li>Reestruturar dívida (alongar prazo, reduzir custo)</li>
                    <li>Avaliar se crescimento vale o custo - às vezes é melhor ser menor e lucrativo</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)


def renderizar_discussao_lucro_desempenho():
    """Discussão: lucro contábil vs. desempenho econômico."""
    
    st.markdown("### 💬 Discussão: Lucro Contábil vs. Desempenho Econômico")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Questão Central:</strong><br>
            <em>"Uma empresa lucrativa é necessariamente uma empresa de bom desempenho econômico?"</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Conceitos fundamentais
    st.markdown("#### 📚 Conceitos Fundamentais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px;'>
                <h4>📊 Lucro Contábil</h4>
                <ul>
                    <li>Receitas menos despesas pelo regime de competência</li>
                    <li>Segue normas contábeis (CPCs/IFRS)</li>
                    <li>Sujeito a escolhas contábeis e estimativas</li>
                    <li>Não considera custo de oportunidade</li>
                    <li>Pode ser positivo mesmo destruindo valor</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>💰 Lucro Econômico (EVA/Residual)</h4>
                <ul>
                    <li>Lucro operacional menos custo do capital</li>
                    <li>Considera remuneração dos acionistas</li>
                    <li>Positivo = criação de valor real</li>
                    <li>Negativo = destruição de valor</li>
                    <li>Mais difícil de calcular, mais informativo</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Simulador EVA
    st.markdown("#### 🧮 Simulador: Lucro Contábil vs. Econômico")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Dados da Empresa:**")
        lucro_operacional = st.number_input("Lucro Operacional após IR (NOPAT) R$", min_value=0, value=500000, step=50000, key="nopat")
        capital_investido = st.number_input("Capital Investido R$", min_value=0, value=5000000, step=500000, key="capital")
        custo_capital = st.slider("Custo de Capital (WACC) %", min_value=5.0, max_value=25.0, value=12.0, step=0.5, key="wacc")
    
    with col2:
        st.markdown("**Resultados:**")
        
        roic = (lucro_operacional / capital_investido) * 100 if capital_investido > 0 else 0
        encargo_capital = capital_investido * (custo_capital / 100)
        eva = lucro_operacional - encargo_capital
        
        st.metric("ROIC", f"{roic:.1f}%")
        st.metric("Encargo do Capital", f"R$ {encargo_capital:,.0f}")
        
        if eva > 0:
            st.metric("EVA (Lucro Econômico)", f"R$ {eva:,.0f}", delta="Criando Valor!", delta_color="normal")
        else:
            st.metric("EVA (Lucro Econômico)", f"R$ {eva:,.0f}", delta="Destruindo Valor!", delta_color="inverse")
    
    # Interpretação
    st.markdown(f"""
        <div style='background-color: {"#dcfce7" if eva > 0 else "#fee2e2"}; padding: 15px; border-radius: 10px; margin-top: 15px;'>
            <strong>Interpretação:</strong><br>
            A empresa tem lucro contábil de <strong>R$ {lucro_operacional:,.0f}</strong>, mas após remunerar o capital 
            investido à taxa de <strong>{custo_capital}%</strong>, o lucro econômico é de <strong>R$ {eva:,.0f}</strong>.<br><br>
            {"✅ A empresa CRIA valor para os acionistas - retorno acima do custo de capital." if eva > 0 else 
             "❌ A empresa DESTRÓI valor - seria melhor investir o capital em alternativas com retorno igual ao WACC."}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Casos para discussão
    st.markdown("#### 🎯 Casos para Discussão em Sala")
    
    casos_discussao = [
        {
            "titulo": "Caso A: Banco Tradicional vs. Fintech",
            "descricao": """Um banco tradicional reporta lucro de R$ 2 bilhões com ROE de 12%. 
            Uma fintech reporta prejuízo de R$ 100 milhões mas cresce 200% ao ano.""",
            "pergunta": "Qual empresa tem melhor desempenho econômico?",
            "pontos": [
                "Como avaliar empresas em estágios diferentes?",
                "O prejuízo da fintech pode ser 'investimento'?",
                "ROE de 12% é bom? Depende do custo de capital...",
                "Crescimento futuro vs. lucro presente"
            ]
        },
        {
            "titulo": "Caso B: A Fábrica de Lucros",
            "descricao": """Uma indústria reporta lucro crescente há 5 anos. Porém, a análise revela: 
            (1) não investe em manutenção, (2) reduziu P&D a zero, (3) cortou treinamento.""",
            "pergunta": "O lucro reportado reflete a realidade econômica?",
            "pontos": [
                "Lucro de curto prazo vs. sustentabilidade",
                "Ativos intangíveis não capturados na contabilidade",
                "Qualidade vs. quantidade de lucro",
                "Responsabilidade da administração e auditoria"
            ]
        },
        {
            "titulo": "Caso C: Recompra de Ações",
            "descricao": """Uma empresa usa R$ 500 milhões de caixa para recomprar ações próprias. 
            O LPA (lucro por ação) aumenta 15%, mas o lucro total fica estável.""",
            "pergunta": "A empresa melhorou seu desempenho ou manipulou indicadores?",
            "pontos": [
                "LPA pode ser manipulado via recompra",
                "Uso do caixa: recompra vs. investimento vs. dividendos",
                "Quando recompra cria valor? Quando destrói?",
                "Importância de olhar lucro total, não só por ação"
            ]
        }
    ]
    
    for caso in casos_discussao:
        with st.expander(f"📌 {caso['titulo']}"):
            st.markdown(f"""
                <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                    {caso['descricao']}
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**❓ {caso['pergunta']}**")
            
            st.markdown("**Pontos para discussão:**")
            for ponto in caso['pontos']:
                st.markdown(f"- {ponto}")
            
            st.text_area(
                "Sua posição:",
                placeholder="Desenvolva seu argumento...",
                height=80,
                key=f"disc_{caso['titulo'][:10]}"
            )
    
    st.markdown("---")
    
    # Quiz final
    st.markdown("#### ✅ Verificação de Aprendizado")
    
    quiz = st.radio(
        "Qual afirmação está CORRETA sobre a relação entre lucro contábil e desempenho econômico?",
        options=[
            "A) Lucro contábil positivo sempre indica criação de valor",
            "B) Lucro econômico considera o custo de oportunidade do capital",
            "C) Empresas com prejuízo contábil sempre destroem valor",
            "D) ROE alto sempre indica bom desempenho econômico"
        ],
        key="quiz_final_m5"
    )
    
    if st.button("Verificar", key="btn_quiz_final"):
        if "B)" in quiz:
            st.success("""
                ✅ **Correto!** O lucro econômico (EVA) deduz do lucro operacional o custo de oportunidade 
                do capital investido. Assim, ele mostra se a empresa está gerando retorno ACIMA do mínimo 
                exigido pelos investidores. Lucro contábil positivo pode coexistir com destruição de valor 
                se o retorno for inferior ao custo de capital.
            """)
        else:
            st.error("""
                ❌ **Incorreto.** A resposta correta é B. O lucro econômico (ou EVA) diferencia-se do 
                lucro contábil justamente por considerar o custo de oportunidade - quanto os investidores 
                poderiam ganhar aplicando o mesmo capital em alternativas de risco similar.
            """)
    
    # Síntese final
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Margens</strong> revelam mais que valores absolutos sobre eficiência</li>
                <li><strong>Lucro crescente com margem decrescente</strong> é sinal de alerta</li>
                <li><strong>Análise vertical</strong> (%) permite comparar empresas de tamanhos diferentes</li>
                <li><strong>Lucro contábil ≠ Desempenho econômico</strong> - considere o custo do capital</li>
                <li><strong>Qualidade do lucro</strong> importa tanto quanto quantidade</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()