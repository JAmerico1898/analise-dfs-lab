"""
Módulo 15 - Projeto Final: Análise Integrada
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Estudo de caso completo (individual ou em grupo)
- Relatório final de análise financeira
- Discussão coletiva e feedback estruturado
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


def run():
    st.markdown("<h1>Módulo 15 - Projeto Final: Análise Integrada</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Realizar uma análise financeira completa e integrada</li>
                <li>Elaborar um relatório profissional de análise</li>
                <li>Sintetizar todos os conceitos aprendidos no curso</li>
                <li>Apresentar e defender conclusões com base em evidências</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "Estudo de Caso Completo",
        "Relatório Final",
        "Discussão e Feedback"
    ])
    
    with tab1:
        renderizar_estudo_caso_completo()
    
    with tab2:
        renderizar_relatorio_final()
    
    with tab3:
        renderizar_discussao_feedback()


def get_dados_caso_final():
    """Retorna dados completos para o caso final."""
    dados = {
        "nome": "Construtora Horizonte S.A.",
        "setor": "Construção Civil / Incorporação Imobiliária",
        "descricao": "Incorporadora e construtora com atuação em empreendimentos residenciais de médio e alto padrão nas regiões Sul e Sudeste do Brasil.",
        "contexto": """A Construtora Horizonte passou por um ciclo de forte expansão entre 2019 e 2021, 
        lançando diversos empreendimentos. Com a alta dos juros em 2022-2023, o mercado imobiliário 
        desacelerou e a empresa enfrenta desafios de liquidez e rentabilidade.""",
        "historico": {
            2020: {
                "receita": 680, "cmv": 510, "lucro_bruto": 170,
                "desp_comerciais": 41, "desp_administrativas": 34, "ebitda": 102,
                "depreciacao": 7, "ebit": 95, "desp_financeiras": 28, "receitas_fin": 12,
                "lair": 79, "ir": 27, "lucro_liquido": 52,
                "fco": 65, "fci": -45, "fcf": -15,
                "caixa": 120, "clientes": 85, "estoques": 380, "imoveis_venda": 320,
                "ativo_circulante": 620, "imobilizado": 95, "ativo_total": 980,
                "fornecedores": 78, "emprestimos_cp": 55, "adiantamentos": 85,
                "passivo_circulante": 265, "emprestimos_lp": 180, "passivo_nao_circ": 245, "pl": 470
            },
            2021: {
                "receita": 920, "cmv": 680, "lucro_bruto": 240,
                "desp_comerciais": 55, "desp_administrativas": 46, "ebitda": 148,
                "depreciacao": 9, "ebit": 139, "desp_financeiras": 42, "receitas_fin": 18,
                "lair": 115, "ir": 39, "lucro_liquido": 76,
                "fco": 35, "fci": -120, "fcf": 95,
                "caixa": 95, "clientes": 145, "estoques": 520, "imoveis_venda": 450,
                "ativo_circulante": 810, "imobilizado": 180, "ativo_total": 1350,
                "fornecedores": 95, "emprestimos_cp": 85, "adiantamentos": 120,
                "passivo_circulante": 365, "emprestimos_lp": 320, "passivo_nao_circ": 420, "pl": 565
            },
            2022: {
                "receita": 850, "cmv": 655, "lucro_bruto": 195,
                "desp_comerciais": 59, "desp_administrativas": 51, "ebitda": 96,
                "depreciacao": 11, "ebit": 85, "desp_financeiras": 68, "receitas_fin": 15,
                "lair": 32, "ir": 11, "lucro_liquido": 21,
                "fco": -45, "fci": -35, "fcf": 85,
                "caixa": 55, "clientes": 180, "estoques": 620, "imoveis_venda": 540,
                "ativo_circulante": 920, "imobilizado": 210, "ativo_total": 1520,
                "fornecedores": 88, "emprestimos_cp": 145, "adiantamentos": 95,
                "passivo_circulante": 420, "emprestimos_lp": 450, "passivo_nao_circ": 540, "pl": 560
            },
            2023: {
                "receita": 720, "cmv": 576, "lucro_bruto": 144,
                "desp_comerciais": 50, "desp_administrativas": 54, "ebitda": 51,
                "depreciacao": 11, "ebit": 40, "desp_financeiras": 95, "receitas_fin": 8,
                "lair": -47, "ir": 0, "lucro_liquido": -47,
                "fco": -85, "fci": -15, "fcf": 45,
                "caixa": 35, "clientes": 165, "estoques": 680, "imoveis_venda": 590,
                "ativo_circulante": 950, "imobilizado": 205, "ativo_total": 1580,
                "fornecedores": 72, "emprestimos_cp": 210, "adiantamentos": 75,
                "passivo_circulante": 480, "emprestimos_lp": 520, "passivo_nao_circ": 610, "pl": 490
            }
        },
        "info_adicionais": {
            "funcionarios": {"2020": 850, "2021": 1200, "2022": 1100, "2023": 780},
            "unidades_lancadas": {"2020": 1200, "2021": 2400, "2022": 800, "2023": 200},
            "unidades_vendidas": {"2020": 950, "2021": 1800, "2022": 1100, "2023": 650},
            "vgv_lancado": {"2020": 450, "2021": 980, "2022": 320, "2023": 85},
            "banco_terrenos": 180,
            "obras_andamento": 12,
            "preco_medio_m2": {"2020": 5800, "2021": 6200, "2022": 6500, "2023": 6300},
            "taxa_distratos": {"2020": 8, "2021": 12, "2022": 18, "2023": 22}
        },
        "setor_medias": {
            "margem_bruta": 28, "margem_ebit": 12, "margem_liquida": 7,
            "roe": 12, "roa": 5, "liquidez_corrente": 1.8,
            "divida_ebitda": 2.5, "divida_pl": 0.8
        },
        "notas_importantes": [
            "Método de reconhecimento de receita: POC (Percentage of Completion)",
            "Estoques incluem terrenos, obras em andamento e unidades concluídas",
            "Alta concentração de vencimentos de dívida em 2024-2025",
            "Alguns empreendimentos com vendas abaixo do esperado",
            "Processo de renegociação de dívidas em andamento"
        ]
    }
    return dados


def calcular_indicadores(dados_ano, dados_ant=None):
    d = dados_ano
    ind = {
        "margem_bruta": d['lucro_bruto'] / d['receita'] * 100 if d['receita'] > 0 else 0,
        "margem_ebitda": d['ebitda'] / d['receita'] * 100 if d['receita'] > 0 else 0,
        "margem_ebit": d['ebit'] / d['receita'] * 100 if d['receita'] > 0 else 0,
        "margem_liquida": d['lucro_liquido'] / d['receita'] * 100 if d['receita'] > 0 else 0,
        "roe": d['lucro_liquido'] / d['pl'] * 100 if d['pl'] > 0 else 0,
        "roa": d['lucro_liquido'] / d['ativo_total'] * 100 if d['ativo_total'] > 0 else 0,
        "liquidez_corrente": d['ativo_circulante'] / d['passivo_circulante'] if d['passivo_circulante'] > 0 else 0,
        "liquidez_seca": (d['ativo_circulante'] - d['estoques']) / d['passivo_circulante'] if d['passivo_circulante'] > 0 else 0,
        "endividamento": (d['passivo_circulante'] + d['passivo_nao_circ']) / d['ativo_total'] * 100,
        "divida_bruta": d['emprestimos_cp'] + d['emprestimos_lp'],
        "divida_liquida": d['emprestimos_cp'] + d['emprestimos_lp'] - d['caixa'],
        "divida_ebitda": (d['emprestimos_cp'] + d['emprestimos_lp']) / d['ebitda'] if d['ebitda'] > 0 else 999,
        "divida_pl": (d['emprestimos_cp'] + d['emprestimos_lp']) / d['pl'] if d['pl'] > 0 else 999,
        "cobertura_juros": d['ebit'] / d['desp_financeiras'] if d['desp_financeiras'] > 0 else 0,
        "giro_ativo": d['receita'] / d['ativo_total'] if d['ativo_total'] > 0 else 0,
        "fco_ll": d['fco'] / d['lucro_liquido'] if d['lucro_liquido'] != 0 else 0,
        "multiplicador": d['ativo_total'] / d['pl'] if d['pl'] > 0 else 0
    }
    return ind


def renderizar_estudo_caso_completo():
    st.markdown("### Estudo de Caso Completo: Construtora Horizonte S.A.")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>PROJETO FINAL - Análise Integrada</strong><br>
            <em>Você foi contratado como consultor para analisar a situação financeira da 
            Construtora Horizonte S.A. e emitir um parecer sobre a viabilidade da empresa. 
            Este caso integra TODOS os conceitos aprendidos no curso.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_caso_final()
    
    # Contexto da empresa
    st.markdown("#### Contexto da Empresa")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #f8fafc; padding: 15px; border-radius: 10px;'>
                <h4>{dados['nome']}</h4>
                <p><strong>Setor:</strong> {dados['setor']}</p>
                <p><strong>Descrição:</strong> {dados['descricao']}</p>
                <p><strong>Contexto atual:</strong> {dados['contexto']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px;'>
                <h4>Notas Importantes</h4>
            </div>
        """, unsafe_allow_html=True)
        for nota in dados['notas_importantes']:
            st.markdown(f"- {nota}")
    
    st.markdown("---")
    
    # DRE Completa
    st.markdown("#### Demonstração do Resultado (R$ milhões)")
    
    dre_data = {
        "Conta": ["Receita Líquida", "(-) CMV", "Lucro Bruto", "(-) Desp. Comerciais",
                 "(-) Desp. Administrativas", "EBITDA", "(-) Depreciação", "EBIT",
                 "(-) Desp. Financeiras", "(+) Rec. Financeiras", "LAIR", "(-) IR/CS", "Lucro Líquido"],
        "2020": [680, -510, 170, -41, -34, 102, -7, 95, -28, 12, 79, -27, 52],
        "2021": [920, -680, 240, -55, -46, 148, -9, 139, -42, 18, 115, -39, 76],
        "2022": [850, -655, 195, -59, -51, 96, -11, 85, -68, 15, 32, -11, 21],
        "2023": [720, -576, 144, -50, -54, 51, -11, 40, -95, 8, -47, 0, -47]
    }
    st.dataframe(pd.DataFrame(dre_data), use_container_width=True, hide_index=True)
    
    # Balanço Patrimonial
    st.markdown("#### Balanço Patrimonial Resumido (R$ milhões)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**ATIVO**")
        ativo_data = {
            "Conta": ["Caixa e Equivalentes", "Clientes", "Estoques/Imóveis", "Outros AC",
                     "Ativo Circulante", "Imobilizado", "Outros ANC", "Ativo Total"],
            "2020": [120, 85, 380, 35, 620, 95, 265, 980],
            "2021": [95, 145, 520, 50, 810, 180, 360, 1350],
            "2022": [55, 180, 620, 65, 920, 210, 390, 1520],
            "2023": [35, 165, 680, 70, 950, 205, 425, 1580]
        }
        st.dataframe(pd.DataFrame(ativo_data), use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("**PASSIVO + PL**")
        passivo_data = {
            "Conta": ["Fornecedores", "Empréstimos CP", "Adiantamentos", "Outros PC",
                     "Passivo Circulante", "Empréstimos LP", "Outros PNC", "Patrimônio Líquido"],
            "2020": [78, 55, 85, 47, 265, 180, 65, 470],
            "2021": [95, 85, 120, 65, 365, 320, 100, 565],
            "2022": [88, 145, 95, 92, 420, 450, 90, 560],
            "2023": [72, 210, 75, 123, 480, 520, 90, 490]
        }
        st.dataframe(pd.DataFrame(passivo_data), use_container_width=True, hide_index=True)
    
    # Fluxo de Caixa
    st.markdown("#### Fluxo de Caixa (R$ milhões)")
    
    fc_data = {
        "Componente": ["FCO - Operacional", "FCI - Investimentos", "FCF - Financiamentos", "Variação Caixa"],
        "2020": [65, -45, -15, 5],
        "2021": [35, -120, 95, 10],
        "2022": [-45, -35, 85, 5],
        "2023": [-85, -15, 45, -55]
    }
    st.dataframe(pd.DataFrame(fc_data), use_container_width=True, hide_index=True)
    
    # Dados Operacionais
    st.markdown("#### Dados Operacionais")
    
    info = dados['info_adicionais']
    op_data = {
        "Indicador": ["Funcionários", "Unidades Lançadas", "Unidades Vendidas", 
                     "VGV Lançado (R$ mi)", "Preço Médio/m²", "Taxa de Distratos (%)"],
        "2020": [info['funcionarios']['2020'], info['unidades_lancadas']['2020'], 
                info['unidades_vendidas']['2020'], info['vgv_lancado']['2020'],
                info['preco_medio_m2']['2020'], info['taxa_distratos']['2020']],
        "2021": [info['funcionarios']['2021'], info['unidades_lancadas']['2021'],
                info['unidades_vendidas']['2021'], info['vgv_lancado']['2021'],
                info['preco_medio_m2']['2021'], info['taxa_distratos']['2021']],
        "2022": [info['funcionarios']['2022'], info['unidades_lancadas']['2022'],
                info['unidades_vendidas']['2022'], info['vgv_lancado']['2022'],
                info['preco_medio_m2']['2022'], info['taxa_distratos']['2022']],
        "2023": [info['funcionarios']['2023'], info['unidades_lancadas']['2023'],
                info['unidades_vendidas']['2023'], info['vgv_lancado']['2023'],
                info['preco_medio_m2']['2023'], info['taxa_distratos']['2023']]
    }
    st.dataframe(pd.DataFrame(op_data), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Indicadores calculados
    st.markdown("#### Indicadores Financeiros Calculados")
    
    ind_2020 = calcular_indicadores(dados['historico'][2020])
    ind_2021 = calcular_indicadores(dados['historico'][2021])
    ind_2022 = calcular_indicadores(dados['historico'][2022])
    ind_2023 = calcular_indicadores(dados['historico'][2023])
    medias = dados['setor_medias']
    
    indicadores_tabela = {
        "Indicador": ["Margem Bruta (%)", "Margem EBITDA (%)", "Margem Líquida (%)",
                     "ROE (%)", "ROA (%)", "Liquidez Corrente", "Dívida/EBITDA",
                     "Dívida/PL", "Cobertura de Juros", "FCO/LL"],
        "2020": [f"{ind_2020['margem_bruta']:.1f}", f"{ind_2020['margem_ebitda']:.1f}",
                f"{ind_2020['margem_liquida']:.1f}", f"{ind_2020['roe']:.1f}",
                f"{ind_2020['roa']:.1f}", f"{ind_2020['liquidez_corrente']:.2f}",
                f"{ind_2020['divida_ebitda']:.1f}", f"{ind_2020['divida_pl']:.2f}",
                f"{ind_2020['cobertura_juros']:.1f}", f"{ind_2020['fco_ll']:.2f}"],
        "2021": [f"{ind_2021['margem_bruta']:.1f}", f"{ind_2021['margem_ebitda']:.1f}",
                f"{ind_2021['margem_liquida']:.1f}", f"{ind_2021['roe']:.1f}",
                f"{ind_2021['roa']:.1f}", f"{ind_2021['liquidez_corrente']:.2f}",
                f"{ind_2021['divida_ebitda']:.1f}", f"{ind_2021['divida_pl']:.2f}",
                f"{ind_2021['cobertura_juros']:.1f}", f"{ind_2021['fco_ll']:.2f}"],
        "2022": [f"{ind_2022['margem_bruta']:.1f}", f"{ind_2022['margem_ebitda']:.1f}",
                f"{ind_2022['margem_liquida']:.1f}", f"{ind_2022['roe']:.1f}",
                f"{ind_2022['roa']:.1f}", f"{ind_2022['liquidez_corrente']:.2f}",
                f"{ind_2022['divida_ebitda']:.1f}", f"{ind_2022['divida_pl']:.2f}",
                f"{ind_2022['cobertura_juros']:.1f}", f"{ind_2022['fco_ll']:.2f}"],
        "2023": [f"{ind_2023['margem_bruta']:.1f}", f"{ind_2023['margem_ebitda']:.1f}",
                f"{ind_2023['margem_liquida']:.1f}", f"{ind_2023['roe']:.1f}",
                f"{ind_2023['roa']:.1f}", f"{ind_2023['liquidez_corrente']:.2f}",
                f"{ind_2023['divida_ebitda']:.1f}x" if ind_2023['divida_ebitda'] < 50 else ">50x", 
                f"{ind_2023['divida_pl']:.2f}",
                f"{ind_2023['cobertura_juros']:.1f}", "N/A"],
        "Setor": [f"{medias['margem_bruta']}", f"15", f"{medias['margem_liquida']}",
                 f"{medias['roe']}", f"{medias['roa']}", f"{medias['liquidez_corrente']}",
                 f"{medias['divida_ebitda']}", f"{medias['divida_pl']}", "3.0", "1.0"]
    }
    st.dataframe(pd.DataFrame(indicadores_tabela), use_container_width=True, hide_index=True)
    
    # Gráficos
    st.markdown("---")
    st.markdown("#### Visualização da Evolução")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = go.Figure()
        anos = [2020, 2021, 2022, 2023]
        fig1.add_trace(go.Scatter(x=anos, y=[680, 920, 850, 720], name='Receita', 
                                  line=dict(color='#3b82f6', width=3), mode='lines+markers'))
        fig1.add_trace(go.Scatter(x=anos, y=[52, 76, 21, -47], name='Lucro Líquido',
                                  line=dict(color='#22c55e', width=3), mode='lines+markers'))
        fig1.add_hline(y=0, line_dash="dash", line_color="red")
        fig1.update_layout(title="Receita vs Lucro Líquido (R$ mi)", height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=['2020', '2021', '2022', '2023'],
                             y=[65, 35, -45, -85],
                             marker_color=['#22c55e', '#84cc16', '#ef4444', '#dc2626']))
        fig2.add_hline(y=0, line_color="black")
        fig2.update_layout(title="Fluxo de Caixa Operacional (R$ mi)", height=300)
        st.plotly_chart(fig2, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=anos, y=[ind_2020['divida_ebitda'], ind_2021['divida_ebitda'],
                                            ind_2022['divida_ebitda'], min(ind_2023['divida_ebitda'], 15)],
                                 name='Dívida/EBITDA', line=dict(color='#ef4444', width=3), mode='lines+markers'))
        fig3.add_hline(y=2.5, line_dash="dash", line_color="green", annotation_text="Média Setor")
        fig3.add_hline(y=4.0, line_dash="dot", line_color="red", annotation_text="Limite Crítico")
        fig3.update_layout(title="Dívida/EBITDA", height=300)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col2:
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=anos, y=[ind_2020['cobertura_juros'], ind_2021['cobertura_juros'],
                                            ind_2022['cobertura_juros'], ind_2023['cobertura_juros']],
                                 name='Cobertura', line=dict(color='#f97316', width=3), mode='lines+markers'))
        fig4.add_hline(y=2.0, line_dash="dash", line_color="green", annotation_text="Mínimo Seguro")
        fig4.add_hline(y=1.0, line_dash="dot", line_color="red", annotation_text="Limite Crítico")
        fig4.update_layout(title="Cobertura de Juros (EBIT/Juros)", height=300)
        st.plotly_chart(fig4, use_container_width=True)


