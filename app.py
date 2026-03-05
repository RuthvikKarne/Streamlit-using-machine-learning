import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Insurance Clearance Data")

uploaded_file = st.file_uploader("Upload a file", type="csv")

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    option = st.selectbox(
        "Choose an option",
        ["Linear Regression", "Multiple Regression"]
    )

    if option == "Linear Regression":

        columnselector = st.radio(
            "Select column",
            ["age", "bmi"]
        )

        if columnselector == "age":
            age_input = st.text_input("Enter age")

            if st.button("Predict Age Charge"):
                if age_input != "":
                    age = float(age_input)

                    X = data[['age']]
                    Y = data['charges']

                    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

                    model = LinearRegression()
                    model.fit(X_train, Y_train)

                    prediction = model.predict(pd.DataFrame({'age':[age]}))

                    st.write("Predicted Insurance Charge:", prediction[0])

        if columnselector == "bmi":
            bmi_input = st.text_input("Enter bmi")

            if st.button("Predict BMI Charge"):
                if bmi_input != "":
                    bmi = float(bmi_input)

                    X = data[['bmi']]
                    Y = data['charges']

                    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

                    model = LinearRegression()
                    model.fit(X_train, Y_train)

                    prediction = model.predict(pd.DataFrame({'bmi':[bmi]}))

                    st.write("Predicted Insurance Charge:", prediction[0])

    if option == "Multiple Regression":

        age_input = st.text_input("Enter age")
        bmi_input = st.text_input("Enter bmi")

        if st.button("Predict Charge"):
            if age_input != "" and bmi_input != "":
                age = float(age_input)
                bmi = float(bmi_input)

                X = data[['age','bmi']]
                Y = data['charges']

                X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

                model = LinearRegression()
                model.fit(X_train, Y_train)

                prediction = model.predict(pd.DataFrame({'age':[age], 'bmi':[bmi]}))

                st.write("Predicted Insurance Charge:", prediction[0])
