# AI Game Builder — LLM Pipeline with Self-Correction, RAG & Memory

## Overview

AI Game Builder is a backend system that converts natural language prompts into playable **Phaser.js games** using a structured **LLM pipeline**.

Unlike one-shot generation systems, this project introduces:

* **Intermediate representations (GDD)**
* **Validation layers**
* **Iterative correction loops**
* **RAG (Retrieval-Augmented Generation)**
* **Persistent memory of past failures**

This makes the system more reliable and closer to real-world AI coding systems.

---

## Problem

LLMs often generate **incorrect or non-executable code** due to:

* API hallucinations
* Syntax errors
* Lack of grounding

---

## Solution

This project treats code generation as a **multi-stage pipeline** instead of a single prompt.

```
User Prompt
   ↓
Game Design Generator (GDD)
   ↓
Code Generator (Phaser HTML)
   ↓
Validator (detects errors)
   ↓
LLM Correction Loop
   ↓
Memory + RAG (improves future runs)
```

---

## Key Features

*  **Iterative Correction Loop**

  * Automatically fixes errors using LLM feedback
*  **RAG Integration**

  * Injects Phaser rules to reduce hallucinations
*  **Memory System**

  * Stores past errors to improve future generations
*  **Validator**

  * Detects incorrect APIs, syntax issues, and bad patterns
*  **Structured Pipeline**

  * Uses Game Design Document (GDD) as intermediate representation

---

##  Example Output

### Generated GDD

* Genre: Action
* Mechanics: Gravity, Jumping, Collision, Score

### Generated Code Issues (Real Example)

* Incorrect API usage (`this.add.sprite` instead of physics)
* Syntax error (`this physics.add.sprite`)
* Invalid methods (`setBodyImpulse`, `colliderect`)

See actual output: 

---

##  Correction Loop Behavior

```
Attempt 1 → Error detected
Attempt 2 → Same error persists
Attempt 3 → Still unresolved
```

This revealed a key insight:

> LLMs fail to correct code unless correction is **constrained and guided**

---

##  Key Learnings

* LLMs are unreliable in unconstrained generation
* Validation + feedback loops are essential
* RAG must be **minimal and targeted**
* Convergence is critical for iterative systems
* Memory helps reduce repeated failures

---

## ⚠️ Limitations

- Code generation not fully reliable
- Requires multiple retries
- Limited Phaser coverage

---

##  Tech Stack

* **Backend:** FastAPI
* **LLM Runtime:** Ollama (local models like Llama3, CodeLlama)
* **Game Engine:** Phaser.js
* **Language:** Python

---

##  Project Structure

```
backend/
├── pipeline/
│   ├── orchestrator.py
│   ├── gdd_agent.py
│   ├── code_agent.py
│   ├── correction_agent.py
│   ├── validator.py
│
├── rag/
├── memory/
├── utils.py
```

---

## 🎮 Demo

Below is a working example generated (and stabilized) by the pipeline:

👉 Open `demo/flappy.html` in browser

Features:
- Bird jump mechanic
- Procedural pipe generation
- Collision detection
- Score tracking
---

##  Future Work

* Hybrid template + LLM system (for stability)
* Vector database for advanced RAG
* AST-based code validation
* Multi-model routing (design vs code generation)
* Frontend game editor

---

##  Why This Project Matters

This project explores how to build **reliable AI systems** using:

* Structured pipelines
* Feedback loops
* Self-correction mechanisms

It moves beyond simple prompt engineering into **system design for AI-assisted programming**.

---

##  Author

Nishant Tiwari

---

##  If you found this interesting, consider starring the repo!

