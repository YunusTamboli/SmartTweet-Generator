from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        brand = request.form.get("brand")
        industry = request.form.get("industry")
        objective = request.form.get("objective")
        product = request.form.get("product")

        brand_lower = brand.lower()

        tone = "engaging"
        audience = "general audience"
        theme = "innovation"

        if "nike" in brand_lower:
            tone = "motivational"
            audience = "athletes and fitness enthusiasts"
            theme = "performance and achievement"

            templates = [
                f"Push beyond limits with {brand}. Every step counts.",
                f"Train harder. Run faster with {brand}.",
                f"Built for champions. Discover {product}.",
                f"Your journey to greatness starts today.",
                f"Fuel your ambition with {brand}.",
                f"Designed for athletes who never quit.",
                f"Performance meets determination.",
                f"Step into confidence with {brand}.",
                f"Victory starts with preparation.",
                f"Greatness begins with the first step."
            ]

        elif "apple" in brand_lower:
            tone = "premium and minimal"
            audience = "tech enthusiasts"
            theme = "innovation and simplicity"

            templates = [
                "Simplicity meets innovation.",
                "Designed with precision.",
                "Experience the future with Apple.",
                "Powerful. Elegant. Effortless.",
                "Technology reimagined.",
                "Innovation made simple.",
                "Where design meets performance.",
                "The next generation of technology.",
                "Minimal design. Maximum impact.",
                "Precision engineered."
            ]

        else:
            templates = [
                f"Discover the future of {industry} with {brand}.",
                f"Innovation starts with {brand}.",
                f"Experience the difference with {product}.",
                f"{brand} is shaping the future of {industry}.",
                f"Built for people who expect more.",
                f"The next step in {industry} begins now.",
                f"Where innovation meets reliability.",
                f"Smarter solutions with {brand}.",
                f"Upgrade your experience with {brand}.",
                f"Explore what {brand} can do for you."
            ]

        tweets = random.sample(templates, 10)

        analysis = {
            "tone": tone,
            "audience": audience,
            "theme": theme,
            "objective": objective
        }

        return render_template(
            "result.html",
            tweets=tweets,
            analysis=analysis,
            brand=brand
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)