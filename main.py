import streamlit as st

#criar a barra lateral
with st.sidebar:
    st.title("Calculadora IMC")

    st.header("O que é IMC")
    st.markdown("IMC é uma sigla para: índice de massa corporal, com ele você calcula o seu peso de uma forma mais detalhada")

    #linha com texto
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5
    - **Peso ideal**: IMC entre 18.5 e 24.9
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade mórbida**: IMC acima de 40          
    """)


st.title("Calculadora IMC")

#entrada de dados - peso
peso = st.number_input(label="Digite o seu peso (Kg)", min_value=0.0, step=0.10, format="%.1f")
altura = st.number_input(label="Digite a sua altura(Metros)", min_value=0.0, step=0.10, format="%.2f")

if st.button("Calcular"):
    if peso > 0 and altura > 0:
        imc = peso / (altura **2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal

        if imc < 18.5:
            classe = "Abaixo do peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29.0:
            classe = "Sobrepreso"
        elif imc < 39.0:
            classe = "Obesidade"
        else:
            classe = "Obesidade Mórbida"

        st.success("Cálculo realizado com sucesso")

        #escrever os valores
        st.write(f"o seu IMC é {imc:.2f}")
        st.write(f"classificação {classe}")
        st.write(f"comparação com o IMC ideal (21.7): ***{imc_delta:.2f}***")

        #dividir a linha em colunas
        col1, col2 = st.columns(2)

        col1.metric("Classificação", classe, f"{imc_delta:.2f}", delta_color="inverse")

        col2.metric("IMC", f"{imc:.2f})", f"{imc_delta:.2f}", delta_color="off")
        #criar uma linha
        st.divider()
        st.image("./imc.jpg")
else:
        #mostrar mensagem de erro
        st.error("por favor, insira valores válidos para o peso e altura")