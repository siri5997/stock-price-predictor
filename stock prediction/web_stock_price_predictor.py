import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Add a logo and text side by side
col1, col2 = st.columns([1, 5])  # Adjust column width proportions
with col1:
    st.image(r"C:\Users\Shirisha S\OneDrive\Pictures\logo.png", width=100)  # Adjust logo size
with col2:
    st.markdown(
        """
        <div style='display: flex; align-items: center; font-size: 24px;'>
            DAYANANDA SAGAR ACADEMY OF TECHNOLOGY AND MANAGEMENT (Autonomous under VTU)
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style='display: flex; align-items: center; font-size: 16px;'>
             Opp. to Art of Living International Centre, Kanakpura Road, Udaypura Bangalore-560082
        </div>
        """,
        unsafe_allow_html=True,
    )

# Title for the app
st.title("Stock Price Predictor App")

# Input for stock ID
stock = st.text_input("Enter the Stock ID", "GOOG")

# Fetch stock data
end = datetime.now()
start = datetime(end.year - 20, end.month, end.day)
google_data = yf.download(stock, start, end)

# Load pre-trained model
model = load_model("Latest_stock_price_model.keras")

# Display stock data
st.subheader("Stock Data")
st.write(google_data)

# Split data for testing
splitting_len = int(len(google_data) * 0.7)
x_test = pd.DataFrame(google_data.Close[splitting_len:])
actual_data = google_data.Close[splitting_len:]

# Simulate predicted values as a placeholder (replace this with your model's actual predictions)
# For demonstration, we'll scale the actual data slightly to create dummy predicted values.
predicted_data = actual_data * 1.05  # Example: Predicted values are 5% higher than actual

# Define the plot function
def plot_graph(figsize, predicted_values, actual_values):
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(actual_values.index, actual_values, color='blue', label='Actual', linewidth=2)  # Actual data
    ax.plot(predicted_values.index, predicted_values, color='orange', label='Predicted', linewidth=2)  # Predicted data
    ax.set_xlabel('Date')
    ax.set_ylabel('Stock Price')
    ax.set_title('Stock Price Prediction vs Actual')
    ax.legend(loc='upper left')
    return fig

# Create and display the graph
fig = plot_graph(figsize=(10, 5), predicted_values=predicted_data, actual_values=actual_data)
st.pyplot(fig)
