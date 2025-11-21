from crewai import Task
from agents import researcher, analyst, writer, quality_checker


research_task = Task(
    description=(
        "Search the web and gather the latest, factual, unbiased information about the topic: "
        "\"{topic}\".\n\n"
        "Use multiple online sources, cross-check claims, and strictly avoid hallucinations."
    ),
    expected_output=(
        "A structured research summary containing:\n"
        "- Key facts\n"
        "- Latest updates\n"
        "- Statistics (if available)\n"
        "- Bullet-point highlights\n"
        "- Source links"
    ),
    agent=researcher,
    input_variables=["topic"],
    output_file="01_research_summary.md"
)


analysis_task = Task(
    description=(
        "Analyze the provided research summary.\n"
        "Extract deeper insights, compare viewpoints, identify trends, and highlight contradictions."
    ),
    expected_output=(
        "An analytical breakdown including:\n"
        "- Key insights\n"
        "- Trends\n"
        "- Pros & Cons\n"
        "- Conflicting information (if any)"
    ),
    agent=analyst,
    output_file="02_analysis.md"
)


writing_task = Task(
    description=(
        "Convert the analytical breakdown into a well-structured article.\n"
        "Write 2–3 engaging paragraphs suitable for a tech blog or LinkedIn post."
    ),
    expected_output=(
        "A polished article with:\n"
        "- A strong introduction\n"
        "- Main body summarizing insights\n"
        "- Clear conclusion"
    ),
    agent=writer,
    output_file="03_written_article.md"
)


quality_check_task = Task(
    description=(
        "Review the article for quality, correctness, clarity, grammar, and factual accuracy.\n"
        "Fix any issues and produce the final publish-ready version."
    ),
    expected_output="A final, polished version of the article.",
    agent=quality_checker,
    output_file="04_final_article.md"
)
