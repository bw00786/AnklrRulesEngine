// src/components/RuleBuilder.jsx
import React, { useState } from 'react';
import { 
  Button, 
  Card, 
  Steps, 
  Form, 
  Input, 
  Select,
  message,
  Alert 
} from 'antd';
import ConditionBuilder from './ConditionBuilder';
import ActionBuilder from './ActionBuilder';
import RulePreview from './RulePreview';
import { parseDSL } from './ActionBuilder';

const { Step } = Steps;
const { Option } = Select;

const RuleBuilder = ({ onSubmit, onComplete }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [rules, setRules] = useState([]);
  const [form] = Form.useForm();

  const steps = [
    { title: 'Rule Metadata' },
    { title: 'Conditions' },
    { title: 'Actions' },
    { title: 'Review' }
  ];

  // Fixed: Removed duplicate handleFinish declaration
  const handleFinish = async () => {
    try {
      const values = await form.validateFields();
    
      
      const newRule = {
        name: values.name,
        description: values.description,
        context: values.context || 'RMD_Distribution',
        priority: values.priority,
        conditions: values.conditions?.map(c => ({
          field: c.field,
          operator: c.operator,
          value: c.value
        })) || [],
        actions: values.actions?.map(a => parseDSL(a.dsl)) || []
      };

      setRules(prev => [...prev, newRule]);
      onSubmit([newRule]);
      form.resetFields();
      setCurrentStep(steps.length - 1); // Stay in Review after saving
      message.success('Rule saved successfully!');
    } catch (error) {
      message.error('Cannot save - please fix validation errors');
    }
  };

  const handleNext = async () => {
    try {
      const currentStepFields = {
        0: ['name', 'description', 'priority'],
        1: ['conditions'],
        2: ['actions']
      }[currentStep];
  
      await form.validateFields(currentStepFields);
      setCurrentStep(prev => prev + 1);
    } catch (error) {
      message.error(`Please complete required fields in ${steps[currentStep].title} step`);
    }
  };

  return (
    <div className="rule-builder">
      <Steps current={currentStep} style={{ marginBottom: 24 }}>
        {steps.map(step => <Step key={step.title} title={step.title} />)}
      </Steps>
  
      <Form form={form} layout="vertical">
        {/* Step 0: Metadata */}
        <div style={{ display: currentStep === 0 ? 'block' : 'none' }}>
          <Card title="Rule Metadata">
            <Form.Item 
              name="name" 
              label="Rule Name"
              rules={[{ required: true, message: 'Please enter a rule name' }]}
            >
              <Input placeholder="Enter rule name" />
            </Form.Item>
  
            <Form.Item
              name="description"
              label="Description"
              rules={[{ required: true, message: 'Please enter a description' }]}
            >
              <Input.TextArea rows={3} placeholder="Rule description" />
            </Form.Item>
  
            <Form.Item
              name="context"
              label="Context"
              initialValue="RMD_Distribution"
            >
              <Select>
                <Option value="RMD_Distribution">RMD Distribution</Option>
                <Option value="Other_Context">Other Context</Option>
              </Select>
            </Form.Item>
  
            <Form.Item
              name="priority"
              label="Priority"
              rules={[{ required: true, message: 'Please select priority' }]}
              initialValue={5}
            >
              <Select>
                {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(n => (
                  <Option key={n} value={n}>
                    {n} - {n === 10 ? 'Highest' : n === 1 ? 'Lowest' : ''}
                  </Option>
                ))}
              </Select>
            </Form.Item>
          </Card>
        </div>
  
        {/* Step 1: Conditions */}
        <div style={{ display: currentStep === 1 ? 'block' : 'none' }}>
          <ConditionBuilder form={form} />
        </div>
  
        {/* Step 2: Actions */}
        <div style={{ display: currentStep === 2 ? 'block' : 'none' }}>
          <ActionBuilder form={form} />
        </div>
  
        {/* Step 3: Review */}
        <div style={{ display: currentStep === 3 ? 'block' : 'none' }}>
          <RulePreview rules={rules} />
          {form.getFieldsError().some(f => f.errors.length > 0) && (
            <Alert
              message="Validation Errors Exist"
              description="Please go back and fix the highlighted fields"
              type="error"
              showIcon
            />
          )}
        </div>
  
        {/* Navigation buttons */}
        <div className="navigation-buttons" style={{ marginTop: 24 }}>
          {currentStep > 0 && (
            <Button onClick={() => setCurrentStep(currentStep - 1)}>
              Previous
            </Button>
          )}
  
          {currentStep < steps.length - 1 ? (
            <Button type="primary" onClick={handleNext}>
              Next
            </Button>
          ) : (
            <div>
              <Button 
                type="primary" 
                onClick={handleFinish}
                style={{ marginRight: 8 }}
              >
                Save Rule
              </Button>
              <Button 
                type="primary" 
                onClick={() => onComplete(rules)}
              >
                Submit All Rules ({rules.length})
              </Button>
            </div>
          )}
        </div>
      </Form>
    </div>
  );

}

export default RuleBuilder;