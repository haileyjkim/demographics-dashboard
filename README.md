Interactive Demographics Dashboard
1. Executive Summary
Problem: Comparing demographics between two groups is a common task in many different fields. Butterfly plots are a great way to visualize and understand differences, however creating them often require manual coding, making it difficult for users with little to no technical experience to do analysis. 

Solution: This project is a containerized web application that makes creating demographic visualizations easier. Users can upload raw CSV data sets and the application processes the data using Python statistical libraries to return a butterfly plot and summary statistics, allowing anyone to create butterfly plots. 

2. System Overview
Course content: Flask API

Architecture Diagram: ![Alt text](/Users/haileykim/Downloads/VScode/final/assets/architecture.png)

User Interface: HTML/Bootstrap Frontend

Backend: Flask (Python)

Data Processing: Pandas (Cleaning) -> Matplotlib/Seaborn (Visualization)

Container: Docker

Data/Models: The system accepts user-uploaded .csv files.

1. How to Run (Local)
Docker

Quick Start (Single Command)
Run the following command in the terminal to build and launch the application:

`sh run.sh`

(Or manually):

`# Build the image
docker build -t butterfly-dashboard .

# Run the container (Access at localhost:5001)
docker run --rm -p 5001:5000 butterfly-dashboard`

Open your browser to http://localhost:5001 to view the interface. 

4. Design Decisions
Why Flask & Docker?

Flask: Lightweight and allows the use of Python libraries (Pandas, Seaborn) for data processing and visualization. A heavier framework like Django would have been too much for a single-page tool.

In-Memory Plotting: Instead of saving images to the disk, the application saves plots to a BytesIO buffer and encodes them as Base64 strings. This ensures the app is "stateless" and faster.

Smart Data Prep: The analysis logic includes an edge-case handler that detects whether the uploaded CSV is raw data or a summary table, ensuring the app is robust to different user inputs. 

Trade-offs & Limitations:

State: The app is stateless; uploaded data is lost once the page refreshes. This is good for privacy but bad for persistent analysis.

Security: Basic error handling is implemented, but the app does not currently scan uploaded files for malicious payloads beyond basic extension checks. 

5. Results & Evaluation
Functionality Check:

Upload: Successfully processes CSV files.

Visualization: Correctly renders "Butterfly Plots" comparing two groups.

Statistics: Accurately displays a summary table (Mean, Count, Std Dev).

![Alt text](/Users/haileykim/Downloads/VScode/final/assets/screenshot.png)

6. What's Next

Cloud Deployment: Deploying to Azure App Service to make it publicly accessible. 

Database Integration: Adding a SQLite database to save historical analysis results.

Enhanced Stats: Including T-tests or ANOVA analysis directly in the dashboard output. 

7. Links

GitHub Repo: [INSERT YOUR REPO URL HERE] 