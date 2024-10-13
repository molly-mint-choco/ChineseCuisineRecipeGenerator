import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

function App() {
  const [photo, setPhoto] = useState(null);
  const [instructions, setInstructions] = useState('');
  const [recipe, setRecipe] = useState('');

  const handlePhotoChange = (event) => {
    setPhoto(event.target.files[0]);
  };

  const handleInputChange = (event) => {
    setInstructions(event.target.value);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append('photo', photo);
    formData.append('additional_instructions', instructions);

    try {
      const response = await axios.post('http://127.0.0.1:7000/recipe', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setRecipe(response.data.recipe); // Assuming response contains { recipe: "...markdown formatted string..." }
    } catch (error) {
      console.error('Error fetching recipe', error);
    }
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.header}>What Can I Cook Today?</h1>
      
      <div style={styles.uploadSection}>
        <input type="file" onChange={handlePhotoChange} required style={styles.uploadInput} />
      </div>

      <div style={styles.inputSection}>
        <textarea
          placeholder="Enter any additional instructions (optional)"
          value={instructions}
          onChange={handleInputChange}
          style={styles.textInput}
        />
      </div>

      <button onClick={handleSubmit} style={styles.button}>Submit</button>

      <div style={styles.resultSection}>
        {recipe && <ReactMarkdown>{recipe}</ReactMarkdown>}
      </div>
    </div>
  );
}

const styles = {
  container: {
    textAlign: 'center',
    fontFamily: 'Arial, sans-serif',
    maxWidth: '600px',
    margin: '0 auto',
    padding: '50px',
  },
  header: {
    fontSize: '2rem',
    marginBottom: '20px',
  },
  uploadSection: {
    marginBottom: '20px',
  },
  uploadInput: {
    padding: '10px',
    fontSize: '1rem',
  },
  inputSection: {
    marginBottom: '20px',
  },
  textInput: {
    width: '100%',
    height: '100px',
    fontSize: '1rem',
    padding: '10px',
    borderRadius: '5px',
    border: '1px solid #ccc',
  },
  button: {
    padding: '10px 20px',
    fontSize: '1rem',
    backgroundColor: '#007bff',
    color: 'white',
    borderRadius: '5px',
    border: 'none',
    cursor: 'pointer',
  },
  resultSection: {
    marginTop: '30px',
    textAlign: 'left',
  },
};

export default App;
