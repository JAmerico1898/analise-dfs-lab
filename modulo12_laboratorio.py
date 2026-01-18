import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 12.
    Foco: Análise Comparativa e Benchmarking Setorial.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .benchmarking-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #b45309;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .comparison-header {
            color: #1e293b;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.3rem;
            margin-bottom: 15px;
            text-align: center;
        }
        .highlight-slate {
            background-color: #f1f5f9;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }
        .metric-label {
            color: #475569;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .vs-badge {
            display: inline-block;
            background-color: #1e293b;
            color: white;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 12: Análise Comparativa e Benchmarking</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, aprendemos que os números não falam sozinhos. Eles precisam da régua do setor e da comparação com pares para ganhar significado real.")

    st.divider()

    # --- 1. ANÁLISE COMPARATIVA ENTRE DUAS EMPRESAS ---
    st.subheader("1. Laboratório de Benchmarking: Varejo A vs. Varejo B")
    st.markdown("""
    Analise o desempenho de duas gigantes do setor de varejo alimentar. Embora atuem no mesmo segmento, 
    seus indicadores contam histórias distintas sobre eficiência e estratégia.
    """)

    # Dados das Empresas
    dados_varejo = {
        "Indicador (KPI)": [
            "Margem Líquida (%)", 
            "Giro do Ativo (x)", 
            "ROE (%)", 
            "Liquidez Corrente", 
            "Dívida Líquida / EBITDA"
        ],
        "Varejo Premium (Empresa A)": [8.5, 0.9, 15.0, 1.8, 1.2],
        "Atacarejo (Empresa B)": [2.1, 4.2, 15.0, 1.1, 2.5]
    }
    df_varejo = pd.DataFrame(dados_varejo)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='comparison-header'>Quadro Comparativo de Performance</div>", unsafe_allow_html=True)
        st.table(df_varejo.set_index("Indicador (KPI)"))
    
    with col2:
        st.markdown("<div class='highlight-slate'>", unsafe_allow_html=True)
        st.markdown("<p class='metric-label'>O Paradoxo do ROE</p>", unsafe_allow_html=True)
        st.write("Note que ambas possuem o **mesmo ROE de 15,0%**.")
        st.write("Qual delas você considera mais resiliente a uma crise econômica?")
        
        escolha_varejo = st.radio(
            "Selecione sua visão:",
            ["Empresa A (Premium)", "Empresa B (Atacarejo)"],
            key="radio_varejo"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Verificar Insights do Benchmarking"):
        if escolha_varejo == "Empresa A (Premium)":
            st.success("Excelente! A Empresa A possui maior gordura operacional (Margem de 8.5%) e menor endividamento. Ela sacrifica o giro pela segurança.")
        else:
            st.info("Visão estratégica! A Empresa B foca em volume extremo (Giro de 4.2x). Ela é eficiente, mas opera no fio da navalha; qualquer queda de consumo impacta seu caixa rapidamente devido à margem baixa.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. DISCUSSÃO: POR QUE INDICADORES IGUAIS PODEM SIGNIFICAR COISAS DIFERENTES? ---
    st.subheader("2. Painel de Discussão: A Ilusão dos Números")
    
    st.markdown("""
    <div class='benchmarking-card'>
        <p><strong>Desafio Reflexivo:</strong> Imagine duas empresas com o mesmo Índice de Liquidez Corrente de 2.0. 
        A Empresa 1 tem 80% do seu ativo circulante em <strong>caixa disponível</strong>. 
        A Empresa 2 tem 80% do seu ativo circulante em <strong>estoques de moda de coleções passadas</strong>.</p>
        <p style='font-style: italic; color: #b45309;'>“Mesmo número, realidades opostas.”</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Clique para ver os fatores que distorcem as comparações"):
        st.markdown("""
        1. **Idade dos Ativos:** Ativos antigos (depreciados) inflam artificialmente o ROA e o Giro do Ativo.
        2. **Localização Geográfica:** Incentivos fiscais regionais distorcem a comparação de Lucro Líquido.
        3. **Integração Vertical:** Uma empresa que fabrica tudo terá margens maiores, mas giros menores que uma que apenas revende.
        4. **Métodos Contábeis:** Escolhas entre FIFO/LIFO ou diferentes taxas de depreciação.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. TRABALHO EM GRUPO: DESAFIO DE APRESENTAÇÃO ---
    st.subheader("3. Atividade Prática: Squad de Análise")
    
    st.info("Instruções para o Trabalho em Grupo (Entrega da Aula):")
    
    with st.form("form_trabalho_grupo"):
        st.markdown("""
        **Objetivo:** Escolher um setor da B3 (Ex: Siderurgia, Bancos, Elétricas) e comparar duas empresas rivais.
        
        **Checklist de Análise:**
        - Quem é o benchmark de lucratividade (Margem)?
        - Quem é o benchmark de eficiência operacional (Giro)?
        - Quem corre mais risco financeiro (Alavancagem)?
        """)
        
        nomes_grupo = st.text_input("Nomes dos integrantes do grupo:")
        setor_escolhido = st.selectbox("Setor em análise:", ["Bancos", "Varejo", "Energia Elétrica", "Siderurgia/Mineração", "Aéreo"])
        conclusao_preliminar = st.text_area("Resumo da conclusão do grupo (máx 5 linhas):")
        
        submit_trabalho = st.form_submit_button("Registrar Entrega do Grupo")
        
        if submit_trabalho:
            if len(conclusao_preliminar) > 20:
                st.balloons()
                st.success(f"Trabalho do setor de {setor_escolhido} registrado com sucesso!")
                st.info("Preparem-se para a apresentação curta de 5 minutos ao final da aula.")
            else:
                st.error("Por favor, desenvolva melhor a conclusão antes de submeter.")

if __name__ == "__main__":
    run()