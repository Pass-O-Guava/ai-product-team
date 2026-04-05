"""OpenClaw agent wrapper using subprocess."""
import json
import subprocess
import sys
from typing import Any, Optional


class OpenClawClient:
    """Thin wrapper around the OpenClaw CLI for agent invocation."""

    def __init__(self, binary: str = "openclaw"):
        self.binary = binary

    def invoke(self, task: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        """
        Invoke an OpenClaw agent/task via CLI.
        Returns parsed JSON output, or raises RuntimeError.
        """
        args = [self.binary, "invoke", task]
        if params:
            args.append("--params")
            args.append(json.dumps(params))
        try:
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=120,
            )
            if result.returncode != 0:
                raise RuntimeError(f"OpenClaw error: {result.stderr.strip()}")
            out = result.stdout.strip()
            if out:
                try:
                    return json.loads(out)
                except json.JSONDecodeError:
                    return {"output": out}
            return {}
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"OpenClaw invoke timed out after 120s: {task}")
        except FileNotFoundError:
            raise RuntimeError(f"OpenClaw binary not found: {self.binary}")

    def is_available(self) -> bool:
        """Check whether the OpenClaw CLI is accessible."""
        try:
            subprocess.run(
                [self.binary, "--version"],
                capture_output=True,
                timeout=5,
            )
            return True
        except Exception:
            return False


# Global singleton
client = OpenClawClient()
