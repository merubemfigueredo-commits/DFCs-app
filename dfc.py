import streamlit as st
import pandas as pd
import io
from datetime import datetime

st.set_page_config(page_title="Fluxo de Caixa", page_icon="💰", layout="wide")
st.title("Demonstração do Fluxo de Caixa")
st.caption("Análise comparativa pelos métodos Direto e Indireto")

def fmt(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def gerar_excel_fluxo(tipo, dados):
    output = io.BytesIO()
    if tipo == "Direto":
        linhas = [
            ["ATIVIDADES OPERACIONAIS", ""],
            ["Recebimentos de Clientes", dados["rec_clientes"]],
            ["Pagamentos a Fornecedores", dados["pag_forn"]],
            ["Caixa Líquido das Ativ. Operacionais", dados["cx_op"]],
            ["", ""],
            ["ATIVIDADES DE INVESTIMENTO", ""],
            ["Caixa Líquido das Ativ. de Investimento", dados["cx_inv"]],
            ["", ""],
            ["ATIVIDADES DE FINANCIAMENTO", ""],
            ["Caixa Líquido das Ativ. de Financiamento", dados["cx_fin"]],
            ["", ""],
            [f"VARIAÇÃO LÍQUIDA DE CAIXA", dados["variacao"]],
        ]
    else:
        linhas = [
            ["ATIVIDADES OPERACIONAIS", ""],
            ["Lucro Líquido do Exercício", dados["lucro"]],
            ["Depreciação e Amortização", dados["deprec"]],
            ["Caixa Líquido das Ativ. Operacionais", dados["cx_op2"]],
            ["", ""],
            [f"VARIAÇÃO LÍQUIDA DE CAIXA", dados["variacao2"]],
        ]

    df = pd.DataFrame(linhas, columns=["Descrição", "Valor"])
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=f"Fluxo {tipo}", index=False, startrow=2)
        worksheet = writer.sheets[f"Fluxo {tipo}"]
        worksheet.cell(row=1, column=1, value=f"Fluxo de Caixa - Método {tipo}")
    return output.getvalue()

# A LINHA ESTÁ AQUI EMBAIXO 👇
tab1, tab2 = st.tabs(["Método Direto", "Método Indireto"])

with tab1:
    st.header("Método Direto")
    col1, col2 = st.columns(2)
    with col1:
        rec_clientes = st.number_input("Recebimentos de Clientes", value=0.0)
        pag_forn = st.number_input("Pagamentos a Fornecedores", value=0.0)
    with col2:
        compra_ativ = st.number_input("Compra de Ativos", value=0.0)
        emp_obtidos = st.number_input("Empréstimos Obtidos", value=0.0)
    
    cx_op = rec_clientes - pag_forn
    cx_inv = -compra_ativ
    cx_fin = emp_obtidos
    variacao = cx_op + cx_inv + cx_fin
    
    st.metric("Variação Líquida de Caixa", fmt(variacao))

    dados_direto = locals() # TEM QUE ESTAR DENTRO DO with tab1
    excel_bytes = gerar_excel_fluxo("Direto", dados_direto)
    st.download_button("⬇️ Baixar Excel Direto", data=excel_bytes, file_name="fluxo_direto.xlsx")

with tab2:
    st.header("Método Indireto")
    lucro = st.number_input("Lucro Líquido", value=0.0)
    deprec = st.number_input("Depreciação", value=0.0)
    
    cx_op2 = lucro + deprec
    variacao2 = cx_op2
    
    st.metric("Variação Líquida de Caixa", fmt(variacao2))

    dados_indireto = locals() # TEM QUE ESTAR DENTRO DO with tab2
    excel_bytes = gerar_excel_fluxo("Indireto", dados_indireto)
    st.download_button("⬇️ Baixar Excel Indireto", data=excel_bytes, file_name="fluxo_indireto.xlsx")
