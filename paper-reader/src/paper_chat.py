import argparse
import os
from datetime import datetime

import ell
from ell import Message
from openai import OpenAI
from rich import print as rprint
from rich.markdown import Markdown
from rich.panel import Panel

# MODEL = "llama3.2"
MODEL = "llama3.2:1b"

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

# ell.config.verbose = True

ell.config.register_model(MODEL, client)


# initialized with a paper, user can chat with it about the paper
@ell.complex(model=MODEL, client=client, temperature=0.1)
def academic_chat_bot(
    message_history: list[Message], markdown_content: str
) -> list[Message]:
    """
    You are a highly specialized assistant trained to help users quickly and efficiently comprehend academic papers. Your primary function is to:

    1. **Extract Key Information**: Provide summaries, key findings, and critical insights from academic papers, including abstracts, introductions, conclusions, and important figures or formulas.

    2. **Clarify Terminology**: Define complex or unfamiliar terms in simple and concise language, with appropriate contextual understanding from the field of study.

    3. **Explain Concepts**: Offer clear and detailed explanations of complex concepts, methodologies, and theoretical frameworks found in the academic text.

    4. **Identify Citations**: Highlight important references and citations that are crucial for understanding the background or context of the paper.

    5. **Answer Questions**: Respond to user queries about the paper, providing precise and accurate information from the text.

    6. **Make Connections**: Help users connect ideas from one paper to broader research trends or other relevant works in the field.

    7. **Stay Focused on Content**: Stick to the content of the paper and assist the user with academic understanding. Do not provide unrelated information unless asked directly.

    You will receive academic papers in markdown format and must respond accordingly to help the user comprehend the material as efficiently as possible.
    """
    # Combine the paper content with the conversation history
    last_message = message_history[-1].text if message_history else ""
    return f"Paper content:\n{markdown_content}\n\nQuestion: {last_message}"


@ell.complex(model=MODEL, client=client, temperature=0.1)
def organize_conversation_bot(
    message_history: list[Message], original_content: str
) -> list[Message]:
    """
    You are an organizational assistant tasked with maintaining, updating, and improving notes based on the interaction history of another LLM and its user. Your primary function is to:

    1. **Read and Analyze Input**:
       - **Input 1**: Existing markdown notes, which may include sections such as summaries, explanations, citations, and observations.
       - **Input 2**: Recent conversation history between the user and another LLM. This will include insights, clarifications, questions, and new information.

    2. **Update and Organize Notes**:
       - **Combine Information**: Integrate the new insights, explanations, and responses from the conversation history with the existing notes.
       - **Organize Clearly**: Reorganize the content in a clear, logical, and structured way. Use appropriate markdown features such as:
         - **Headings**: For key sections or newly added topics (e.g., # Summary, ## Key Concepts, ### Questions Answered).
         - **Lists and Bullets**: For bullet points, explanations, or points of interest.
         - **Tables**: For organizing data, citations, or comparisons where relevant.
       - **Improve Clarity**: Ensure that the updated notes are concise, well-structured, and easy to read.

    3. **Maintain Markdown Format**:
       - Format the output using markdown syntax for proper structuring. Use appropriate tags like `#` for headings, `*` or `-` for bullet points, and `|` for tables if necessary.
       - Add new content under relevant headings, and create new sections as needed based on the conversation history.

    4. **Enhance Notes**:
       - **Summarize New Insights**: Synthesize the conversation history to create concise summaries.
       - **Highlight Important Details**: Add key points from the conversation history into the notes, ensuring that they align with the existing content.
       - **Organize Logically**: Ensure that the notes flow logically and are easy to navigate. Reorder sections, if needed, to improve understanding.

    5. **Preserve Context**:
       - Keep any critical information from the original markdown notes intact unless the conversation history provides a better, more updated version.
       - Cross-reference new additions with existing content to avoid duplication and ensure consistency.
    """
    return f"Original notes:\n{original_content}\n\nConversation history:\n{message_history}"


