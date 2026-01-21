"""
Módulo 2 - Estrutura e Lógica das Demonstrações
Laboratório de Análise de Demonstrações Financeiras
"""

import streamlit as st


def run():
    """Função principal do módulo - chamada pelo hub central."""
    
    st.markdown("<h1>📑 Módulo 2 - Estrutura e Lógica das Demonstrações</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="welcome-card">
            <h3>🎯 Objetivos de Aprendizagem</h3>
            <p>Ao final desta atividade, você será capaz de:</p>
            <ul>
                <li>Mapear eventos econômicos nas demonstrações financeiras corretas</li>
                <li>Compreender a interligação entre BP, DRE e DFC</li>
                <li>Identificar como um mesmo fato contábil aparece em múltiplas demonstrações</li>
                <li>Aplicar a lógica das partidas dobradas na análise financeira</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs([
        "🗺️ Exercício Guiado", 
        "👥 Atividade em Dupla", 
        "📝 Exercícios Estruturais"
    ])
    
    with tab1:
        renderizar_exercicio_guiado()
    
    with tab2:
        renderizar_atividade_dupla()
    
    with tab3:
        renderizar_exercicios_estruturais()


def renderizar_exercicio_guiado():
    """Exercício guiado de mapeamento de eventos."""
    
    st.markdown("### 🗺️ Exercício Guiado: Mapeamento de Eventos Econômicos")
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #b45309; margin-bottom: 20px;'>
            <strong>Objetivo:</strong><br>
            <em>Compreender como eventos econômicos são registrados nas demonstrações financeiras.</em>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📚 Revisão: As Três Demonstrações Principais")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background-color: #dbeafe; padding: 15px; border-radius: 10px; text-align: center; min-height: 180px;'>
                <h4>📊 Balanço Patrimonial</h4>
                <p style='font-size: 0.85rem;'>Fotografia em um momento</p>
                <hr>
                <p style='font-size: 0.8rem;'><strong>Ativo = Passivo + PL</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #dcfce7; padding: 15px; border-radius: 10px; text-align: center; min-height: 180px;'>
                <h4>📈 DRE</h4>
                <p style='font-size: 0.85rem;'>Performance no período</p>
                <hr>
                <p style='font-size: 0.8rem;'><strong>Receitas - Despesas = Lucro</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background-color: #fce7f3; padding: 15px; border-radius: 10px; text-align: center; min-height: 180px;'>
                <h4>💵 DFC</h4>
                <p style='font-size: 0.85rem;'>Movimentação de caixa</p>
                <hr>
                <p style='font-size: 0.8rem;'><strong>Entradas - Saídas = Variação</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### 🎯 Mapeie os Eventos nas Demonstrações")
    
    eventos = [
        {
            "id": 1,
            "titulo": "Venda a Prazo",
            "descricao": "Vendeu R$ 100.000 com prazo de 30 dias. CMV de R$ 60.000.",
            "bp": "↑ Clientes +R$ 100.000\n↓ Estoques -R$ 60.000\n↑ PL +R$ 40.000",
            "dre": "↑ Receita +R$ 100.000\n↑ CMV -R$ 60.000\n= Lucro Bruto +R$ 40.000",
            "dfc": "Sem impacto (não houve caixa)",
            "explicacao": "Gera receita por competência, mas só afeta caixa no recebimento."
        },
        {
            "id": 2,
            "titulo": "Financiamento Bancário",
            "descricao": "Empréstimo de R$ 500.000, prazo 3 anos, juros 12% a.a.",
            "bp": "↑ Caixa +R$ 500.000\n↑ Empréstimos +R$ 500.000",
            "dre": "Sem impacto imediato\n(juros ao longo do tempo)",
            "dfc": "↑ Entrada Financiamento +R$ 500.000",
            "explicacao": "Aumenta ativo e passivo igualmente. Juros só na DRE quando incorridos."
        },
        {
            "id": 3,
            "titulo": "Compra de Equipamento à Vista",
            "descricao": "Máquina por R$ 200.000, paga à vista.",
            "bp": "↑ Imobilizado +R$ 200.000\n↓ Caixa -R$ 200.000",
            "dre": "Sem impacto imediato\n(depreciação ao longo do tempo)",
            "dfc": "↓ Saída Investimento -R$ 200.000",
            "explicacao": "Troca de ativos no BP. Depreciação afetará DRE gradualmente."
        },
        {
            "id": 4,
            "titulo": "Pagamento de Salários",
            "descricao": "Pagou R$ 80.000 de salários do mês.",
            "bp": "↓ Caixa -R$ 80.000\n↓ Salários a Pagar -R$ 80.000",
            "dre": "Se provisionado: sem impacto\nSe não: Despesa -R$ 80.000",
            "dfc": "↓ Saída Operacional -R$ 80.000",
            "explicacao": "Despesa por competência, caixa quando pago."
        },
        {
            "id": 5,
            "titulo": "Recebimento de Cliente",
            "descricao": "Recebeu R$ 75.000 de venda do mês anterior.",
            "bp": "↑ Caixa +R$ 75.000\n↓ Clientes -R$ 75.000",
            "dre": "Sem impacto\n(receita já reconhecida)",
            "dfc": "↑ Entrada Operacional +R$ 75.000",
            "explicacao": "Conversão de ativo. Receita já estava na DRE."
        }
    ]
    
    evento_sel = st.selectbox(
        "Selecione um evento:",
        options=[f"{e['id']}. {e['titulo']}" for e in eventos],
        key="evento_guiado"
    )
    
    idx = int(evento_sel.split(".")[0]) - 1
    evento = eventos[idx]
    
    st.markdown(f"""
        <div style='background-color: #f0f9ff; padding: 15px; border-radius: 10px; margin: 15px 0;'>
            <strong>📋 {evento['titulo']}:</strong> {evento['descricao']}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### 🤔 Sua Análise")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text_area("Impacto no BP:", placeholder="Contas afetadas...", height=100, key=f"r_bp_{evento['id']}")
    with col2:
        st.text_area("Impacto na DRE:", placeholder="Receitas/despesas...", height=100, key=f"r_dre_{evento['id']}")
    with col3:
        st.text_area("Impacto na DFC:", placeholder="Entradas/saídas...", height=100, key=f"r_dfc_{evento['id']}")
    
    if st.button("📖 Ver Resposta", key=f"btn_{evento['id']}", type="primary"):
        st.markdown("##### ✅ Resposta Comentada")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""<div style='background-color: #dbeafe; padding: 15px; border-radius: 10px;'>
                <strong>📊 BP</strong><br><pre style='font-size: 0.8rem;'>{evento['bp']}</pre></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div style='background-color: #dcfce7; padding: 15px; border-radius: 10px;'>
                <strong>📈 DRE</strong><br><pre style='font-size: 0.8rem;'>{evento['dre']}</pre></div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<div style='background-color: #fce7f3; padding: 15px; border-radius: 10px;'>
                <strong>💵 DFC</strong><br><pre style='font-size: 0.8rem;'>{evento['dfc']}</pre></div>""", unsafe_allow_html=True)
        
        st.info(f"💡 {evento['explicacao']}")
    
    st.markdown("---")
    st.markdown("""
        <div style='background-color: #f0fdf4; padding: 15px; border-radius: 10px;'>
            <strong>💡 Dica:</strong> Lembre-se: <strong>Competência</strong> (DRE) reconhece quando ocorre; 
            <strong>Caixa</strong> (DFC) quando o dinheiro entra/sai.
        </div>
    """, unsafe_allow_html=True)


def renderizar_atividade_dupla():
    """Atividade em dupla sobre fatos em múltiplas demonstrações."""
    
    st.markdown("### 👥 Atividade em Dupla: Fatos em Múltiplas Demonstrações")
    
    st.markdown("""
        <div style='background-color: #e0e7ff; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #3b82f6; margin-bottom: 20px;'>
            <strong>Objetivo:</strong> Identificar como um mesmo fato aparece em várias demonstrações.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #fef3c7; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
            <strong>📋 Instruções:</strong>
            <ol>
                <li>Forme dupla com um colega</li>
                <li>Analisem os cenários apresentados</li>
                <li>Identifiquem TODAS as demonstrações afetadas</li>
                <li>Comparem com a resposta</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    cenarios = [
        {
            "id": 1,
            "titulo": "Depreciação de Equipamentos",
            "descricao": "Reconheceu R$ 25.000 de depreciação mensal.",
            "afetadas": ["BP", "DRE"],
            "bp": "↓ Imobilizado -R$ 25.000\n↓ PL -R$ 25.000",
            "dre": "↑ Despesa Depreciação -R$ 25.000",
            "dfc": "Não afeta (despesa não-caixa)",
            "conexao": "Depreciação: despesa na DRE, reduz ativo no BP, sem efeito no caixa."
        },
        {
            "id": 2,
            "titulo": "Distribuição de Dividendos",
            "descricao": "Pagou R$ 150.000 em dividendos.",
            "afetadas": ["BP", "DFC"],
            "bp": "↓ Caixa -R$ 150.000\n↓ PL -R$ 150.000",
            "dre": "Não afeta (não é despesa)",
            "dfc": "↓ Saída Financiamento -R$ 150.000",
            "conexao": "Dividendos: saem do PL, não passam pela DRE (são distribuição, não despesa)."
        },
        {
            "id": 3,
            "titulo": "Venda de Imobilizado com Lucro",
            "descricao": "Vendeu veículo por R$ 45.000 (valor contábil R$ 30.000).",
            "afetadas": ["BP", "DRE", "DFC"],
            "bp": "↑ Caixa +R$ 45.000\n↓ Imobilizado -R$ 30.000\n↑ PL +R$ 15.000",
            "dre": "↑ Ganho na venda +R$ 15.000",
            "dfc": "↑ Entrada Investimento +R$ 45.000",
            "conexao": "Aparece nas TRÊS: altera ativos (BP), gera resultado (DRE), entrada de caixa (DFC)."
        },
        {
            "id": 4,
            "titulo": "Provisão para Devedores Duvidosos",
            "descricao": "Constituiu PCLD de R$ 20.000.",
            "afetadas": ["BP", "DRE"],
            "bp": "↓ Clientes -R$ 20.000 (PCLD)\n↓ PL -R$ 20.000",
            "dre": "↑ Despesa PCLD -R$ 20.000",
            "dfc": "Não afeta (estimativa contábil)",
            "conexao": "PCLD: antecipa perdas como despesa, reduz recebíveis, sem caixa."
        }
    ]
    
    cenario_sel = st.selectbox(
        "Selecione o cenário:",
        options=[f"Cenário {c['id']}: {c['titulo']}" for c in cenarios],
        key="cenario_dupla"
    )
    
    idx = int(cenario_sel.split(":")[0].replace("Cenário ", "")) - 1
    cenario = cenarios[idx]
    
    st.markdown(f"""
        <div style='background-color: #ffffff; padding: 20px; border-radius: 10px; 
                    border: 2px solid #1e293b; margin: 15px 0;'>
            <h4>{cenario['titulo']}</h4>
            <p>{cenario['descricao']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### 📋 Quais demonstrações são afetadas?")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        check_bp = st.checkbox("📊 BP", key=f"c_bp_{cenario['id']}")
    with col2:
        check_dre = st.checkbox("📈 DRE", key=f"c_dre_{cenario['id']}")
    with col3:
        check_dfc = st.checkbox("💵 DFC", key=f"c_dfc_{cenario['id']}")
    with col4:
        check_dmpl = st.checkbox("📑 DMPL", key=f"c_dmpl_{cenario['id']}")
    
    discussao = st.text_area("💬 Discussão em dupla:", placeholder="Conclusões...", height=80, key=f"disc_{cenario['id']}")
    
    if st.button("✅ Verificar", key=f"btn_v_{cenario['id']}", type="primary"):
        respostas = []
        if check_bp: respostas.append("BP")
        if check_dre: respostas.append("DRE")
        if check_dfc: respostas.append("DFC")
        if check_dmpl: respostas.append("DMPL")
        
        corretas = set(cenario['afetadas'])
        usuario = set(respostas)
        
        if corretas == usuario:
            st.success("🎉 Correto!")
        elif corretas.issubset(usuario):
            st.warning("⚠️ Marcaram demonstrações a mais.")
        elif usuario.issubset(corretas) and len(usuario) > 0:
            st.warning("⚠️ Faltaram algumas.")
        else:
            st.error("❌ Revisem a análise.")
        
        st.markdown("##### 📖 Resposta:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            cor = "#dcfce7" if "BP" in cenario['afetadas'] else "#f3f4f6"
            st.markdown(f"""<div style='background-color: {cor}; padding: 15px; border-radius: 10px;'>
                <strong>📊 BP</strong><br><pre style='font-size: 0.8rem;'>{cenario['bp']}</pre></div>""", unsafe_allow_html=True)
        with col2:
            cor = "#dcfce7" if "DRE" in cenario['afetadas'] else "#f3f4f6"
            st.markdown(f"""<div style='background-color: {cor}; padding: 15px; border-radius: 10px;'>
                <strong>📈 DRE</strong><br><pre style='font-size: 0.8rem;'>{cenario['dre']}</pre></div>""", unsafe_allow_html=True)
        with col3:
            cor = "#dcfce7" if "DFC" in cenario['afetadas'] else "#f3f4f6"
            st.markdown(f"""<div style='background-color: {cor}; padding: 15px; border-radius: 10px;'>
                <strong>💵 DFC</strong><br><pre style='font-size: 0.8rem;'>{cenario['dfc']}</pre></div>""", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='background-color: #e0e7ff; padding: 15px; border-radius: 10px; margin-top: 15px;'>
                <strong>🔗 Conexão:</strong> {cenario['conexao']}
            </div>
        """, unsafe_allow_html=True)


def renderizar_exercicios_estruturais():
    """Lista de exercícios estruturais (entregável)."""
    
    st.markdown("### 📝 Lista de Exercícios Estruturais")
    
    st.markdown("""
        <div style='background-color: #fee2e2; padding: 20px; border-radius: 10px; 
                    border-left: 5px solid #dc2626; margin-bottom: 20px;'>
            <strong>📌 ENTREGÁVEL</strong><br>
            <em>Complete e entregue conforme orientação do professor.</em>
        </div>
    """, unsafe_allow_html=True)
    
    if 'respostas_m2' not in st.session_state:
        st.session_state.respostas_m2 = {}
    if 'verificado_m2' not in st.session_state:
        st.session_state.verificado_m2 = False
    
    st.markdown("---")
    
    # Exercício 1
    st.markdown("#### Exercício 1: Classificação de Contas")
    
    contas = [
        ("Fornecedores", "BP - Passivo Circulante"),
        ("Receita de Vendas", "DRE - Receita Operacional"),
        ("Máquinas e Equipamentos", "BP - Ativo Não Circulante (Imobilizado)"),
        ("Despesas com Salários", "DRE - Despesas Operacionais"),
        ("Capital Social", "BP - Patrimônio Líquido"),
        ("Pagamento a Fornecedores", "DFC - Atividades Operacionais (Saída)"),
    ]
    
    opcoes = [
        "Selecione...", "BP - Ativo Circulante", "BP - Ativo Não Circulante (Imobilizado)",
        "BP - Passivo Circulante", "BP - Passivo Não Circulante", "BP - Patrimônio Líquido",
        "DRE - Receita Operacional", "DRE - Custos", "DRE - Despesas Operacionais",
        "DFC - Atividades Operacionais (Entrada)", "DFC - Atividades Operacionais (Saída)",
        "DFC - Atividades de Investimento", "DFC - Atividades de Financiamento"
    ]
    
    for i, (conta, _) in enumerate(contas):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"**{conta}**")
        with col2:
            st.session_state.respostas_m2[f"ex1_{i}"] = st.selectbox(
                f"Class. {conta}", options=opcoes, key=f"ex1_{i}", label_visibility="collapsed"
            )
    
    st.markdown("---")
    
    # Exercício 2
    st.markdown("#### Exercício 2: Equação Patrimonial")
    st.markdown("Complete: **Ativo = R$ 500.000** | **PL = R$ 180.000** | **Passivo = ?**")
    
    passivo = st.number_input("Passivo Total (R$):", min_value=0, max_value=500000, value=0, step=10000, key="ex2_passivo")
    st.session_state.respostas_m2["ex2_passivo"] = passivo
    
    if passivo > 0:
        if passivo == 320000:
            st.success("✅ Correto! 500.000 = 320.000 + 180.000")
        else:
            st.warning("⚠️ Verifique: A = P + PL")
    
    st.markdown("---")
    
    # Exercício 3
    st.markdown("#### Exercício 3: Análise de Transação")
    st.markdown("**Compra de mercadorias a prazo: R$ 50.000**")
    
    st.session_state.respostas_m2["ex3_1"] = st.text_input("3.1 Qual conta do Ativo é afetada?", key="ex3_1")
    st.session_state.respostas_m2["ex3_2"] = st.text_input("3.2 Qual conta do Passivo é afetada?", key="ex3_2")
    st.session_state.respostas_m2["ex3_3"] = st.text_area("3.3 Afeta a DRE? Justifique.", height=60, key="ex3_3")
    st.session_state.respostas_m2["ex3_4"] = st.text_area("3.4 Afeta a DFC? Justifique.", height=60, key="ex3_4")
    
    st.markdown("---")
    
    # Exercício 4
    st.markdown("#### Exercício 4: Verdadeiro ou Falso")
    
    afirmacoes = [
        ("O BP demonstra posição financeira em um momento.", "V", "Correto. BP é uma fotografia."),
        ("Venda a prazo afeta imediatamente o caixa.", "F", "Falso. Gera contas a receber, não caixa."),
        ("Depreciação gera saída de caixa.", "F", "Falso. É despesa não-caixa."),
        ("Dividendos são despesa na DRE.", "F", "Falso. São distribuição de lucro."),
        ("Passivo + PL = Ativo.", "V", "Correto. Equação patrimonial."),
    ]
    
    for i, (texto, _, _) in enumerate(afirmacoes):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{i+1}.** {texto}")
        with col2:
            st.session_state.respostas_m2[f"ex4_{i}"] = st.radio(f"R{i+1}", ["V", "F"], horizontal=True, key=f"ex4_{i}", label_visibility="collapsed")
    
    st.markdown("---")
    
    # Exercício 5
    st.markdown("#### Exercício 5: Questão Dissertativa")
    st.markdown("**Por que é importante entender a conexão entre as demonstrações financeiras?**")
    st.session_state.respostas_m2["ex5"] = st.text_area("Sua resposta:", height=120, key="ex5")
    
    st.markdown("---")
    
    if st.button("📊 Verificar Respostas Objetivas", type="primary"):
        st.session_state.verificado_m2 = True
    
    if st.session_state.verificado_m2:
        st.markdown("### 📋 Gabarito")
        
        # Ex1
        st.markdown("#### Exercício 1:")
        acertos1 = 0
        for i, (conta, resp_correta) in enumerate(contas):
            resp = st.session_state.respostas_m2.get(f"ex1_{i}", "")
            if resp == resp_correta:
                st.success(f"✅ {conta}: {resp_correta}")
                acertos1 += 1
            else:
                st.error(f"❌ {conta}: Sua: {resp} | Correta: {resp_correta}")
        
        # Ex3
        st.markdown("#### Exercício 3 - Gabarito:")
        st.info("""
            **3.1** Estoques aumenta R$ 50.000
            **3.2** Fornecedores aumenta R$ 50.000
            **3.3** Não afeta a DRE (mercadoria ainda não vendida)
            **3.4** Não afeta a DFC (compra a prazo, sem saída de caixa)
        """)
        
        # Ex4
        st.markdown("#### Exercício 4:")
        acertos4 = 0
        for i, (texto, resp_correta, just) in enumerate(afirmacoes):
            resp = st.session_state.respostas_m2.get(f"ex4_{i}", "")
            if resp == resp_correta:
                st.success(f"✅ {i+1}. {resp_correta} - {just}")
                acertos4 += 1
            else:
                st.error(f"❌ {i+1}. Sua: {resp} | Correta: {resp_correta} - {just}")
        
        # Resumo
        total = len(contas) + 1 + len(afirmacoes)
        acertos = acertos1 + (1 if st.session_state.respostas_m2.get("ex2_passivo") == 320000 else 0) + acertos4
        pct = (acertos / total) * 100
        
        cor = "#dcfce7" if pct >= 70 else "#fef3c7" if pct >= 50 else "#fee2e2"
        msg = "🌟 Excelente!" if pct >= 80 else "👍 Bom trabalho!" if pct >= 60 else "📚 Revise o conteúdo."
        
        st.markdown(f"""
            <div style='background-color: {cor}; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;'>
                <h3>Resultado: {acertos}/{total} ({pct:.0f}%)</h3>
                <p>{msg}</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='background-color: #f0f9ff; padding: 15px; border-radius: 10px; margin-top: 15px;'>
                <strong>📝 Nota:</strong> Questões dissertativas serão avaliadas pelo professor.
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    run()