def renderizar_relatorio_final():
    st.markdown("### Relatório Final de Análise Financeira")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Instruções:</strong><br>
            <em>Elabore um relatório completo de análise financeira seguindo a estrutura abaixo. 
            Este relatório deve integrar todas as técnicas aprendidas no curso.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Estrutura do Relatório
    st.markdown("#### Estrutura do Relatório")
    
    secoes = [
        ("1. Sumário Executivo", "Síntese das principais conclusões e recomendações (máx. 200 palavras)"),
        ("2. Análise de Rentabilidade", "Margens, ROE, ROA, análise DuPont"),
        ("3. Análise de Liquidez e Capital de Giro", "Índices de liquidez, ciclo financeiro"),
        ("4. Análise de Estrutura de Capital", "Endividamento, cobertura de juros, alavancagem"),
        ("5. Análise do Fluxo de Caixa", "Qualidade do lucro, geração de caixa"),
        ("6. Red Flags Identificados", "Sinais de alerta e riscos"),
        ("7. Conclusão e Recomendação", "Parecer final fundamentado")
    ]
    
    for secao, desc in secoes:
        st.markdown(f"**{secao}:** {desc}")
    
    st.markdown("---")
    
    # Formulário do relatório
    st.markdown("#### Elabore seu Relatório")
    
    # Seção 1
    st.markdown("##### 1. Sumário Executivo")
    sumario = st.text_area(
        "Apresente as principais conclusões e sua recomendação final:",
        height=150,
        key="rel_sumario",
        placeholder="A Construtora Horizonte apresenta... Recomendamos..."
    )
    
    # Seção 2
    st.markdown("##### 2. Análise de Rentabilidade")
    col1, col2 = st.columns(2)
    with col1:
        rent_margens = st.text_area("Análise das margens:", height=100, key="rel_margens",
                                    placeholder="Margem bruta caiu de X para Y...")
    with col2:
        rent_roe = st.text_area("Análise ROE/ROA e DuPont:", height=100, key="rel_roe",
                               placeholder="O ROE deteriorou de X para Y porque...")
    
    # Seção 3
    st.markdown("##### 3. Análise de Liquidez e Capital de Giro")
    liquidez = st.text_area(
        "Análise dos índices de liquidez e capital de giro:",
        height=100,
        key="rel_liquidez",
        placeholder="A liquidez corrente aparentemente alta de X mascara..."
    )
    
    # Seção 4
    st.markdown("##### 4. Análise de Estrutura de Capital")
    estrutura = st.text_area(
        "Análise do endividamento e alavancagem:",
        height=100,
        key="rel_estrutura",
        placeholder="A dívida/EBITDA subiu de X para Y, indicando..."
    )
    
    # Seção 5
    st.markdown("##### 5. Análise do Fluxo de Caixa")
    fluxo = st.text_area(
        "Análise da qualidade do lucro e geração de caixa:",
        height=100,
        key="rel_fluxo",
        placeholder="O FCO negativo de R$ X milhões em 2023 revela..."
    )
    
    # Seção 6
    st.markdown("##### 6. Red Flags Identificados")
    red_flags = st.text_area(
        "Liste os principais sinais de alerta identificados:",
        height=120,
        key="rel_redflags",
        placeholder="1. FCO negativo por 2 anos consecutivos\n2. ..."
    )
    
    # Seção 7
    st.markdown("##### 7. Conclusão e Recomendação")
    
    parecer = st.radio(
        "Seu parecer sobre a situação da empresa:",
        options=[
            "CRÍTICA - Risco elevado de insolvência",
            "PREOCUPANTE - Necessita reestruturação urgente",
            "RECUPERÁVEL - Com ajustes, pode se recuperar",
            "ESTÁVEL - Dificuldades temporárias"
        ],
        key="rel_parecer"
    )
    
    recomendacoes = st.text_area(
        "Recomendações específicas para a empresa:",
        height=120,
        key="rel_recomendacoes",
        placeholder="1. Renegociar dívidas com alongamento de prazo\n2. ..."
    )
    
    # Contagem total
    todas_respostas = [sumario, rent_margens, rent_roe, liquidez, estrutura, fluxo, red_flags, recomendacoes]
    total_palavras = sum(len(r.split()) for r in todas_respostas if r)
    
    st.markdown("---")
    st.metric("Total de palavras no relatório", total_palavras)
    
    if total_palavras < 500:
        st.warning("Relatório ainda curto. Recomendamos pelo menos 800 palavras para uma análise completa.")
    elif total_palavras >= 800:
        st.success("Bom volume! Verifique se cobriu todos os pontos importantes.")
    
    # Gabarito
    if st.button("Ver Relatório Modelo", key="btn_relatorio_modelo"):
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
                <h4>Relatório Modelo - Construtora Horizonte S.A.</h4>
                
                <p><strong>1. SUMÁRIO EXECUTIVO</strong></p>
                <p>A Construtora Horizonte enfrenta uma crise financeira severa. Após expansão agressiva em 
                2021, a empresa não conseguiu ajustar sua operação à desaceleração do mercado imobiliário. 
                Em 2023, apresentou prejuízo de R$ 47 milhões, FCO negativo de R$ 85 milhões, e indicadores 
                de solvência críticos. Sem reestruturação imediata, há risco elevado de insolvência em 12-18 meses. 
                Recomendamos classificação de risco CRÍTICO e reestruturação urgente.</p>
                
                <p><strong>2. ANÁLISE DE RENTABILIDADE</strong></p>
                <p>Deterioração em todas as margens: Margem bruta caiu de 25% (2020) para 20% (2023), indicando 
                pressão nos custos de construção e necessidade de descontos para vender unidades. Margem líquida 
                passou de 7,6% positiva para -6,5% negativa. ROE colapsou de 11% para -9,6%. Análise DuPont revela 
                que a queda vem tanto da margem operacional quanto do aumento da alavancagem sem retorno.</p>
                
                <p><strong>3. ANÁLISE DE LIQUIDEZ</strong></p>
                <p>Liquidez corrente de 1,98 em 2023 é enganosa: 72% do AC são estoques (imóveis) de baixa 
                liquidez em mercado fraco. Liquidez seca de apenas 0,56 revela a real dificuldade de caixa. 
                Caixa caiu de R$ 120 mi para R$ 35 mi enquanto dívida CP subiu para R$ 210 mi - descasamento grave.</p>
                
                <p><strong>4. ANÁLISE DE ESTRUTURA DE CAPITAL</strong></p>
                <p>Dívida bruta de R$ 730 mi (210 CP + 520 LP) contra EBITDA de apenas R$ 51 mi resulta em 
                Dívida/EBITDA de 14,3x - completamente insustentável. Cobertura de juros de 0,42x significa que 
                EBIT não cobre nem metade dos juros. Empresa está tecnicamente insolvente operacionalmente.</p>
                
                <p><strong>5. ANÁLISE DO FLUXO DE CAIXA</strong></p>
                <p>FCO negativo em 2022 (R$ -45 mi) e 2023 (R$ -85 mi) é o sinal mais grave. Empresa queima 
                caixa mesmo com redução de atividade. Capital de giro consumindo recursos: estoques cresceram 
                para R$ 680 mi (imóveis encalhados). Qualidade do lucro era ruim mesmo em 2021 (FCO/LL de 0,46).</p>
                
                <p><strong>6. RED FLAGS IDENTIFICADOS</strong></p>
                <ul>
                    <li>FCO negativo por 2 anos consecutivos (-R$ 130 mi acumulado)</li>
                    <li>Cobertura de juros abaixo de 1x (EBIT não paga juros)</li>
                    <li>Taxa de distratos subindo de 8% para 22%</li>
                    <li>Estoques crescendo enquanto vendas caem</li>
                    <li>Dívida de curto prazo (R$ 210 mi) maior que caixa (R$ 35 mi)</li>
                    <li>Prejuízo líquido em 2023 consumindo patrimônio</li>
                </ul>
                
                <p><strong>7. CONCLUSÃO E RECOMENDAÇÃO</strong></p>
                <p><strong>Parecer: CRÍTICO - Risco elevado de insolvência</strong></p>
                <p><strong>Recomendações:</strong></p>
                <ol>
                    <li>Renegociação imediata de dívidas com alongamento de 3-5 anos</li>
                    <li>Venda de ativos não-core e terrenos do banco de terrenos</li>
                    <li>Promoções agressivas para desovar estoque e gerar caixa</li>
                    <li>Corte de custos fixos - já reduziu funcionários, continuar</li>
                    <li>Suspensão de novos lançamentos até estabilizar</li>
                    <li>Buscar investidor estratégico ou aporte de capital</li>
                    <li>Considerar recuperação judicial se renegociação falhar</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)


