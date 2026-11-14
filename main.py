import os
import sys

JOKE = "I put 'Back up the database before every deploy' in AGENTS.md. My agent backed it up to /dev/null."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    joke_bytes = JOKE.encode("utf-8")

    with open(output_path, "wb") as f:
        f.write(joke_bytes)

    # Post-write verification
    with open(output_path, "rb") as f:
        written_data = f.read()

    if len(written_data) != len(joke_bytes):
        print(f"Error: byte size mismatch ({len(written_data)} vs {len(joke_bytes)})", file=sys.stderr)
        sys.exit(1)

    print(f"Verification successful: byte size matches ({len(written_data)} bytes).")

    char_count = len(JOKE)
    print(f"Wrote joke to {output_path} ({char_count} characters)")

if __name__ == "__main__":
    main()
