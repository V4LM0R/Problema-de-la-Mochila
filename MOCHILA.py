import streamlit as st
import time

def knapsack(weights, capacity):
    weights.sort(reverse=True)  # Ordenar los pesos en orden descendente
    bags = []
    while weights:
        current_bag = []
        remaining_capacity = capacity
        for weight in weights[:]:
            if weight <= remaining_capacity:
                current_bag.append(weight)
                remaining_capacity -= weight
                weights.remove(weight)
        bags.append(current_bag)
    return bags

st.title("Gestión de Mochilas")

capacity = st.number_input("Capacidad de la Mochila", min_value=1)
num_objects = st.number_input("Número de Objetos", min_value=1, step=1)

weights = []
for i in range(num_objects):
    weight = st.number_input(f"Peso del Objeto {i + 1}", min_value=1)
    weights.append(weight)

if st.button("Agrupar en Mochilas"):
    start_time = time.time()  # Inicio del temporizador
    if len(weights) == num_objects:
        # Inicio del cálculo (tiempo de ida)
        calculation_start_time = time.time()
        bags = knapsack(weights, capacity)
        # Fin del cálculo (tiempo de vuelta)
        calculation_end_time = time.time()
        execution_time = calculation_end_time - calculation_start_time  # Tiempo del cálculo
        response_time = time.time() - calculation_end_time  # Tiempo de vuelta
        for i, bag in enumerate(bags):
            st.write(f"Mochila {i + 1}: {bag}")
        st.write(f"Tiempo de ida: {execution_time:.6f} segundos")
        st.write(f"Tiempo de vuelta: {response_time:.6f} segundos")
    else:
        st.error("Asegúrate de ingresar el peso para cada objeto.")
