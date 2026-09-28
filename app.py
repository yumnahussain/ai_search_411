import os
import json
from flask import Flask, render_template, jsonify, request
from uninformed import bfs, dfs, ucs, ids
from informed import greedy_best_first, a_star

app = Flask(__name__)

MAP_DATA_FILE = os.path.join(app.root_path, "map_data.json")

ALGORITHMS = {
    "bfs": bfs,
    "dfs": dfs,
    "ucs": ucs,
    "ids": ids,
    "greedy": greedy_best_first,
    "astar": a_star,
}


def load_map_data():
    """Load graph and location data from map_data.json if available."""
    if os.path.exists(MAP_DATA_FILE):
        try:
            with open(MAP_DATA_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {MAP_DATA_FILE}: {e}")
    return {
        "region": "State / Metro Area",
        "total_cities": 0,
        "total_edges": 0,
        "locations": {},
        "graph": {}
    }


@app.route("/")
def index():
    """Renders the main deployment webpage."""
    return render_template("index.html")


@app.route("/api/map", methods=["GET"])
def get_map():
    """Returns map locations and graph connections."""
    data = load_map_data()
    return jsonify(data)


@app.route("/api/search", methods=["POST"])
def search():
    """Run the requested graph search and return data used by the visualizer."""
    payload = request.get_json() or {}
    start = payload.get("start", "")
    goal = payload.get("goal", "")
    algorithm = payload.get("algorithm", "")

    search_function = ALGORITHMS.get(algorithm)
    if search_function is None:
        return jsonify({
            "message": f"The '{algorithm}' algorithm is not available.",
            "path": [],
        }), 400

    map_data = load_map_data()
    result = search_function(map_data, start, goal)
    path = result["path"] or []

    return jsonify({
        "status": "success" if path else "no_path",
        "message": "Path found." if path else "No path found for the selected cities.",
        "path": path,
        "cost": result["distance"],
        "nodes_expanded": result["expanded"],
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
