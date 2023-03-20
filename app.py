from joblib import dump, load
import streamlit as st
import pandas as pd

modelo = load("model_kc_house.pkl")

def main():
    st.sidebar.image("casa.png")
    st.sidebar.markdown("[Meu LinkedIn](https://www.linkedin.com/in/bruno-cipriano-minhaqui-da-silva-90b4254a/)")

    st.title("App para realizar previsão de preço de casa")

    st.markdown("""
    ### Descrição Variáveis
    - bedrooms - Número de quartos.
    - bathrooms - Número de banheiros, no qual .5 conta como lavabo.
    - floors - Número de andares.
    - waterfront - Tem vista para o mar (1) ou não (0). (categórico)
    - view - Valor de 0 a 4 informando se a vista é boa. (categórico)
    - condition - Valor de 1 a 5 sobre a condição da casa. (categórico)
    - grade - Nota de 1 a 13, no qual 1-3 pequenas construções, 7 construção e desing mediano, e 11-13 para construções de alto nível.
    - yr_built - Ano de construção da casa.
    """)

    quartos = st.number_input("Número de quartos", min_value=1)
    banheiros = st.number_input("Total banheiros", min_value=1)
    andares = st.number_input("Total de andares", min_value=1)
    
    if st.checkbox("Vista para o mar"):
        vista_mar = 1
    else:
        vista_mar = 0
    
    vista_casa = st.selectbox("A vista da casa é boa?", [0,1,2,3,4])
    condicao = st.selectbox("Qual a condição da casa?", [1,2,3,4,5])
    grade = st.selectbox("Qual é o tamanho (grade) da casa?", [1,2,3,4,5,6,7,8,9,10,11,12,13])
    ano = st.number_input("Qual é o ano de construção da casa?", min_value=1)

    output = ''

    input_dict = {"bedrooms":quartos, "bathrooms":banheiros, 
                  "floors":andares, "waterfront":vista_mar, 
                  "view":vista_casa, "condition":condicao, 
                  "grade":grade, "yr_built":ano}
    
    input_df = pd.DataFrame([input_dict])
    
    if st.button("Realizar Previsão"):
        output = modelo.predict(input_df)
        output = "$" + str(output[0])

    st.success(f"A previsão do preço da casa é {output}")


if __name__ == "__main__":
    main()