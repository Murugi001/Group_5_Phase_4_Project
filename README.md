# PROJECT OVERVIEW
# FROM TWEETS TO STRATEGY: PREDICTING SENTIMENT AND SHARING CUSTOMER ENGAGEMENT  

## 📌 Business Understanding
In the current digital landscape, social media platforms such as **X (Formerly Twitter)**  have become powerful spaces where consumers express their opinions, experiences, and perceptions about brands and products. These online conversations offer organizations a valuable opportunity to measure customer sentiment, evaluate brand perception, and shape strategies that drive competitive advantage. 
The project, “From Tweets to Strategy: Predicting Sentiment and Shaping Customer Engagement,” is motivated by the need for businesses to translate unstructured social media data into actionable insights.  

---

## 🎯 Business Objectives  
1. Analyze customer perception of **Apple** and **Google** brands, including their products and services.  
2. Build a predictive model that classifies the sentiment of tweets.  
3. Provide actionable insights to:  
   - Shape marketing campaigns  
   - Improve customer service  
   - Strengthen engagement strategies  

---

## 👥 Target Audience  
- **Marketing Teams** (Apple & Google) → Design campaigns that amplify positive sentiment.  
- **Customer Engagement & Experience Managers** → Strengthen relationships and improve satisfaction.  
- **Product Managers** (iPhone, Pixel, Android, iOS) → Align features with consumer expectations revealed in sentiment analysis.  
- **Competitive Strategy Analysts** → Benchmark brand perception across categories and identify opportunities for competitve advantage.  
- **Executives & Senior Leadership** → Use sentiment-driven insights for strategic planning, market positioning and long term brand growth.  

---

## 📂Data Understanding
- The dataset used in this project was sourced from Data World and contributed by Kent Cavender-Bares on August 30, 2013. It consists of 9,093 entries containing crowd-sourced sentiment assessments of tweets mentioning different brands and products. Each record includes the original tweet, a sentiment label (positive, negative, or neutral), and, when relevant, the specific brand or product associated with the sentiment. Annotators evaluated not only whether a sentiment was present but also its intended target, making this dataset a valuable resource for studying public perception, brand engagement, and emotional tone on social media.

---

## 📂 Data Preprocessing  
Missing Values; Filled missing product references with a placeholder token ("No_Target") & Dropped rows with empty tweets or missing sentiment labels
Categorical Standardization; Unified sentiment labels into three categories: positive, negative, neutral 
Text Cleaning; Converted all tweet text to lowercase & Removed URLs, mentions (@user), hashtags, numbers, and special characters
Tokenization & Stopword Removal; Split cleaned text into tokens & Removed common stopwords to reduce noise.
Feature Transformation; Applied TF-IDF vectorization to convert text into numerical features for model training.   

---

## 🤖 Modeling Approach  
- Baseline models: Logistic Regression, Naïve Bayes, Support Vector Machine(SVM).  
- Evaluation metrics: Accuracy, Precision, Recall, F1-score.  
- Best-performing model selected for business insights.  

---

## 📊 Insights & Business Value  
- **Apple vs Google Sentiment:** Identified key differences in consumer perception.  
- **Product-Level Insights:** Highlighted which product categories drive positive or negative conversations.  
- **Strategic Recommendations:** Suggested targeted engagement strategies for each brand.  

---

## 🛠️ Tech Stack  
- **Languages:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, TensorFlow/Keras, NLTK, Transformers  
- **Tools:** Jupyter Notebook, Matplotlib, Seaborn  

---

## 🚀 How to Run  
1. Clone this repository:  
   ```bash
   git clone <repo-link>
   cd <repo-folder>
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:  
   ```bash
   jupyter notebook index.ipynb
   ```
4. Tableau Link
https://public.tableau.com/app/profile/agnes.chomba/viz/FROMTWEETSTOSTRATEGYPREDICTINGSENTIMENTANDSHAPINGCUSTOMERENGAGEMENT/Dashboard1?publish=yes 

---

## 📌 Next Steps  
- Deploy best-performing sentiment model as a web API.  
- Extend analysis to other tech brands.  
- Automate real-time monitoring of tweets for brand health tracking.  
