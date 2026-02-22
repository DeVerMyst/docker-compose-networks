FROM python:3.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_SYSTEM_PYTHON=1
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-cache -r pyproject.toml
COPY . .
CMD ["uvicorn", "child_api:app", "--host", "0.0.0.0", "--port", "8001"]