import streamlit as st

st.set_page_config(
    page_title="Fluxo de Caixa",
    page_icon="💰",
    layout="wide"
)

st.title("Demonstração do Fluxo de Caixa")
st.caption("Análise comparativa pelos métodos Direto e Indireto")

aba_direto, aba_indireto = st.tabs(["Método Direto", "Método Indireto"])

# ─────────────────────────────────────────────
# MÉTODO DIRETO
# ─────────────────────────────────────────────
with aba_direto:
    col_inputs, col_demo = st.columns([1, 1])

    with col_inputs:
        st.subheader("🔵 Atividades Operacionais — Entradas")
        rec_clientes   = st.number_input("Recebimentos de Clientes",        value=850_000.0, step=1000.0, key="d_rec_cli")
        rec_juros      = st.number_input("Recebimento de Juros/Dividendos", value=12_000.0,  step=1000.0, key="d_rec_jur")
        outros_rec     = st.number_input("Outros Recebimentos",             value=8_000.0,   step=1000.0, key="d_outros_rec")

        st.subheader("🔴 Atividades Operacionais — Saídas")
        pag_forn   = st.number_input("Pagamentos a Fornecedores", value=-420_000.0, step=1000.0, key="d_forn")
        pag_sal    = st.number_input("Pagamentos de Salários",    value=-180_000.0, step=1000.0, key="d_sal")
        pag_imp    = st.number_input("Pagamentos de Impostos",    value=-65_000.0,  step=1000.0, key="d_imp")
        pag_alug   = st.number_input("Pagamentos de Aluguéis",    value=-36_000.0,  step=1000.0, key="d_alug")
        pag_serv   = st.number_input("Pagamentos de Serviços",    value=-24_000.0,  step=1000.0, key="d_serv")
        outros_pag = st.number_input("Outros Pagamentos",         value=-15_000.0,  step=1000.0, key="d_outros_pag")

        st.subheader("🟣 Atividades de Investimento")
        compra_ativ  = st.number_input("Aquisição de Ativos Imobilizados", value=-120_000.0, step=1000.0, key="d_compra")
        venda_ativ   = st.number_input("Venda de Ativos Imobilizados",     value=45_000.0,   step=1000.0, key="d_venda")
        aplic_fin    = st.number_input("Aplicações Financeiras",           value=-80_000.0,  step=1000.0, key="d_aplic")
        resg_fin     = st.number_input("Resgates de Aplicações",           value=60_000.0,   step=1000.0, key="d_resg")

        st.subheader("🟠 Atividades de Financiamento")
        emp_obtidos  = st.number_input("Empréstimos Obtidos",         value=200_000.0,  step=1000.0, key="d_emp")
        amort_emp    = st.number_input("Amortização de Empréstimos",  value=-150_000.0, step=1000.0, key="d_amort")
        pag_div      = st.number_input("Pagamento de Dividendos",     value=-50_000.0,  step=1000.0, key="d_div")

    # Cálculos
    cx_op  = rec_clientes + rec_juros + outros_rec + pag_forn + pag_sal + pag_imp + pag_alug + pag_serv + outros_pag
    cx_inv = compra_ativ + venda_ativ + aplic_fin + resg_fin
    cx_fin = emp_obtidos + amort_emp + pag_div
    variacao = cx_op + cx_inv + cx_fin

    def fmt(v):
        return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    with col_demo:
        st.subheader("📄 Demonstrativo — Método Direto")
        st.divider()

        st.markdown("**ATIVIDADES OPERACIONAIS**")
        st.write(f"Recebimentos de Clientes: **{fmt(rec_clientes)}**")
        st.write(f"Recebimento de Juros/Dividendos: **{fmt(rec_juros)}**")
        st.write(f"Outros Recebimentos: **{fmt(outros_rec)}**")
        st.write(f"Pagamentos a Fornecedores: **{fmt(pag_forn)}**")
        st.write(f"Pagamentos de Salários: **{fmt(pag_sal)}**")
        st.write(f"Pagamentos de Impostos: **{fmt(pag_imp)}**")
        st.write(f"Pagamentos de Aluguéis: **{fmt(pag_alug)}**")
        st.write(f"Pagamentos de Serviços: **{fmt(pag_serv)}**")
        st.write(f"Outros Pagamentos: **{fmt(outros_pag)}**")
        cor_op = "green" if cx_op >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. Operacionais: :{cor_op}[{fmt(cx_op)}]**")
        st.divider()

        st.markdown("**ATIVIDADES DE INVESTIMENTO**")
        st.write(f"Aquisição de Ativos Imobilizados: **{fmt(compra_ativ)}**")
        st.write(f"Venda de Ativos Imobilizados: **{fmt(venda_ativ)}**")
        st.write(f"Aplicações Financeiras: **{fmt(aplic_fin)}**")
        st.write(f"Resgates de Aplicações: **{fmt(resg_fin)}**")
        cor_inv = "green" if cx_inv >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. de Investimento: :{cor_inv}[{fmt(cx_inv)}]**")
        st.divider()

        st.markdown("**ATIVIDADES DE FINANCIAMENTO**")
        st.write(f"Empréstimos Obtidos: **{fmt(emp_obtidos)}**")
        st.write(f"Amortização de Empréstimos: **{fmt(amort_emp)}**")
        st.write(f"Pagamento de Dividendos: **{fmt(pag_div)}**")
        cor_fin = "green" if cx_fin >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. de Financiamento: :{cor_fin}[{fmt(cx_fin)}]**")
        st.divider()

        cor_var = "green" if variacao >= 0 else "red"
        st.markdown(f"## Variação Líquida de Caixa: :{cor_var}[{fmt(variacao)}]")


