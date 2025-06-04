import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  }
});

export const createRules = async (rules) => {
  try {
    const response = await api.post('http://localhost:8000/rules/bulk', { rules });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default api;