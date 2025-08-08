# 🎯 Least Squares Illustration

An interactive Pygame application to visualize least squares polynomial regression. Click to add data points, choose the polynomial degree, and watch the curve fit in real time. Great for teaching and exploring the geometric intuition behind regression.

---

## 📸 Some drafts of the progress of development

![WhatsApp Görsel 2025-08-08 saat 20 56 13_a87047af](https://github.com/user-attachments/assets/c035b62c-c4e3-4d47-ab62-eef2b7288e91)

---

## 🧠 Features

- 🖱️ Interactive point placement (click to add)
- 📈 Real-time least squares curve fitting (linear, quadratic, cubic, ...)
- ⚙️ Polynomial degree input with instant updates
- 🧮 Visual grid with zoom and pan controls
- 🎨 Clean modular code with separation of UI, math, and logic

---

## 📁 Project Structure

```
least-squares-illustration/
├── README.md
├── pyproject.toml
└── src/
    ├── __init__.py
    ├── main.py          # Entry point – initializes app
    ├── fitter.py        # Computes polynomial regression
    ├── grid.py          # Handles grid visuals and transformations
    ├── ui.py            # UI panel using pygame_gui
    └── settings.py      # Constants, enums, colors, styling
```

---

## 🧰 Installation

> Recommended: use a virtual environment

```bash
# Clone the repo
git clone https://github.com/your-username/least-squares-illustration.git
cd least-squares-illustration

# Create virtual environment
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
# or, if using poetry
poetry install
```

---

## ▶️ Running the App

```bash
# Using poetry
poetry run python src/main.py

```

---

## 🧪 Requirements

- Python 3.10+
- Pygame
- pygame_gui
- numpy

If not using `poetry`, install with:

```bash
pip install pygame pygame_gui numpy
```

---

## ✍️ Usage

- Click anywhere on the grid to place a data point
- Use the UI panel to set the polynomial degree (e.g., 1 for linear)
- Pan: hold right mouse button and drag
- Zoom: use scroll wheel
- Curve updates instantly based on added points and degree

---

## 🧹 To Do

- Save/load point sets
- Toggle error display (residuals)
- Export graph as image
- Animate regression steps
- Add real-time equation display

---

## 🧑‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License. See `LICENSE` for details.

---
