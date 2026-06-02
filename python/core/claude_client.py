import os
import time
import anthropic

class ClaudeClient:
    MODEL = "claude-sonnet-4-6"
    MAX_TOKENS = 1024

    def __init__(self):
        self.api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            # fallback: read directly from .env
            with open(os.path.expanduser("~/.env") if not os.path.exists(".env") else ".env") as f:
                for line in f:
                    if line.startswith("ANTHROPIC_API_KEY="):
                        self.api_key = line.strip().split("=", 1)[1].strip('"').strip("'")
        if not self.api_key:
            raise EnvironmentError("ANTHROPIC_API_KEY not set")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def ask(self, prompt, system=None, verbose=False):
        kwargs = {
            "model": self.MODEL,
            "max_tokens": self.MAX_TOKENS,
            "messages": [{"role": "user", "content": prompt}],
        }
        if system:
            kwargs["system"] = system
        t0 = time.time()
        response = self.client.messages.create(**kwargs)
        latency = round((time.time() - t0) * 1000)
        text = response.content[0].text
        if verbose:
            u = response.usage
            print(f"[claude] {latency}ms | in={u.input_tokens} out={u.output_tokens}")
        return text

if __name__ == "__main__":
    print("Testing Claude API connection...")
    try:
        client = ClaudeClient()
        reply = client.ask("Confirm you are connected as itops-ai assistant in one sentence.", verbose=True)
        print(f"\n✓ Connected\n{reply}")
    except Exception as e:
        print(f"\n✗ Failed: {e}")
