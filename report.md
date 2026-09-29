# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Yumna Hussain
- **UID (netID):** yhuss3
- **UIN:** 673006309

---

## Section 1: Selected City Region
- **Selected Region:** Greater Seattle Area, Washington, USA

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 35
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://four11-project-1-ai-search.onrender.com/
- **Video Presentation Link:** [Provide an accessible link to your 5–7 minute video presentation]

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    A* is the best algorithm for this route finding problem. It looks at the distance already traveled and estimates how far the destination is using the heuristic, which reduces the number of nodes we need to explore. This makes it better than UCS because it explores fewer nodes. It is also more efficient than Greedy because it finds the shortest route, and it is more cost effective than BFS and DFS because they do not consider the road distance when choosing which city to explore next.
- **Search Efficiency (Nodes expanded/time taken comparison):** For the route from Everett, WA to Lakewood, WA, BFS and UCS both explored 22 nodes and found a route that cost 81.57 miles. DFS explored 18 nodes, but found a longer route of 107.01 miles because it follows one path before checking other routes. IDS found the same 81.57-mile route as BFS, but it explored 450 nodes because it repeats the search at different levels. Greedy Best-First Search explored the fewest nodes with only 8. A* explored 9 nodes and found the same 81.57-mile route. Even though Greedy explored one less node, A* is more reliable because it finds the lowest-cost route.
- **Link the idea of search algorithm to today Generative AI.** 
    The search algorithm is important in Generative AI because the concept of predicting the next best token relies on both cost, efficiency, and accuracy. A good combination of cost, efficiency, and accuracy is also what makes for the most optimal search algorithm. A generative AI model should be able to predict the RIGHT token, in the cheapest way possible while providing accurate information.
