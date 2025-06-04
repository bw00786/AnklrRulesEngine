import json

def test_integration_evaluate_simple_rule(client, db_session):
    # 1. Insert a rule: if age > 70 then action = {"type":"old","parameters":{}}
    insert = """
    INSERT INTO rules2021 (context, name, priority, description, conditions, actions, active)
    VALUES (
      'test',
      'oldRule',
      10,
      'older than 70',
      'age > 70',
      '[{"type":"flag_old","parameters":{}}]',
      1
    )
    """
    db_session.execute(insert)
    db_session.commit()

    # 2. Call /evaluate_rules/
    resp = client.post(
      "/evaluate_rules/",
      json={"context":"test","facts":{"age":75}}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["matched_rules"] == 1
    assert data["actions_triggered"][0]["type"] == "flag_old"
