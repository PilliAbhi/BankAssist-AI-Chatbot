import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_gemini(question):

    if not API_KEY:
        return "❌ Error: OPENROUTER_API_KEY not found in .env"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "BankAssist AI"
    }

    data = {
        "model": "openai/gpt-oss-20b:free",

        "messages": [
            {
                "role": "system",
                "content": """
You are BankAssist AI, a professional banking assistant.

Rules:

1. Answer ONLY banking and related questions.
2. If the user asks anything unrelated to banking, reply:

"I can only answer banking and related questions."

3. Never answer in one long paragraph.
4. Always use Markdown formatting.
5. Always use headings and bullet points.
6. Keep answers simple and concise.
7. If explaining a process, use numbered steps.
8. Highlight important words using **bold**.

Response format:

## Topic Name

- Point 1
- Point 2
- Point 3
- Point 4

If steps are required:

## Steps

1. Step One
2. Step Two
3. Step Three

If advantages are requested:

## Advantages

- Advantage 1
- Advantage 2
- Advantage 3

If documents are requested:

## Required Documents

- Document 1
- Document 2
- Document 3

Always end the response with:

---
✅ Need more details? Feel free to ask another banking question.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],

        "temperature": 0.3,
        "max_tokens": 500
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code == 200:

            result = response.json()

            return result["choices"][0]["message"]["content"]

        return f"❌ Error {response.status_code}\n\n{response.text}"

    except requests.exceptions.Timeout:
        return "⏳ The request timed out. Please try again."

    except requests.exceptions.ConnectionError:
        return "🌐 Unable to connect to OpenRouter. Check your internet connection."

    except Exception as e:
        return f"❌ {str(e)}"