import React, { useState } from 'react';
import axios from 'axios';
import { styled } from '@mui/system';
import {
  Container,
  Typography,
  Button,
  CircularProgress,
  Paper,
  Box,
  Grid,
  List,
  ListItem,
  ListItemText,
  Card,
  CardContent,
  colors
} from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

// Create styled components using MUI v5's styled
const UploadCard = styled(Card)(({ theme }) => ({
  marginTop: theme.spacing(4),
  padding: theme.spacing(3),
  border: `2px dashed ${theme.palette?.primary?.main || '#1976d2'}`, // Fallback color
  '&:hover': {
    borderColor: theme.palette?.primary?.dark || '#1565c0', // Fallback color
  },
}));

const LoadingBox = styled(Box)(({ theme }) => ({
  display: 'flex',
  justifyContent: 'center',
  padding: theme.spacing(3),
}));

const ReportSection = styled(Paper)(({ theme }) => ({
  marginTop: theme.spacing(4),
}));

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [report, setReport] = useState(null);
  const [error, setError] = useState(null);

  const isValidFile = (file) => {
    return file && file.name.match(/\.(xlsx)$/i);
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    
    if (!isValidFile(file)) {
      setError('Please upload a valid Excel file (.xlsx)');
      setSelectedFile(null);
      return;
    }
    
    setError(null);
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      setUploading(true);
      const response = await axios.post('http://localhost:8000/upload_rules/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      setReport(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.detail || 'Upload failed. Please try again.');
      setReport(null);
    } finally {
      setUploading(false);
    }
  };

  return (
    <Container maxWidth="md" sx={{ minHeight: '100vh', py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        RMD Rules Engine Upload Portal
      </Typography>

      <UploadCard variant="outlined">
        <CardContent>
          <input
            accept=".xlsx"
            style={{ display: 'none' }}
            id="file-upload"
            type="file"
            onChange={handleFileChange}
          />
          <label htmlFor="file-upload">
            <Button
              variant="contained"
              color="primary"
              component="span"
              startIcon={<CloudUploadIcon />}
            >
              Choose Excel File
            </Button>
          </label>

          {selectedFile && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="body1">
                Selected file: {selectedFile.name}
              </Typography>
              <Button
                variant="contained"
                color="secondary"
                onClick={handleUpload}
                disabled={uploading}
                sx={{ mt: 2 }}
              >
                {uploading ? 'Uploading...' : 'Upload File'}
              </Button>
            </Box>
          )}

          {error && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="body1" color="error">
                {error}
              </Typography>
            </Box>
          )}
        </CardContent>
      </UploadCard>

      {uploading && (
        <LoadingBox>
          <CircularProgress />
        </LoadingBox>
      )}

      {report && (
        <ReportSection elevation={3}>
          <Box sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>
              Upload Report
            </Typography>

            <Grid container spacing={3}>
              <Grid item xs={12} md={6}>
                <Typography variant="body1">
                  Status: <Box component="span" color="success.main">{report.status}</Box>
                </Typography>
                <Typography variant="body1">
                  Report ID: {report.report_id}
                </Typography>
              </Grid>

              <Grid item xs={12} md={6}>
                <Typography variant="body1">
                  Successful Uploads: {report.successful_uploads}
                </Typography>
                <Typography variant="body1">
                  Failed Uploads: {report.failed_uploads}
                </Typography>
              </Grid>
            </Grid>

            {report.errors.length > 0 && (
              <Box sx={{ mt: 3 }}>
                <Typography variant="h6">Errors:</Typography>
                <List dense>
                  {report.errors.map((error, index) => (
                    <ListItem key={index} sx={{ color: 'error.main' }}>
                      <ListItemText
                        primary={`Row ${error.row}: ${error.error}`}
                        secondary={`Data: ${JSON.stringify(error.data)}`}
                      />
                    </ListItem>
                  ))}
                </List>
              </Box>
            )}
          </Box>
        </ReportSection>
      )}
    </Container>
  );
}

export default App;