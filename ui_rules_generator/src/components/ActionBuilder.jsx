// ActionBuilder.jsx
import React from 'react';
import { Form, Input, Button, Card, message } from 'antd';

const parseDSL = (dslText) => {
  const lines = dslText
    .split(";")
    .map(line => line.trim())
    .filter(line => line.length > 0);

  const result = {
    type: undefined,
    parameters: {}
  };

  for (let line of lines) {
    const match = line.match(/^set\s+(.+?)\s+to\s+(.+)$/i);
    if (!match) {
      throw new Error(`Invalid DSL syntax: "${line}"`);
    }

    let [, key, value] = match;
    // Trim whitespace from key and value
    key = key.trim();
    value = value.trim();


    // Strip quotes from value if present
    value = value.trim().replace(/^["'](.+?)["']$/, '$1');

    if (key.toLowerCase() === 'type') {
      result.type = value;
    } else {
      result.parameters[key] = value;
    }
  }

  if (!result.type) {
    throw new Error("Missing required 'type' in DSL");
  }

  return result;
};

const ActionBuilder = ({ form }) => (
  <Card title="Define Actions">
    <Form.List name="actions">
      {(fields, { add, remove }) => (
        <>
          {fields.map(({ key, name, ...restField }) => (
            <div key={key} className="action-row" style={{ marginBottom: 16 }}>
              <Form.Item
                {...restField}
                name={[name, 'dsl']}
                label="Action DSL"
                rules={[
                  { required: true, message: 'Please enter DSL for the action' },
                  {
                    validator: (_, value) => {
                      try {
                        parseDSL(value);
                        return Promise.resolve();
                      } catch (error) {
                        return Promise.reject(new Error(error.message));
                      }
                    },
                  },
                ]}
              >
                <Input.TextArea
                  placeholder={`Example:\nset type to calculate_rmd_amount;\nset formula to 'prior_year_end_balance / uniform_life_table_factor';\nset description to "Annual RMD calculation";`}
                  rows={5}
                  style={{ width: '100%' }}
                />
              </Form.Item>
              <Button onClick={() => remove(name)}>Remove</Button>
            </div>
          ))}
          <Button onClick={() => add()}>Add Action</Button>
        </>
      )}
    </Form.List>
  </Card>
);

export { parseDSL };
export default ActionBuilder;