# ─────────────────────────────────────────────
# MÉTODO INDIRETO
# ─────────────────────────────────────────────
with aba_indireto:
    col_inputs, col_demo = st.columns([1, 1])

    with col_inputs:
        st.subheader("🔵 Lucro Líquido do Exercício")
        lucro = st.number_input("Lucro Líquido", value=180_000.0, step=1000.0, key="i_lucro")

        st.subheader("🔵 Ajustes — Itens sem Efeito Caixa")
        deprec    = st.number_input("Depreciação e Amortização",      value=45_000.0, step=1000.0, key="i_dep")
        amort_int = st.number_input("Amortização de Intangíveis",     value=12_000.0, step=1000.0, key="i_amort_int")
        perda_at  = st.number_input("Perda na Venda de Ativos",       value=-8_000.0, step=1000.0, key="i_perda")
        ganho_at  = st.number_input("Ganho na Venda de Ativos",       value=15_000.0, step=1000.0, key="i_ganho")

        st.subheader("🔵 Variações no Capital de Giro")
        var_cr    = st.number_input("Variação em Contas a Receber",          value=-32_000.0, step=1000.0, key="i_cr")
        var_est   = st.number_input("Variação em Estoques",                  value=18_000.0,  step=1000.0, key="i_est")
        var_oac   = st.number_input("Variação em Outros Ativos Circulantes", value=-5_000.0,  step=1000.0, key="i_oac")
        var_forn  = st.number_input("Variação em Fornecedores",              value=24_000.0,  step=1000.0, key="i_forn")
        var_sal   = st.number_input("Variação em Salários a Pagar",          value=-10_000.0, step=1000.0, key="i_sal")
        var_imp   = st.number_input("Variação em Impostos a Pagar",          value=8_000.0,   step=1000.0, key="i_imp")
        var_opc   = st.number_input("Variação em Outros Passivos Circulantes", value=12_000.0, step=1000.0, key="i_opc")

        st.subheader("🟣 Atividades de Investimento")
        compra2   = st.number_input("Aquisição de Ativos Imobilizados", value=-120_000.0, step=1000.0, key="i_compra")
        venda2    = st.number_input("Venda de Ativos Imobilizados",     value=45_000.0,   step=1000.0, key="i_venda")
        aplic2    = st.number_input("Aplicações Financeiras",           value=-80_000.0,  step=1000.0, key="i_aplic")
        resg2     = st.number_input("Resgates de Aplicações",           value=60_000.0,   step=1000.0, key="i_resg")

        st.subheader("🟠 Atividades de Financiamento")
        emp2      = st.number_input("Empréstimos Obtidos",        value=200_000.0,  step=1000.0, key="i_emp")
        amort2    = st.number_input("Amortização de Empréstimos", value=-150_000.0, step=1000.0, key="i_amort")
        div2      = st.number_input("Pagamento de Dividendos",    value=-50_000.0,  step=1000.0, key="i_div")

    # Cálculos
    ajustes_nc  = deprec + amort_int + perda_at + ganho_at
    var_capgiro = var_cr + var_est + var_oac + var_forn + var_sal + var_imp + var_opc
    cx_op2      = lucro + ajustes_nc + var_capgiro
    cx_inv2     = compra2 + venda2 + aplic2 + resg2
    cx_fin2     = emp2 + amort2 + div2
    variacao2   = cx_op2 + cx_inv2 + cx_fin2

    with col_demo:
        st.subheader("📄 Demonstrativo — Método Indireto")
        st.divider()

        st.markdown("**ATIVIDADES OPERACIONAIS**")
        st.write(f"Lucro Líquido do Exercício: **{fmt(lucro)}**")
        st.markdown("*Ajustes por itens sem efeito caixa:*")
        st.write(f"  Depreciação e Amortização: **{fmt(deprec)}**")
        st.write(f"  Amortização de Intangíveis: **{fmt(amort_int)}**")
        st.write(f"  Perda na Venda de Ativos: **{fmt(perda_at)}**")
        st.write(f"  Ganho na Venda de Ativos: **{fmt(ganho_at)}**")
        st.markdown("*Variações no capital de giro:*")
        st.write(f"  Contas a Receber: **{fmt(var_cr)}**")
        st.write(f"  Estoques: **{fmt(var_est)}**")
        st.write(f"  Outros Ativos Circulantes: **{fmt(var_oac)}**")
        st.write(f"  Fornecedores: **{fmt(var_forn)}**")
        st.write(f"  Salários a Pagar: **{fmt(var_sal)}**")
        st.write(f"  Impostos a Pagar: **{fmt(var_imp)}**")
        st.write(f"  Outros Passivos Circulantes: **{fmt(var_opc)}**")
        cor_op2 = "green" if cx_op2 >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. Operacionais: :{cor_op2}[{fmt(cx_op2)}]**")
        st.divider()

        st.markdown("**ATIVIDADES DE INVESTIMENTO**")
        st.write(f"Aquisição de Ativos Imobilizados: **{fmt(compra2)}**")
        st.write(f"Venda de Ativos Imobilizados: **{fmt(venda2)}**")
        st.write(f"Aplicações Financeiras: **{fmt(aplic2)}**")
        st.write(f"Resgates de Aplicações: **{fmt(resg2)}**")
        cor_inv2 = "green" if cx_inv2 >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. de Investimento: :{cor_inv2}[{fmt(cx_inv2)}]**")
        st.divider()

        st.markdown("**ATIVIDADES DE FINANCIAMENTO**")
        st.write(f"Empréstimos Obtidos: **{fmt(emp2)}**")
        st.write(f"Amortização de Empréstimos: **{fmt(amort2)}**")
        st.write(f"Pagamento de Dividendos: **{fmt(div2)}**")
        cor_fin2 = "green" if cx_fin2 >= 0 else "red"
        st.markdown(f"**Caixa Líquido das Ativ. de Financiamento: :{cor_fin2}[{fmt(cx_fin2)}]**")
        st.divider()

        cor_var2 = "green" if variacao2 >= 0 else "red"
        st.markdown(f"## Variação Líquida de Caixa: :{cor_var2}[{fmt(variacao2)}]")
