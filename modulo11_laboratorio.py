import streamlit as st
import pandas as pd

def run():
    """
    Função principal do Módulo 11.
    Foco: Análise Integrada através do Modelo DuPont.
    """
    
    # Estilização CSS local para consistência visual (Boutique Acadêmica)
    st.markdown("""
        <style>
        .dupont-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border-left: 5px solid #1e293b;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .driver-box {
            background-color: #f8fafc;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            text-align: center;
        }
        .metric-header {
            color: #b45309;
            font-family: 'Merriweather', serif;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 10px;
        }
        .formula-text {
            font-family: 'Courier New', Courier, monospace;
            color: #475569;
            font-size: 0.9rem;
        }
        .interpretation-box {
            background-color: #1e293b;
            color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            border-right: 5px solid #b45309;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Título do Módulo
    st.markdown("<h1>Módulo 11: Análise Integrada Modelo DuPont</h1>", unsafe_allow_html=True)
    st.write("Nesta unidade, vamos decompor o ROE em seus três drivers fundamentais: Eficiência Operacional, Eficiência de Ativos e Alavancagem Financeira.")

    st.divider()

    # --- 1. APLICAÇÃO COMPLETA DO MODELO DUPONT ---
    st.subheader("1. Simulador da Árvore DuPont")
    st.markdown("""
    Insira os dados base para decompor o retorno da empresa. 
    Observe como cada alavanca contribui para o resultado final do acionista.
    """)

    with st.container():
        col_data1, col_data2 = st.columns(2)
        with col_data1:
            lucro_liquido = st.number_input("Lucro Líquido (R$):", min_value=1, value=12000)
            receita_liquida = st.number_input("Receita Líquida (R$):", min_value=1, value=100000)
        with col_data2:
            ativo_total = st.number_input("Ativo Total (R$):", min_value=1, value=80000)
            patrimonio_liquido = st.number_input("Patrimônio Líquido (R$):", min_value=1, value=50000)

        # Cálculos DuPont
        margem_liquida = (lucro_liquido / receita_liquida)
        giro_ativo = (receita_liquida / ativo_total)
        maf = (ativo_total / patrimonio_liquido) # Multiplicador de Alavancagem Financeira
        
        roa = (margem_liquida * giro_ativo) * 100
        roe = (margem_liquida * giro_ativo * maf) * 100

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='metric-header'>Drivers de Valor:</div>", unsafe_allow_html=True)
        
        d_col1, d_col2, d_col3 = st.columns(3)
        with d_col1:
            st.markdown("<div class='driver-box'>", unsafe_allow_html=True)
            st.metric("Margem Líquida", f"{margem_liquida*100:.1f}%")
            st.caption("Eficiência de Custos")
            st.markdown("</div>", unsafe_allow_html=True)
        with d_col2:
            st.markdown("<div class='driver-box'>", unsafe_allow_html=True)
            st.metric("Giro do Ativo", f"{giro_ativo:.2f}x")
            st.caption("Eficiência de Ativos")
            st.markdown("</div>", unsafe_allow_html=True)
        with d_col3:
            st.markdown("<div class='driver-box'>", unsafe_allow_html=True)
            st.metric("MAF (Alavancagem)", f"{maf:.2f}x")
            st.caption("Estrutura de Capital")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        res_col1, res_col2 = st.columns(2)
        with res_col1:
            st.metric("ROA (Retorno sobre Ativo)", f"{roa:.1f}%", help="Margem x Giro")
        with res_col2:
            st.metric("ROE (Retorno sobre PL)", f"{roe:.1f}%", delta=f"{(roe-roa):.1f}% vs ROA", help="Margem x Giro x MAF")

    st.info("**Nota do Professor:** O ROE é o produto final. Se ele subir, o Modelo DuPont nos diz 'quem' foi o responsável: o corte de custos (Margem), a rapidez nas vendas (Giro) ou o uso de dívida (MAF).")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2. DIAGNÓSTICO COMPARATIVO ENTRE EMPRESAS ---
    st.subheader("2. Diagnóstico: Empresa 'Líder' vs. Empresa 'Eficiente'")
    st.markdown("""
    Duas empresas do mesmo setor apresentam o **mesmo ROE de 18%**. Qual delas você recomendaria para um investidor conservador?
    """)

    dados_comp = {
        "Indicador": ["Margem Líquida", "Giro do Ativo", "Multiplicador (MAF)", "ROE Final"],
        "Empresa A (Varejo de Luxo)": ["20.0%", "0.60x", "1.50x", "18.0%"],
        "Empresa B (Atacarejo)": ["4.0%", "3.00x", "1.50x", "18.0%"]
    }
    st.table(pd.DataFrame(dados_comp))

    escolha_diag = st.radio(
        "Qual a principal diferença estratégica revelada pelo DuPont?",
        [
            "A Empresa A ganha na exclusividade (margem) e a B na escala (giro).",
            "A Empresa B é superior porque vende mais rápido.",
            "As empresas são operativamente idênticas pois o ROE é o mesmo."
        ]
    )

    if st.button("Validar Diagnóstico Comparativo"):
        if "exclusividade" in escolha_diag:
            st.success("Perfeito! O Modelo DuPont revela que, embora o retorno final seja igual, as estratégias são opostas. O investidor deve escolher aquela cujo risco operacional (perda de margem vs. parada de estoque) ele prefere carregar.")
        else:
            st.error("Resposta incompleta. Analise como os drivers de Margem e Giro se compensam para formar o mesmo retorno.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. EXERCÍCIO INTERPRETATIVO ESCRITO ---
    st.subheader("3. Exercício de Síntese Analítica")
    
    st.markdown("""
    <div class="interpretation-box">
        <p style="text-align: center; font-style: italic;">
            "Um aumento no ROE provocado exclusivamente pelo aumento do Multiplicador de Alavancagem (MAF) é sempre uma notícia positiva para o acionista?"
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_dupont_escrito"):
        st.write("Desenvolva sua análise crítica:")
        resposta_aluno = st.text_area(
            "Explique a relação entre o risco financeiro e a decomposição DuPont quando a rentabilidade operacional (ROA) permanece estagnada.",
            placeholder="Discorra sobre custo da dívida, risco de insolvência e alavancagem..."
        )
        
        submit_btn = st.form_submit_button("Submeter para Avaliação")
        
        if submit_btn:
            if len(resposta_aluno) > 40:
                st.balloons()
                st.info("""
                **Comentário Pedagógico:**
                Excelente reflexão. Se o ROA (Margem x Giro) não cresce, mas o ROE sobe via MAF, a empresa está apenas tomando mais risco. 
                Isso é perigoso porque a alavancagem potencializa ganhos, mas também acelera perdas em momentos de crise.
                """)
                st.success("Sua interpretação técnica foi registrada com sucesso!")
            else:
                st.warning("Por favor, elabore uma resposta mais profunda para demonstrar seu domínio sobre o risco financeiro.")

if __name__ == "__main__":
    run()