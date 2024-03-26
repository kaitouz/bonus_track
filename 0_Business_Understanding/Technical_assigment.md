# 1. General Provisions

## 1.1 Research Project Title

LapLens - Telegram Laptop Price Prediction Bot

## 1.2 Problem Statement

The project aims to assist users in easily determining the price of a laptop based on descriptions of its configuration parameters. The primary objective is to develop a Telegram bot capable of predicting laptop prices accurately and efficiently. It's essential to note that this project is solely for educational purposes within the scope of a diploma project and does not serve any commercial objectives.

## 1.3 Normative Documentation
## 1.4 Development Sources
- Human:
    - Developed by a student with prior experience deploying small-scale machine learning models.

- Resources:
    - Utilization of publicly available Python libraries for Telegram bot development (e.g., python-telegram-bot).
    - Implementation of open-source machine learning libraries (e.g., TensorFlow, scikit-learn).
    - Utilization of publicly available laptop price datasets (if applicable) for training and validation purposes.

## 1.5 Customer-Side Consultants

N/A (assuming self-development)

## 1.6 Patent Cleanliness and Licensing Requirements

No specific patents or licenses anticipated for this project.

# 2. List of Terms and Definitions
...

# 3. List of Abbreviations
...


# 4. Objectives and Tasks of the Work

- Objectives:
    - Develop a Telegram bot to facilitate users in predicting the price of a laptop based on provided descriptions.

- Tasks:
    1. Conduct project analysis: Identify problems, requirements, and goals.
    2. Data collection: Gather data from public laptop price datasets and potentially crawl data from online sales websites.
    3. Analyze and preprocess data to prepare it for model training.
    4. Develop a machine learning model capable of accurately predicting laptop prices.
    5. Develop a Telegram bot application integrating the trained model for price prediction functionality.
    6. Deploy the Telegram bot and monitor its performance. Implement maintenance procedures as necessary.


# 5. Positioning
The operating environment of the project involves implementing MLOps at level 0, where steps are performed manually. This includes manual data collection, preprocessing, model training, and deployment processes. There will be interaction with other systems, primarily involving data exchange formats for inputting laptop descriptions and receiving predicted prices.

Roles and number of users of the developed and/or supplied technologies and/or tools (solutions) include:
- Developers: Involved in the design, development, and deployment of the Telegram bot and machine learning model.
- End-users: Users of the Telegram bot who input laptop descriptions and receive predicted prices.
- Data Providers: Suppliers of publicly available laptop price datasets used for model training.


# 6. Input and Output Data

## Format Description
- Input Data Format: Users will provide laptop descriptions, which may include parameters such as brand, model, processor, RAM, storage, graphics card, screen size, etc. This input data will be in textual format.
- Output Data Format: The bot will provide the predicted price of the laptop based on the provided description. Optionally, the bot can provide additional information like confidence level in the prediction. The output will be in numerical format.

## Compatibility and Exchange Between Components
- The input data will be exchanged between the Telegram bot interface and the machine learning model.
- The output data (predicted price) will be displayed within the Telegram bot interface to the users.

## Data Storage
- Type of Information: Input laptop descriptions, predicted prices.
- Frequency of Use: Input data will be used whenever a user interacts with the bot. Predicted prices will be generated upon user requests.
- Access Capabilities: Read access for both input and output data.
- Entities and Relationships: Each input laptop description is associated with a predicted price.
- Integrity Constraints: Ensure accuracy and consistency of input data during preprocessing and model training phases.

## Data Sources
- Publicly available laptop price datasets.
- Optionally, data crawled from online sales websites.

## Results Structure and Format
- The predicted price will be a single numerical value representing the estimated price of the laptop.
- Volume: One predicted price per input laptop description.

## Data Relevance and Quality
- Relevance: Data should accurately reflect current laptop prices to provide meaningful predictions.
- Representativeness: The dataset should cover a wide range of laptops to ensure the model's generalization capability.
- Completeness: Ensure that all necessary parameters are included in the laptop descriptions.
- Reliability and Accuracy: Data should be sourced from reputable sources to ensure reliability and accuracy.
- Anonymization: User data anonymization will be implemented to protect user privacy.

# 7. Functional Requirements
## Architecture of the Solution
- The solution will consist of a Telegram bot interface and a machine learning model backend.
- The machine learning model will utilize various algorithms and mathematical models for price prediction.

## Hypotheses, Algorithms, and Mathematical Models
- Hypotheses: The model assumes that the provided laptop descriptions contain sufficient information to accurately predict prices.
- Algorithms and Mathematical Models: Regression algorithms (e.g., linear regression, random forest regression) will be employed for price prediction.

## Methods Implemented by the Technologies
- Input Data Access: The Telegram bot will provide an interface for users to input laptop descriptions.
- Output Data Display: The predicted prices will be displayed within the Telegram bot interface.
- Preprocessing of Input Data: Data preprocessing techniques will be employed to clean and normalize input data before feeding it into the model.
- Control of Data Characteristics: Ensure that input data characteristics meet the model's requirements for accurate predictions.
- Data Archiving: Historical input-output data pairs may be archived for analysis and model improvement purposes.

# 8. Constraints
## Restrictions on Third-Party Libraries and Services
- The project will primarily utilize open-source libraries for development to ensure transparency and accessibility.
- The use of third-party libraries and services will be limited to those with permissive licenses compatible with the project's objectives.

