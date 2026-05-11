# ResumeMatchingEngine
AI Talent Matcher: Advanced TF-IDF & Global Allocation

#  Project Overview

This project is an AI-driven recruitment engine developed for the Redrob AI Campus Hackathon. It automates the matching of candidates to specific Job Descriptions (JDs) using Information Retrieval (IR) techniques. Unlike basic keyword search, this system evaluates the "uniqueness" of skills and the "focus" of a candidate's profile to find the most mathematically compatible match.




# Core Logic & Methodology

1. Skill Normalization & Sanitization
   Resumes are inherently messy. To ensure accuracy, the system implements a strict normalization pipeline:

   Alias Mapping: Standardizes variations (e.g., "Pyhton" → "python", "Reacts" → "react").

   Tokenization: Splits raw data into discrete tokens while respecting multi-word phrases.

   Noise Reduction: Discards any skill not present in the provided SKILL_ALIASES to ensure the vector space remains relevant.


2. The Vector Space Model (TF-IDF)
   Instead of simple counting, we use TF-IDF to weigh skills.

   Term Frequency (TF): Measures how much a candidate focuses on a specific skill. A candidate with fewer, more specialized skills will have a higher TF for those skills.

   Inverse Document Frequency (IDF): This is the system's "intelligence." It lowers the weight of common skills (like Python) and boosts the weight of rare skills (like BERT or Kotlin).


3. Similarity CalculationWe represent each resume as a TF-IDF vector and each JD as a binary vector. The Cosine Similarity formula is applied to measure the angle between these vectors:$$Cosine(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$A score of 1.00 indicates perfect alignment, while 0.00 indicates no shared skills.



#  The Two Versions: Evolution of the Engine

# Version 1: The Independent Recommender
  Mechanism: Ranks every candidate for every JD independently.

  Use Case: Ideal for a single company looking for the best talent regardless of market competition.

  Pros: Guaranteed top technical matches for each individual role.
  
#  Version 2: The Global Allocation Optimizer (Final Choice)
   The Problem: In a real-world campus placement, a "superstar" candidate often appears as the top choice for 10 different companies, creating a "talent bottleneck" and leaving other JDs unfilled.

   The Solution: This version implements a Global Priority Assignment algorithm.

   Mechanism:

   Calculates all possible Candidate-JD match scores.

   Sorts the entire market by the highest score first.

   Assigns the candidate to their best-fit role and removes them from the available pool for others.

   Impact: This ensures a fair and realistic distribution of talent, providing companies with candidates who are actually available for hire.