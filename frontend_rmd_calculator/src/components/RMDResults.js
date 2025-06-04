import React, { useState } from 'react';
import { format } from 'date-fns';
import './RMDCalculator.css';


const RMDCalculator = () => {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  
  const currentYear = new Date().getFullYear();
  
  const [formData, setFormData] = useState({
    participant_age: '',
    participant_status: 'Active',
    account_balance: '',
    dob: '',
    plan_type: '401K',
    marital_status: 'Spouse is not more than 10 years younger',
    current_year: currentYear,
    current_month: new Date().getMonth() + 1,
    current_day: new Date().getDate(),
    attains_age_73_in_2025: 'N',
    prior_year_end_balance: '',
    beneficiary: 'Spouse',
    beneficiary_allocation: 100,
    beneficiary_age_plus_10: '',
    uniform_life_table_factor: '',
    distribution_schedule: 'monthly',
    distribution_start_date: format(new Date(), 'yyyy-MM-dd'),
    distribution_end_date: '',
    distribution_end_type: 'ongoing'
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    
    if (name === 'dob') {
      const birthDate = new Date(value);
      const today = new Date();
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDiff = today.getMonth() - birthDate.getMonth();
      
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
      
      const attains73In2025 = 
        (birthDate.getFullYear() === 1952) || 
        (birthDate.getFullYear() === 1953 && 
        ((birthDate.getMonth() < today.getMonth()) || 
        (birthDate.getMonth() === today.getMonth() && birthDate.getDate() <= today.getDate())));
      
      setFormData({
        ...formData,
        [name]: value,
        participant_age: age,
        attains_age_73_in_2025: attains73In2025 ? 'Y' : 'N'
      });
    } else {
      setFormData({
        ...formData,
        [name]: value
      });
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      const payload = {
        context: "RMD_Distribution",
        facts: {
          ...formData,
          account_balance: parseFloat(formData.account_balance),
          prior_year_end_balance: parseFloat(formData.prior_year_end_balance),
          beneficiary_age_plus_10: parseInt(formData.beneficiary_age_plus_10),
          beneficiary_allocation: parseInt(formData.beneficiary_allocation),
          uniform_life_table_factor: parseFloat(formData.uniform_life_table_factor),
        }
      };
      
      const response = await fetch('http://localhost:8080/api/evaluate_rmd', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      
      if (!response.ok) {
        throw new Error(`API request failed with status: ${response.status}`);
      }
      
      const data = await response.json();
      setResults(data);
      
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rmd-calculator">
      <div className="calculator-container">
        <h1>Required Minimum Distribution Calculator</h1>
        <p className="description">
          Determine eligibility and calculate Required Minimum Distributions for retirement accounts.
        </p>
        
        <form onSubmit={handleSubmit} className="calculator-form">
          {/* Keep all form fields exactly as they were in your original code */}
          {/* ... [All your existing form fields remain unchanged] ... */}
          
          <div className="form-actions">
            <button type="submit" className="btn-primary" disabled={loading}>
              {loading ? 'Calculating...' : 'Calculate RMD'}
            </button>
            <button type="button" className="btn-secondary" onClick={() => window.location.reload()}>
              Reset
            </button>
          </div>
        </form>
      </div>

      {error && (
        <div className="results-container error">
          <h2>Error</h2>
          <p>{error}</p>
        </div>
      )}

      {results && !error && (
        <div className="results-container">
          <h2>RMD Calculation Results</h2>
          
          <div className="results-section">
            <h3>Eligibility Summary</h3>
            <div className="result-row">
              <span className="result-label">Eligible for RMD:</span>
              <span className="result-value">{results.eligible ? 'Yes' : 'No'}</span>
            </div>
            {results.eligible && (
              <>
                <div className="result-row">
                  <span className="result-label">RMD Status:</span>
                  <span className="result-value">{results.rmd_status}</span>
                </div>
                <div className="result-row">
                  <span className="result-label">Annual RMD Amount:</span>
                  <span className="result-value">
                    ${results.annual_rmd_amount?.toFixed(2) || '0.00'}
                  </span>
                </div>
              </>
            )}
          </div>
          
          {results.eligible && results.calculation_details && (
            <div className="results-section">
              <h3>Calculation Details</h3>
              <div className="result-row">
                <span className="result-label">Account Balance Used:</span>
                <span className="result-value">
                  ${(results.calculation_details.balance_used?.toFixed(2) || 'N/A')}
                </span>
              </div>
              <div className="result-row">
                <span className="result-label">Life Expectancy Factor:</span>
                <span className="result-value">
                  {results.calculation_details.divisor_used || 'N/A'}
                </span>
              </div>
              <div className="result-row">
                <span className="result-label">Calculation Method:</span>
                <span className="result-value">
                  {results.calculation_details.calculation_method}
                </span>
              </div>
            </div>
          )}

          {results.eligible && (
            <div className="results-section">
              <h3>Additional Information</h3>
              <div className="result-row">
                <span className="result-label">Rules Matched:</span>
                <span className="result-value">{results.rules_matched}</span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default RMDCalculator;