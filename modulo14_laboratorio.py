"""
Módulo 14 - Tomada de Decisão: Crédito e Investimento
Laboratório de Análise de Demonstrações Financeiras
=======================================================
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def run():
    st.markdown("<h1>Módulo 14 - Tomada de Decisão: Crédito e Investimento</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Aplicar análise financeira para decisões reais de crédito e investimento</li>
                <li>Elaborar recomendações fundamentadas com base em indicadores</li>
                <li>Defender decisões com argumentos técnicos sólidos</li>
                <li>Compreender as diferentes perspectivas de credores e investidores</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "Simulação: Analista de Crédito",
        "Simulação: Analista de Investimento",
        "Discussão em Grupo"
    ])
    
    with tab1:
        renderizar_simulacao_credito()
    
    with tab2:
        renderizar_simulacao_investimento()
    
    with tab3:
        renderizar_discussao_grupo()


def get_empresa_analise():
    dados = {
        "nome": "Indústria Brasileira de Máquinas S.A. (IBM-SA)",
        "setor": "Bens de Capital / Máquinas Industriais",
        "descricao": "Fabricante de máquinas e equipamentos para indústria de alimentos e bebidas",
        "historico": {
            2021: {
                "receita": 850, "cmv": 595, "lucro_bruto": 255,
                "desp_operacionais": 127, "ebitda": 153, "depreciacao": 25,
                "ebit": 128, "desp_financeiras": 38, "receitas_fin": 8,
                "lair": 98, "ir": 33, "lucro_liquido": 65,
                "fco": 78, "fci": -45, "fcf": -20,
                "caixa": 95, "clientes": 145, "estoques": 180,
                "ativo_circulante": 450, "imobilizado": 320, "ativo_total": 850,
                "fornecedores": 85, "emprestimos_cp": 65, "passivo_circulante": 195,
                "emprestimos_lp": 180, "passivo_nao_circ": 220, "pl": 435
            },
            2022: {
                "receita": 980, "cmv": 686, "lucro_bruto": 294,
                "desp_operacionais": 147, "ebitda": 176, "depreciacao": 29,
                "ebit": 147, "desp_financeiras": 52, "receitas_fin": 10,
                "lair": 105, "ir": 36, "lucro_liquido": 69,
                "fco": 62, "fci": -85, "fcf": 35,
                "caixa": 80, "clientes": 185, "estoques": 220,
                "ativo_circulante": 520, "imobilizado": 380, "ativo_total": 1020,
                "fornecedores": 95, "emprestimos_cp": 90, "passivo_circulante": 245,
                "emprestimos_lp": 250, "passivo_nao_circ": 295, "pl": 480
            },
            2023: {
                "receita": 1150, "cmv": 805, "lucro_bruto": 345,
                "desp_operacionais": 172, "ebitda": 207, "depreciacao": 34,
                "ebit": 173, "desp_financeiras": 72, "receitas_fin": 12,
                "lair": 113, "ir": 38, "lucro_liquido": 75,
                "fco": 45, "fci": -95, "fcf": 65,
                "caixa": 65, "clientes": 240, "estoques": 275,
                "ativo_circulante": 620, "imobilizado": 450, "ativo_total": 1250,
                "fornecedores": 105, "emprestimos_cp": 130, "passivo_circulante": 310,
                "emprestimos_lp": 350, "passivo_nao_circ": 400, "pl": 540
            }
        },
        "solicitacao_credito": {
            "valor": 150, "prazo": 5,
            "finalidade": "Expansão da capacidade produtiva e modernização de equipamentos",
            "garantias_oferecidas": "Máquinas e equipamentos (valor contábil R$ 200 mi)",
            "taxa_proposta": "CDI + 3,5% a.a."
        },
        "dados_mercado": {
            "preco_acao": 28.50, "acoes_emitidas": 50, "valor_mercado": 1425,
            "dividend_yield": 2.8, "beta": 1.15, "pl_ratio": 19.0, "ev_ebitda": 9.8
        },
        "setor_medias": {
            "margem_bruta": 28, "margem_ebit": 12, "roe": 14,
            "liquidez_corrente": 1.5, "divida_ebitda": 2.0, "cobertura_juros": 4.0
        }
    }
    return dados


def calcular_indicadores_completos(dados_ano):
    d = dados_ano
    ind = {
        "margem_bruta": d['lucro_bruto'] / d['receita'] * 100,
        "margem_ebitda": d['ebitda'] / d['receita'] * 100,
        "margem_ebit": d['ebit'] / d['receita'] * 100,
        "margem_liquida": d['lucro_liquido'] / d['receita'] * 100,
        "roe": d['lucro_liquido'] / d['pl'] * 100,
        "roa": d['lucro_liquido'] / d['ativo_total'] * 100,
        "roic": (d['ebit'] * 0.66) / (d['pl'] + d['emprestimos_cp'] + d['emprestimos_lp']) * 100,
        "liquidez_corrente": d['ativo_circulante'] / d['passivo_circulante'],
        "liquidez_seca": (d['ativo_circulante'] - d['estoques']) / d['passivo_circulante'],
        "endividamento": (d['passivo_circulante'] + d['passivo_nao_circ']) / d['ativo_total'] * 100,
        "divida_liquida": d['emprestimos_cp'] + d['emprestimos_lp'] - d['caixa'],
        "divida_ebitda": (d['emprestimos_cp'] + d['emprestimos_lp']) / d['ebitda'],
        "divida_pl": (d['emprestimos_cp'] + d['emprestimos_lp']) / d['pl'],
        "cobertura_juros": d['ebit'] / d['desp_financeiras'],
        "giro_ativo": d['receita'] / d['ativo_total'],
        "pmr": d['clientes'] / d['receita'] * 360,
        "pme": d['estoques'] / d['cmv'] * 360,
        "pmp": d['fornecedores'] / d['cmv'] * 360,
        "fco_ll": d['fco'] / d['lucro_liquido'] if d['lucro_liquido'] > 0 else 0,
        "multiplicador": d['ativo_total'] / d['pl']
    }
    ind['ciclo_financeiro'] = ind['pme'] + ind['pmr'] - ind['pmp']
    return ind


def renderizar_simulacao_credito():
    st.markdown("### Simulação: Você é o Analista de Crédito")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Cenário:</strong><br>
            <em>Você é analista de crédito do Banco Nacional de Desenvolvimento. A empresa IBM-SA 
            solicitou um empréstimo para expansão. Você deve analisar os dados e emitir um parecer 
            técnico recomendando aprovação, aprovação com ressalvas, ou rejeição.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_empresa_analise()
    
    st.markdown("#### Solicitação de Crédito")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px;'>
                <h4>{dados['nome']}</h4>
                <p><strong>Setor:</strong> {dados['setor']}</p>
                <p><strong>Descrição:</strong> {dados['descricao']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        sol = dados['solicitacao_credito']
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>Detalhes da Operação</h4>
                <p><strong>Valor:</strong> R$ {sol['valor']} milhões</p>
                <p><strong>Prazo:</strong> {sol['prazo']} anos</p>
                <p><strong>Finalidade:</strong> {sol['finalidade']}</p>
                <p><strong>Garantias:</strong> {sol['garantias_oferecidas']}</p>
                <p><strong>Taxa:</strong> {sol['taxa_proposta']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### Dados Financeiros (3 anos)")
    
    dre_data = {
        "Conta": ["Receita Líquida", "Lucro Bruto", "EBITDA", "EBIT", 
                 "Despesas Financeiras", "Lucro Líquido", "FCO"],
        "2021": [850, 255, 153, 128, 38, 65, 78],
        "2022": [980, 294, 176, 147, 52, 69, 62],
        "2023": [1150, 345, 207, 173, 72, 75, 45]
    }
    st.dataframe(pd.DataFrame(dre_data), use_container_width=True, hide_index=True)
    
    bp_data = {
        "Conta": ["Ativo Total", "Ativo Circulante", "Caixa", "Passivo Circulante",
                 "Empréstimos CP", "Empréstimos LP", "Patrimônio Líquido"],
        "2021": [850, 450, 95, 195, 65, 180, 435],
        "2022": [1020, 520, 80, 245, 90, 250, 480],
        "2023": [1250, 620, 65, 310, 130, 350, 540]
    }
    st.dataframe(pd.DataFrame(bp_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("#### Indicadores-Chave para Análise de Crédito")
    
    ind_2021 = calcular_indicadores_completos(dados['historico'][2021])
    ind_2022 = calcular_indicadores_completos(dados['historico'][2022])
    ind_2023 = calcular_indicadores_completos(dados['historico'][2023])
    medias = dados['setor_medias']
    
    ind_credito = {
        "Indicador": [
            "Liquidez Corrente", "Liquidez Seca", "Cobertura de Juros",
            "Dívida/EBITDA", "Dívida/PL", "Endividamento (%)",
            "FCO/Lucro Líquido", "Margem EBITDA (%)"
        ],
        "2021": [
            f"{ind_2021['liquidez_corrente']:.2f}", f"{ind_2021['liquidez_seca']:.2f}",
            f"{ind_2021['cobertura_juros']:.2f}x", f"{ind_2021['divida_ebitda']:.2f}x",
            f"{ind_2021['divida_pl']:.2f}x", f"{ind_2021['endividamento']:.1f}%",
            f"{ind_2021['fco_ll']:.2f}", f"{ind_2021['margem_ebitda']:.1f}%"
        ],
        "2022": [
            f"{ind_2022['liquidez_corrente']:.2f}", f"{ind_2022['liquidez_seca']:.2f}",
            f"{ind_2022['cobertura_juros']:.2f}x", f"{ind_2022['divida_ebitda']:.2f}x",
            f"{ind_2022['divida_pl']:.2f}x", f"{ind_2022['endividamento']:.1f}%",
            f"{ind_2022['fco_ll']:.2f}", f"{ind_2022['margem_ebitda']:.1f}%"
        ],
        "2023": [
            f"{ind_2023['liquidez_corrente']:.2f}", f"{ind_2023['liquidez_seca']:.2f}",
            f"{ind_2023['cobertura_juros']:.2f}x", f"{ind_2023['divida_ebitda']:.2f}x",
            f"{ind_2023['divida_pl']:.2f}x", f"{ind_2023['endividamento']:.1f}%",
            f"{ind_2023['fco_ll']:.2f}", f"{ind_2023['margem_ebitda']:.1f}%"
        ],
        "Setor": ["1.50", "1.00", "4.00x", "2.00x", "0.80x", "55%", "1.00", "17%"]
    }
    
    st.dataframe(pd.DataFrame(ind_credito), use_container_width=True, hide_index=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        anos = [2021, 2022, 2023]
        fig1.add_trace(go.Scatter(
            x=anos, y=[ind_2021['cobertura_juros'], ind_2022['cobertura_juros'], ind_2023['cobertura_juros']],
            name='Cobertura de Juros', line=dict(color='#3b82f6', width=3), mode='lines+markers'
        ))
        fig1.add_hline(y=4.0, line_dash="dash", line_color="green", annotation_text="Mínimo Recomendado")
        fig1.add_hline(y=2.0, line_dash="dot", line_color="red", annotation_text="Limite Crítico")
        fig1.update_layout(title="Evolução da Cobertura de Juros", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=['2021', '2022', '2023'],
            y=[ind_2021['divida_ebitda'], ind_2022['divida_ebitda'], ind_2023['divida_ebitda']],
            marker_color=['#22c55e', '#f97316', '#ef4444']
        ))
        fig2.add_hline(y=2.0, line_dash="dash", line_color="green", annotation_text="Média do Setor")
        fig2.add_hline(y=3.0, line_dash="dot", line_color="red", annotation_text="Limite Covenant")
        fig2.update_layout(title="Dívida/EBITDA", height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    st.markdown("#### Simulação: Impacto do Novo Empréstimo")
    
    divida_atual = 130 + 350
    ebitda_atual = 207
    juros_atuais = 72
    divida_nova = divida_atual + 150
    juros_novos = juros_atuais + (150 * 0.135)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Situação Atual (2023)**")
        st.metric("Dívida Total", f"R$ {divida_atual} mi")
        st.metric("Dívida/EBITDA", f"{divida_atual/ebitda_atual:.2f}x")
        st.metric("Cobertura de Juros", f"{173/juros_atuais:.2f}x")
    
    with col2:
        st.markdown("**Situação Projetada**")
        st.metric("Dívida Total", f"R$ {divida_nova} mi", delta=f"+R$ 150 mi")
        st.metric("Dívida/EBITDA", f"{divida_nova/ebitda_atual:.2f}x", 
                 delta=f"+{(divida_nova/ebitda_atual)-(divida_atual/ebitda_atual):.2f}x", delta_color="inverse")
        st.metric("Cobertura de Juros", f"{173/juros_novos:.2f}x",
                 delta=f"{(173/juros_novos)-(173/juros_atuais):.2f}x", delta_color="inverse")
    
    st.markdown("---")
    st.markdown("#### Elabore seu Parecer de Crédito")
    
    decisao = st.radio(
        "Sua recomendação:",
        options=[
            "APROVAR - Risco aceitável, operação recomendada",
            "APROVAR COM RESSALVAS - Necessita condições adicionais",
            "REJEITAR - Risco elevado, não recomendado"
        ],
        key="decisao_credito"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        pontos_fortes = st.text_area("Pontos Fortes identificados:", height=100, key="credito_fortes")
    with col2:
        pontos_fracos = st.text_area("Pontos de Atenção/Riscos:", height=100, key="credito_fracos")
    
    if "RESSALVAS" in decisao:
        condicoes = st.text_area("Condições/Covenants exigidos:", height=80, key="credito_condicoes")
    
    parecer_final = st.text_area("Parecer conclusivo (mínimo 100 palavras):", height=120, key="credito_parecer")
    
    palavras_parecer = len(parecer_final.split()) if parecer_final else 0
    st.caption(f"Palavras: {palavras_parecer}/100 mínimo")
    
    if st.button("Ver Parecer Modelo", key="btn_parecer_credito"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>Parecer Modelo</h4>
                <p><strong>Recomendação: APROVAR COM RESSALVAS</strong></p>
                <p><strong>Pontos Fortes:</strong> Crescimento consistente de receita (CAGR 16%), 
                margens acima da média setorial, garantias reais cobrem 133% do valor.</p>
                <p><strong>Pontos de Atenção:</strong> Dívida/EBITDA em 2,3x subirá para 3,0x, 
                cobertura de juros em queda, FCO em deterioração.</p>
                <p><strong>Condições:</strong> Covenant Dívida/EBITDA máximo 3,5x, Cobertura mínima 2,0x, 
                garantia adicional de recebíveis, restrição de dividendos.</p>
            </div>
        """, unsafe_allow_html=True)


