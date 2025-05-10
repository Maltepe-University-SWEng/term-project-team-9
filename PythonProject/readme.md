FULL PROJECT FILES : https://github.com/alpsalcioglu/mau IN THIS REPO
# FıkraBot - AI-Powered Turkish Joke Generator

FıkraBot is an innovative AI-powered application that generates Turkish jokes using a custom-trained language model. The project combines a Python backend for AI processing with a modern Node.js frontend for user interaction.

## Architecture

### Backend Architecture

The backend is built using two main components:

1. **AI Model (PyTorch)**
   - Custom Transformer-based decoder model
   - Architecture:
     - Embedding layer (10,000 vocab size)
     - Positional Encoding
     - Transformer Decoder (2 layers, 4 attention heads)
     - Linear output layer
   - Uses SentencePiece tokenizer for text processing
   - Model parameters:
     - Vocabulary size: 10,000
     - Model dimension: 256
     - Maximum sequence length: 50
     - Number of attention heads: 4
     - Number of decoder layers: 2

2. **API Server**
   - Built with Flask
   - Provides RESTful endpoints for joke generation
   - Handles text generation requests
   - Manages model inference

### Frontend Stack

The frontend is built with modern web technologies:

- **Server**: Node.js with Express.js
- **View Engine**: EJS (Embedded JavaScript templates)
- **Key Dependencies**:
  - `express`: Web application framework
  - `axios`: HTTP client for API requests
  - `express-session`: Session management
  - `mongoose`: MongoDB interaction
  - `jsonwebtoken`: JWT authentication
  - `bcryptjs`: Password hashing
  - `body-parser`: Request parsing
  - `cookie-parser`: Cookie handling

## Features

- Real-time joke generation
- Interactive chat-like interface
- Session management
- User authentication
- Responsive design
- Error handling and validation

## Technical Requirements

### Backend Requirements
- Python 3.8+
- PyTorch
- SentencePiece
- Flask
- CUDA-compatible GPU (optional, for faster inference)

### Frontend Requirements
- Node.js 18+
- npm or yarn
- MongoDB (for user management)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd PythonProject
```

2. Install backend dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
./run_api.sh
```

2. Start the frontend server:
```bash
./run_frontend.sh
```

Or use the combined starter:
```bash
node run.js
```

The application will be available at:
- Frontend: http://localhost:3001
- Backend API: http://localhost:5001

## Project Structure

```
PythonProject/
├── api/                  # Flask backend
├── frontend/            # Node.js frontend
│   ├── public/         # Static files
│   ├── views/          # EJS templates
│   └── app.js          # Express application
├── model.ipynb          # Model training notebook
├── app.py              # Streamlit interface
├── run.js              # Combined starter
└── model_v11.pth       # Trained model weights
```

## Model Training

The model was trained on a curated dataset of Turkish jokes. The training process and data preparation can be found in `model.ipynb`. The model uses a custom Transformer architecture optimized for Turkish language generation.

## License

[Add your license information here]

## Contributors

[Add contributor information here]
