# Passo a passo do projeto
# Componentes e funcionalidades da sistema:
    # titulo - Sistema de Vendas
    # seção: Cadastrar vendas
        # campo: data
        # campo: vendedor [Ana, Bruno, Carla]
        # Produto [Notebook, Celular, Fone]
        # Quantidade
        # Valor
        # Botão Cadastrar Venda
            # Quando clicar no botão a venda deve ser adicionada na tabela de vendas cadastradas
            # Dashboard deve ser atualizado para refletir a venda cadastrada
    # seção: Vendas cadastradas
        # Tabela com as vendas cadastradas
    # seção: Dashboard
        # Card/Métrica -> Faturamento Total
        # Gráfico de Barras com as vendas por vendedor
        # Gráfico de Pizza com a participação de cada produto nas vendas

#
# *** Start here ***
#
# Import the required libraries
import streamlit as st
import pandas as pd
import plotly.express as px

#
# Carregar base de dados
tabela_vendas = pd.read_csv("vendas.csv")

#
# Exibe o titulo da pagina
st.write("# Sistema de Vendas DMPSO")

#
# Sessão: Cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data da Venda")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla", "Delmário"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# Logica de cadastro
if botao_cadastrar:
    if valor == 0 or quantidade == 0 or vendedor == "":
	    st.sidebar.warning("Erro no preenchimento")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade , valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.sidebar.success("Venda cadastrada!")


#
# Sessão: Visualizar vendas cadastradas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# Sessão: Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()

st.metric("Faturamento Total", f"R$ {faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), border = True, format = "localized")


# Gráfico de Barras com as vendas por vendedor
# Cria o gráfico
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color ="produto")

# Exibe o gráfico
st.plotly_chart(grafico1)

# Gráfico de Pizza com a participação de cada produto nas vendas
# Cria o gráfico
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.3)

# Exibe o gráfico
st.plotly_chart(grafico2)


#grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
#st.plotly_chart(grafico2)