def renderizar_simulacao_investimento():
    st.markdown("### Simulação: Você é o Analista de Investimentos")
    
    st.markdown("""
        <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #22c55e; margin-bottom: 20px;'>
            <strong>Cenário:</strong><br>
            <em>Você é analista de uma gestora de fundos de ações. Precisa avaliar se a IBM-SA 
            é uma boa oportunidade de investimento para o fundo.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_empresa_analise()
    merc = dados['dados_mercado']
    
    st.markdown("#### Dados de Mercado")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Preço da Ação", f"R$ {merc['preco_acao']:.2f}")
    with col2:
        st.metric("Valor de Mercado", f"R$ {merc['valor_mercado']} mi")
    with col3:
        st.metric("P/L", f"{merc['pl_ratio']:.1f}x")
    with col4:
        st.metric("EV/EBITDA", f"{merc['ev_ebitda']:.1f}x")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Dividend Yield", f"{merc['dividend_yield']:.1f}%")
    with col2:
        st.metric("Beta", f"{merc['beta']:.2f}")
    with col3:
        st.metric("Ações Emitidas", f"{merc['acoes_emitidas']} mi")
    with col4:
        lpa = dados['historico'][2023]['lucro_liquido'] / merc['acoes_emitidas']
        st.metric("LPA", f"R$ {lpa:.2f}")
    
    st.markdown("---")
    st.markdown("#### Análise SWOT")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>Forças</h4>
                <ul>
                    <li>Líder no segmento de máquinas para alimentos</li>
                    <li>Crescimento de receita consistente</li>
                    <li>Margens acima da média do setor</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px;'>
                <h4>Fraquezas</h4>
                <ul>
                    <li>Endividamento crescente</li>
                    <li>FCO em deterioração</li>
                    <li>Capital de giro pressionado</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <h4>Oportunidades</h4>
                <ul>
                    <li>Expansão para América Latina</li>
                    <li>Indústria 4.0 e automação</li>
                    <li>Substituição de importações</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>Ameaças</h4>
                <ul>
                    <li>Competição de importados chineses</li>
                    <li>Ciclo econômico adverso</li>
                    <li>Taxa de juros elevada</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### Elabore sua Recomendação")
    
    recomendacao = st.radio(
        "Sua recomendação:",
        options=["COMPRAR", "MANTER", "VENDER"],
        key="recomendacao_invest"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        preco_alvo = st.number_input("Preço-alvo (12 meses):", min_value=0.0, max_value=100.0, 
                                     value=28.50, step=0.50, key="preco_alvo")
        upside = ((preco_alvo / merc['preco_acao']) - 1) * 100
        st.metric("Upside/Downside", f"{upside:+.1f}%")
    with col2:
        metodologia = st.selectbox("Metodologia:", options=["DCF", "Múltiplos", "Soma das Partes"], key="metodologia")
    
    tese = st.text_area("Tese de investimento (mínimo 150 palavras):", height=150, key="tese_investimento")
    palavras_tese = len(tese.split()) if tese else 0
    st.caption(f"Palavras: {palavras_tese}/150 mínimo")
    
    if st.button("Ver Relatório Modelo", key="btn_relatorio"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>Relatório Modelo</h4>
                <p><strong>Recomendação: MANTER | Preço-alvo: R$ 32,00 | Upside: +12%</strong></p>
                <p>A IBM-SA apresenta fundamentos operacionais sólidos, mas P/L de 19x e EV/EBITDA de 9,8x 
                estão acima das médias setoriais. A deterioração do FCO/LL é um sinal de alerta. 
                Aguardar queda de juros ou melhora do FCO para recomendar compra.</p>
            </div>
        """, unsafe_allow_html=True)


