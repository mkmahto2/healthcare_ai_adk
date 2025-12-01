# Deploying the Healthcare ADK Agent

This folder contains a small Flask web wrapper for the ADK agent and a Dockerfile
so you can deploy the agent as a web service (Cloud Run, Cloud Run for Anthos,
GKE, or any container host).

Local run (recommended for testing)

1. Create a venv and install deps:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r deploy/requirements.txt
```

2. Ensure `GEMINI_API_KEY` and `MODEL_NAME` are set in `config.py` (or as environment variables). Example `config.py`:

```py
GEMINI_API_KEY = "YOUR_API_KEY"
MODEL_NAME = "models/text-bison-001"
```

3. Run the service locally:

```powershell
python deploy/app.py
# or using gunicorn for production-like server
gunicorn -b 0.0.0.0:8080 deploy.app:app
```

Container build and run

```powershell
# From repository root
docker build -t healthcare-adk-agent -f deploy/Dockerfile .
docker run -p 8080:8080 -e GEMINI_API_KEY="${env:GEMINI_API_KEY}" healthcare-adk-agent
```

Deploy to Cloud Run (GCP)

1. Build and push image to Artifact Registry or Container Registry.
2. Deploy to Cloud Run with environment vars for `GEMINI_API_KEY`.

Example (gcloud):

```powershell
# Build and push (Cloud Build or docker+gcloud)
gcloud builds submit --tag gcr.io/PROJECT-ID/healthcare-adk-agent

# Deploy
gcloud run deploy healthcare-adk-agent --image gcr.io/PROJECT-ID/healthcare-adk-agent --platform managed --region us-central1 --set-env-vars GEMINI_API_KEY="${env:GEMINI_API_KEY}",MODEL_NAME="models/text-bison-001"
```

GitHub Actions

There is a deploy workflow template at `.github/workflows/deploy-cloudrun.yml`.
It expects a GCP service account JSON stored in `GCP_SA_KEY` secret and the
target `PROJECT_ID` and `IMAGE` to be set as workflow inputs or secrets.

Security note

- Do not store API keys in the repository. Use environment variables or secret
  managers (GCP Secret Manager, GitHub Secrets) and bind them at deploy time.
- Prefer service account + ADC for server deployments rather than using API keys
  in production.
