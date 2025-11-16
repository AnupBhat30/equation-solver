# 🤯 CRAZY HANDWRITTEN EQUATION SOLVER 🤯

![Mind Blown](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

## 🚀 What the HECK is this?!

Welcome to the **ULTIMATE HANDWRITTEN EQUATION SOLVER** - the app that turns your chicken scratch into actual MATH! 🐔➗📐

Ever scribbled `2+2=fish` on a napkin and wondered why your calculator laughed at you? Well, wonder no more! This AI-powered monstrosity uses a Convolutional Neural Network (CNN) trained on thousands of handwritten digits and operators to:

- 📝 **Recognize your terrible handwriting**
- 🔢 **Convert scribbles to equations**
- 🧮 **Actually SOLVE them**
- 🎯 **Give you confidence scores** (because we know you're skeptical)

## 🎨 Features That Will Blow Your Mind

### ✏️ Draw Like a Toddler

- **Canvas Drawing**: Scribble equations directly in your browser
- **Real-time Recognition**: Watch as the AI tries to decipher your hieroglyphics
- **Confidence Meter**: See how sure the AI is about your artistic masterpiece

### 📸 Upload Your Mess

- **Image Upload**: Snap a photo of your notebook chaos
- **Multi-format Support**: PNG, JPG, JPEG - we don't discriminate
- **Smart Detection**: Finds individual characters even in your tornado handwriting

### 🧠 AI Magic

- **CNN-Powered**: Trained on 14 classes (0-9 digits + 4 operators)
- **Character Segmentation**: Splits your equation into individual symbols
- **Equation Building**: Reconstructs your math from the pieces
- **Safe Evaluation**: Won't crash if you write `2++2` (but it'll judge you silently)

## 🛠️ Tech Stack (Because Nerds Care)

- **Frontend**: Streamlit (because web dev is hard 😅)
- **AI Brain**: TensorFlow/Keras CNN
- **Image Processing**: OpenCV (the unsung hero)
- **Drawing Canvas**: streamlit-drawable-canvas
- **Math Engine**: Python's eval() (don't tell anyone)

## 🚀 Quick Start (Don't Overthink It)

### Prerequisites

- Python 3.8+ (we're not savages)
- A computer (preferably one that works)

### Installation

```bash
# Clone this masterpiece
git clone <your-repo-url>
cd handwritten-equation-solver

# Install dependencies (it's just 6 packages, we kept it lean!)
pip install -r requirements.txt

# Or if you're fancy with uv:
uv pip install -r requirements.txt
```

### Run the Magic

```bash
streamlit run equation_solver.py
```

Boom! 🎆 Your app is now running at `http://localhost:8501`

## 📊 How It Works (The Boring Technical Stuff)

### The Model

- **Architecture**: 3 Conv2D layers + MaxPooling + Dropout + Dense layers
- **Input**: 32x32 grayscale images
- **Output**: 14 classes (0-9, +, -, ×, ÷)
- **Training Data**: Custom dataset with ~10k+ images per class
- **Accuracy**: Somewhere in the 90s% (we don't brag... much)

### The Pipeline

1. **Image Preprocessing**: Convert to grayscale, threshold, find contours
2. **Character Segmentation**: Extract individual symbols with padding
3. **CNN Prediction**: Classify each character
4. **Equation Assembly**: Sort by position and build the string
5. **Math Evaluation**: Safely compute the result

## 🎯 Usage Examples

### Drawing Mode

1. Click "Draw on Canvas"
2. Scribble `3+5` (or try `2×8` if you're feeling fancy)
3. Hit "Analyze Drawing"
4. Watch the AI struggle with your handwriting
5. Get your answer + confidence scores

### Upload Mode

1. Take a photo of `7-2×3`
2. Upload the image
3. Let the AI work its magic
4. Profit! (or at least get the answer)

## 🐛 Known Issues (We Call Them "Features")

- **Handwriting Recognition**: Works best with clear, separated characters
- **Operators**: Sometimes confuses `×` with `+` (hey, they look similar!)
- **Complex Equations**: Stick to basic arithmetic for now
- **Division Symbol**: `/` works, but `÷` might need better lighting

## 🤝 Contributing (If You're Brave Enough)

Found a bug? Want to improve the model? Have suggestions?

1. Fork it
2. Create your feature branch (`git checkout -b feature/amazing-improvement`)
3. Commit your changes (`git commit -m 'Add amazing improvement'`)
4. Push to the branch (`git push origin feature/amazing-improvement`)
5. Open a Pull Request

## 📜 License

This project is licensed under the **"Do Whatever You Want" License** - see the LICENSE file for details. (Actually, it's MIT, but we like to keep it fun)

## 🙏 Acknowledgments

- **TensorFlow/Keras**: For making deep learning accessible
- **OpenCV**: For image processing wizardry
- **Streamlit**: For turning Python scripts into web apps
- **The Dataset**: Whoever collected those thousands of handwritten samples
- **You**: For reading this far down

## 🎉 Final Thoughts

This project started as a fun experiment and turned into something actually useful! The model training notebook shows the journey from raw data to a working CNN, and the Streamlit app brings it all together in a user-friendly interface.

---

## 🎁 **FREE FOR ALL MINI PROJECTS!** 🎁

**Hey fellow developers, students, and curious minds!**

Feel free to use this project for your mini projects, assignments, or just messing around. Seriously - it's not worth wasting time reinventing the wheel if you don't want to learn something new. Take it, modify it, break it, fix it, make it your own!

**Why?** Because:

- ✅ **Complete working example** of CNN + Streamlit
- ✅ **Real-world application** (handwriting recognition)
- ✅ **Educational value** (see how AI pipelines work)
- ✅ **Easy to extend** (add more operators, improve accuracy, etc.)
- ✅ **No strings attached** - MIT licensed

**Pro tip:** If you're learning ML/AI, the `equation_solver.ipynb` notebook is gold - it shows the complete model training process from data loading to evaluation!

---

_Made with ❤️, ☕, and way too many late nights debugging TensorFlow_

![Happy Coding](https://media.giphy.com/media/SWoSkN6DxTszqIKEqv/giphy.gif)