def read_markdown_file(file_path: str) -> str:
    """
    Reads the content of a markdown file and returns it as a string.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.

    """
    try:
        with open(file_path, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        msg = f"The file at {file_path} does not exist."
        raise FileNotFoundError(msg)
    except Exception as e:
        msg = f"An error occurred while reading the file: {e}"
        raise Exception(msg)


def parse_args():
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument(
        "input_file", type=str, help="Path to the input markdown file."
    )
    parser.add_argument(
        "output_file", type=str, help="Path to the output markdown file."
    )
    return parser.parse_args()


# Add different conversation modes for specific purposes
@ell.complex(model=MODEL, client=client, temperature=0.1)
def paper_chat_mode(
    mode: str, message_history: list[Message], markdown_content: str
) -> list[Message]:
    """
    Different chat modes for different purposes:
    - 'summary': Quick overview and key points
    - 'deep': Detailed analysis and explanations
    - 'critique': Critical analysis and limitations
    - 'connect': Find connections to other papers/concepts
    - 'explain': Explain complex concepts in simple terms.
    """
    system_prompt = """
    You are a highly specialized assistant trained to help users quickly and efficiently comprehend academic papers. Your primary function is to:

    1. **Extract Key Information**: Provide summaries, key findings, and critical insights from academic papers, including abstracts, introductions, conclusions, and important figures or formulas.

    2. **Clarify Terminology**: Define complex or unfamiliar terms in simple and concise language, with appropriate contextual understanding from the field of study.

    3. **Explain Concepts**: Offer clear and detailed explanations of complex concepts, methodologies, and theoretical frameworks found in the academic text.

    4. **Identify Citations**: Highlight important references and citations that are crucial for understanding the background or context of the paper.

    5. **Answer Questions**: Respond to user queries about the paper, providing precise and accurate information from the text.

    6. **Make Connections**: Help users connect ideas from one paper to broader research trends or other relevant works in the field.

    7. **Stay Focused on Content**: Stick to the content of the paper and assist the user with academic understanding. Do not provide unrelated information unless asked directly.

    You will receive academic papers in markdown format and must respond accordingly to help the user comprehend the material as efficiently as possible.
    """

    mode_prompts = {
        "summary": """You are a research assistant helping to summarize academic papers.
                     Provide a concise summary focusing on:
                     - Key findings and contributions
                     - Main methodology
                     - Important conclusions
                     Keep the summary clear and focused on the most important points.""",
        "deep": """You are a research expert conducting in-depth analysis of academic papers.
                  Focus on:
                  - Detailed methodology analysis
                  - Assumptions and their validity
                  - Experimental design and results
                  - Theoretical foundations
                  Provide thorough explanations and insights.""",
        "critique": """You are a peer reviewer critically analyzing this paper.
                      Focus on:
                      - Methodological strengths and weaknesses
                      - Potential limitations and biases
                      - Validity of conclusions
                      - Suggestions for improvement
                      Be constructive but thorough in your critique.""",
        "connect": """You are a research coordinator identifying connections between papers.
                     Focus on:
                     - Related work and references
                     - Similar methodologies or findings
                     - Potential applications in other fields
                     - Future research directions
                     Help build connections to the broader research landscape.""",
        "explain": """You are a teacher explaining complex academic concepts.
                     Focus on:
                     - Breaking down complex terms and ideas
                     - Using simple analogies and examples
                     - Providing clear, step-by-step explanations
                     - Answering common questions
                     Make the content accessible while maintaining accuracy.""",
    }

    system_prompt += mode_prompts.get(mode, mode_prompts["summary"])

    # Combine the last message with mode-specific context
    last_message = message_history[-1].text if message_history else ""
    prompt = f"Mode: {mode}\n\nPaper content:\n{markdown_content}\n\nQuestion: {last_message}"

    return [
        ell.system(system_prompt),
        ell.user(prompt),
    ]


def display_response(response: str, mode: str = "chat") -> None:
    """
    Enhance terminal output with rich formatting.
    Different modes get different visual styles to help distinguish types of responses.
    """
    styles = {
        "chat": {
            "title": "AI Response",
            "border_style": "blue",
            "padding": (1, 2),
        },
        "summary": {
            "title": "📝 Summary",
            "border_style": "green",
            "padding": (1, 2),
        },
        "deep": {
            "title": "🔍 Deep Analysis",
            "border_style": "magenta",
            "padding": (1, 2),
        },
        "critique": {
            "title": "⚖️ Critical Review",
            "border_style": "yellow",
            "padding": (1, 2),
        },
        "connect": {
            "title": "🔗 Connections",
            "border_style": "cyan",
            "padding": (1, 2),
        },
        "explain": {
            "title": "📚 Explanation",
            "border_style": "bright_blue",
            "padding": (1, 2),
        },
        "error": {
            "title": "❌ Error",
            "border_style": "red",
            "padding": (1, 2),
        },
    }

    # Get style configuration for the current mode
    style = styles.get(mode, styles["chat"])

    content = Markdown(response)

    # Display the panel with mode-specific styling
    rprint(
        Panel(
            content,
            title=style["title"],
            border_style=style["border_style"],
            padding=style["padding"],
        )
    )


# note: maybe be useful in the future, when introducing section-based chunking
class ReadingProgress:
    def __init__(self, paper_content: str) -> None:
        self.sections = self._extract_sections(paper_content)
        self.progress = {section: 0 for section in self.sections}
        self.notes = {section: [] for section in self.sections}

    def _extract_sections(self, content: str) -> list[str]:
        """Extract section headers from markdown content."""
        sections = []
        for line in content.split("\n"):
            if line.startswith("##") and not line.startswith("###"):
                # Extract section name without ## and whitespace
                section = line.replace("#", "").strip()
                sections.append(section)
        return sections if sections else ["Main Content"]

    def update_progress(self, section: str, status: int) -> None:
        """Update reading progress (0-100%) for a section."""
        self.progress[section] = status

    def add_note(self, section: str, note: str) -> None:
        """Add a note to a specific section."""
        self.notes[section].append(note)

    def get_summary(self) -> str:
        """Get reading progress summary."""
        summary = "## Reading Progress\n\n"
        for section, progress in self.progress.items():
            summary += f"- {section}: {progress}% complete\n"
        return summary


def export_to_obsidian(notes: dict, filename: str):
    """Export notes to Obsidian-compatible format."""
    obsidian_content = "---\n"
    obsidian_content += f"title: {filename}\n"
    obsidian_content += f"date: {datetime.now().strftime('%Y-%m-%d')}\n"
    obsidian_content += "tags: [research, papers]\n"
    obsidian_content += "---\n\n"

    for section, section_notes in notes.items():
        obsidian_content += f"## {section}\n\n"
        for note in section_notes:
            obsidian_content += f"- {note}\n"

    return obsidian_content


if __name__ == "__main__":
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file

    # Read and enhance paper content
    paper_content = read_markdown_file(input_file)
    original_content = (
        read_markdown_file(output_file) if os.path.exists(output_file) else ""
    )

    # Initialize reading progress
    message_history = []

    # Display initial summary
    display_response(
        "Welcome! I'll help you read this paper. Here's a quick summary:",
        "chat",
    )
    response = paper_chat_mode("summary", [], paper_content)
    display_response(response.text, "summary")
    message_history.extend(response)

    while True:
        print("-" * 79)
        print("Available modes: summary, deep, critique, connect, explain")
        user_input = input("You: (type 'exit' to quit) ")

        if user_input.lower() == "exit":
            break

        # Check if mode is specified
        if user_input.startswith("/"):
            mode = user_input[1:].split()[0]
            query = " ".join(user_input.split()[1:])
            if mode in ["summary", "deep", "critique", "connect", "explain"]:
                message_history.append(ell.user(query))
                print("-" * 79)
                print(f"Thinking... (Mode: {mode})")
                response = paper_chat_mode(
                    mode, message_history, paper_content
                )
                display_response(response.text, mode)
                message_history.extend(response)
                continue

        # Default chat mode
        message_history.append(ell.user(user_input))
        print("-" * 79)
        print("Thinking...")
        response = academic_chat_bot(message_history, paper_content)
        display_response(response.text)
        message_history.extend(response)

    print("-" * 79)
    user_input = input("Save conversation? (y/N): ")
    if user_input.lower() == "y":
        print("Thinking...")
        response = organize_conversation_bot(message_history, original_content)

        # Export to both markdown and Obsidian formats
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(response.text)

        print("Conversation saved to", output_file)

    print("Exiting...")
