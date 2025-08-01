import os
import requests
import base64
from flask import Flask, request, render_template, redirect
from dotenv import load_dotenv

app = Flask(__name__)

# ========================
# 🔐 Load or Request API Key
# ========================
def get_api_key():
    load_dotenv()
    api_key = os.getenv("IMGBB_API_KEY")

    if not api_key:
        print("🔐 Please enter your Imgbb API key:")
        api_key = input("➡️ API Key: ").strip()

        # Save to .env
        with open(".env", "a") as f:
            f.write(f"\nIMGBB_API_KEY={api_key}\n")
        print("✅ API key saved to .env file.")

    return api_key


API_KEY = get_api_key()

# ========================
# 🌐 Image Upload Route
# ========================
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            encoded_image = base64.b64encode(file.read()).decode("utf-8")
            url = "https://api.imgbb.com/1/upload"
            payload = {
                "key": API_KEY,
                "image": encoded_image
            }
            res = requests.post(url, data=payload)
            if res.status_code == 200:
                data = res.json()
                image_url = data["data"]["url"]
                print(f"Image uploaded successfully: {image_url}")
                return render_template("upload_result.html", image_url=image_url)
            else:
                return f"❌ Error uploading image: {res.text}"
    return render_template("upload_form.html")

# ========================
# 🚀 Run App
# ========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)