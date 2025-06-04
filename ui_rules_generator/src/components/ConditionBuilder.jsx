import React from 'react';
import { Form, Select, Input, Button, Card } from 'antd';

const ConditionBuilder = ({ form }) => {
  const operators = ['==', '!=', '>', '<', '>=', '<=', 'in'];
  const availableFields = [ // Renamed from fields to avoid conflict
    'participant_age', 
    'participant_status',
    'ownership_percentage',
    'plan_type',
    'refRule', 
    'dob',
    'qcd_amount',
    'missed_rmd',
    'marital_status',
    'prior_year_end_balance',
    'uniform_life_table_factor'
  ];

  const renderValueInput = (operator) => {
    if (operator === 'in') {
      return <Input placeholder="Comma separated values (e.g. 401K,403B)" />;
    }
    return <Input placeholder="Enter value" />;
  };

  return (
    <Card title="Define Conditions">
      <Form.List name="conditions">
        {(fields, { add, remove }) => (
          <>
            {fields.map(({ key, name, ...restField }) => (
              <div key={key} className="condition-row">
                <Form.Item
                  {...restField}
                  name={[name, 'field']}
                >
                  <Select placeholder="Select field" style={{ width: 200 }}>
                    {availableFields.map(f => (
                      <Select.Option key={f} value={f}>
                        {f.replace(/_/g, ' ').toLowerCase()}
                      </Select.Option>
                    ))}
                  </Select>
                </Form.Item>

                <Form.Item
                  {...restField}
                  name={[name, 'operator']}
                >
                  <Select placeholder="Operator" style={{ width: 100 }}>
                    {operators.map(op => (
                      <Select.Option key={op} value={op}>
                        {op}
                      </Select.Option>
                    ))}
                  </Select>
                </Form.Item>

                <Form.Item
                  {...restField}
                  name={[name, 'value']}
                >
                  {renderValueInput(form.getFieldValue(['conditions', name, 'operator']))}
                </Form.Item>

                <Button onClick={() => remove(name)}>Remove</Button>
              </div>
            ))}
            <Button onClick={() => add()}>Add Condition</Button>
          </>
        )}
      </Form.List>
    </Card>
  );
};

export default ConditionBuilder;