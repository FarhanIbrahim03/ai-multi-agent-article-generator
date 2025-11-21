from crewai import Crew
from agents import researcher, analyst, writer, quality_checker
from tasks import (
    research_task,
    analysis_task,
    writing_task,
    quality_check_task
)


def create_crew():
    crew = Crew(
        agents=[researcher, analyst, writer, quality_checker],
        tasks=[research_task, analysis_task, writing_task, quality_check_task],
        verbose=True,
        planning=False  # enables task sequencing & smarter orchestration
    )
    return crew


if __name__ == "__main__":
    crew = create_crew()

    result = crew.kickoff(inputs={"topic": "Latest advancements in AI agents"})

    print("\n=== MODEL USED ===")
    print("LLM:", crew.agents[0].llm.model)

    print("\n=== Final Answer ===\n")
    print(result)