## Hardware Limitations
- Computing power: The project will be developed considering constraints on computing resources, ensuring that algorithms and models are optimized for efficient execution.
- Parallel Processing: Utilization of parallel processing techniques will be limited to the capabilities of the hardware available.
- Access to Internet and Local Network: The Telegram bot will require internet access for communication with users. Local network access may be required for accessing datasets or resources if applicable.

## Data Repository Limitations
- Data repositories used for storage and access will be selected based on their compatibility with the project's requirements.
- Consideration will be given to data repository limitations such as storage capacity, access permissions, and data integrity.

# 9. Assumptions and Dependencies

## Library Versions and Software Compatibility
The project assumes compatibility between the versions of libraries and software used in development.
Dependencies on specific library versions will be documented to ensure consistent functionality across different environments.

## Factors Affecting Product Functionality
- User behavior, such as the frequency and consistency of input data, may influence the usability and effectiveness of the Telegram bot.

## Diversity and Variability of Data
- The project assumes diversity and variability in the input data describing laptop configurations.
- Variations in data quality, completeness, and accuracy are expected and will be addressed through preprocessing and validation techniques.

## Dependencies
- The project depends on the availability and accessibility of public laptop price datasets for model training and evaluation.
- Dependencies on external services, such as internet connectivity for Telegram bot operation, may impact the product's functionality.
- Changes in the underlying architecture or infrastructure may introduce dependencies that require modifications to the project implementation.

# 10. System Requirements and Performance
## Resource Availability
- Sufficient computational resources to support model training and inference.
- Adequate storage for dataset storage and model parameters.
## Response Time
- Aim for quick response times to user queries, ideally within a few seconds.
## Throughput
- Support a high throughput of user requests, ensuring smooth operation during peak usage periods.
## Data Capacity
- Accommodate large datasets for training the machine learning model.
- Efficiently manage and store user input data and model output data.
## Predictability of Real-time Systems
- Maintain consistent performance even under varying loads and user traffic.
## Access Time
- Minimize latency in accessing and processing user input data.
## Behavior in Reduced Functionality Mode
- Provide essential functionalities even in situations of reduced resources or system failures.
## Resource Efficiency
- Optimize resource utilization to ensure efficient operation of the bot application.

# 11. Quality Attributes

- **Model Quality:** Continuously refine the model through regular evaluation, tuning, and exploration of advanced algorithms.
- **Data Quality:** Apply data preprocessing techniques such as cleaning, outlier detection, and feature engineering. Ensure data is up-to-date and representative.
- **Reliability:** Implement robust error handling, fault tolerance mechanisms, and rigorous testing procedures.
- **Resilience:** Implement redundancy, backup systems, and automated recovery mechanisms.
- **Data Processing Speed:** Optimize algorithms, leverage parallel processing, and utilize efficient data structures. Scale hardware resources or adopt cloud-based solutions as needed.


# 12. Security Requirements
- User privacy should be respected, and no personal information beyond the laptop description should be collected.
- Implement best practices to prevent unauthorized access to the bot or underlying systems.

# 13. Deployment Requirements
- The bot can be deployed on a cloud platform or a dedicated server with a Telegram bot API connection.
# 14. Documentation
- User manual explaining how to interact with the bot.
- Technical documentation

# 15. Acceptance Procedure
- Successful deployment of the bot on the chosen platform.
- Functionality testing to ensure the bot meets the requirements outlined in this document.
- User acceptance testing to confirm the bot is easy to use and provides valuable information.

# 16. Work Schedule

| № | Stage name               | Start of work | Completion of work | Details                                                                                                                                                                                                                                                                    | Result of Work                       |
|---|--------------------------|---------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| 1 | Project Analysis         |               |                    | - Define specific goals and success criteria for the bot. <br/>  - Research and choose suitable machine learning libraries and frameworks, tech stack.                                                                                                                            | Requirements Document, Project Plan  |
| 2 | Data Collection          |               |                    | - Identify and collect relevant laptop price datasets. <br/>- Set up development environment and version control system (e.g., Git).                                                                                                                                            | Raw Data Files                       |
| 3 | Data Preprocessing       |               |                    | - Preprocess the collected laptop price data (cleaning, handling missing values, feature engineering).                                                                                                                                                                     | Cleaned and Preprocessed Data        |
| 4 | Model Development        |               |                    | - Choose a machine learning model suitable for tasks (e.g., Random Forest, Gradient Boosting Regression).  <br/>- Train the model on the training data, evaluating performance on the validation set.  <br/>- Fine-tune hyperparameters of the model to improve accuracy.            | Trained Machine Learning Model       |
| 5 | Telegram Bot Development |               |                    | - Conduct thorough testing of the bot's functionality with various laptop descriptions.  <br/>- Gather feedback and iterate on the design based on insights.                                                                                                                    | Developed Telegram Bot               |
| 6 | Deployment & Testing     |               |                    | - Deploy the bot on the chosen platform (cloud or server) and configure Telegram bot API connection.  <br/>- Prepare user manuals and any additional documentation.                                                                                                             | Deployed Bot, Testing Reports        |
| 7 | Monitoring & Maintenance |               |                    | - Monitor the bot's performance in production and address any issues that arise. <br/>- Retrain the machine learning model periodically with new data to improve accuracy over time. <br/>- Consider adding new features or functionalities based on user feedback and future needs. | Maintenance Plan, Monitoring Reports |


# 17. Appendices

https://core.telegram.org/bots/api
https://python-telegram-bot.org/
https://pandas.pydata.org/docs/
