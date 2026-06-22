# 🎯 Word Predictor AI - Web Application

A beautiful, intelligent web-based word predictor using an **LSTM neural network** trained on classical literature texts. This application provides real-time word predictions with a modern, responsive user interface.

---

## ✨ Features

- 🔮 **Real-time Predictions** - Get top 3 word predictions as you type
- 🎨 **Beautiful UI** - Modern, responsive design with gradient backgrounds and smooth animations
- ⌨️ **Virtual Keyboard** - Full QWERTY keyboard with backspace and enter keys for easy interaction
- 📱 **Mobile Friendly** - Works seamlessly on desktop, tablet, and mobile devices
- ⚡ **Fast Inference** - Quick prediction response using pre-trained LSTM model
- 🧠 **Deep Learning** - Powered by TensorFlow/Keras neural network architecture

---

## 📚 Libraries & Dependencies

### Core Dependencies

| Library        | Version | Purpose                                                      |
| -------------- | ------- | ------------------------------------------------------------ |
| **Flask**      | 2.3.0   | Lightweight web framework for building the web application   |
| **TensorFlow** | 2.14.0+ | Deep learning framework for neural network model inference   |
| **NumPy**      | 1.26.0+ | Numerical computing for array operations and data processing |
| **Python**     | 3.8+    | Programming language runtime                                 |

### Built-in Libraries Used

- **pickle** - Serialization for loading pre-trained model tokenizer and configuration
- **os** - Operating system operations for file path handling
- **json** - JSON handling for API responses

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Word_Predictor
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Ensure Model Files

Make sure the following files are in the project root directory:

- `next_word_model.keras` - Pre-trained LSTM neural network model
- `tokenizer.pkl` - Text tokenizer for converting text to sequences
- `model_config.pkl` - Model configuration (max_sequence_len, vocab_size)

---

## 💻 Running the Application

### Start the Flask Server

```bash
python app.py
```

### Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

### Using the Predictor

1. Type text in the input field
2. See real-time word predictions appear below
3. Click on a predicted word or use the virtual keyboard
4. Press Enter or click the "Predict" button to confirm

---

## 📁 Project Structure

```
Word_Predictor/
├── app.py                    # Flask application and API endpoints
├── next_word_model.keras     # Pre-trained LSTM model
├── tokenizer.pkl             # Text tokenizer (serialized)
├── model_config.pkl          # Model configuration (serialized)
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── word_predictor1.ipynb     # Jupyter notebook with model training code
└── templates/
    └── index.html            # Frontend HTML/CSS/JavaScript
```

---

## 🏗️ Architecture

### Backend

- **Flask** serves the web application and REST API endpoints
- **TensorFlow/Keras** loads and runs the pre-trained LSTM model
- **NumPy** handles numerical operations for predictions
- Tokenizer converts text input to sequences for model inference

### Frontend

- **HTML/CSS** for responsive UI design
- **JavaScript** for real-time API calls and virtual keyboard interaction
- Displays predictions with confidence scores

---

## 🔌 API Endpoints

### POST `/predict`

Predicts the next words given input text.

**Request**:

```json
{
  "text": "the quick brown",
  "top_k": 3
}
```

**Response**:

```json
{
  "predictions": [
    { "word": "fox", "confidence": 0.87 },
    { "word": "dog", "confidence": 0.09 },
    { "word": "cat", "confidence": 0.04 }
  ]
}
```

---

## 👥 Team Members & Contributors

<!-- Add your team members below with their roles and GitHub profiles -->

