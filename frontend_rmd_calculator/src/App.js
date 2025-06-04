import { useState } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import RmdCalculator from './components/RMDCalculator';
import RuleSubmitForm from './components/RuleSubmitForm';
import { Button, Box, Switch, Typography, FormControlLabel } from '@mui/material';

const theme = createTheme();

function App() {
  const [selectedComponent, setSelectedComponent] = useState('rmd');
  const [llmEnabled, setLlmEnabled] = useState(true);

  return (
    <ThemeProvider theme={theme}>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <Box sx={{ maxWidth: 800, margin: '0 auto', p: 3 }}>
          <Box sx={{ mb: 3, display: 'flex', gap: 2, alignItems: 'center' }}>
            <Box sx={{ flexGrow: 1, display: 'flex', gap: 2 }}>
              <Button
                variant={selectedComponent === 'rmd' ? 'contained' : 'outlined'}
                onClick={() => setSelectedComponent('rmd')}
              >
                RMD Calculator
              </Button>
              <Button
                variant={selectedComponent === 'rule' ? 'contained' : 'outlined'}
                onClick={() => setSelectedComponent('rule')}
              >
                Rule Submit Form
              </Button>
            </Box>
            {selectedComponent === 'rule' && (
              <FormControlLabel
                control={
                  <Switch
                    checked={llmEnabled}
                    onChange={(e) => setLlmEnabled(e.target.checked)}
                  />
                }
                label="LLM Enabled"
                labelPlacement="start"
              />
            )}
          </Box>

          {selectedComponent === 'rmd' ? (
            <RmdCalculator />
          ) : (
            <RuleSubmitForm featureFlags={{ llmEnabled }} />
          )}
        </Box>
      </LocalizationProvider>
    </ThemeProvider>
  );
}

export default App;