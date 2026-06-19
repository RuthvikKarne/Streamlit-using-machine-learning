<div align="center">
  <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit Logo" width="300" />
  <h1>Insurance Charge Predictor</h1>
  <p><b>A Machine Learning Web Application built with Streamlit and Scikit-Learn</b></p>
</div>

<hr>

<h2>🌟 Overview</h2>
<p>
  This repository contains a simple yet powerful <b>Machine Learning web application</b> developed using <b>Streamlit</b>. The app is designed to predict insurance charges based on user attributes like age and BMI using <b>Linear Regression</b> and <b>Multiple Regression</b> models.
</p>

<h2>🚀 Features</h2>
<ul>
  <li><b>Data Upload:</b> Allows users to dynamically upload their own CSV datasets (e.g., <code>insurance_cleaned.csv</code>) for training the model.</li>
  <li><b>Linear Regression:</b> Predicts the insurance charge based on a single independent variable:
    <ul>
      <li>Age</li>
      <li>BMI (Body Mass Index)</li>
    </ul>
  </li>
  <li><b>Multiple Regression:</b> Predicts the insurance charge using a combination of multiple independent variables (Age and BMI).</li>
  <li><b>Interactive UI:</b> Simple, intuitive, and interactive user interface powered by Streamlit.</li>
</ul>

<h2>🛠️ Technology Stack</h2>
<ul>
  <li><b>Frontend / UI:</b> <a href="https://streamlit.io/" target="_blank">Streamlit</a></li>
  <li><b>Data Manipulation:</b> <a href="https://pandas.pydata.org/" target="_blank">Pandas</a></li>
  <li><b>Machine Learning:</b> <a href="https://scikit-learn.org/" target="_blank">Scikit-Learn</a></li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
<code>
📦 Streamlit-using-machine-learning
 ┣ 📜 app.py                 # The main Streamlit application script
 ┣ 📜 insurance_cleaned.csv  # Sample dataset for testing the application
 ┣ 📜 requirements.txt       # List of Python dependencies
 ┗ 📜 README.md              # Project documentation
</code>
</pre>

<h2>⚙️ Installation & Setup</h2>
<p>Follow these steps to run the application locally on your machine:</p>

<ol>
  <li>
    <b>Clone the repository:</b>
    <pre><code>git clone https://github.com/your-username/Streamlit-using-machine-learning.git
cd Streamlit-using-machine-learning</code></pre>
  </li>
  <li>
    <b>Install the required dependencies:</b>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>
    <b>Run the Streamlit application:</b>
    <pre><code>streamlit run app.py</code></pre>
  </li>
</ol>

<h2>💡 How to Use</h2>
<ol>
  <li>Launch the app and wait for it to open in your browser.</li>
  <li>Upload the <code>insurance_cleaned.csv</code> file (or a similar dataset) using the file uploader widget.</li>
  <li>Choose the type of regression model you want to use from the dropdown menu (<b>Linear Regression</b> or <b>Multiple Regression</b>).</li>
  <li>Provide the required inputs (Age, BMI, or both) in the text fields.</li>
  <li>Click the <b>Predict Charge</b> button to view the predicted insurance charge based on the trained model.</li>
</ol>

<hr>
<div align="center">
  <p><i>Developed with ❤️ using Streamlit & Python</i></p>
</div>
