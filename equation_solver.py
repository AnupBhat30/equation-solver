import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import io
from streamlit_drawable_canvas import st_canvas
from datetime import datetime

# Set page config
st.set_page_config(page_title="Handwritten Equation Solver", page_icon="🧮", layout="wide")

# Title and description
st.title("🧮 Handwritten Equation Solver")
st.markdown("""
Upload an image of a handwritten mathematical equation, and the AI will solve it for you!
Supports digits (0-9) and basic operations (+, -, ×, ÷)
""")

# Label mapping
labels = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: '+', 11: '÷', 12: '×', 13: '-'
}

def safe_eval(equation_str):
    """Safely evaluate the equation"""
    try:
        # Replace symbols for evaluation
        equation_eval = equation_str.replace('×', '*').replace('÷', '/')
        # Check for valid characters
        if not all(c in '0123456789+-*/.() ' for c in equation_eval):
            return None
        result = eval(equation_eval)
        return result
    except:
        return None

@st.cache_resource
def load_trained_model():
    """Load the pre-trained model"""
    try:
        model = load_model('cnn_model.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(image):
    """Preprocess the uploaded image"""
    # Convert PIL Image to numpy array
    image = np.array(image)

    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    return image

def predict_equation(image, model):
    """Predict the equation from the image"""
    # Threshold the image
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get bounding boxes and sort by x-coordinate
    bounding_boxes = [cv2.boundingRect(contour) for contour in contours]
    sorted_indices = sorted(range(len(bounding_boxes)), key=lambda i: bounding_boxes[i][0])
    sorted_contours = [contours[i] for i in sorted_indices]

    rois = []
    padding = 15

    # Extract regions of interest
    for contour in sorted_contours:
        x, y, w, h = cv2.boundingRect(contour)
        x_start = max(0, x - padding)
        y_start = max(0, y - padding)
        x_end = min(image.shape[1], x + w + padding)
        y_end = min(image.shape[0], y + h + padding)

        roi = image[y_start:y_end, x_start:x_end]
        roi = cv2.resize(roi, (32, 32))
        rois.append(roi)

    if len(rois) == 0:
        return None, None, None, []

    # Prepare for prediction
    rois = np.array(rois)
    rois = rois / 255.0
    rois = np.expand_dims(rois, axis=-1)

    # Predict
    predictions = model.predict(rois, verbose=0)
    predicted_labels = np.argmax(predictions, axis=1)
    confidence_scores = np.max(predictions, axis=1)

    # Draw bounding boxes on image
    image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    for i, contour in enumerate(sorted_contours):
        x, y, w, h = cv2.boundingRect(contour)
        label = labels[predicted_labels[i]]
        confidence = confidence_scores[i]
        
        # Color code: green for high confidence, orange for medium, red for low
        if confidence > 0.8:
            color = (0, 255, 0)
        elif confidence > 0.6:
            color = (0, 165, 255)
        else:
            color = (0, 0, 255)
        
        cv2.rectangle(image_color, (x, y), (x+w, y+h), color, 2)
        cv2.putText(image_color, f"{label}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Build equation string
    equation = ''.join([labels[predicted_labels[i]] for i in range(len(predicted_labels))])

    # Return confidence scores along with other data
    return equation, confidence_scores, image_color, [labels[predicted_labels[i]] for i in range(len(predicted_labels))]

# Main app
def main():
    # Load model
    model = load_trained_model()

    if model is None:
        st.error("Failed to load model. Please ensure 'cnn_model.keras' is in the same directory.")
        return

    st.success("Model loaded successfully! ✅")

    # Add sidebar with information
    with st.sidebar:
        st.markdown("### 📋 About")
        st.markdown("""
        This app uses a CNN to recognize handwritten equations and solve them.
        
        **Supported:**
        - Digits: 0-9
        - Operators: + − × ÷
        
        **Tips:**
        - Write clearly with good spacing
        - Light background preferred
        - High contrast helps accuracy
        """)
        
        st.markdown("---")
        st.markdown("### ⚙️ Canvas Settings")
        stroke_width = st.slider("Brush size", 1, 10, 3)
        st.markdown("---")
        
        if st.button("🎨 How to use", key="help_btn"):
            st.session_state.show_help = not st.session_state.get('show_help', False)

    # Tabs for input method
    tab1, tab2 = st.tabs(["📝 Draw on Canvas", "📤 Upload Image"])

    with tab1:
        st.subheader("Draw your equation here")
        
        # Drawing canvas
        canvas_result = st_canvas(
            fill_color="rgba(255, 255, 255, 0)",
            stroke_width=stroke_width,
            stroke_color="#000000",
            background_color="#FFFFFF",
            height=250,
            width=800,
            drawing_mode="freedraw",
            key="canvas",
        )

        col_clear, col_predict = st.columns([1, 3])
        
        with col_clear:
            if st.button("🗑️ Clear Canvas", key="clear_canvas"):
                st.rerun()
        
        with col_predict:
            canvas_predict = st.button("🔍 Analyze Drawing", key="predict_canvas")

        canvas_image_data = None
        if canvas_predict and canvas_result.image_data is not None:
            # Get canvas image
            canvas_image = canvas_result.image_data
            canvas_image_data = canvas_image
            
            # Convert to PIL Image for consistency
            pil_image = Image.fromarray(canvas_image.astype('uint8'))
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Your Drawing")
                st.image(pil_image, use_container_width=True)
            
            # Process image
            with st.spinner('Analyzing equation...'):
                gray_image = preprocess_image(pil_image)
                equation, confidence, annotated_image, characters = predict_equation(gray_image, model)
            
            with col2:
                st.subheader("Detected Equation")
                if equation:
                    st.image(annotated_image, use_container_width=True)
                else:
                    st.warning("No equation detected. Please draw more clearly.")
            
            # Display results
            if equation:
                st.markdown("---")
                st.markdown("### 🎯 Results")

                result_col1, result_col2 = st.columns(2)

                with result_col1:
                    st.markdown(f"**Detected Equation:**")
                    st.markdown(f"# `{equation}`")

                with result_col2:
                    st.markdown(f"**Average Confidence:**")
                    avg_confidence = np.mean(confidence)
                    st.markdown(f"# `{avg_confidence:.1%}`")
                    
                    # Show confidence bar
                    if avg_confidence > 0.8:
                        st.success("High confidence ✅")
                    elif avg_confidence > 0.6:
                        st.warning("Medium confidence ⚠️")
                    else:
                        st.error("Low confidence ❌")

                # Character breakdown
                with st.expander("📊 Character Details", expanded=False):
                    for i, (char, conf) in enumerate(zip(characters, confidence), 1):
                        col_char, col_conf = st.columns([1, 3])
                        with col_char:
                            st.metric(f"Char {i}", char)
                        with col_conf:
                            st.progress(float(conf), text=f"{conf:.1%}")
                
                # Try to solve the equation
                result = safe_eval(equation)
                if result is not None:
                    st.info(f"✅ **Solution:** {equation} = **{result}**")
                else:
                    st.warning("⚠️ Could not evaluate the equation. Check for typos or unsupported operations.")

    with tab2:
        # File uploader
        uploaded_file = st.file_uploader(
            "Upload an image of a handwritten equation",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a clear image with handwritten digits and operators"
        )

        # Create two columns
        col1, col2 = st.columns(2)

        if uploaded_file is not None:
            # Read and display original image
            image = Image.open(uploaded_file)

            with col1:
                st.subheader("Original Image")
                st.image(image, use_container_width=True)

            # Process image
            with st.spinner('Analyzing equation...'):
                gray_image = preprocess_image(image)
                equation, confidence, annotated_image, characters = predict_equation(gray_image, model)

            with col2:
                st.subheader("Detected Equation")
                if equation:
                    st.image(annotated_image, use_container_width=True)
                else:
                    st.warning("No equation detected. Please try with a clearer image.")

            # Display results
            if equation:
                st.markdown("---")
                st.markdown("### 🎯 Results")

                result_col1, result_col2 = st.columns(2)

                with result_col1:
                    st.markdown(f"**Detected Equation:**")
                    st.markdown(f"# `{equation}`")

                with result_col2:
                    st.markdown(f"**Average Confidence:**")
                    avg_confidence = np.mean(confidence)
                    st.markdown(f"# `{avg_confidence:.1%}`")
                    
                    if avg_confidence > 0.8:
                        st.success("High confidence ✅")
                    elif avg_confidence > 0.6:
                        st.warning("Medium confidence ⚠️")
                    else:
                        st.error("Low confidence ❌")

                # Character breakdown
                with st.expander("📊 Character Details", expanded=False):
                    for i, (char, conf) in enumerate(zip(characters, confidence), 1):
                        col_char, col_conf = st.columns([1, 3])
                        with col_char:
                            st.metric(f"Char {i}", char)
                        with col_conf:
                            st.progress(float(conf), text=f"{conf:.1%}")
                
                # Try to solve the equation
                result = safe_eval(equation)
                if result is not None:
                    st.info(f"✅ **Solution:** {equation} = **{result}**")
                else:
                    st.warning("⚠️ Could not evaluate the equation. Check for typos or unsupported operations.")

        else:
            st.info("👆 Upload an image to get started!")

            # Show example
            st.markdown("---")
            st.markdown("### 📝 Tips for best results:")
            st.markdown("""
            - Write digits and operators clearly with good spacing
            - Use a plain white/light background
            - Ensure good lighting and contrast
            - Supported operators: + (add), - (sub), × (mul), ÷ (div)
            """)

if __name__ == "__main__":
    main()