from __future__ import annotations

import os
from flask import Flask, request, jsonify

# Make sure the parent package is importable when running in Docker
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents import healthcare_agent

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "service": "healthcare-adk-agent"})


@app.route("/v1/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt") or data.get("query") or data.get("text")
    if not prompt:
        return jsonify({"error": "missing prompt"}), 400

    try:
        res = healthcare_agent(prompt)
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
