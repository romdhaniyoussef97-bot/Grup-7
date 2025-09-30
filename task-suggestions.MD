
## 👥 Task Distribution

### Person 1 – API Client & Integration
**Responsibilities**
- Connect to TMDb API and fetch:
  - Movies by title and genre  
  - Related movie recommendations  
  - Reviews  
- Integrate all modules (`movie`, `review`, `favorites`, `suggestions`) so they work together.  
- Perform final end-to-end testing.  

---

### Person 2 – Movie Model & Filtering
**Responsibilities**
- Create `Movie` class with attributes:
  - title, genre, rating, vote_count, id  
- Implement filtering by:
  - Genre  
  - Rating / minimum vote count  
- Implement suggestion logic:
  - Recommend movies based on genre & rating preferences  

---

### Person 3 – Reviews & Sentiment Analysis
**Responsibilities**
- Fetch reviews from the API client.  
- Apply **VADER Sentiment Analysis**:
  - Positive, Neutral, Negative classification  
- Summarize community sentiment for each movie.  
- Return clean results for console output.  

---

### Person 4 – Favorites & Console Menu
**Responsibilities**
- Build the **text-based console menu**, example layout:

Main Menu:  
1. Search movie by title  
2. Browse by genre  
3. Filter by rating  
4. Suggest movies by genre & rating  
5. Show reviews & sentiment  
6. Manage favorites  
7. Exit  

- Implement favorites system:
  - Save/remove favorites in JSON  
  - Optional: extend to SQLite  
- Display movies & favorites using **PrettyTable**  

---
            +------------------+
            |   Console Menu   |  <-- User input (search, filter, suggest)
            +--------+---------+
                     |
                     v
            +------------------+
            |   API Client     |  <-- Fetch movies, reviews, recommendations
            +--------+---------+
                     |
         -------------------------
         |                       |
         v                       v
 +---------------+        +---------------+
 |   Movie       |        |   Review      |  <-- Sentiment analysis
 |   Module      |        |   Module      |
 +-------+-------+        +-------+-------+
         |                       |
         |                       v
         |                Sentiment results
         |
         v
 +---------------+
 |   Favorites   |  <-- Save/remove favorites
 +-------+-------+
         |
         v
 +------------------+
 | Console Output   |  <-- Display movies, suggestions, reviews, favorites
 +------------------+
