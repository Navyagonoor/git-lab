import streamlit as st

# Set title
st.title("🧮 Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")

# Choose operation
operation = st.selectbox("Choose Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result is: {result:.2f}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result is: {result:.2f}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result is: {result:.2f}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result:.2f}")
        else:
            st.error("Division by zero is not allowed!")

# Footer
st.caption("Built with ❤️ using Streamlit")
