# Dual-LLM AI Assistant

A multi-model AI assistant built with Python and Streamlit that integrates multiple large language models, intelligently routes user questions, compares model responses, and evaluates response quality.

## Overview

The Dual-LLM AI Assistant provides a unified interface for interacting with different AI models.

The application currently supports:-

* Gemini
* ChatGPT
* Automatic question routing
* Model fallback handling
* Response comparison
* AI-powered response evaluation
* Professional Streamlit interface

The project is designed as an experiment in multi-model AI orchestration and demonstrates how different language models can be integrated into a single application.

## Features

### Multi-Model Integration

Interact with multiple AI providers through a single application.

### Intelligent Question Routing

The application analyzes the user's question and identifies its category, such as:

* Coding
* Explanation
* Comparison
* General

The router then selects an appropriate model.

### Fallback Handling

If the selected model fails or becomes unavailable, the application attempts to use the alternative model.

### Response Comparison

When both models are available, their responses can be compared using the built-in evaluation system.

### AI-Powered Evaluation

Gemini can act as an evaluator and analyze responses based on:

* Accuracy
* Relevance
* Clarity
* Completeness
* Overall quality

### Streamlit Interface

The project includes a professional browser-based interface with:

* Model selection
* Automatic routing
* Response panels
* Model comparison
* Evaluation results
* Error handling

## Architecture

```text
                    User
                      |
                      v
              Streamlit Interface
                      |
                      v
                Question Router
                      |
          +-----------+-----------+
          |           |           |
       Coding    Explanation  Comparison
          |           |           |
          +-----------+-----------+
                      |
                      v
                 AI Model
                      |
                      v
                  Response
                      |
                      v
              Evaluation System
                      |
                      v
                Final Result
```

## Technology Stack

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Core application logic              |
| Streamlit     | Web interface                       |
| Gemini API    | AI model integration and evaluation |
| OpenAI API    | ChatGPT integration                 |
| python-dotenv | Environment variable management     |
| Git           | Version control                     |
| GitHub        | Project hosting                     |

## Project Structure

```text
dual-llm-assistant/
│
├── app.py
├── streamlit_app.py
├── router.py
├── evaluator.py
├── gemini_client.py
├── openai_client.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd dual-llm-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API keys

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

Never commit the `.env` file to GitHub.

The project includes `.env` in `.gitignore` to protect API credentials.

## Running the Application

Start the Streamlit application with:

```bash
python -m streamlit run streamlit_app.py
```

The application will open in your browser.

## Available Modes

### Auto Router

Automatically categorizes the user's question and selects the appropriate model.

### Gemini

Sends the question directly to Gemini.

### ChatGPT

Sends the question directly to ChatGPT.

### Compare Both

Attempts to generate responses from both models and evaluates them when both APIs are available.

## Terminal Version

The project also includes a command-line interface.

Run:

```bash
python app.py
```

The terminal application provides:

```text
1. Gemini
2. ChatGPT
3. Compare Both Models
4. Auto Router
5. Test AI Evaluator
```

## Environment and Security

API credentials are stored using environment variables rather than being hard-coded into the source code.

The `.env` file is excluded from version control through `.gitignore`.

This prevents sensitive API credentials from being accidentally published to GitHub.

## Current Limitations

The application depends on the availability and quota of the configured AI APIs.

If an API is unavailable or does not have sufficient quota, the application displays an appropriate error and attempts fallback handling where applicable.

The current routing system uses rule-based question classification and can be further improved with an AI-based routing system.

## Future Improvements

Potential future enhancements include:

* AI-based routing instead of keyword-based routing
* Support for additional LLM providers
* More advanced response evaluation
* Conversation history
* User authentication
* Response export
* Performance and latency tracking
* Token usage monitoring
* Model performance analytics
* Persistent chat sessions

## Learning Outcomes

This project demonstrates practical experience with:

* Python application development
* REST/API integration
* Large language model APIs
* Prompt engineering
* Multi-model orchestration
* Response evaluation
* Error handling
* Environment variable management
* Streamlit application development
* Git and GitHub workflow

## Author

**Mittapally Sai Vivek**

Computer Science and Engineering

GitHub: https://github.com/viveksai1700-del

## License

This project is intended for educational and portfolio purposes.