def renderizar_discussao_grupo():
    st.markdown("### Discussão em Grupo: Defesa da Decisão")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>ATIVIDADE EM GRUPO</strong><br>
            <em>Dividam-se em grupos. Cada grupo assumirá um papel e defenderá sua posição.</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Papéis para o Debate")
    
    papeis = [
        ("Analista de Crédito (conservador)", "APROVAR COM RESSALVAS", "#dbeafe"),
        ("Analista de Investimentos (otimista)", "COMPRAR", "#dcfce7"),
        ("Analista de Risco (cético)", "CAUTELA / VENDER", "#fee2e2"),
        ("CFO da Empresa", "EMPRESA É SÓLIDA", "#fef3c7")
    ]
    
    for papel, posicao, cor in papeis:
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <strong>{papel}</strong> - Posição: {posicao}
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### Estrutura do Debate")
    
    estrutura = [
        ("1. Apresentação Inicial", "2 min/grupo"),
        ("2. Questionamentos Cruzados", "5 min"),
        ("3. Réplicas", "1 min/grupo"),
        ("4. Considerações Finais", "1 min/grupo"),
        ("5. Votação da Turma", "2 min")
    ]
    
    for fase, tempo in estrutura:
        st.markdown(f"- **{fase}** ({tempo})")
    
    st.markdown("---")
    st.markdown("#### Template de Preparação")
    
    grupo_papel = st.selectbox("Selecione o papel do seu grupo:", 
                               options=[p[0] for p in papeis], key="grupo_papel_debate")
    argumentos = st.text_area("Desenvolva seus argumentos:", height=120, key="argumentos_debate")
    contra_argumentos = st.text_area("Antecipe contra-argumentos:", height=100, key="contra_argumentos")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>Síntese do Módulo</h4>
            <ul>
                <li><strong>Perspectivas diferentes, mesmos dados:</strong> Credor foca em risco; investidor em retorno</li>
                <li><strong>Não existe resposta única:</strong> Análise financeira envolve julgamento</li>
                <li><strong>Fundamentação é essencial:</strong> Decisões precisam de dados e lógica</li>
                <li><strong>Trade-off risco-retorno:</strong> Maior retorno potencial = maior risco</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()