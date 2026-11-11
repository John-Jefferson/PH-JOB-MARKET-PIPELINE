#splitting titles and descriptions
skills = [
  "Python", "SQL", "MySQL", "PostgreSQL", "Microsoft SQL Server", "Oracle SQL", "SQLite", "MariaDB",
  "MongoDB", "Cassandra", "Redis", "Excel", "Microsoft Excel", "Google Sheets", "Power BI", "Tableau",
  "Looker", "Looker Studio", "Qlik Sense", "QlikView", "SAP BusinessObjects", "MicroStrategy", "IBM Cognos",
  "SSRS", "SSIS", "SSAS", "DAX", "Power Query", "Power Pivot", "VBA", "Macros",
  "Data Analysis", "Data Analytics", "Business Analytics", "Statistical Analysis", "Data Visualization",
  "Reporting", "Dashboarding", "KPI Tracking", "Forecasting", "Predictive Analytics", "Descriptive Analytics",
  "Diagnostic Analytics", "Prescriptive Analytics", "Data Mining", "Data Modeling", "Data Cleaning",
  "Data Wrangling", "Data Transformation", "Data Governance", "Data Quality", "Data Validation", "Data Entry",
  "Data Encoding", "Data Processing", "Data Collection", "Data Integration", "Data Aggregation", "Data Migration",
  "Data Warehousing", "Data Lake", "Data Lakehouse", "ETL", "ELT",
  "Apache Airflow", "Apache Spark", "PySpark", "Apache Kafka", "Apache Flink", "Apache Hive", "Apache Hadoop",
  "HDFS", "MapReduce", "Databricks", "Snowflake", "Amazon Redshift", "Google BigQuery", "Azure Synapse",
  "Azure Data Factory", "AWS Glue", "Talend", "Informatica", "Pentaho", "Alteryx", "Matillion", "dbt",
  "Data Build Tool", "Jupyter", "Jupyter Notebook", "Google Colab", "Anaconda",
  "NumPy", "Pandas", "Polars", "SciPy", "Statsmodels", "Scikit-learn", "TensorFlow", "Keras", "PyTorch",
  "XGBoost", "LightGBM", "CatBoost",
  "Machine Learning", "Deep Learning", "Artificial Intelligence", "Natural Language Processing", "NLP",
  "Computer Vision", "Feature Engineering", "Model Deployment", "Model Evaluation", "A/B Testing",
  "Hypothesis Testing", "Regression Analysis", "Time Series Analysis", "Cluster Analysis", "Classification",
  "Decision Trees", "Random Forest", "Neural Networks", "Statistical Modeling", "Bayesian Analysis",
  "Data Storytelling", "Business Intelligence", "BI", "Data Reporting", "Report Automation", "Data Automation",
  "Automation Scripting", "Python Scripting", "Shell Scripting", "Bash", "Linux", "Unix",
  "Git", "GitHub", "GitLab", "Bitbucket", "Version Control", "CI/CD", "Docker", "Kubernetes",
  "REST API", "API Integration", "Web Scraping", "Selenium", "BeautifulSoup", "Scrapy",
  "JSON", "XML", "CSV", "Parquet", "Avro", "ORC",
  "Cloud Computing", "AWS", "Amazon Web Services", "Microsoft Azure", "Google Cloud Platform", "GCP",
  "Azure Blob Storage", "Amazon S3", "Google Cloud Storage", "Azure Data Lake", "AWS Lambda", "Azure Functions",
  "Google Cloud Functions", "Streamlit", "Dash", "Flask", "FastAPI", "Django",
  "ERP", "SAP", "Salesforce", "CRM Analytics", "Workday", "Oracle ERP", "NetSuite",
  "Master Data Management", "MDM", "Metadata Management", "Data Catalog", "Data Lineage",
  "Information Management", "Data Security", "Data Privacy", "Data Compliance", "GDPR",
  "Data Architecture", "Solution Architecture", "Database Design", "Database Administration",
  "Database Management", "Query Optimization", "Performance Tuning", "Stored Procedures", "Triggers", "Views",
  "Indexing", "Normalization", "Denormalization", "Dimensional Modeling", "Star Schema", "Snowflake Schema",
  "Fact Tables", "Dimension Tables", "OLTP", "OLAP",
  "Customer Analytics", "Marketing Analytics", "Financial Analytics", "Healthcare Analytics", "Risk Analytics",
  "Fraud Detection", "Supply Chain Analytics", "Operations Analytics", "People Analytics", "HR Analytics"
]

