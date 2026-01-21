"""
Módulo 12 - Análise Setorial e Benchmarking
Laboratório de Análise de Demonstrações Financeiras
=======================================================
Conteúdo:
- Análise comparativa entre duas empresas do mesmo setor
- Discussão: por que indicadores iguais podem significar coisas diferentes?
- Trabalho em grupo com apresentação curta
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>🏭 Módulo 12 - Análise Setorial e Benchmarking</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Realizar análise comparativa (benchmarking) entre empresas do mesmo setor</li>
                <li>Compreender por que indicadores iguais podem ter interpretações diferentes</li>
                <li>Contextualizar indicadores financeiros dentro da realidade setorial</li>
                <li>Apresentar análises de forma estruturada e convincente</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "📊 Análise Comparativa",
        "🤔 Indicadores em Contexto",
        "👥 Trabalho em Grupo"
    ])
    
    with tab1:
        renderizar_analise_comparativa()
    
    with tab2:
        renderizar_indicadores_contexto()
    
    with tab3:
        renderizar_trabalho_grupo()


def get_dados_setor_varejo():
    """Retorna dados de duas empresas do setor de varejo para comparação."""
    
    dados = {
        "Magazine Aurora S.A.": {
            "perfil": "Varejista tradicional com lojas físicas em shoppings e ruas",
            "modelo": "Lojas próprias, estoque próprio, crediário próprio",
            "fundacao": 1965,
            "lojas": 450,
            "funcionarios": 28000,
            "dados": {
                "receita": 12500,
                "cmv": 8750,
                "lucro_bruto": 3750,
                "desp_vendas": 1875,
                "desp_admin": 625,
                "ebit": 1250,
                "desp_fin": 375,
                "lair": 925,
                "ir": 315,
                "lucro_liquido": 610,
                "ativo_total": 8500,
                "ativo_circulante": 4250,
                "estoques": 2125,
                "clientes": 1700,
                "imobilizado": 3400,
                "passivo_circulante": 3400,
                "fornecedores": 1275,
                "emprestimos_cp": 1020,
                "passivo_nao_circ": 2125,
                "emprestimos_lp": 1700,
                "patrimonio_liquido": 2975
            }
        },
        "Digital Store Ltda.": {
            "perfil": "E-commerce puro com marketplace e fulfillment",
            "modelo": "Plataforma digital, sellers terceiros, logística própria",
            "fundacao": 2012,
            "lojas": 0,
            "funcionarios": 8500,
            "dados": {
                "receita": 15000,
                "cmv": 11250,
                "lucro_bruto": 3750,
                "desp_vendas": 2250,
                "desp_admin": 450,
                "ebit": 1050,
                "desp_fin": 180,
                "lair": 920,
                "ir": 313,
                "lucro_liquido": 607,
                "ativo_total": 6000,
                "ativo_circulante": 3600,
                "estoques": 900,
                "clientes": 1500,
                "imobilizado": 1200,
                "passivo_circulante": 3000,
                "fornecedores": 1800,
                "emprestimos_cp": 450,
                "passivo_nao_circ": 900,
                "emprestimos_lp": 600,
                "patrimonio_liquido": 2100
            }
        },
        "medias_setor": {
            "margem_bruta": 28.0,
            "margem_ebit": 8.0,
            "margem_liquida": 4.5,
            "roe": 18.0,
            "roa": 7.0,
            "liquidez_corrente": 1.20,
            "giro_ativo": 1.80,
            "endividamento": 65.0
        }
    }
    return dados


def calcular_indicadores(dados):
    """Calcula todos os indicadores financeiros."""
    d = dados
    
    indicadores = {
        # Rentabilidade
        "margem_bruta": d['lucro_bruto'] / d['receita'] * 100,
        "margem_ebit": d['ebit'] / d['receita'] * 100,
        "margem_liquida": d['lucro_liquido'] / d['receita'] * 100,
        "roe": d['lucro_liquido'] / d['patrimonio_liquido'] * 100,
        "roa": d['lucro_liquido'] / d['ativo_total'] * 100,
        
        # Liquidez
        "liquidez_corrente": d['ativo_circulante'] / d['passivo_circulante'],
        "liquidez_seca": (d['ativo_circulante'] - d['estoques']) / d['passivo_circulante'],
        
        # Estrutura
        "endividamento": (d['passivo_circulante'] + d['passivo_nao_circ']) / d['ativo_total'] * 100,
        "divida_pl": (d['emprestimos_cp'] + d['emprestimos_lp']) / d['patrimonio_liquido'],
        "imobilizacao_pl": d['imobilizado'] / d['patrimonio_liquido'] * 100,
        
        # Eficiência
        "giro_ativo": d['receita'] / d['ativo_total'],
        "giro_estoque": d['cmv'] / d['estoques'],
        "pme": d['estoques'] / d['cmv'] * 360,
        "pmr": d['clientes'] / d['receita'] * 360,
        "pmp": d['fornecedores'] / d['cmv'] * 360,
        
        # DuPont
        "multiplicador": d['ativo_total'] / d['patrimonio_liquido'],
        
        # Produtividade
        "receita_func": d['receita'] / (d.get('funcionarios', 1) / 1000) if 'funcionarios' in d else 0,
    }
    
    # Ciclo financeiro
    indicadores['ciclo_financeiro'] = indicadores['pme'] + indicadores['pmr'] - indicadores['pmp']
    
    return indicadores


def renderizar_analise_comparativa():
    """Análise comparativa entre duas empresas do mesmo setor."""
    
    st.markdown("### 📊 Análise Comparativa: Varejo Tradicional vs E-commerce")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Contexto:</strong><br>
            <em>Duas empresas do setor de varejo com modelos de negócio distintos. 
            Ambas competem pelos mesmos consumidores, mas operam de formas completamente diferentes. 
            Seu desafio é comparar os indicadores e entender o que eles revelam sobre cada modelo.</em>
        </div>
    """, unsafe_allow_html=True)
    
    dados = get_dados_setor_varejo()
    
    # Perfil das empresas
    st.markdown("#### 🏢 Perfil das Empresas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        emp1 = dados["Magazine Aurora S.A."]
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 20px; border-radius: 10px;'>
                <h4>🏬 Magazine Aurora S.A.</h4>
                <p><strong>Modelo:</strong> {emp1['perfil']}</p>
                <p><strong>Operação:</strong> {emp1['modelo']}</p>
                <p>📅 Fundação: {emp1['fundacao']} | 🏪 {emp1['lojas']} lojas | 👥 {emp1['funcionarios']:,} funcionários</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        emp2 = dados["Digital Store Ltda."]
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
                <h4>💻 Digital Store Ltda.</h4>
                <p><strong>Modelo:</strong> {emp2['perfil']}</p>
                <p><strong>Operação:</strong> {emp2['modelo']}</p>
                <p>📅 Fundação: {emp2['fundacao']} | 🌐 100% digital | 👥 {emp2['funcionarios']:,} funcionários</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dados financeiros
    st.markdown("#### 📋 Dados Financeiros (R$ milhões)")
    
    dados_tabela = {
        "Conta": ["Receita Líquida", "CMV", "Lucro Bruto", "Despesas Vendas", "Despesas Admin.",
                 "EBIT", "Despesas Financeiras", "Lucro Líquido", "Ativo Total", 
                 "Estoques", "Imobilizado", "Patrimônio Líquido"],
        "Magazine Aurora": [12500, 8750, 3750, 1875, 625, 1250, 375, 610, 8500, 2125, 3400, 2975],
        "Digital Store": [15000, 11250, 3750, 2250, 450, 1050, 180, 607, 6000, 900, 1200, 2100]
    }
    
    df_dados = pd.DataFrame(dados_tabela)
    st.dataframe(df_dados, use_container_width=True, hide_index=True)
    
    # Calcular indicadores
    ind_aurora = calcular_indicadores(dados["Magazine Aurora S.A."]['dados'])
    ind_digital = calcular_indicadores(dados["Digital Store Ltda."]["dados"])
    medias = dados["medias_setor"]
    
    st.markdown("---")
    st.markdown("#### 📈 Comparativo de Indicadores")
    
    # Tabela de indicadores
    ind_tabela = {
        "Indicador": ["Margem Bruta (%)", "Margem EBIT (%)", "Margem Líquida (%)", 
                     "ROE (%)", "ROA (%)", "Liquidez Corrente", "Giro do Ativo",
                     "Endividamento (%)", "PME (dias)", "Ciclo Financeiro (dias)"],
        "Magazine Aurora": [
            f"{ind_aurora['margem_bruta']:.1f}", f"{ind_aurora['margem_ebit']:.1f}",
            f"{ind_aurora['margem_liquida']:.1f}", f"{ind_aurora['roe']:.1f}",
            f"{ind_aurora['roa']:.1f}", f"{ind_aurora['liquidez_corrente']:.2f}",
            f"{ind_aurora['giro_ativo']:.2f}", f"{ind_aurora['endividamento']:.1f}",
            f"{ind_aurora['pme']:.0f}", f"{ind_aurora['ciclo_financeiro']:.0f}"
        ],
        "Digital Store": [
            f"{ind_digital['margem_bruta']:.1f}", f"{ind_digital['margem_ebit']:.1f}",
            f"{ind_digital['margem_liquida']:.1f}", f"{ind_digital['roe']:.1f}",
            f"{ind_digital['roa']:.1f}", f"{ind_digital['liquidez_corrente']:.2f}",
            f"{ind_digital['giro_ativo']:.2f}", f"{ind_digital['endividamento']:.1f}",
            f"{ind_digital['pme']:.0f}", f"{ind_digital['ciclo_financeiro']:.0f}"
        ],
        "Média Setor": [
            f"{medias['margem_bruta']:.1f}", f"{medias['margem_ebit']:.1f}",
            f"{medias['margem_liquida']:.1f}", f"{medias['roe']:.1f}",
            f"{medias['roa']:.1f}", f"{medias['liquidez_corrente']:.2f}",
            f"{medias['giro_ativo']:.2f}", f"{medias['endividamento']:.1f}",
            "45", "30"
        ]
    }
    
    df_ind = pd.DataFrame(ind_tabela)
    st.dataframe(df_ind, use_container_width=True, hide_index=True)
    
    # Destaque: indicadores muito semelhantes
    st.markdown("---")
    st.markdown("#### 🎯 Destaque: Indicadores Surpreendentemente Semelhantes")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Lucro Bruto</h4>
                <h2>R$ 3.750 mi</h2>
                <p>IGUAL para ambas!</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Lucro Líquido</h4>
                <h2>~R$ 608 mi</h2>
                <p>Diferença < 1%!</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; text-align: center;'>
                <h4>Margem Bruta</h4>
                <h2>~25-30%</h2>
                <p>Muito próximas!</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.info("🤔 **Pergunta-chave:** Se os lucros são quase iguais, as empresas são equivalentes como investimento?")
    
    # Gráficos comparativos
    st.markdown("---")
    st.markdown("#### 📊 Visualização Comparativa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar
        categorias = ['Margem Bruta', 'Margem EBIT', 'ROE', 'ROA', 'Giro Ativo', 'Liquidez']
        
        valores_aurora = [
            ind_aurora['margem_bruta']/40*100,
            ind_aurora['margem_ebit']/15*100,
            ind_aurora['roe']/30*100,
            ind_aurora['roa']/15*100,
            ind_aurora['giro_ativo']/3*100,
            ind_aurora['liquidez_corrente']/2*100
        ]
        
        valores_digital = [
            ind_digital['margem_bruta']/40*100,
            ind_digital['margem_ebit']/15*100,
            ind_digital['roe']/30*100,
            ind_digital['roa']/15*100,
            ind_digital['giro_ativo']/3*100,
            ind_digital['liquidez_corrente']/2*100
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=valores_aurora + [valores_aurora[0]],
            theta=categorias + [categorias[0]],
            fill='toself',
            name='Magazine Aurora',
            line_color='#3b82f6'
        ))
        
        fig.add_trace(go.Scatterpolar(
            r=valores_digital + [valores_digital[0]],
            theta=categorias + [categorias[0]],
            fill='toself',
            name='Digital Store',
            line_color='#22c55e'
        ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Perfil Comparativo (normalizado)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Barras de eficiência
        fig2 = go.Figure()
        
        metricas = ['Giro Ativo', 'Giro Estoque', 'ROA']
        aurora_vals = [ind_aurora['giro_ativo'], ind_aurora['giro_estoque'], ind_aurora['roa']]
        digital_vals = [ind_digital['giro_ativo'], ind_digital['giro_estoque'], ind_digital['roa']]
        
        fig2.add_trace(go.Bar(name='Magazine Aurora', x=metricas, y=aurora_vals, marker_color='#3b82f6'))
        fig2.add_trace(go.Bar(name='Digital Store', x=metricas, y=digital_vals, marker_color='#22c55e'))
        
        fig2.update_layout(barmode='group', title="Indicadores de Eficiência", height=400)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Análise DuPont comparativa
    st.markdown("---")
    st.markdown("#### 🔬 Decomposição DuPont: Como Chegam ao Mesmo Lucro?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        margem_a = ind_aurora['margem_liquida']/100
        giro_a = ind_aurora['giro_ativo']
        mult_a = ind_aurora['multiplicador']
        
        st.markdown(f"""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px;'>
                <h4>Magazine Aurora - ROE: {ind_aurora['roe']:.1f}%</h4>
                <p><strong>Margem:</strong> {ind_aurora['margem_liquida']:.1f}% (maior)</p>
                <p><strong>Giro:</strong> {ind_aurora['giro_ativo']:.2f}x (menor)</p>
                <p><strong>Alavancagem:</strong> {ind_aurora['multiplicador']:.2f}x (maior)</p>
                <hr>
                <p><strong>Fórmula:</strong> {margem_a*100:.1f}% × {giro_a:.2f} × {mult_a:.2f} = {ind_aurora['roe']:.1f}%</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        margem_d = ind_digital['margem_liquida']/100
        giro_d = ind_digital['giro_ativo']
        mult_d = ind_digital['multiplicador']
        
        st.markdown(f"""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <h4>Digital Store - ROE: {ind_digital['roe']:.1f}%</h4>
                <p><strong>Margem:</strong> {ind_digital['margem_liquida']:.1f}% (menor)</p>
                <p><strong>Giro:</strong> {ind_digital['giro_ativo']:.2f}x (maior)</p>
                <p><strong>Alavancagem:</strong> {ind_digital['multiplicador']:.2f}x (menor)</p>
                <hr>
                <p><strong>Fórmula:</strong> {margem_d*100:.1f}% × {giro_d:.2f} × {mult_d:.2f} = {ind_digital['roe']:.1f}%</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.warning("""
        ⚠️ **Insight Importante:** 
        
        Ambas chegam a ROEs próximos (~20% vs ~29%), mas por caminhos opostos:
        - **Aurora:** Margem maior + Giro menor + Mais alavancagem
        - **Digital:** Margem menor + Giro maior + Menos alavancagem
        
        O ROE da Digital Store é de melhor QUALIDADE (menos dependente de dívida).
    """)


def renderizar_indicadores_contexto():
    """Discussão sobre por que indicadores iguais podem significar coisas diferentes."""
    
    st.markdown("### 🤔 Por Que Indicadores Iguais Podem Significar Coisas Diferentes?")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Conceito Central:</strong><br>
            <em>Indicadores financeiros são ferramentas de análise, não verdades absolutas. 
            O mesmo número pode ter interpretações completamente diferentes dependendo do 
            contexto: setor, modelo de negócio, momento do ciclo econômico, estratégia da empresa.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Casos de ambiguidade
    st.markdown("#### 📚 Casos de Indicadores Ambíguos")
    
    casos = [
        {
            "titulo": "Caso 1: Liquidez Corrente = 1,2",
            "empresa_a": {
                "nome": "Supermercado Diário",
                "setor": "Varejo Alimentar",
                "contexto": "Estoque gira 52x/ano, clientes pagam à vista, fornecedores dão 45 dias",
                "interpretacao": "ADEQUADA - O modelo de negócio não precisa de mais liquidez. Caixa 'parado' seria ineficiente."
            },
            "empresa_b": {
                "nome": "Indústria Pesada S.A.",
                "setor": "Máquinas e Equipamentos",
                "contexto": "Ciclo produtivo de 6 meses, clientes pagam em 90 dias, estoque de matéria-prima",
                "interpretacao": "INSUFICIENTE - O ciclo longo exige mais folga. Pode ter problemas de caixa."
            },
            "licao": "A liquidez adequada depende do ciclo operacional de cada negócio."
        },
        {
            "titulo": "Caso 2: Margem Líquida = 3%",
            "empresa_a": {
                "nome": "Atacadão Distribuidor",
                "setor": "Atacado",
                "contexto": "Volume gigantesco, giro de 15x/ano, operação eficiente",
                "interpretacao": "EXCELENTE - No atacado, 3% é margem saudável. O lucro vem do volume."
            },
            "empresa_b": {
                "nome": "Consultoria Premium",
                "setor": "Serviços Profissionais",
                "contexto": "Clientes pagam R$ 2.000/hora, baixo custo variável",
                "interpretacao": "PÉSSIMA - Consultoria deveria ter margem de 20-30%. Algo está muito errado."
            },
            "licao": "A margem aceitável varia dramaticamente entre setores."
        },
        {
            "titulo": "Caso 3: ROE = 25%",
            "empresa_a": {
                "nome": "TechStart Inovações",
                "setor": "Tecnologia",
                "contexto": "Startup em crescimento, baixa alavancagem, reinveste tudo",
                "interpretacao": "BOM - ROE alto vindo de margem e inovação. Sustentável."
            },
            "empresa_b": {
                "nome": "Varejo Alavancado S.A.",
                "setor": "Varejo",
                "contexto": "Margem de 2%, alavancagem de 5x, taxa de juros subindo",
                "interpretacao": "PREOCUPANTE - ROE depende de dívida. Uma crise pode eliminar o retorno."
            },
            "licao": "A origem do ROE (operação vs alavancagem) define sua qualidade."
        },
        {
            "titulo": "Caso 4: Endividamento = 70%",
            "empresa_a": {
                "nome": "Concessão Energia S.A.",
                "setor": "Utilities",
                "contexto": "Receita garantida por contrato de 30 anos, tarifa reajustada por inflação",
                "interpretacao": "NORMAL - Setor regulado com fluxo previsível comporta mais dívida."
            },
            "empresa_b": {
                "nome": "Moda Tendência Ltda.",
                "setor": "Vestuário",
                "contexto": "Vendas sazonais, preferências mudam rápido, competição intensa",
                "interpretacao": "PERIGOSO - Setor volátil não combina com dívida alta. Risco de insolvência."
            },
            "licao": "A tolerância a dívida depende da previsibilidade do fluxo de caixa."
        },
        {
            "titulo": "Caso 5: Giro do Ativo = 0,5x",
            "empresa_a": {
                "nome": "Shoppings Brasil S.A.",
                "setor": "Propriedades Comerciais",
                "contexto": "Ativos são imóveis de alto valor, receita vem de aluguéis estáveis",
                "interpretacao": "ESPERADO - Negócio imobiliário tem giro baixo por natureza."
            },
            "empresa_b": {
                "nome": "Varejo Express",
                "setor": "Comércio",
                "contexto": "Lojas com estoque, deveria ter giro alto",
                "interpretacao": "RUIM - Varejista com giro tão baixo está com ativos improdutivos."
            },
            "licao": "O giro esperado depende da natureza dos ativos do negócio."
        }
    ]
    
    for caso in casos:
        with st.expander(f"📌 {caso['titulo']}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                    <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px;'>
                        <h4>{caso['empresa_a']['nome']}</h4>
                        <p><strong>Setor:</strong> {caso['empresa_a']['setor']}</p>
                        <p><strong>Contexto:</strong> {caso['empresa_a']['contexto']}</p>
                        <p><strong>Interpretação:</strong> ✅ {caso['empresa_a']['interpretacao']}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                    <div style='background-color: #fee2e2; padding: 15px; border-radius: 10px;'>
                        <h4>{caso['empresa_b']['nome']}</h4>
                        <p><strong>Setor:</strong> {caso['empresa_b']['setor']}</p>
                        <p><strong>Contexto:</strong> {caso['empresa_b']['contexto']}</p>
                        <p><strong>Interpretação:</strong> ⚠️ {caso['empresa_b']['interpretacao']}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            st.info(f"💡 **Lição:** {caso['licao']}")
    
    st.markdown("---")
    
    # Framework de contextualização
    st.markdown("#### 🎯 Framework: Como Contextualizar Indicadores")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px;'>
            <h4>Checklist de Contextualização</h4>
            <ol>
                <li><strong>Qual é o setor?</strong> Compare com médias setoriais, não com médias gerais</li>
                <li><strong>Qual é o modelo de negócio?</strong> Asset-light vs asset-heavy, B2B vs B2C</li>
                <li><strong>Qual é o ciclo operacional?</strong> Define necessidade de liquidez e capital de giro</li>
                <li><strong>Qual é o momento do ciclo?</strong> Expansão, maturidade, declínio</li>
                <li><strong>Qual é a estratégia?</strong> Crescimento agressivo vs estabilidade</li>
                <li><strong>Quais são os riscos específicos?</strong> Regulatório, tecnológico, competitivo</li>
                <li><strong>Como está o ambiente macro?</strong> Juros, câmbio, economia</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Exercício interativo
    st.markdown("#### ✏️ Exercício: Você é o Analista")
    
    st.markdown("""
        **Situação:** Você recebeu os seguintes indicadores de três empresas, todas com ROE de 15%:
    """)
    
    exercicio_data = {
        "Indicador": ["Margem Líquida", "Giro do Ativo", "Multiplicador", "Setor"],
        "Empresa X": ["15%", "0,5x", "2,0x", "?"],
        "Empresa Y": ["3%", "2,5x", "2,0x", "?"],
        "Empresa Z": ["5%", "1,0x", "3,0x", "?"]
    }
    
    st.dataframe(pd.DataFrame(exercicio_data), use_container_width=True, hide_index=True)
    
    st.markdown("**Identifique o provável setor de cada empresa:**")
    
    col1, col2, col3 = st.columns(3)
    
    opcoes_setor = ["Selecione...", "Varejo/Atacado", "Software/SaaS", "Banco/Financeiro", 
                   "Indústria Pesada", "Utilities/Concessões"]
    
    with col1:
        resp_x = st.selectbox("Empresa X:", opcoes_setor, key="setor_x")
    with col2:
        resp_y = st.selectbox("Empresa Y:", opcoes_setor, key="setor_y")
    with col3:
        resp_z = st.selectbox("Empresa Z:", opcoes_setor, key="setor_z")
    
    if st.button("Verificar Respostas", key="btn_setores"):
        acertos = 0
        
        # Empresa X: Alta margem, baixo giro = Software/SaaS ou Utilities
        if resp_x in ["Software/SaaS", "Utilities/Concessões"]:
            st.success("✅ Empresa X: Correto! Alta margem + baixo giro = modelo de alta rentabilidade por unidade")
            acertos += 1
        else:
            st.error("❌ Empresa X: A combinação de alta margem (15%) e baixo giro (0,5x) é típica de Software/SaaS ou Utilities")
        
        # Empresa Y: Baixa margem, alto giro = Varejo/Atacado
        if resp_y == "Varejo/Atacado":
            st.success("✅ Empresa Y: Correto! Baixa margem + alto giro = modelo de volume")
            acertos += 1
        else:
            st.error("❌ Empresa Y: A combinação de baixa margem (3%) e alto giro (2,5x) é típica de Varejo/Atacado")
        
        # Empresa Z: Margem média, giro médio, alta alavancagem = Banco
        if resp_z == "Banco/Financeiro":
            st.success("✅ Empresa Z: Correto! Alta alavancagem é característica de bancos")
            acertos += 1
        else:
            st.error("❌ Empresa Z: Alta alavancagem (3,0x) com margem e giro medianos é típica de Bancos/Financeiras")
        
        if acertos == 3:
            st.balloons()
            st.success("🏆 Excelente! Você identificou corretamente os padrões setoriais!")


def renderizar_trabalho_grupo():
    """Trabalho em grupo com apresentação curta."""
    
    st.markdown("### 👥 Trabalho em Grupo: Apresentação de Análise Comparativa")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>📋 ATIVIDADE AVALIATIVA EM GRUPO</strong><br>
            <em>Cada grupo deve preparar uma apresentação de 5-7 minutos comparando as duas 
            empresas do caso (Magazine Aurora vs Digital Store), com recomendação de investimento.</em>
        </div>
    """, unsafe_allow_html=True)
    
    # Estrutura da apresentação
    st.markdown("#### 📑 Estrutura Sugerida para a Apresentação")
    
    estrutura = [
        {
            "slide": "1. Introdução",
            "tempo": "30 seg",
            "conteudo": "Apresentação das duas empresas e objetivo da análise",
            "dica": "Seja direto. Contextualize o setor brevemente."
        },
        {
            "slide": "2. Comparativo de Indicadores",
            "tempo": "1 min",
            "conteudo": "Principais indicadores lado a lado com destaque para diferenças",
            "dica": "Use tabela ou gráfico. Destaque os 3-4 indicadores mais relevantes."
        },
        {
            "slide": "3. Análise DuPont",
            "tempo": "1,5 min",
            "conteudo": "Decomposição do ROE de cada empresa",
            "dica": "Mostre como cada uma chega ao seu ROE. Identifique a fonte do retorno."
        },
        {
            "slide": "4. Pontos Fortes e Fracos",
            "tempo": "1,5 min",
            "conteudo": "Análise qualitativa de cada modelo de negócio",
            "dica": "Equilibre aspectos positivos e negativos. Seja específico."
        },
        {
            "slide": "5. Riscos Identificados",
            "tempo": "1 min",
            "conteudo": "Principais riscos de cada empresa",
            "dica": "Pense em: operacional, financeiro, de mercado, tecnológico."
        },
        {
            "slide": "6. Recomendação",
            "tempo": "1 min",
            "conteudo": "Qual empresa é melhor investimento? Por quê?",
            "dica": "Tome uma posição clara. Justifique com dados."
        },
        {
            "slide": "7. Q&A",
            "tempo": "1 min",
            "conteudo": "Perguntas da turma/professor",
            "dica": "Esteja preparado para defender sua análise."
        }
    ]
    
    for item in estrutura:
        with st.expander(f"📌 {item['slide']} ({item['tempo']})"):
            st.markdown(f"**Conteúdo:** {item['conteudo']}")
            st.info(f"💡 **Dica:** {item['dica']}")
    
    st.markdown("---")
    
    # Template de preparação
    st.markdown("#### ✏️ Template de Preparação do Grupo")
    
    st.markdown("**Preencha as seções abaixo para estruturar sua apresentação:**")
    
    grupo_nome = st.text_input("Nome do Grupo:", placeholder="Ex: Grupo Alpha", key="grupo_nome")
    
    st.markdown("##### 1. Síntese Comparativa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Magazine Aurora - Principais Características:**")
        aurora_carac = st.text_area(
            "Liste 3-5 características distintivas:",
            placeholder="Ex: Modelo tradicional, alta capilaridade, crediário próprio...",
            height=100,
            key="aurora_carac"
        )
    
    with col2:
        st.markdown("**Digital Store - Principais Características:**")
        digital_carac = st.text_area(
            "Liste 3-5 características distintivas:",
            placeholder="Ex: 100% digital, marketplace, logística eficiente...",
            height=100,
            key="digital_carac"
        )
    
    st.markdown("##### 2. Análise de Indicadores-Chave")
    
    ind_escolhidos = st.multiselect(
        "Selecione os 4 indicadores mais importantes para sua análise:",
        options=["Margem Bruta", "Margem EBIT", "Margem Líquida", "ROE", "ROA", 
                "Liquidez Corrente", "Giro do Ativo", "Endividamento", "Ciclo Financeiro",
                "Giro de Estoque", "PMR", "PMP"],
        default=["ROE", "Margem EBIT", "Giro do Ativo", "Endividamento"],
        key="ind_escolhidos"
    )
    
    justif_ind = st.text_area(
        "Por que esses indicadores são os mais relevantes para esta comparação?",
        placeholder="Justifique a escolha dos indicadores...",
        height=80,
        key="justif_ind"
    )
    
    st.markdown("##### 3. Pontos Fortes e Fracos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        aurora_fortes = st.text_area("Pontos FORTES - Magazine Aurora:", height=80, key="aurora_fortes")
        aurora_fracos = st.text_area("Pontos FRACOS - Magazine Aurora:", height=80, key="aurora_fracos")
    
    with col2:
        digital_fortes = st.text_area("Pontos FORTES - Digital Store:", height=80, key="digital_fortes")
        digital_fracos = st.text_area("Pontos FRACOS - Digital Store:", height=80, key="digital_fracos")
    
    st.markdown("##### 4. Riscos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        riscos_aurora = st.text_area(
            "Principais riscos - Magazine Aurora:",
            placeholder="Operacional, financeiro, tecnológico, competitivo...",
            height=80,
            key="riscos_aurora"
        )
    
    with col2:
        riscos_digital = st.text_area(
            "Principais riscos - Digital Store:",
            placeholder="Operacional, financeiro, tecnológico, competitivo...",
            height=80,
            key="riscos_digital"
        )
    
    st.markdown("##### 5. Recomendação Final")
    
    recomendacao = st.radio(
        "Qual empresa vocês recomendam como melhor investimento?",
        options=["Magazine Aurora S.A.", "Digital Store Ltda.", "Nenhuma das duas"],
        key="recomendacao_grupo"
    )
    
    justif_recom = st.text_area(
        "Justificativa da recomendação (mínimo 100 palavras):",
        placeholder="Explique por que escolheram essa empresa, considerando risco e retorno...",
        height=120,
        key="justif_recom"
    )
    
    palavras_justif = len(justif_recom.split()) if justif_recom else 0
    st.caption(f"Palavras: {palavras_justif}/100 mínimo")
    
    st.markdown("---")
    
    # Critérios de avaliação
    st.markdown("#### 📊 Critérios de Avaliação da Apresentação")
    
    criterios = {
        "Critério": [
            "Clareza e Organização",
            "Qualidade da Análise Quantitativa", 
            "Profundidade da Análise Qualitativa",
            "Coerência da Recomendação",
            "Capacidade de Resposta às Perguntas",
            "Gestão do Tempo"
        ],
        "Peso": ["20%", "25%", "20%", "20%", "10%", "5%"],
        "Descrição": [
            "Slides bem estruturados, linguagem clara, fluxo lógico",
            "Uso correto dos indicadores, DuPont bem aplicado, números precisos",
            "Contextualização setorial, riscos bem identificados, insights originais",
            "Recomendação fundamentada nos dados, posição clara e defendida",
            "Segurança nas respostas, conhecimento demonstrado além dos slides",
            "Apresentação dentro do tempo, sem correria ou sobra excessiva"
        ]
    }
    
    df_criterios = pd.DataFrame(criterios)
    st.dataframe(df_criterios, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Dicas finais
    st.markdown("""
        <div style='background-color: #dcfce7; padding: 20px; border-radius: 10px;'>
            <h4>💡 Dicas para uma Boa Apresentação</h4>
            <ul>
                <li><strong>Ensaiem juntos:</strong> Cada membro deve conhecer o trabalho todo</li>
                <li><strong>Sejam visuais:</strong> Gráficos comunicam melhor que tabelas extensas</li>
                <li><strong>Tomem posição:</strong> Análise sem conclusão não agrega valor</li>
                <li><strong>Antecipem perguntas:</strong> Pensem no que o professor pode questionar</li>
                <li><strong>Controlem o tempo:</strong> Pratiquem com cronômetro</li>
                <li><strong>Dividam as falas:</strong> Todos devem participar da apresentação</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Síntese do módulo
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; margin-top: 20px;'>
            <h4>📝 Síntese do Módulo</h4>
            <ul>
                <li><strong>Benchmarking é essencial:</strong> Números só fazem sentido em comparação</li>
                <li><strong>Contexto importa mais que o número:</strong> Mesmo indicador, interpretações diferentes</li>
                <li><strong>Setores têm padrões próprios:</strong> Compare sempre com peers</li>
                <li><strong>Modelos de negócio explicam diferenças:</strong> Asset-light vs asset-heavy, margem vs giro</li>
                <li><strong>Qualidade do ROE importa:</strong> Operacional > Alavancagem</li>
                <li><strong>Análise precisa de conclusão:</strong> Tome posição fundamentada</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()