"""
Módulo 4 - Leitura e Interpretação do Balanço
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Análise dirigida de um balanço real simplificado
- Identificação de pontos fortes e fragilidades financeiras
- Exercício individual: classificação de contas e interpretação econômica
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📊 Módulo 4 - Leitura e Interpretação do Balanço</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Analisar um balanço patrimonial real de forma estruturada</li>
                <li>Identificar pontos fortes e fragilidades na estrutura patrimonial</li>
                <li>Classificar corretamente as contas patrimoniais</li>
                <li>Interpretar economicamente os números do balanço</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🔍 Análise Dirigida",
        "⚖️ Forças e Fragilidades",
        "📝 Exercício Individual"
    ])
    
    with tab1:
        renderizar_analise_dirigida()
    
    with tab2:
        renderizar_forcas_fragilidades()
    
    with tab3:
        renderizar_exercicio_individual()


def get_balanco_empresa():
    """Retorna o balanço patrimonial da empresa exemplo."""
    
    balanco = {
        "empresa": "Indústria Comercial Brasileira S.A.",
        "setor": "Bens de Consumo",
        "data": "31/12/2023",
        "ativo": {
            "circulante": {
                "Caixa e Equivalentes": 45000,
                "Aplicações Financeiras": 120000,
                "Contas a Receber": 280000,
                "(-) PCLD": -15000,
                "Estoques": 195000,
                "Impostos a Recuperar": 35000,
                "Despesas Antecipadas": 12000,
            },
            "nao_circulante": {
                "Realizável LP": {
                    "Créditos com Partes Relacionadas": 45000,
                    "Depósitos Judiciais": 28000,
                },
                "Investimentos": {
                    "Participações Societárias": 85000,
                },
                "Imobilizado": {
                    "Terrenos": 150000,
                    "Edificações": 320000,
                    "Máquinas e Equipamentos": 480000,
                    "(-) Depreciação Acumulada": -285000,
                },
                "Intangível": {
                    "Marcas e Patentes": 45000,
                    "Softwares": 32000,
                    "(-) Amortização Acumulada": -18000,
                }
            }
        },
        "passivo": {
            "circulante": {
                "Fornecedores": 165000,
                "Empréstimos CP": 95000,
                "Salários e Encargos": 48000,
                "Impostos a Pagar": 62000,
                "Dividendos a Pagar": 35000,
                "Provisões CP": 22000,
            },
            "nao_circulante": {
                "Empréstimos LP": 280000,
                "Debêntures": 150000,
                "Provisões LP": 45000,
                "Impostos Diferidos": 38000,
            },
            "patrimonio_liquido": {
                "Capital Social": 450000,
                "Reservas de Capital": 65000,
                "Reservas de Lucros": 180000,
                "Ajustes de Avaliação": -12000,
                "Lucros Acumulados": 0,
            }
        }
    }
    
    return balanco


def calcular_totais(balanco):
    """Calcula os totais do balanço."""
    
    # Ativo Circulante
    ac = sum(balanco['ativo']['circulante'].values())
    
    # Ativo Não Circulante
    anc_realizavel = sum(balanco['ativo']['nao_circulante']['Realizável LP'].values())
    anc_investimentos = sum(balanco['ativo']['nao_circulante']['Investimentos'].values())
    anc_imobilizado = sum(balanco['ativo']['nao_circulante']['Imobilizado'].values())
    anc_intangivel = sum(balanco['ativo']['nao_circulante']['Intangível'].values())
    anc = anc_realizavel + anc_investimentos + anc_imobilizado + anc_intangivel
    
    ativo_total = ac + anc
    
    # Passivo Circulante
    pc = sum(balanco['passivo']['circulante'].values())
    
    # Passivo Não Circulante
    pnc = sum(balanco['passivo']['nao_circulante'].values())
    
    # Patrimônio Líquido
    pl = sum(balanco['passivo']['patrimonio_liquido'].values())
    
    passivo_total = pc + pnc + pl
    
    return {
        'ac': ac, 'anc': anc, 'ativo_total': ativo_total,
        'pc': pc, 'pnc': pnc, 'pl': pl, 'passivo_total': passivo_total,
        'anc_realizavel': anc_realizavel, 'anc_investimentos': anc_investimentos,
        'anc_imobilizado': anc_imobilizado, 'anc_intangivel': anc_intangivel
    }


def renderizar_analise_dirigida():
    """Análise dirigida de um balanço real simplificado."""
    
    st.markdown("### 🔍 Análise Dirigida de Balanço Patrimonial")
    
    balanco = get_balanco_empresa()
    totais = calcular_totais(balanco)
    
    st.markdown(f"""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Empresa:</strong> {balanco['empresa']}<br>
            <strong>Setor:</strong> {balanco['setor']}<br>
            <strong>Data-Base:</strong> {balanco['data']}<br>
            <em>Valores em R$ mil</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Visualização do Balanço
    st.markdown("#### 📋 Balanço Patrimonial Completo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### ATIVO")
        
        # Ativo Circulante
        st.markdown("**Ativo Circulante**")
        df_ac = pd.DataFrame([
            {"Conta": k, "Valor": f"R$ {v:,.0f}"} 
            for k, v in balanco['ativo']['circulante'].items()
        ])
        st.dataframe(df_ac, use_container_width=True, hide_index=True)
        st.markdown(f"**Total AC: R$ {totais['ac']:,.0f}**")
        
        st.markdown("---")
        
        # Ativo Não Circulante
        st.markdown("**Ativo Não Circulante**")
        
        st.caption("Realizável a Longo Prazo")
        for conta, valor in balanco['ativo']['nao_circulante']['Realizável LP'].items():
            st.markdown(f"- {conta}: R$ {valor:,.0f}")
        
        st.caption("Investimentos")
        for conta, valor in balanco['ativo']['nao_circulante']['Investimentos'].items():
            st.markdown(f"- {conta}: R$ {valor:,.0f}")
        
        st.caption("Imobilizado")
        for conta, valor in balanco['ativo']['nao_circulante']['Imobilizado'].items():
            st.markdown(f"- {conta}: R$ {valor:,.0f}")
        
        st.caption("Intangível")
        for conta, valor in balanco['ativo']['nao_circulante']['Intangível'].items():
            st.markdown(f"- {conta}: R$ {valor:,.0f}")
        
        st.markdown(f"**Total ANC: R$ {totais['anc']:,.0f}**")
        
        st.markdown("---")
        st.markdown(f"### ATIVO TOTAL: R$ {totais['ativo_total']:,.0f}")
    
    with col2:
        st.markdown("##### PASSIVO + PL")
        
        # Passivo Circulante
        st.markdown("**Passivo Circulante**")
        df_pc = pd.DataFrame([
            {"Conta": k, "Valor": f"R$ {v:,.0f}"} 
            for k, v in balanco['passivo']['circulante'].items()
        ])
        st.dataframe(df_pc, use_container_width=True, hide_index=True)
        st.markdown(f"**Total PC: R$ {totais['pc']:,.0f}**")
        
        st.markdown("---")
        
        # Passivo Não Circulante
        st.markdown("**Passivo Não Circulante**")
        df_pnc = pd.DataFrame([
            {"Conta": k, "Valor": f"R$ {v:,.0f}"} 
            for k, v in balanco['passivo']['nao_circulante'].items()
        ])
        st.dataframe(df_pnc, use_container_width=True, hide_index=True)
        st.markdown(f"**Total PNC: R$ {totais['pnc']:,.0f}**")
        
        st.markdown("---")
        
        # Patrimônio Líquido
        st.markdown("**Patrimônio Líquido**")
        df_pl = pd.DataFrame([
            {"Conta": k, "Valor": f"R$ {v:,.0f}"} 
            for k, v in balanco['passivo']['patrimonio_liquido'].items()
        ])
        st.dataframe(df_pl, use_container_width=True, hide_index=True)
        st.markdown(f"**Total PL: R$ {totais['pl']:,.0f}**")
        
        st.markdown("---")
        st.markdown(f"### PASSIVO + PL: R$ {totais['passivo_total']:,.0f}")
    
    # Verificação
    if totais['ativo_total'] == totais['passivo_total']:
        st.success("✅ Balanço fechado corretamente: Ativo = Passivo + PL")
    else:
        st.error("❌ Erro: Balanço não fecha!")
    
    st.markdown("---")
    
    # Análise Gráfica
    st.markdown("#### 📊 Análise Visual da Estrutura Patrimonial")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Composição do Ativo
        fig_ativo = go.Figure(data=[go.Pie(
            labels=['Ativo Circulante', 'ANC - Realizável', 'ANC - Investimentos', 'ANC - Imobilizado', 'ANC - Intangível'],
            values=[totais['ac'], totais['anc_realizavel'], totais['anc_investimentos'], 
                   totais['anc_imobilizado'], totais['anc_intangivel']],
            hole=.4,
            marker_colors=['#3b82f6', '#93c5fd', '#60a5fa', '#2563eb', '#1d4ed8']
        )])
        fig_ativo.update_layout(title="Composição do Ativo", height=350)
        st.plotly_chart(fig_ativo, use_container_width=True)
    
    with col2:
        # Composição do Passivo + PL
        fig_passivo = go.Figure(data=[go.Pie(
            labels=['Passivo Circulante', 'Passivo Não Circulante', 'Patrimônio Líquido'],
            values=[totais['pc'], totais['pnc'], totais['pl']],
            hole=.4,
            marker_colors=['#ef4444', '#f97316', '#22c55e']
        )])
        fig_passivo.update_layout(title="Composição das Fontes de Recursos", height=350)
        st.plotly_chart(fig_passivo, use_container_width=True)
    
    # Análise Guiada
    st.markdown("---")
    st.markdown("#### 🎯 Roteiro de Análise Dirigida")
    
    perguntas_analise = [
        {
            "pergunta": "1. Qual a proporção entre Ativo Circulante e Ativo Total?",
            "calculo": f"AC/AT = {totais['ac']:,.0f} / {totais['ativo_total']:,.0f} = {(totais['ac']/totais['ativo_total'])*100:.1f}%",
            "interpretacao": "Indica quanto dos recursos está em ativos de curto prazo (mais líquidos)."
        },
        {
            "pergunta": "2. Qual o Capital Circulante Líquido (CCL)?",
            "calculo": f"CCL = AC - PC = {totais['ac']:,.0f} - {totais['pc']:,.0f} = R$ {(totais['ac']-totais['pc']):,.0f}",
            "interpretacao": "CCL positivo indica folga financeira; negativo indica dependência de recursos de terceiros de curto prazo."
        },
        {
            "pergunta": "3. Qual a proporção de capital próprio vs terceiros?",
            "calculo": f"PL/PT = {totais['pl']:,.0f} / {totais['passivo_total']:,.0f} = {(totais['pl']/totais['passivo_total'])*100:.1f}%",
            "interpretacao": "Quanto maior, menor a dependência de capital de terceiros."
        },
        {
            "pergunta": "4. Qual o endividamento total?",
            "calculo": f"(PC+PNC)/AT = ({totais['pc']:,.0f}+{totais['pnc']:,.0f}) / {totais['ativo_total']:,.0f} = {((totais['pc']+totais['pnc'])/totais['ativo_total'])*100:.1f}%",
            "interpretacao": "Mostra quanto do ativo é financiado por terceiros."
        },
        {
            "pergunta": "5. Qual a imobilização do PL?",
            "calculo": f"Imob/PL = {totais['anc_imobilizado']:,.0f} / {totais['pl']:,.0f} = {(totais['anc_imobilizado']/totais['pl'])*100:.1f}%",
            "interpretacao": "Quanto do capital próprio está aplicado em ativos fixos."
        }
    ]
    
    for item in perguntas_analise:
        with st.expander(item['pergunta']):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"**Cálculo:**")
                st.code(item['calculo'])
            with col2:
                st.markdown(f"**Interpretação:**")
                st.info(item['interpretacao'])
            
            resposta_aluno = st.text_area(
                "Sua análise adicional:",
                placeholder="O que esse indicador revela sobre a empresa?",
                height=60,
                key=f"analise_{item['pergunta'][:20]}"
            )