qualifications = [
  "Bachelor", "College", "Undergraduate", "Associate Degree", "Master's Degree", "Doctorate",
  "PhD", "Postgraduate", "Vocational", "Technical Course", "Diploma", "Certificate Program", "Computer Science", "Information Technology", "Information Systems", "Data Science", "Statistics",
  "Mathematics", "Applied Mathematics", "Business Analytics", "Analytics", "Computer Engineering",
  "Software Engineering", "Industrial Engineering", "Electronics Engineering", "Business Administration",
  "Management Information Systems", "Economics", "Finance", "Accounting", "Actuarial Science", "Physics",
  "Data Analytics", "Operations Research", "Engineering", "STEM", "Graduate",   "Authorized to Work", "Work Authorization", "Eligible to Work", "Permanent Resident", "Citizen",
  "Employment Eligibility", "No Sponsorship Required", "Willing to Relocate", "Can Work Onsite",
  "Can Work Hybrid", "Can Work Remote", "Flexible Schedule", "Shift Work", "Night Shift",
  "Weekend Availability", "Travel Requirement", "Passport Holder", "Fresh Graduate", "Fresh Graduates Welcome", "Entry-Level Candidates", "Open to Fresh Graduates",
  "Recent Graduates", "Graduating Students", "Career Shifters", "CPA", "Certified Public Accountant", "Licensed Engineer", "Professional License", "Board Passer",
  "Civil Service Eligible", "PRC License", "Professional Certification", "Relevant Certification",
  "Industry Certification"
]
Seniority_Level = ["entry-level", "junior", "mid-level", "senior"]
#EMPLOYMENT TYPE IS IN THE TABLE ALREADY
Work_Setup = ["on-site", "WFH", "hybrid", "freelance", "remote"]
soft_skills = [
  "Communication", "Verbal Communication", "Written Communication", "Presentation Skills", "Public Speaking","Active Listening", "Interpersonal Skills", "Business Communication", "Professional Communication","Client Communication", "Stakeholder Communication", "Cross-functional Communication","Technical Communication", "Negotiation", "Persuasion", "Facilitation",
  "Teamwork", "Collaboration", "Cooperation", "Partnership", "Relationship Building", "Team Player",
  "Cross-functional Collaboration", "Collaborative Mindset", "Networking", "Peer Support", "Knowledge Sharing",
  "Problem Solving", "Critical Thinking", "Analytical Thinking", "Logical Thinking", "Strategic Thinking",
  "Decision Making", "Troubleshooting", "Root Cause Analysis", "Judgment", "Reasoning", "Innovation",
  "Creative Thinking", "Solution-Oriented", "Resourcefulness",
  "Time Management", "Prioritization", "Organization", "Organizational Skills", "Planning", "Scheduling",
  "Task Management", "Project Coordination", "Attention to Deadlines", "Multitasking", "Workload Management",
  "Efficiency",
  "Adaptability", "Flexibility", "Agility", "Resilience", "Learning Agility", "Continuous Learning",
  "Growth Mindset", "Open-Mindedness", "Willingness to Learn", "Curiosity", "Self-Development", "Adaptable",
  "Professionalism", "Integrity", "Accountability", "Responsibility", "Reliability", "Dependability",
  "Commitment", "Ownership", "Self-Motivation", "Self-Discipline", "Work Ethic", "Ethical Conduct",
  "Trustworthiness", "Initiative", "Dedication",
  "Leadership", "Mentorship", "Coaching", "People Development", "Team Building", "Influencing",
  "Motivating Others", "Conflict Resolution", "Delegation", "Guidance", "Inspiring Others",
  "Leadership Potential",
  "Customer Service", "Customer Focus", "Customer Orientation", "Client Focus", "Service Orientation",
  "Relationship Management", "Client Relations", "Customer Satisfaction", "Empathy", "User-Centric Mindset",
  "Emotional Intelligence", "Empathy", "Self-Awareness", "Self-Control", "Emotional Maturity",
  "Relationship Management", "Social Awareness", "Patience", "Compassion", "Respectfulness",
  "Attention to Detail", "Detail-Oriented", "Accuracy", "Precision", "Thoroughness", "Quality Consciousness",
  "Quality Focus", "Meticulousness", "Consistency", "Compliance Awareness",
  "Self-Starter", "Proactive", "Initiative", "Autonomous", "Independent Worker", "Self-Driven",
  "Self-Managed", "Ownership Mindset", "Entrepreneurial Mindset", "Results-Oriented",
  "Business Acumen", "Data Storytelling", "Stakeholder Management", "Requirements Gathering",
  "Consultative Mindset", "Curiosity", "Investigative Mindset", "Research Skills", "Business Understanding",
  "Process Improvement", "Continuous Improvement", "Insight Generation", "Strategic Perspective",
  "Decision Support"
]