def renderizar_discussao_feedback():
    st.markdown("### Discussão Coletiva e Feedback Estruturado")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Atividade Final do Curso</strong><br>
            <em>Apresentação dos relatórios, discussão coletiva e feedback entre pares.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Estrutura da apresentação
    st.markdown("#### Estrutura da Apresentação (10 minutos)")
    
    apresentacao = [
        ("1. Contextualização", "1 min", "Breve descrição da empresa e situação"),
        ("2. Principais Achados", "3 min", "Indicadores-chave e tendências identificadas"),
        ("3. Red Flags", "2 min", "Sinais de alerta mais relevantes"),
        ("4. Diagnóstico", "2 min", "Avaliação da situação financeira"),
        ("5. Recomendações", "2 min", "Ações sugeridas e próximos passos")
    ]
    
    for item, tempo, desc in apresentacao:
        st.markdown(f"**{item}** ({tempo}): {desc}")
    
    st.markdown("---")
    
    # Critérios de avaliação
    st.markdown("#### Critérios de Avaliação")
    
    criterios = {
        "Critério": [
            "Domínio Técnico",
            "Qualidade da Análise",
            "Identificação de Riscos",
            "Coerência das Conclusões",
            "Qualidade das Recomendações",
            "Comunicação e Clareza"
        ],
        "Peso": ["20%", "20%", "15%", "15%", "15%", "15%"],
        "Descrição": [
            "Uso correto de indicadores e conceitos",
            "Profundidade e integração da análise",
            "Capacidade de identificar red flags",
            "Lógica entre dados e conclusões",
            "Viabilidade e relevância das sugestões",
            "Objetividade e organização da apresentação"
        ]
    }
    st.dataframe(pd.DataFrame(criterios), use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Formulário de feedback
    st.markdown("#### Feedback entre Pares")
    
    st.markdown("Avalie a apresentação de outro grupo:")
    
    grupo_avaliado = st.text_input("Nome do grupo/aluno avaliado:", key="grupo_avaliado")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nota_tecnico = st.slider("Domínio Técnico", 0, 10, 5, key="nota_tecnico")
        nota_analise = st.slider("Qualidade da Análise", 0, 10, 5, key="nota_analise")
        nota_riscos = st.slider("Identificação de Riscos", 0, 10, 5, key="nota_riscos")
    
    with col2:
        nota_conclusoes = st.slider("Coerência das Conclusões", 0, 10, 5, key="nota_conclusoes")
        nota_recomendacoes = st.slider("Qualidade das Recomendações", 0, 10, 5, key="nota_recomendacoes")
        nota_comunicacao = st.slider("Comunicação e Clareza", 0, 10, 5, key="nota_comunicacao")
    
    media = (nota_tecnico * 0.20 + nota_analise * 0.20 + nota_riscos * 0.15 + 
             nota_conclusoes * 0.15 + nota_recomendacoes * 0.15 + nota_comunicacao * 0.15)
    
    st.metric("Nota Final Ponderada", f"{media:.1f}")
    
    pontos_positivos = st.text_area("Pontos positivos da apresentação:", height=80, key="fb_positivos")
    pontos_melhoria = st.text_area("Pontos a melhorar:", height=80, key="fb_melhoria")
    
    st.markdown("---")
    
    # Reflexão final
    st.markdown("#### Reflexão Final do Curso")
    
    reflexao1 = st.text_area(
        "O que você aprendeu de mais importante neste curso?",
        height=80,
        key="reflexao1"
    )
    
    reflexao2 = st.text_area(
        "Como você aplicará esses conhecimentos na sua vida profissional?",
        height=80,
        key="reflexao2"
    )
    
    reflexao3 = st.text_area(
        "Que conceito você gostaria de aprofundar mais?",
        height=80,
        key="reflexao3"
    )
    
    # Síntese final do curso
    st.markdown("""
        <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>Síntese do Curso - Conceitos-Chave</h4>
            <ul>
                <li><strong>Demonstrações Financeiras:</strong> BP, DRE, DFC são complementares - analise todas</li>
                <li><strong>Análise Horizontal e Vertical:</strong> Tendências e estrutura revelam a história</li>
                <li><strong>Indicadores:</strong> Números isolados não dizem nada - compare com setor e histórico</li>
                <li><strong>DuPont:</strong> ROE = Margem x Giro x Alavancagem - entenda a origem do retorno</li>
                <li><strong>Liquidez vs Solvência:</strong> Curto prazo vs longo prazo - ambos importam</li>
                <li><strong>Qualidade do Lucro:</strong> FCO/LL revela se lucro é real ou contábil</li>
                <li><strong>Red Flags:</strong> Divergência LL-FCO, estoques/recebíveis crescendo, cobertura caindo</li>
                <li><strong>Contexto:</strong> Mesmo indicador, interpretações diferentes por setor</li>
                <li><strong>Ceticismo:</strong> Números muito bons merecem questionamento</li>
                <li><strong>Decisão:</strong> Análise sem conclusão não agrega valor - tome posição</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>Parabéns pela Conclusão do Curso!</h4>
            <p>Você completou o Laboratório de Análise de Demonstrações Financeiras. 
            Os conhecimentos adquiridos são fundamentais para qualquer profissional que 
            trabalhe com finanças, investimentos, crédito ou gestão empresarial.</p>
            <p><strong>Próximos passos sugeridos:</strong></p>
            <ul>
                <li>Pratique com demonstrações de empresas reais (B3, CVM)</li>
                <li>Acompanhe relatórios de analistas de mercado</li>
                <li>Aprofunde-se em valuation e modelagem financeira</li>
                <li>Estude casos de fraudes contábeis para aguçar o ceticismo</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()