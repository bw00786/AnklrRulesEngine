import React, { useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  TextField,
  Button,
  Grid,
  Paper,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Card,
  CardContent,
  Chip,
  CircularProgress,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  Alert
} from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/system';

const StyledCard = styled(Card)(({ theme }) => ({
  marginTop: theme.spacing(4),
  boxShadow: theme.shadows[4],
  borderRadius: '12px',
  background: theme.palette.background.paper,
}));

const ResultSection = styled(Paper)(({ theme, eligible }) => ({
  padding: theme.spacing(3),
  marginTop: theme.spacing(3),
  backgroundColor: eligible ? '#e8f5e9' : '#ffebee',
  borderRadius: '8px',
  borderLeft: `4px solid ${eligible ? '#4caf50' : '#f44336'}`
}));

const RmdCalculator = () => {
  const [formData, setFormData] = useState({
    participant_age: '',
    participant_status: 'Active',
    plan_type: '401K',
    prior_year_end_balance: '',
    uniform_life_table_factor: '16.5',
    dob: null,
    ownership_percent: '',
    marital_status: 'Single'
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const planTypes = ['401K', '403B', '457B', 'IRA', 'Roth IRA'];
  const statusOptions = ['Active', 'Not Active', 'Deceased'];
  const maritalStatuses = ['Single', 'Divorced', 'Married', 'Widowed'];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    
    try {
      const payload = {
        context: "RMD_Distribution",
        facts: {
          ...formData,
          dob: formData.dob?.toISOString().split('T')[0],
          marital_status: formData.marital_status,
          // Convert all numeric fields to proper types
          participant_age: parseInt(formData.participant_age, 10),
          prior_year_end_balance: parseFloat(formData.prior_year_end_balance),
          uniform_life_table_factor: parseFloat(formData.uniform_life_table_factor),
          ownership_percent: parseFloat(formData.ownership_percent)
        }
      };

      const response = await axios.post('http://localhost:8000/evaluate_rules/', payload);
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Error calculating RMD');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom sx={{ fontWeight: 600 }}>
        RMD Distribution Calculator
      </Typography>

      <StyledCard>
        <CardContent>
          <form onSubmit={handleSubmit}>
            <Grid container spacing={3}>
              <Grid item xs={12} sm={6}>
                <DatePicker
                  label="Date of Birth"
                  value={formData.dob}
                  onChange={(newValue) => setFormData({ ...formData, dob: newValue })}
                  renderInput={(params) => <TextField {...params} fullWidth />}
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Participant Age"
                  name="participant_age"
                  type="number"
                  value={formData.participant_age}
                  onChange={handleChange}
                  required
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Plan Type</InputLabel>
                  <Select
                    name="plan_type"
                    value={formData.plan_type}
                    onChange={handleChange}
                    label="Plan Type"
                  >
                    {planTypes.map(type => (
                      <MenuItem key={type} value={type}>{type}</MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Participant Status</InputLabel>
                  <Select
                    name="participant_status"
                    value={formData.participant_status}
                    onChange={handleChange}
                    label="Participant Status"
                  >
                    {statusOptions.map(status => (
                      <MenuItem key={status} value={status}>{status}</MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12} sm={6}>
                <FormControl fullWidth>
                  <InputLabel>Marital Status</InputLabel>
                  <Select
                    name="marital_status"
                    value={formData.marital_status}
                    onChange={handleChange}
                    label="Marital Status"
                  >
                    {maritalStatuses.map(status => (
                      <MenuItem key={status} value={status}>{status}</MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Prior Year Balance ($)"
                  name="prior_year_end_balance"
                  type="number"
                  value={formData.prior_year_end_balance}
                  onChange={handleChange}
                  inputProps={{
                    step: "0.01"
                  }}
                  required
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Uniform Life Table Factor"
                  name="uniform_life_table_factor"
                  type="number"
                  value={formData.uniform_life_table_factor}
                  onChange={handleChange}
                  inputProps={{
                    step: "0.1"
                  }}
                  required
                />
              </Grid>

              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Ownership Percent"
                  name="ownership_percent"
                  type="number"
                  value={formData.ownership_percent}
                  onChange={handleChange}
                  inputProps={{
                    step: "0.1"
                  }}
                  required
                />
              </Grid>

              <Grid item xs={12}>
                <Button
                  type="submit"
                  variant="contained"
                  size="large"
                  disabled={loading}
                  sx={{ py: 1.5 }}
                >
                  {loading ? <CircularProgress size={24} /> : 'Calculate RMD'}
                </Button>
              </Grid>
            </Grid>
          </form>

          {error && (
            <Alert severity="error" sx={{ mt: 3 }}>
              {error}
            </Alert>
          )}
        </CardContent>
      </StyledCard>

      {/* Result display remains unchanged */}
      {result && (
  <div>
    <ResultSection eligible={result.eligible} sx={{ mt: 4 }}>
      <Typography variant="h5" gutterBottom sx={{ fontWeight: 600 }}>
        RMD Eligibility: {result.eligible ? 'Required' : 'Not Required'}
      </Typography>
      
      {result.eligible && (
        <div>
          <Typography variant="h6" sx={{ mt: 2 }}>
            Annual RMD Amount: ${result.annual_rmd_amount?.toLocaleString() || 'N/A'}
          </Typography>
          
          <Grid container spacing={2} sx={{ mt: 1 }}>
            <Grid item xs={6}>
              <Typography variant="body1">
                Balance Used: ${result.calculation_details?.balance_used?.toLocaleString()}
              </Typography>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="body1">
                Divisor Used: {result.calculation_details?.divisor_used}
              </Typography>
            </Grid>
            <Grid item xs={12}>
              <Typography variant="body2" color="textSecondary">
                Calculation Method: {result.calculation_details?.calculation_method}
              </Typography>
            </Grid>
          </Grid>
        </div>
      )}
    </ResultSection>

    <StyledCard sx={{ mt: 4 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom sx={{ fontWeight: 600 }}>
          Matched Rules ({result.rules_matched})
        </Typography>
        
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '16px' }}>
          {result.raw_response.matched_rule_names.map((rule) => (
            <Chip
              key={rule}
              label={rule}
              color="primary"
              variant="outlined"
              sx={{ fontWeight: 500 }}
            />
          ))}
        </div>

        <Accordion>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography variant="subtitle1">Detailed API Response</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <pre style={{ 
              whiteSpace: 'pre-wrap', 
              wordBreak: 'break-word',
              backgroundColor: '#f5f5f5',
              padding: '16px',
              borderRadius: '4px'
            }}>
              {JSON.stringify(result.raw_response, null, 2)}
            </pre>
          </AccordionDetails>
        </Accordion>
      </CardContent>
    </StyledCard>
  </div>
)}
</Container>
  );
};

export default RmdCalculator;