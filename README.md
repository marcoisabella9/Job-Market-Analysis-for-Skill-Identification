<h1>Job Market Analysis for Skill Identification</h1>
<h2>Description of the Project</h2>
<p>This project aims to analyze job listings to identify the most important skills required for various job roles in 
  computer science, data science, and AI. 
  It involves data collection through web scraping, data preprocessing, feature engineering, model development, 
  and visualization to provide insights into job market trends and skill requirements. </p>
<h2>How to Use/Setup</h2>
<h3><strong>Note: For first time use must uncomment the webscraper portion.</strong></h3>
<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/your_username/job-market-analysis.git
cd job-market-analysis</code></pre>
        </li>
        <li>
          <strong>Install Dependencies and Uncomment Webscraper portion if neccessary.</strong>
        </li>
        <li><strong>Run the Preprocessing and Analysis</strong>:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

  <h2>Training</h2>
    <ul>
        <li><strong>Data Collection</strong>:
            <ul>
                <li>Web scraping job listings from SimplyHired and Glassdoor. Each group of listing comes from a simple search for Software Engineering roles on the respective site.</li>
                <li>Extracting job titles, companies, locations, qualifications, and skills.</li>
                <li><strong>Tools Used</strong>: Selenium, pandas, scikit-learn, matplotlib.</li>
                <li><strong>Data Sources</strong>: SimplyHired, Glassdoor.</li>
                <li><strong>Collected Attributes</strong>: Job title, company, location, qualifications (skills), experience level.</li>
                <li><strong>Number of Data Samples</strong>: 1000+ job listings.</li>
            </ul>
        </li>
        <li><strong>Data Preprocessing</strong>:
            <ul>
                <li><strong>Data Cleaning</strong>: Unwanted keywords like 'experience', 'years', 'senior' are filtered
                  from qualifications. Experience levels are extracted by idnetifying relevant keywords.
                  Rows with empty skills are removed.</li>
                <li><strong>Data Integration</strong>: All data is stored in the csv file which is later processed.
                  After the skills are encoded, the new skills dataframe is integrated with the original dataframe.
                  One-Hot Encoding is performed, converting categorical columns, title, location, experience level into
                  binary columns.</li>
                <li><strong>Data Ingestion</strong>: The data is read from a CSV file and further processed.</li>
                <li><strong>Data Description and Metadata Specification</strong>:
                    <pre><code>Sample Data:
title,company,location,qualifications
Software Developer - AI Trainer,DataAnnotation,"New York, NY","['Writing skills', 'C#', 'English', 'Mid-level', 'SQL', 'C++', ""Bachelor's degree"", 'JavaScript', 'Swift', 'AI', 'Grammar Experience', 'Python', 'HTML']"</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Feature Engineering</strong>:
            <ul>
                <li>CountVectorizer tokenizes required_skills into a matrix of word counts and converts each skill into a feature.</li>
                <li>Original required_skills column is dropped and new info is encoded in skill columns.</li>
                <li>Feature data is scaled with StandardScaler, improving performance.</li>
                <li><strong>Data Processing</strong>: Tokenizing skills, one-hot encoding categorical features, and scaling numerical features.</li>
            </ul>
        </li>
        <li><strong>Model Development and Evaluation</strong>:
            <ul>
                <li><strong>Train and Test Data Partition</strong>: Splitting data into training (80%) and testing (20%) sets.</li>
            </ul>
        </li>
        <li><strong>Skill Importance</strong>:
            <ul>
                <li><strong>Description</strong>: Utilizes RandomForestClassifier to identify important features/skills for different job roles.</li>
                <li><strong>Identified Important Skills</strong>:
                    <ul>
                        <li>Software Developer: Python, SQL, JavaScript</li>
                        <li>Data Scientist: Python, R, Machine Learning</li>
                        <li>AI Engineer: TensorFlow, Keras, Neural Networks</li>
                        <li>Front-End Developer: HTML, CSS, JavaScript</li>
                        <li>Back-End Developer: Node.js, SQL, REST APIs</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>

  <h2>Visualization</h2>

  <h3>Sample Qualifications Ratings</h3>
    <img src="Qualifications Figure.png" alt="Sample Figure of Qualifications">

  <h2>Discussion and Conclusions</h2>
    <ul>
        <li><strong>Project Findings</strong>: The analysis provided insights into the most demanded skills for various job roles in the tech industry. Python, SQL, and JavaScript emerged as top skills across multiple roles.</li>
        <li><strong>Challenges Encountered</strong>: Handling inconsistencies in job titles and qualifications, integrating data from different sources, and extracting relevant skills from job descriptions.
        Scraping posed a great challenge in the beginning as I had to not only iterate through a huge amount of listings, but also idenitfy and interact with things like buttons to display more jobs, which were different across each site and listings that were incomplete or varied from each other.</li>
        <li><strong>Recommendations</strong>: To improve model performance, I could utilize more advanced techniques to better extract and standardize skills from job descriptions, identify more features, and continuously update the dataset to reflect current market trends.</li>
    </ul>
</body>
</html>
