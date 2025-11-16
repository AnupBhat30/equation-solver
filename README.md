# Handwritten Equation Solver

![Mind Blown](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

## Overview

Welcome to the Handwritten Equation Solver, an AI-powered application that converts handwritten equations into solvable mathematical expressions using a Convolutional Neural Network (CNN) trained on thousands of handwritten digits and operators.

This tool recognizes handwritten input, converts scribbles to equations, solves them, and provides confidence scores for the predictions.

## Features

### Drawing Interface

- **Canvas Drawing**: Scribble equations directly in the browser.
- **Real-time Recognition**: Observe the AI deciphering your handwriting.
- **Confidence Meter**: View the AI's confidence in recognizing each character.

### Image Upload

- **Image Upload**: Upload photos of handwritten equations.
- **Multi-format Support**: Supports PNG, JPG, and JPEG formats.
- **Smart Detection**: Identifies individual characters in varied handwriting styles.

### AI Capabilities

- **CNN-Powered**: Utilizes a Convolutional Neural Network trained on 14 classes (digits 0-9 and operators +, -, ×, ÷).
- **Character Segmentation**: Separates equations into individual symbols.
- **Equation Building**: Reconstructs mathematical expressions from recognized components.
- **Safe Evaluation**: Handles invalid inputs without crashing.

## Tech Stack

- **Frontend**: Streamlit for web interface.
- **AI Framework**: TensorFlow/Keras for the CNN model.
- **Image Processing**: OpenCV for preprocessing.
- **Drawing Canvas**: streamlit-drawable-canvas for user input.
- **Math Engine**: Python's eval() for computation.

## Quick Start

### Prerequisites

- Python 3.8 or higher.
- A compatible computer system.

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd handwritten-equation-solver

# Install dependencies
pip install -r requirements.txt

# Alternatively, using uv:
uv pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run equation_solver.py
```

The application will be available at `http://localhost:8501`.

## How It Works

### The Model

- **Architecture**: Consists of 3 Conv2D layers, MaxPooling, Dropout, and Dense layers.
- **Input**: 32x32 grayscale images.
- **Output**: 14 classes (0-9, +, -, ×, ÷).
- **Training Data**: Custom dataset with approximately 10,000 images per class.
- **Accuracy**: Achieves high accuracy in the 90s percentile.

### The Pipeline

1. **Image Preprocessing**: Convert to grayscale, apply thresholding, and detect contours.
2. **Character Segmentation**: Extract individual symbols with appropriate padding.
3. **CNN Prediction**: Classify each character.
4. **Equation Assembly**: Sort characters by position and construct the equation string.
5. **Math Evaluation**: Safely compute the result.

## Usage Examples

### Drawing Mode

1. Select "Draw on Canvas".
2. Write an equation such as `3+5` or `2×8`.
3. Click "Analyze Drawing".
4. Review the recognized equation, solution, and confidence scores.

### Upload Mode

1. Capture a photo of an equation like `7-2×3`.
2. Upload the image.
3. Allow the AI to process and solve the equation.

## Known Issues

- **Handwriting Recognition**: Performs best with clear, well-separated characters.
- **Operators**: May occasionally confuse similar-looking operators like `×` and `+`.
- **Complex Equations**: Currently optimized for basic arithmetic.
- **Division Symbol**: Recognizes `/` reliably; `÷` may require clearer input.

## Contributing

To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/improvement`).
3. Commit changes (`git commit -m 'Add improvement'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- TensorFlow/Keras for deep learning framework.
- OpenCV for image processing.
- Streamlit for web application development.
- The dataset contributors for training samples.
- The open-source community for tools and resources.

## Final Thoughts

This project demonstrates the integration of machine learning with web applications for practical handwriting recognition. The training notebook (`equation_solver.ipynb`) provides a complete guide to model development, and the Streamlit app offers an accessible interface.

---

## Educational Use

This project serves as a complete example of CNN implementation with Streamlit for mini projects, assignments, or learning purposes. It includes a real-world application of handwriting recognition with educational value in understanding AI pipelines. The code is MIT licensed and easy to extend.

The `equation_solver.ipynb` notebook is particularly valuable for those learning machine learning, as it details the full model training process.

---

_Made with love, coffee, and way too many late nights debugging TensorFlow_

![Happy Coding](https://media.giphy.com/media/SWoSkN6DxTszqIKEqv/giphy.gif)

Made for Neural Networks and Deep Learning Lab mini project.
