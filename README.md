Stock Price Predictor App
A simple, interactive web app to predict and visualise stock prices using AI. Built with Streamlit,
TensorFlow/Keras, and yFinance, this project allows users to enter any stock ticker and view its
historical data alongside predicted price trends.
Features
- Fetches 20 years of historical stock data automatically using yfinance.
- Loads a pre-trained AI model for price predictions.
- Visual comparison between actual and predicted stock prices.
- Clean, user-friendly interface built using Streamlit.
- Graphs generated with Matplotlib for clarity.
Tech Stack
- Python (Pandas, NumPy)
- Streamlit (for interactive web app)
- TensorFlow / Keras (for AI model loading)
- yFinance (for fetching live stock data)
- Matplotlib (for plotting)
How it works
1. User enters a stock ticker (e.g., GOOG, AAPL, TSLA).
2. The app downloads the stock's historical data from Yahoo Finance.
3. Loads a pre-trained LSTM/AI model to predict future stock prices.
4. Displays the raw data and graphical comparison between predicted and actual prices.
Getting Started
1. Clone this repository:
 git clone https://github.com/siri5997/stock-price-predictor.git
 cd stock-price-predictor
2. Install dependencies:
 pip install -r requirements.txt
3. Ensure you have your Latest_stock_price_model.keras in the project folder.
4. Run the app:
 streamlit run web_stock_price_predictor.py
Future Improvements
- Use real model predictions instead of placeholder scaling for demo.
- Add multi-stock comparison and date-range filtering.
- Deploy on Streamlit Cloud for live demo.
License
This project is open source under the MIT License.
Acknowledgements
- Dayananda Sagar Academy of Technology and Management for guidance.
- All open-source libraries used to make this project possible.
