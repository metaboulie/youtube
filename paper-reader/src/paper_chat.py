import argparse
import os
import ell
from ell import Message
from openai import OpenAI

MODEL = "llama3.2"

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

# ell.config.verbose = True

ell.config.register_model(MODEL, client)

# ell.init(store="./logdir", autocommit=True, verbose=True)


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

    **Capabilities**:
    - Handle markdown-formatted text efficiently, recognizing headings, subheadings, lists, and code blocks.
    - Perform topic extraction and summarization for quick review.
    - Provide cross-references to related academic content when requested.

    You will receive academic papers in markdown format and must respond accordingly to help the user comprehend the material as efficiently as possible.
    """
    return f"Context:\n ---------- \n {markdown_content} \n ---------------\n History: {message_history[:-1]} \n ---------- \n Question: {message_history[-1]} \n ---------------\n Response:"


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
    return f"Existing notes:\n ---------- \n {original_content} \n ---------------\n Conversation history: {message_history} \n ---------- \n  Updated notes:"


def read_markdown_file(file_path: str) -> str:
    """
    Reads the content of a markdown file and returns it as a string.

    Args:
        file_path (str): The path to the markdown file.

    Returns:
        str: The content of the markdown file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")


def parse_args():
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument(
        "input_file", type=str, help="Path to the input markdown file."
    )
    parser.add_argument(
        "output_file", type=str, help="Path to the output markdown file."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file
    paper_content = read_markdown_file(input_file)
    original_content = (
        read_markdown_file(output_file) if os.path.exists(output_file) else ""
    )

    message_history = []

    while True:
        print("-" * 79)
        user_input = input("You: (type 'exit' to quit) ")
        if user_input.lower() == "exit":
            break
        message_history.append(ell.user(user_input))
        print("-" * 79)
        print("Thinking...")
        response = academic_chat_bot(message_history, paper_content)
        print("Bot:", response.text)
        message_history.append(response)

    print("-" * 79)
    user_input = input("Save conversation? (y/N): ")
    if user_input.lower() == "y":
        print("Thinking...")
        response = organize_conversation_bot(message_history, original_content)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(response.text)

        print("Conversation saved to", output_file)

    print("Exiting...")
