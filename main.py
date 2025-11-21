from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from crew import create_crew
import os
import uuid

app = FastAPI()


class RequestModel(BaseModel):
    topic: str


@app.post("/run")
def run_pipeline(request: RequestModel):
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": request.topic})

    # Extract final output
    final_output = result.raw if hasattr(result, "raw") else result

    # ensure folder exists
    os.makedirs("outputs", exist_ok=True)

    # create safe filename based on topic
    safe_topic = (
        request.topic
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
        .replace(",", "_")
        .replace(".", "_")
    )

    filename = f"{safe_topic}.md"
    save_path = os.path.join("outputs", filename)

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(final_output)

    print("Saved file:", save_path)

    # Extracting each task's output in order
    steps = {}
    if hasattr(result, "tasks_output") and result.tasks_output:
        if len(result.tasks_output) >= 1:
            steps["research"] = result.tasks_output[0].raw
        if len(result.tasks_output) >= 2:
            steps["analysis"] = result.tasks_output[1].raw
        if len(result.tasks_output) >= 3:
            steps["writing"] = result.tasks_output[2].raw
        if len(result.tasks_output) >= 4:
            steps["quality_check"] = result.tasks_output[3].raw

    return {
        "topic": request.topic,
        "final_article": final_output,
        "download_url": f"/download/{filename}",
        "steps": steps
    }


@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join("outputs", filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    return FileResponse(path=file_path, filename=filename, media_type="text/markdown")
