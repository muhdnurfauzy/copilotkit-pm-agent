import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from copilotkit import CopilotKitRemoteEndpoint, Action
from copilotkit.integrations.fastapi import add_fastapi_endpoint

app = FastAPI()

# Enable CORS so your React/Next.js frontend can communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example backend agent action
def handle_task_creation(title: str, priority: str = "normal"):
    return f"Task '{title}' created with {priority} priority in backend."

# Define the CopilotKit action schema
task_action = Action(
    name="create_task",
    description="Creates a task in the backend system",
    parameters=[
        {"name": "title", "type": "string", "description": "Title of the task", "required": True},
        {"name": "priority", "type": "string", "description": "Priority (low, normal, high)", "required": False},
    ],
    handler=handle_task_creation,
)

# Mount the CopilotKit endpoint
sdk = CopilotKitRemoteEndpoint(actions=[task_action])
add_fastapi_endpoint(app, sdk, "/copilotkit")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)