def renderizar_forcas_fragilidades():
    """Identificação de pontos fortes e fragilidades financeiras."""
    
    st.markdown("### ⚖️ Identificação de Forças e Fragilidades")
    
    balanco = get_balanco_empresa()
    totais = calcular_totais(balanco)
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Analisar o balanço identificando aspectos positivos (forças) e pontos de atenção 
            (fragilidades) na estrutura patrimonial da empresa.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Indicadores calculados
    ccl = totais['ac'] - totais['pc']
    liquidez_corrente = totais['ac'] / totais['pc']
    liquidez_seca = (totais['ac'] - balanco['ativo']['circulante']['Estoques']) / totais['pc']
    endividamento = (totais['pc'] + totais['pnc']) / totais['ativo_total']
    composicao_endiv = totais['pc'] / (totais['pc'] + totais['pnc'])
    imobilizacao_pl = totais['anc_imobilizado'] / totais['pl']
    
    st.markdown("#### 📈 Indicadores-Chave")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Liquidez Corrente", f"{liquidez_corrente:.2f}", 
                 delta="Adequado" if liquidez_corrente > 1 else "Atenção",
                 delta_color="normal" if liquidez_corrente > 1 else "inverse")
        st.metric("Liquidez Seca", f"{liquidez_seca:.2f}")
    
    with col2:
        st.metric("CCL", f"R$ {ccl:,.0f}",
                 delta="Positivo" if ccl > 0 else "Negativo",
                 delta_color="normal" if ccl > 0 else "inverse")
        st.metric("Endividamento", f"{endividamento*100:.1f}%")
    
    with col3:
        st.metric("Composição Endiv.", f"{composicao_endiv*100:.1f}% CP")
        st.metric("Imobilização PL", f"{imobilizacao_pl*100:.1f}%")
    
    st.markdown("---")
    
    # Análise de Forças e Fragilidades
    st.markdown("#### 🎯 Sua Análise")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                <h4>💪 PONTOS FORTES</h4>
                <p>Identifique aspectos positivos da estrutura patrimonial</p>
            </div>
        """, unsafe_allow_html=True)
        
        forcas_opcoes = [
            "Liquidez corrente acima de 1 (folga financeira)",
            "Capital Circulante Líquido positivo",
            "Boa reserva de caixa e aplicações",
            "Endividamento controlado (< 60%)",
            "Maior parte da dívida é de longo prazo",
            "Patrimônio Líquido robusto",
            "Baixa imobilização do PL",
            "Diversificação dos ativos",
            "Provisão adequada para devedores duvidosos"
        ]
        
        forcas_selecionadas = []
        for i, forca in enumerate(forcas_opcoes):
            if st.checkbox(forca, key=f"forca_{i}"):
                forcas_selecionadas.append(forca)
        
        outras_forcas = st.text_area(
            "Outras forças identificadas:",
            placeholder="Descreva outros pontos positivos...",
            height=80,
            key="outras_forcas"
        )
    
    with col2:
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
                <h4>⚠️ FRAGILIDADES</h4>
                <p>Identifique pontos de atenção ou riscos</p>
            </div>
        """, unsafe_allow_html=True)
        
        fragilidades_opcoes = [
            "Elevado volume de recebíveis (risco de inadimplência)",
            "Estoques elevados (risco de obsolescência)",
            "Concentração de vencimentos no curto prazo",
            "Alta dependência de capital de terceiros",
            "Imobilização excessiva do capital próprio",
            "Baixa liquidez imediata",
            "Créditos com partes relacionadas (risco de recuperação)",
            "Intangíveis relevantes (risco de impairment)",
            "Provisões podem estar subdimensionadas"
        ]
        
        fragilidades_selecionadas = []
        for i, fragilidade in enumerate(fragilidades_opcoes):
            if st.checkbox(fragilidade, key=f"fragilidade_{i}"):
                fragilidades_selecionadas.append(fragilidade)
        
        outras_fragilidades = st.text_area(
            "Outras fragilidades identificadas:",
            placeholder="Descreva outros pontos de atenção...",
            height=80,
            key="outras_fragilidades"
        )
    
    st.markdown("---")
    
    # Verificar respostas
    if st.button("📊 Ver Análise do Professor", type="primary"):
        st.markdown("#### 📋 Análise Comentada")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                    <h4>💪 Forças Identificáveis</h4>
                    <ul>
                        <li><strong>Liquidez adequada:</strong> LC = 1,58 indica capacidade de pagar obrigações de curto prazo</li>
                        <li><strong>CCL positivo:</strong> R$ 247 mil de folga financeira</li>
                        <li><strong>Caixa + Aplicações:</strong> R$ 165 mil disponíveis imediatamente</li>
                        <li><strong>Composição do endividamento:</strong> 45% no CP - maior parte é LP</li>
                        <li><strong>PCLD constituída:</strong> Provisão de 5,4% sobre recebíveis</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px;'>
                    <h4>⚠️ Fragilidades Identificáveis</h4>
                    <ul>
                        <li><strong>Recebíveis elevados:</strong> 42% do AC - risco de inadimplência</li>
                        <li><strong>Estoques:</strong> 29% do AC - pode indicar giro lento</li>
                        <li><strong>Imobilização do PL:</strong> 97% - quase todo PL está em ativos fixos</li>
                        <li><strong>Créditos com partes relacionadas:</strong> R$ 45 mil - risco de recuperação</li>
                        <li><strong>Endividamento:</strong> 54% do ativo financiado por terceiros</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-top: 15px;'>
                <h4>🎯 Conclusão Geral</h4>
                <p>A empresa apresenta estrutura patrimonial <strong>equilibrada</strong>, com liquidez adequada 
                e endividamento controlado. Os principais pontos de atenção são a <strong>elevada imobilização 
                do patrimônio líquido</strong> e a <strong>concentração em recebíveis</strong>, que merecem 
                monitoramento constante.</p>
                <p>Recomenda-se análise complementar da DRE (para verificar rentabilidade) e DFC 
                (para validar geração de caixa operacional).</p>
            </div>
        """, unsafe_allow_html=True)


def renderizar_exercicio_individual():
    """Exercício individual de classificação e interpretação."""
    
    st.markdown("### 📝 Exercício Individual: Classificação e Interpretação")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>📌 EXERCÍCIO AVALIATIVO</strong><br>
            <em>Complete as atividades abaixo. Suas respostas serão utilizadas para avaliação.</em>
        </div>
    """, unsafe_allow_html=True)
    
    if 'respostas_m4' not in st.session_state:
        st.session_state.respostas_m4 = {}
    if 'verificado_m4' not in st.session_state:
        st.session_state.verificado_m4 = False
    
    # Exercício 1: Classificação de Contas
    st.markdown("#### Exercício 1: Classificação de Contas Patrimoniais")
    st.markdown("Classifique cada conta no grupo correto do Balanço Patrimonial:")
    
    contas_classificar = [
        ("Adiantamento a Fornecedores", "Ativo Circulante", "Direito de receber mercadorias/serviços no curto prazo"),
        ("Empréstimos a Controladas", "Ativo Não Circulante", "Realizável a longo prazo - crédito com partes relacionadas"),
        ("Provisão para Garantias", "Passivo Circulante", "Obrigação estimada por garantias concedidas"),
        ("Ágio em Investimentos", "Ativo Não Circulante", "Intangível gerado em combinação de negócios"),
        ("Debêntures (venc. 5 anos)", "Passivo Não Circulante", "Dívida com vencimento no longo prazo"),
        ("Reserva Legal", "Patrimônio Líquido", "Reserva obrigatória de lucros"),
        ("Duplicatas Descontadas", "Passivo Circulante", "Obrigação assumida ao antecipar recebíveis"),
        ("Marcas Adquiridas", "Ativo Não Circulante", "Ativo intangível com vida útil indefinida"),
    ]
    
    opcoes_classificacao = [
        "Selecione...",
        "Ativo Circulante",
        "Ativo Não Circulante",
        "Passivo Circulante",
        "Passivo Não Circulante",
        "Patrimônio Líquido"
    ]
    
    st.markdown("---")
    
    for i, (conta, resposta_correta, explicacao) in enumerate(contas_classificar):
        col1, col2 = st.columns([2, 2])
        with col1:
            st.markdown(f"**{i+1}. {conta}**")
        with col2:
            st.session_state.respostas_m4[f"class_{i}"] = st.selectbox(
                f"Classificação {i+1}",
                options=opcoes_classificacao,
                key=f"class_{i}",
                label_visibility="collapsed"
            )
    
    st.markdown("---")
    
    # Exercício 2: Interpretação Econômica
    st.markdown("#### Exercício 2: Interpretação Econômica")
    st.markdown("Para cada situação, indique a interpretação correta:")
    
    interpretacoes = [
        {
            "situacao": "A empresa aumentou significativamente sua conta de Estoques em relação ao ano anterior, sem aumento proporcional nas vendas.",
            "opcoes": [
                "A) Indica melhoria na gestão de suprimentos",
                "B) Pode indicar problemas de vendas ou obsolescência",
                "C) Demonstra fortalecimento da liquidez",
                "D) Reflete aumento da demanda futura"
            ],
            "correta": "B",
            "explicacao": "Aumento de estoques sem crescimento de vendas pode indicar dificuldade de comercialização, produtos obsoletos ou erro de planejamento de compras."
        },
        {
            "situacao": "O Patrimônio Líquido da empresa é negativo (Passivo a Descoberto).",
            "opcoes": [
                "A) A empresa é altamente lucrativa",
                "B) Os sócios fizeram aportes recentes",
                "C) Os prejuízos acumulados superaram o capital investido",
                "D) É uma situação normal em empresas de crescimento"
            ],
            "correta": "C",
            "explicacao": "PL negativo indica que prejuízos acumulados consumiram todo o capital próprio. A empresa está tecnicamente insolvente e depende totalmente de terceiros."
        },
        {
            "situacao": "A conta 'Clientes' representa 70% do Ativo Total da empresa.",
            "opcoes": [
                "A) Indica excelente volume de vendas",
                "B) Demonstra política de crédito conservadora",
                "C) Pode indicar risco de concentração e inadimplência",
                "D) Reflete alta eficiência operacional"
            ],
            "correta": "C",
            "explicacao": "Concentração excessiva em recebíveis indica risco de inadimplência, possível dificuldade de cobrança ou prazos muito longos. Empresa fica vulnerável a calotes."
        },
        {
            "situacao": "A empresa possui R$ 500 mil em Caixa, mas também tem R$ 480 mil em Empréstimos de Curto Prazo.",
            "opcoes": [
                "A) Excelente gestão financeira - tem recursos para pagar dívidas",
                "B) Possível ineficiência - está pagando juros com dinheiro parado",
                "C) Indica que a empresa não consegue aplicar recursos",
                "D) Demonstra solidez financeira inquestionável"
            ],
            "correta": "B",
            "explicacao": "Manter caixa elevado simultaneamente com dívidas onerosas é ineficiente: a empresa paga juros sobre empréstimos enquanto o caixa rende menos. Pode indicar restrições contratuais ou má gestão."
        },
        {
            "situacao": "O Ativo Intangível representa 60% do Ativo Total, sendo majoritariamente ágio de aquisições.",
            "opcoes": [
                "A) Indica empresa inovadora e tecnológica",
                "B) Representa risco de impairment se as expectativas não se confirmarem",
                "C) Demonstra crescimento orgânico saudável",
                "D) É característico de empresas industriais"
            ],
            "correta": "B",
            "explicacao": "Ágio elevado depende de premissas de rentabilidade futura. Se os negócios adquiridos não performarem conforme esperado, haverá impairment (baixa) do ágio, afetando fortemente o resultado e o PL."
        }
    ]
    
    for i, item in enumerate(interpretacoes):
        st.markdown(f"**Situação {i+1}:** {item['situacao']}")
        st.session_state.respostas_m4[f"interp_{i}"] = st.radio(
            f"Interpretação {i+1}",
            options=item['opcoes'],
            key=f"interp_{i}",
            label_visibility="collapsed"
        )
        st.markdown("---")
    
    # Exercício 3: Análise Dissertativa
    st.markdown("#### Exercício 3: Análise Dissertativa")
    
    st.markdown("""
        **Com base no balanço analisado neste módulo, responda:**
        
        Você é analista de crédito de um banco e a Indústria Comercial Brasileira S.A. 
        solicita um empréstimo de R$ 300.000 com prazo de 2 anos. Com base na análise 
        do balanço patrimonial, você recomendaria a aprovação do crédito? Justifique 
        sua decisão considerando pelo menos 3 indicadores ou aspectos do balanço.
    """)
    
    st.session_state.respostas_m4['dissertativa'] = st.text_area(
        "Sua análise e recomendação:",
        placeholder="Desenvolva sua argumentação com base nos indicadores analisados...",
        height=200,
        key="dissertativa_m4"
    )
    
    if st.session_state.respostas_m4.get('dissertativa'):
        palavras = len(st.session_state.respostas_m4['dissertativa'].split())
        st.caption(f"Palavras: {palavras} (recomendado: 100-200)")
    
    st.markdown("---")
    
    # Verificação
    if st.button("📊 Verificar Respostas Objetivas", type="primary"):
        st.session_state.verificado_m4 = True
    
    if st.session_state.verificado_m4:
        st.markdown("### 📋 Gabarito")
        
        # Exercício 1
        st.markdown("#### Exercício 1 - Classificação:")
        acertos1 = 0
        for i, (conta, resposta_correta, explicacao) in enumerate(contas_classificar):
            resp = st.session_state.respostas_m4.get(f"class_{i}", "")
            if resp == resposta_correta:
                st.success(f"✅ {conta}: {resposta_correta}")
                acertos1 += 1
            else:
                st.error(f"❌ {conta}: Sua: {resp} | Correta: {resposta_correta}")
                st.caption(f"   💡 {explicacao}")
        
        st.markdown(f"**Acertos: {acertos1}/{len(contas_classificar)}**")
        
        # Exercício 2
        st.markdown("#### Exercício 2 - Interpretação:")
        acertos2 = 0
        for i, item in enumerate(interpretacoes):
            resp = st.session_state.respostas_m4.get(f"interp_{i}", "")
            correta = [o for o in item['opcoes'] if o.startswith(item['correta'])][0]
            if resp and resp[0] == item['correta']:
                st.success(f"✅ Situação {i+1}: {correta}")
                acertos2 += 1
            else:
                st.error(f"❌ Situação {i+1}: Sua: {resp[:1] if resp else 'N/R'} | Correta: {item['correta']}")
                st.caption(f"   💡 {item['explicacao']}")
        
        st.markdown(f"**Acertos: {acertos2}/{len(interpretacoes)}**")
        
        # Resumo
        total = len(contas_classificar) + len(interpretacoes)
        acertos = acertos1 + acertos2
        pct = (acertos / total) * 100
        
        cor = "#dcfce7" if pct >= 70 else "#fef3c7" if pct >= 50 else "#fee2e2"
        msg = "🌟 Excelente!" if pct >= 80 else "👍 Bom trabalho!" if pct >= 60 else "📚 Revise o conteúdo."
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;'>
                <h3>Resultado: {acertos}/{total} ({pct:.0f}%)</h3>
                <p>{msg}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Gabarito dissertativa
        st.markdown("#### Exercício 3 - Elementos esperados na resposta:")
        st.info("""
            **Pontos que devem ser considerados na análise de crédito:**
            
            1. **Liquidez:** LC = 1,58 - adequada para honrar compromissos
            2. **Endividamento atual:** 54% - ainda há espaço para nova dívida
            3. **CCL positivo:** R$ 247 mil - folga financeira
            4. **Composição do endividamento:** 55% LP - perfil de dívida alongado
            5. **Garantias potenciais:** Imobilizado de R$ 665 mil (líquido)
            6. **Risco:** Concentração em recebíveis, imobilização elevada do PL
            
            **Recomendação esperada:** Aprovação com ressalvas (garantias, covenants) 
            ou análise complementar de DRE e DFC para avaliar capacidade de pagamento.
        """)


if __name__ == "__main__":
    run()