jobTitles = [
  "Data Analyst", "Junior Data Analyst", "Senior Data Analyst", "Associate Data Analyst", "Lead Data Analyst",
  "Business Data Analyst", "Reporting Analyst", "Research Analyst", "Operations Analyst", "Performance Analyst",
  "Insights Analyst", "Data Reporting Analyst", "Data Quality Analyst", "Data Governance",
  "Marketing Analyst", "Financial Data Analyst", "HR Data Analyst", "Healthcare Data Analyst", "Risk Analyst",
  "Fraud Analyst", "Product Analyst", "Pricing Analyst", "Supply Chain Analyst", "Sales Analyst",
  "Customer Insights Analyst", "Business Intelligence Analyst", "BI Analyst", "Analytics Analyst",
  "Statistical Analyst", "Quantitative Analyst", "Data Visualization Analyst",

  "Business Intelligence Developer", "Business Intelligence Engineer", "Business Intelligence Consultant",
  "BI Developer", "BI Engineer", "BI Consultant", "BI Specialist", "BI Architect", "BI Manager",
  "Power BI Developer", "Power BI Analyst", "Tableau Developer", "Tableau Analyst", "Looker Developer",
  "Dashboard Developer", "Reporting Developer",

  "Data Engineer", "Junior Data Engineer", "Senior Data Engineer", "Lead Data Engineer",
  "Principal Data Engineer", "Big Data Engineer", "Cloud Data Engineer", "Analytics Engineer",
  "ETL Developer", "ETL Engineer", "Data Integration Engineer", "Data Pipeline Engineer",
  "Data Platform Engineer", "Data Infrastructure Engineer", "Data Warehouse Engineer",
  "Data Warehouse Developer", "Data Migration Engineer", "Data Operations Engineer",
  "Streaming Data Engineer",

  "Database Engineer", "Database Administrator", "Database Developer", "Database Analyst",
  "Database Specialist", "SQL Developer", "SQL Analyst", "SQL Programmer", "MySQL Developer",
  "Oracle Database Administrator", "PostgreSQL Database Administrator", "Microsoft SQL Server DBA",
  "MongoDB Administrator", "NoSQL Engineer",

  "Data Scientist", "Junior Data Scientist", "Senior Data Scientist", "Lead Data Scientist",
  "Principal Data Scientist", "Applied Data Scientist", "Research Data Scientist",
  "Machine Learning Scientist", "AI Data Scientist", "Statistical Scientist", "Quantitative Scientist",
  "Decision Scientist",

  "Machine Learning Engineer", "Machine Learning Developer", "Machine Learning Researcher", "ML Engineer",
  "AI Engineer", "Artificial Intelligence Engineer", "Deep Learning Engineer", "NLP Engineer",
  "Computer Vision Engineer", "MLOps Engineer", "AI Research Engineer",

  "Data Architect", "Enterprise Data Architect", "Cloud Data Architect", "Data Solution Architect",
  "Analytics Architect", "Data Warehouse Architect", "Information Architect", "Big Data Architect",

  "Data Governance Specialist", "Data Governance Manager", "Data Governance Lead", "Data Steward",
  "Master Data Specialist", "Master Data Analyst", "Master Data Manager", "Data Quality Specialist",
  "Data Quality Engineer", "Data Quality Manager", "Data Compliance Analyst", "Metadata Analyst",
  "Metadata Specialist", "Data Catalog Specialist",

  "Data Operations Analyst", "Data Operations Engineer", "Data Operations Specialist",
  "Data Operations Manager", "Data Support Analyst", "Data Support Specialist", "Data Coordinator",
  "Data Administrator", "Data Controller", "Data Specialist",

  "Data Encoder", "Data Entry Clerk", "Data Entry Specialist", "Data Entry Operator",
  "Data Processing Clerk", "Data Processing Specialist", "Records Clerk", "Records Officer",
  "Document Controller", "Information Clerk", "Data Processor", "Data Verification Specialist",

  "Analytics Engineer", "Analytics Consultant", "Analytics Specialist", "Analytics Manager",
  "Analytics Lead", "Decision Support Analyst", "Business Analytics Specialist",
  "Customer Analytics Specialist", "Marketing Analytics Specialist", "Financial Analytics Specialist",
  "People Analytics Specialist", "HR Analytics Specialist", "Supply Chain Analytics Specialist",
  "Operations Analytics Specialist", "Digital Analytics Specialist", "Web Analytics Specialist",
  "Product Analytics Specialist",

  "Cloud Analytics Engineer", "Cloud Database Engineer", "Azure Data Engineer", "AWS Data Engineer",
  "Google Cloud Data Engineer", "Snowflake Engineer", "Databricks Engineer", "BigQuery Engineer",
  "Redshift Engineer",

  "Information Management Specialist", "Data Manager", "Data Management Specialist",
  "Information Governance Specialist", "Data Lifecycle Manager", "Data Asset Manager", "Data Custodian",
  "Information Officer",

  "Statistician", "Biostatistician", "Research Statistician", "Statistical Programmer", "Survey Analyst",
  "Research Data Analyst", "Research Data Manager", "Research Coordinator",

  "Chief Data Officer", "Head of Data", "Director of Data", "Director of Analytics",
  "Director of Data Engineering", "Director of Business Intelligence", "Data Engineering Manager",
  "Analytics Manager", "Data Science Manager", "Data Platform Manager", "Data Team Lead",
  "Head of Analytics", "Head of Business Intelligence",

  "Prompt Data Analyst", "AI Data Annotator", "Data Annotator", "Data Labeler", "Data Curator",
  "Knowledge Engineer", "Knowledge Management Specialist", "Knowledge Analyst",
  "Decision Intelligence Analyst", "Insights Consultant", "Revenue Analyst", "Growth Analyst",
  "Experimentation Analyst"
]

def comparison(description, keywords):
    """
    Checks which keywords from a list appear in the job description.

    Args:
        description (str): Full text of the job posting.
        keywords (list):   List of keywords to search for.

    Returns:
        list: Keywords found in the description (case-insensitive match).
    """
    found = []
    for word in keywords:
        if word.lower() in description.lower():
            found.append(word)
    if found == []:
        return ["None"]
    return found
