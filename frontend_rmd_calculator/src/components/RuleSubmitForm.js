import React, { useState } from 'react';
import { Button, TextField, Box, Typography } from '@mui/material';

export default function RuleSubmitForm({ featureFlags = {} }) {
  const [inputs, setInputs] = useState({
    description: '',
    context: '',
    priority: 1,
    naturalLanguage: '',
    file: null
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    
    // Append required fields
    formData.append('description', inputs.description);
    formData.append('context', inputs.context);
    formData.append('priority', inputs.priority.toString());

    if (featureFlags?.llmEnabled) {
      formData.append('natural_language', inputs.naturalLanguage);
    } else {
      if (inputs.file) {
        formData.append('file', inputs.file);
      }
    }

    try {
      console.log(formData)
      const response = await fetch('http://localhost:8000/submit_rule/', {
        method: 'POST',
        body: formData
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // Handle successful response
    } catch (error) {
      console.error('Submission error:', error);
    }
  };

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
      <TextField
        label="Description"
        fullWidth
        required
        value={inputs.description}
        onChange={(e) => setInputs({...inputs, description: e.target.value})}
        margin="normal"
      />

      <TextField
        label="Context"
        fullWidth
        required
        value={inputs.context}
        onChange={(e) => setInputs({...inputs, context: e.target.value})}
        margin="normal"
      />

      <TextField
        label="Priority"
        type="number"
        fullWidth
        required
        value={inputs.priority}
        onChange={(e) => setInputs({...inputs, priority: parseInt(e.target.value) || 1})}
        margin="normal"
        inputProps={{ min: 1, max: 10 }}
      />

      {featureFlags?.llmEnabled ? (
        <TextField
          label="Rule Description"
          fullWidth
          required
          multiline
          rows={4}
          value={inputs.naturalLanguage}
          onChange={(e) => setInputs({...inputs, naturalLanguage: e.target.value})}
          margin="normal"
        />
      ) : (
        <Box sx={{ mt: 2 }}>
          <input
            type="file"
            accept=".xlsx"
            required
            onChange={(e) => setInputs({...inputs, file: e.target.files[0]})}
          />
        </Box>
      )}

      <Button 
        type="submit" 
        variant="contained" 
        color="primary"
        sx={{ mt: 3 }}
      >
        Submit Rule
      </Button>
    </Box>
  );
}