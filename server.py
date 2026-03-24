print("Starting server...")
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os
import sys
import traceback

# Add your project folder to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app)

# ✅ 2GB upload limit
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 * 1024


# ── Serve frontend ─────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")


# ── Column detection endpoint ──────────────────────────────
@app.route("/api/columns", methods=["POST"])
def get_columns():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    try:
        # ✅ Reset file pointer
        file.seek(0)

        # ✅ Handle encoding issues
        try:
            df = pd.read_csv(file, nrows=5, encoding='utf-8')
        except:
            file.seek(0)
            df = pd.read_csv(file, nrows=5, encoding='latin1')

        return jsonify({
            "columns": list(df.columns),
            "preview": df.head(3).to_dict(orient="records")
        })

    except Exception as e:
        print("COLUMN ERROR:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 400


# ── Main prediction endpoint ───────────────────────────────
@app.route("/api/predict", methods=["POST"])
def predict():
    from main import run_pipeline
    
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file        = request.files["file"]
    date_col    = request.form.get("date_col")
    vendor_col  = request.form.get("vendor_col")
    sales_col   = request.form.get("sales_col")
    brand_col   = request.form.get("brand_col") or None
    product_col = request.form.get("product_col") or None

    if not all([date_col, vendor_col, sales_col]):
        return jsonify({"error": "date_col, vendor_col and sales_col are required"}), 400

    try:
        # ✅ Save file (no RAM overload)
        file_path = "/tmp/temp.csv"
        file.save(file_path)

        # Run ML pipeline
        output, results, best = run_pipeline(
            file_path,
            date_col,
            vendor_col,
            sales_col,
            brand_col,
            product_col
        )

        # Model accuracy table
        model_results = [
            {"model": k, "accuracy": round(v["accuracy"], 2)}
            for k, v in results.items()
            if v.get("accuracy") is not None
        ]
        model_results.sort(key=lambda x: x["accuracy"], reverse=True)

        predictions = output.to_dict(orient="records")

        # ✅ Clean temp file
        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({
            "best_model": best,
            "predictions": predictions,
            "model_results": model_results,
        })

    except Exception as e:
        print("PREDICTION ERROR:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ── SQLite history endpoint ────────────────────────────────
@app.route("/api/history", methods=["GET"])
def history():
    try:
        from database import load_from_db
        df = load_from_db()

        return jsonify({
            "data": df.tail(200).to_dict(orient="records"),
            "total": len(df)
        })

    except Exception as e:
        print("DB ERROR:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# ── Run server ─────────────────────────────────────────────
if __name__ == "__main__":
    import os
    from waitress import serve
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}...")
    serve(app, host="0.0.0.0", port=port)