| Name                   | Role         | GitHub                                               | Contact                     |
| ---------------------- | ------------ | ---------------------------------------------------- | --------------------------- |
| **Tanmay Sahoo**       | Project Lead | [@tanmay-sahoo89](https://github.com/tanmay-sahoo89) | [sahootanmay2005@gmail.com] |
| **[Team Member Name]** | [Role]       | [GitHub Profile]                                     | [Email]                     |
| **[Team Member Name]** | [Role]       | [GitHub Profile]                                     | [Email]                     |
| **[Team Member Name]** | [Role]       | [GitHub Profile]                                     | [Email]                     |
| **[Team Member Name]** | [Role]       | [GitHub Profile]                                     | [Email]                     |

> 💡 **To Add Team Members**: Edit the table above with your teammates' information. Include their GitHub profiles and contact information.

---

## 📚 Model Details

- **Architecture**: LSTM (Long Short-Term Memory) Neural Network
- **Layers**: Embedding → LSTM (128 units) → Dropout (0.2) → Dense (Softmax)
- **Training Data**: Classical literature texts from Project Gutenberg
- **Vocabulary Size**: ~10,000+ words
- **Max Sequence Length**: Dynamic based on training configuration
- **Activation**: Softmax for probability distribution output
- **Input Processing**: Text tokenization and sequence padding

---

## ⌨️ Usage Examples

### Basic Text Prediction

```
Input: "Once upon"
Predictions: ["a", "there", "the"]
```

### Longer Context

```
Input: "The quick brown fox jumps over the"
Predictions: ["lazy", "dark", "sleeping"]
```

---

## 🐛 Troubleshooting

| Issue                         | Solution                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------- |
| **Model not found**           | Ensure `next_word_model.keras`, `tokenizer.pkl`, and `model_config.pkl` are in project root |
| **Module not found**          | Run `pip install -r requirements.txt` to install dependencies                               |
| **Slow predictions**          | Normal on first run. Model loads into memory for subsequent faster predictions              |
| **Port 5000 in use**          | Change port in `app.py`: `app.run(debug=True, port=5001)`                                   |
| **"Unknown word" in results** | These are automatically filtered; increase input length for better predictions              |

---

## 🔧 Keyboard Shortcuts

- **Backspace**: Delete last character
- **Space**: Add space character
- **Enter**: Add newline
- **Clear Button**: Reset entire text field

---

## 🌐 Browser Compatibility

- ✅ Chrome/Edge (latest versions)
- ✅ Firefox (latest versions)
- ✅ Safari (latest versions)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 📝 Model Training Notes

- The model works best with **lowercase input**
- **Predictions improve** with longer context (more input words)
- **Unknown words** are automatically filtered from results
- **Predictions update** with debounce for optimal performance
- **First prediction** may have slight delay while model initializes

---

## 🚀 Future Enhancements

- [ ] Support for multiple languages (Spanish, French, German, etc.)
- [ ] Temperature-based sampling for creative/conservative mode
- [ ] Word prediction history tracking
- [ ] Custom model training interface
- [ ] Export predictions to file (PDF, TXT, JSON)
- [ ] Real-time model switching
- [ ] User preferences and themes
- [ ] API rate limiting and authentication
- [ ] Docker containerization

---

## 📋 Development Workflow

1. Create feature branch: `git checkout -b feature/feature-name`
2. Make changes and test locally
3. Commit changes: `git commit -m "Add feature description"`
4. Push to branch: `git push origin feature/feature-name`
5. Create Pull Request on GitHub
6. Wait for review and merge

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes with clear commit messages
4. **Test** your changes locally
5. **Push** to your fork
6. **Create** a Pull Request with description

---

## 📜 License

This project is licensed under the **MIT License** - see the LICENSE file for more details.

---

## 🙏 Acknowledgments

- **TensorFlow/Keras** - Amazing deep learning framework
- **Flask** - Lightweight and powerful web framework
- **NumPy** - Essential numerical computing library
- **Project Gutenberg** - Free access to classic literature for training data
- All contributors and team members for their support

---

## 📊 Project Statistics

- **Lines of Code**: Python backend + Frontend HTML/CSS/JavaScript
- **Dependencies**: 3 main libraries (Flask, TensorFlow, NumPy)
- **Model Size**: ~5-15 MB (depending on vocab size)
- **Training Data**: Classical literature collection

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Active Development

⭐ If you found this project helpful, please consider giving it a star on GitHub!

---

_Made using LSTM Neural Networks and Flask Web Framework_
