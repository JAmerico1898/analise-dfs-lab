Laboratório de Análise de Demonstrações Financeiras ⚖️

Bem-vindo ao repositório oficial do Laboratório de Análise de Demonstrações Financeiras. Este projeto foi desenvolvido para servir como uma ferramenta pedagógica interativa, acompanhando as 15 aulas de um curso de graduação focado em transformar dados contábeis em inteligência estratégica.

📌 Visão Geral do Projeto

O laboratório utiliza uma arquitetura modular baseada em Streamlit. O objetivo é permitir que alunos sem experiência prévia possam "tocar" nos números, simular cenários e desenvolver um olhar crítico sobre a saúde financeira das empresas.

Identidade Visual

O projeto segue o padrão "Boutique Acadêmica", utilizando uma paleta de cores sofisticada em Azul Marinho (Navy) e Dourado (Gold), garantindo uma experiência de usuário profissional e organizada no Canvas.

🏗️ Arquitetura do Sistema

O aplicativo é composto por um núcleo central e 15 módulos independentes:

main_hub.py: O cérebro do laboratório. Gerencia a navegação, injeta o CSS global e carrega dinamicamente os módulos de aula.

modulo[X]_laboratorio.py: Arquivos independentes que contêm a lógica específica de cada aula (X = 1 a 15).

Estrutura de Arquivos Recomendada:

/projeto-laboratorio
│
├── main_hub.py               # Executar este arquivo
├── modulo1_laboratorio.py
├── modulo2_laboratorio.py
...
└── modulo15_laboratorio.py


📚 Mapa de Módulos (Conteúdo Programático)

Módulo

Título

Foco Pedagógico

01

Introdução à Análise

Usuários da informação e papel da contabilidade.

02

Estrutura e Lógica

Mecânica contábil e interconectividade (A = P + PL).

03

Princípios e Qualidade

Regime de competência e fidedignidade da informação.

04

Interpretação do Balanço

Ativos, passivos e capital de giro inicial.

05

Performance na DRE

Formação do lucro e análise de margens.

06

Fluxo de Caixa (DFC)

Reconciliação do lucro com o caixa real (Método Indireto).

07

Análise Vertical e Horizontal

Tendências temporais e mudanças estruturais.

08

Liquidez e Giro

Ciclo operacional, ciclo financeiro e solvência CP.

09

Endividamento

Estrutura de capital e alavancagem financeira.

10

Rentabilidade (ROE/ROA)

Retorno sobre investimento e custo de oportunidade.

11

Modelo DuPont

Decomposição do ROE em Margem, Giro e Alavancagem.

12

Benchmarking

Comparação setorial e limites da análise.

13

Sinais de Alerta

Red flags, qualidade do lucro e manobras contábeis.

14

Tomada de Decisão

Comitê de crédito vs. Comitê de investimento.

15

Estudo de Caso Final

Análise integrada e parecer técnico final.

🚀 Como Executar

Pré-requisitos:

Python 3.8 ou superior instalado.

Bibliotecas necessárias: streamlit e pandas.

Instalação:

pip install streamlit pandas


Execução:
Salve todos os arquivos na mesma pasta e execute o comando abaixo no terminal:

streamlit run main_hub.py


🎓 Metodologia Pedagógica

Cada módulo no Canvas é estruturado em três pilares:

Discussão Orientada: Provocações teóricas para debate em sala.

Laboratório Numérico: Simuladores onde o aluno manipula variáveis e vê o impacto nos indicadores em tempo real.

Avaliação Formativa: Quizzes e exercícios discursivos com feedback imediato para fixação.

Professor Responsável: Especialista em Análise Financeira e Contabilidade.

Este material é destinado exclusivamente para fins educacionais.