import React, { useState } from 'react';
import { ConfigProvider, Layout, Menu, Button, Modal, message } from 'antd';
import {
  DashboardOutlined,
  FormOutlined,
  DatabaseOutlined,
  SettingOutlined
} from '@ant-design/icons';
import RuleBuilder from './components/RuleBuilder';
import RulePreview from './components/RulePreview';
import './App.css';

const { Header, Sider, Content } = Layout;

const App = () => {
  const [showRulesetForm, setShowRulesetForm] = useState(false);
  const [submissionStatus, setSubmissionStatus] = useState(null);
  const [currentRuleset, setCurrentRuleset] = useState([]);

  const theme = {
    token: {
      colorPrimary: '#1890ff',
      colorSuccess: '#52c41a',
      colorWarning: '#faad14',
      colorError: '#ff4d4f',
      colorInfo: '#1890ff',
      fontSize: 14,
      borderRadius: 6,
      colorTextBase: '#1a3353',
      colorBgBase: '#ffffff',
    },
    components: {
      Layout: {
        headerBg: '#1a3353',
        headerColor: '#ffffff',
        siderBg: '#f0f2f5',
      },
      Button: {
        defaultHoverBorderColor: '#1890ff',
        defaultHoverColor: '#1890ff',
      },
    },
  };

  const handleNewRuleset = () => {
    console.log("New Ruleset button clicked");
    setShowRulesetForm(true);
   //  setCurrentRuleset([]);
  };

  const handleSubmitSuccess = () => {
    console.log('Rules submitted successfully')
    message.success('Rules submitted successfully!');
    setShowRulesetForm(false);
    setSubmissionStatus('success');
  };

  const handleSubmitError = (error) => {
    message.error(`Submission failed: ${error.message}`);
    setSubmissionStatus('error');
  };

  const menuItems = [
    { key: '1', icon: <DashboardOutlined />, label: 'Dashboard' },
    { key: '2', icon: <FormOutlined />, label: 'Rules Builder' },
    { key: '3', icon: <DatabaseOutlined />, label: 'Rules Library' },
    { key: '4', icon: <SettingOutlined />, label: 'Settings' },
  ];

  return (
    <ConfigProvider theme={theme}>
      <Layout style={{ minHeight: '100vh' }}>
        <Sider width={250} theme="light">
          <div className="logo-container">
            <h1 className="logo-text">RMD Rules Studio</h1>
          </div>
          <Menu
            mode="inline"
            defaultSelectedKeys={['2']}
            items={menuItems}
            style={{ padding: '16px 0' }}
          />
        </Sider>

        <Layout>
          <Header style={{ padding: 0, background: theme.components.Layout.headerBg }}>
            <div className="header-content">
              <h2 className="page-title">Rules Authoring Workspace</h2>
              <Button 
                type="primary" 
                size="large"
                onClick={handleNewRuleset}
              >
                + New Ruleset
              </Button>
            </div>
          </Header>

          <Content style={{ margin: '24px 16px', padding: 24, background: '#fff' }}>
            {submissionStatus === 'success' ? (
              <div className="success-message">
                <h3>✓ Rules Submitted Successfully</h3>
                <Button 
                  type="primary" 
                  onClick={() => setSubmissionStatus(null)}
                >
                  View Rules Library
                </Button>
              </div>
            ) : (
              <div className="workspace-container">
                <RulePreview rules={currentRuleset} />
              </div>
            )}
          </Content>
        </Layout>

        <Modal
          title="Create New Ruleset"
          width={1200}
          open={showRulesetForm}
          onCancel={() => {
            setShowRulesetForm(false);
            setCurrentRuleset(currentRuleset);
          }}
          footer={null}
          destroyOnClose// Add this to reset child component state
>
          <RuleBuilder 
            onSubmit={(newRules) => {
              console.log('Adding new rules:', newRules);
              setCurrentRuleset(prev => [...prev, ...newRules]);
            }}
            onComplete={(allRules) => {
              // Connect to your backend API here
              console.log('Final submission:', allRules);
              console.log('Submitted Rules:', allRules); // 👈 Debug log
              try {
                setCurrentRuleset([]); 
                // await api.post('/rules/bulk', { rules: allRules });
                handleSubmitSuccess();
              } catch (error) {
                console.log("hand submit error {}", error)
                handleSubmitError(error);
              }
            }}
            existingRules={currentRuleset} // Pass current rule
          />
        </Modal>
      </Layout>
    </ConfigProvider>
  );
};

export default App;
