# AI_Website_Generator
LLM powered website generator



---

# AI Website Generator – Project Documentation

## 1. Project Overview

The **AI Website Generator** is a web application that allows users to describe a website in natural language and receive a fully generated **HTML + CSS** website with a **live preview**.
The system uses an **open-source Hugging Face language model** running locally via a **FastAPI backend**, eliminating dependency on proprietary APIs.

---

## 2. Key Features

* Form-based user interface for entering website requirements
* AI-powered website code generation (HTML + CSS)
* Live preview using an iframe
* Fully local and open-source model usage
* Export-ready generated code
* Modular backend and frontend architecture

---

## 3. System Architecture

### High-Level Architecture

```
User (Browser)
   |
(HTTP (JSON))
   |
   V 
Frontend (HTML + JS)
   |
(POST /generate)
   |
   V
FastAPI Backend (Python)
   |
(Prompt Engineering)
   |
   V
Hugging Face LLM (TinyLlama)
   |
(Generated Code)
   |
   V
Backend => Frontend => Live Preview
```

---

## 4. Technology Stack

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* iframe (`srcdoc`) for preview

### Backend

* Python 3.10+
* FastAPI
* Uvicorn
* Hugging Face Transformers
* PyTorch

### AI Model

* **TinyLlama (open-source)**
* Runs locally (no API calls required)
* Instruction-tuned LLM

---

## 5. Model Selection Rationale

### Why TinyLlama?

| Criteria          | Reason                          |
| ----------------- | ------------------------------- |
| Open-source       | No licensing or API costs       |
| Lightweight       | Can run on CPU                  |
| Instruction-tuned | Handles structured prompts well |
| Offline capable   | No Hugging Face token required  |

TinyLlama provides a good balance between **performance and resource efficiency**, making it suitable for local development and academic projects.

---

## 6. Backend Design

### Framework: FastAPI

FastAPI was chosen because:

* High performance (ASGI)
* Automatic request validation
* Easy JSON handling
* Built-in documentation support

---

### API Endpoint

#### `POST /generate`

**Request Body**

```json
{
  "prompt": "A portfolio website with contact form"
}
```

**Response Body**

```json
{
  "html": "<div>...</div>",
  "css": "body { ... }"
}
```

---

### Backend Workflow

1. Receive user prompt
2. Inject prompt into instruction template
3. Pass prompt to TinyLlama
4. Parse model output into HTML and CSS
5. Return structured JSON response

---

### Prompt Template Example

```
You are a web developer.
Generate valid HTML and CSS only.
Return JSON in this format:
{
  "html": "...",
  "css": "..."
}
User request: {prompt}
```

This ensures predictable, machine-readable output.

---

## 7. Frontend Design

### UI Components

* Textarea for user prompt
* Generate button
* iframe for live preview

---

### Frontend Workflow

1. User enters website description
2. JavaScript sends POST request to backend
3. Backend returns generated code
4. iframe updates using `srcdoc`

---

### Preview Rendering Logic

```javascript
iframe.srcdoc = `
<style>${css}</style>
${html}
`;
```

This allows instant preview without file downloads or page reloads.

---

## 8. Error Handling

### Frontend

* Empty prompt validation
* Backend error alerts
* JSON parsing checks

### Backend

* Request validation using Pydantic
* Model inference error handling
* Graceful fallback responses

---

## 9. Export Feature (Design)

Although deployment is excluded, the system supports export by:

### Option 1: Manual Copy

* User copies generated HTML/CSS

### Option 2: Download Buttons (Extendable)

* Download `.html` and `.css` files
* ZIP bundling (future enhancement)

---

## 10. Security Considerations

* No user authentication required
* Local-only execution
* No external API calls
* CORS configured for local development

---

## 11. Limitations

* Output quality depends on model size
* No JavaScript generation (by design)
* No persistent storage
* Single-user local usage

---

## 12. Future Enhancements

* JavaScript generation support
* Multi-page website generation
* Model fine-tuning
* Template selection
* User authentication
* Cloud deployment

---

## 13. Project Deliverables Mapping

| Requirement          | Status      |
| -------------------- | ----------- |
| User interface       | Implemented |
| AI model integration | Implemented |
| Live preview         | Implemented |
| Export functionality | Designed    |
| Documentation        | Completed   |

---

## 14. Conclusion

This project demonstrates a complete **AI-assisted web development workflow** using **open-source tools only**. It highlights prompt engineering, model integration, frontend-backend communication, and real-time rendering thus making it a strong foundation for future AI-powered developer tools.

