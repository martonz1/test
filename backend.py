# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# Allow the frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Simple in-memory lesson data (no database yet) ---

lessons = [
    {
        "id": 1,
        "title": "Greetings",
        "words": [
            {"dutch": "Hallo",       "english": "Hello"},
            {"dutch": "Goedemorgen", "english": "Good morning"},
            {"dutch": "Goedemiddag", "english": "Good afternoon"},
            {"dutch": "Goedenavond", "english": "Good evening"},
            {"dutch": "Tot ziens",   "english": "Goodbye"},
        ]
    },
    {
        "id": 2,
        "title": "Numbers",
        "words": [
            {"dutch": "Één",   "english": "One"},
            {"dutch": "Twee",  "english": "Two"},
            {"dutch": "Drie",  "english": "Three"},
            {"dutch": "Vier",  "english": "Four"},
            {"dutch": "Vijf",  "english": "Five"},
        ]
    },
    {
        "id": 3,
        "title": "Colors",
        "words": [
            {"dutch": "Rood",   "english": "Red"},
            {"dutch": "Blauw",  "english": "Blue"},
            {"dutch": "Groen",  "english": "Green"},
            {"dutch": "Geel",   "english": "Yellow"},
            {"dutch": "Zwart",  "english": "Black"},
        ]
    },
]

# --- API Routes ---

@app.get("/api/lessons")
def get_lessons():
    """Return list of all lessons (without words)."""
    return [{"id": l["id"], "title": l["title"], "word_count": len(l["words"])} for l in lessons]

@app.get("/api/lessons/{lesson_id}")
def get_lesson(lesson_id: int):
    """Return a specific lesson with all its words."""
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return lesson
    return {"error": "Lesson not found"}, 404

@app.get("/api/lessons/{lesson_id}/random")
def get_random_word(lesson_id: int):
    """Return a random word from a lesson (for practice)."""
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            word = random.choice(lesson["words"])
            return {"lesson": lesson["title"], "word": word}
    return {"error": "Lesson not found"}, 404

# Serve the frontend
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(f"{__name__}:app", host="0.0.0.0", port=4000, reload=True)
