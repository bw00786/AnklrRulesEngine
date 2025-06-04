// RulePreview.jsx
import React from 'react';
import { Table, Button, Typography } from 'antd';

const { Title } = Typography;

const RulePreview = ({ rules, onFinalSubmit }) => {
    console.log('Rules in Preview:', rules); // 👈 Debug log
  const columns = [
    { title: 'Rule Name', dataIndex: 'name' },
    { title: 'Description', dataIndex: 'description' },
    { title: 'Priority', dataIndex: 'priority' },
    { 
      title: 'Conditions', 
      render: (_, record) => (
        <ul>
          {record.conditions?.map((cond, i) => (
            <li key={i}>{`${cond.field} ${cond.operator} ${cond.value}`}</li>
          ))}
        </ul>
      )
    },
    {
      title: 'Actions',
      render: (_, record) => (
        <ul>
          {record.actions?.map((action, i) => (
            <li key={i}>{`${action.type}: ${JSON.stringify(action.parameters)}`}</li>
          ))}
        </ul>
      )
    }
  ];

  return (
    <div className="rule-preview">
      <Title level={4} style={{ marginBottom: 24 }}>
        Rules to be Submitted ({rules.length})
      </Title>
      
      <Table
        columns={columns}
        dataSource={rules}
        rowKey={(record) => `${record.name}-${record.priority}-${Math.random().toString(36).substr(2, 9)}`} 
        bordered
        pagination={false}
      />

      <div style={{ marginTop: 24, textAlign: 'right' }}>
        <Button 
          type="primary" 
          size="large"
          onClick={onFinalSubmit}
        >
          Confirm Submission ({rules.length} Rules)
        </Button>
      </div>
    </div>
  );
};

export default RulePreview;