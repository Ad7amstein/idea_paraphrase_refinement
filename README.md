# Idea Paraphrase Refinement 🤖

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.118.0-orange.svg)](https://github.com/joaomdmoura/crewAI)

A powerful AI-powered tool for refining and paraphrasing ideas using the CrewAI framework. This project helps transform and enhance ideas through intelligent paraphrasing and refinement processes.

## 🌟 Features

- **AI-Powered Paraphrasing**: Utilizes advanced AI models to rephrase and refine ideas
- **CrewAI Integration**: Built on top of the powerful CrewAI framework
- **Multiple Operation Modes**: Supports training, testing, and replay functionalities
- **Python 3.10+ Support**: Modern Python implementation with type hints
- **Easy-to-Use CLI**: Simple command-line interface for all operations

## 📁 Project Structure

```
idea_paraphrase_refinement/
├── src/                    # Source code
│   └── idea_paraphrase_refinement/
├── tests/                  # Test files
├── knowledge/             # Knowledge base and resources
├── output/                # Generated outputs
└── pyproject.toml         # Project configuration
```

## 🚀 Installation

1. Ensure you have Python 3.10 or higher installed
2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/idea_paraphrase_refinement.git
   cd idea_paraphrase_refinement
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install the package and dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## 🔑 Environment Variables

Before running the project, you need to set up your environment variables. Create a `.env` file in the root directory with the following variables:

```bash
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here  # Required for CrewAI agents

# Optional Configuration
MODEL_NAME=gpt-4  # Default model for agents
TEMPERATURE=0.7   # Controls response randomness
MAX_TOKENS=2000   # Maximum tokens per response
```

Make sure to:
1. Never commit your `.env` file (it's already in .gitignore)
2. Keep your API keys secure
3. Replace the placeholder values with your actual API keys
4. Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## 💻 Usage

The project provides several command-line tools:

```bash
# Run the crew
crewai run

# Train the model
crewai train

# Replay previous runs
crewai replay

# Run tests
test
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for providing the powerful AI framework
- All contributors and users of this project
- The open-source community for their continuous support

---

Made with ❤️ by [Adham Allam](mailto:adham32003200@gmail.com)
