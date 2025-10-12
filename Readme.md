# Flashcard Program

---

## Brief Description

Flashcard Program meant to handle multiple languages and allow setting and sorting by category tags.

---

### TODO

Features to Implement

  > - SQL storage (one SQL db per language)
    > - Category tags system
  > - Sort / Study by Category
  > - Algorithm to determine known and struggle words
  >   - If you get it right X times in a row move to "learned" or "known" maybe separate these two
  > - Missed multiple times flag as need to study and recur more often
  > - Results Page
  >   - Track stats
  > - Errors Page for incomplete flashcards
  >   - Missing info etc

---

### Changelog

---

0.0.0 | Initial | Start: 10 October 2025 | End:

> - Implemented
>   - Basic `user_data.yaml` and `flashcards.db` initialization
>
>   - Basic Input Handling skeleton
>     - Basic String Input
>     - Placeholder flashcard creation input
>
>   - Basic DB Handling
>     - Empty Check
>     - Connection
>     - Tentative DB First Time Setup
>       - For Now creates a basic SQL setup
>         - Languages, Flashcards, Category Tables
>         - Multiple Categories Handling
>     - Return a list of available languages and handling if DNE

---
