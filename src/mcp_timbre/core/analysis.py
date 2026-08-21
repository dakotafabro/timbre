import re
from dataclasses import dataclass


@dataclass
class WritingMetrics:
    sentence_count: int
    avg_sentence_length: float
    short_sentence_pct: float
    long_sentence_pct: float
    qualifier_count: int
    qualifier_density: float
    exclamation_count: int
    question_count: int
    paragraph_count: int
    avg_paragraph_length: float
    word_count: int


QUALIFIERS = [
    "just", "maybe", "perhaps", "somewhat", "slightly", "a bit",
    "kind of", "sort of", "I think", "I believe", "I feel like",
    "probably", "possibly", "might", "could be", "seems like",
    "in my opinion", "to be honest", "actually", "basically",
    "essentially", "generally", "typically", "usually",
]


def compute_metrics(text: str) -> WritingMetrics:
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    words = text.split()
    word_count = len(words)

    sentence_lengths = [len(s.split()) for s in sentences]
    avg_sentence_length = sum(sentence_lengths) / max(len(sentence_lengths), 1)

    short_threshold = 8
    long_threshold = 25
    short_count = sum(1 for l in sentence_lengths if l <= short_threshold)
    long_count = sum(1 for l in sentence_lengths if l >= long_threshold)

    short_pct = short_count / max(len(sentences), 1)
    long_pct = long_count / max(len(sentences), 1)

    text_lower = text.lower()
    qualifier_count = sum(text_lower.count(q) for q in QUALIFIERS)
    qualifier_density = qualifier_count / max(word_count / 100, 1)

    exclamation_count = text.count("!")
    question_count = text.count("?")

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    paragraph_count = len(paragraphs)
    avg_paragraph_length = sum(len(p.split()) for p in paragraphs) / max(paragraph_count, 1)

    return WritingMetrics(
        sentence_count=len(sentences),
        avg_sentence_length=round(avg_sentence_length, 1),
        short_sentence_pct=round(short_pct, 2),
        long_sentence_pct=round(long_pct, 2),
        qualifier_count=qualifier_count,
        qualifier_density=round(qualifier_density, 1),
        exclamation_count=exclamation_count,
        question_count=question_count,
        paragraph_count=paragraph_count,
        avg_paragraph_length=round(avg_paragraph_length, 1),
        word_count=word_count,
    )


def detect_register(text: str, context: str = "") -> str:
    combined = (text + " " + context).lower()

    if any(w in combined for w in ["hi ", "hey ", "dear ", "regards", "kindly", "best,"]):
        return "email"
    if any(w in combined for w in ["slack", "dm", "thread", "channel"]):
        return "slack"
    if any(w in combined for w in ["```", "function", "class ", "def ", "import ", "module"]):
        return "technical"
    if any(w in combined for w in ["abstract", "methodology", "findings", "hypothesis"]):
        return "academic"
    if any(w in combined for w in ["once upon", "she said", "he walked", "the room was"]):
        return "narrative"

    return "general"
