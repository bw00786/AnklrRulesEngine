import { parseDSL } from '../components/ActionBuilder';

describe('parseDSL', () => {
  it('parses a basic action DSL with type and parameters', () => {
    const dsl = `
      set type to calculate_rmd_amount;
      set formula to 'prior_year_end_balance / uniform_life_table_factor';
      set description to "Annual RMD calculation";
    `;

    const expected = {
      type: "calculate_rmd_amount",
      parameters: {
        formula: "prior_year_end_balance / uniform_life_table_factor",
        description: "Annual RMD calculation"
      }
    };

    expect(parseDSL(dsl)).toEqual(expected);
  });

  it('parses values without quotes', () => {
    const dsl = `
      set type to boolean_result;
      set result to True;
    `;

    const expected = {
      type: "boolean_result",
      parameters: {
        result: "True"
      }
    };

    expect(parseDSL(dsl)).toEqual(expected);
  });

  it('throws error for missing type', () => {
    const dsl = `
      set result to True;
    `;

    expect(() => parseDSL(dsl)).toThrow("Missing required 'type' in DSL");
  });

  it('throws error for malformed line', () => {
    const dsl = `
      set type calculate_rmd;
    `;

    expect(() => parseDSL(dsl)).toThrow('Invalid DSL syntax');
  });

  it('ignores trailing semicolons and whitespace', () => {
    const dsl = `
      set type to notify;
      set message to 'Account updated';
    `;

    const expected = {
      type: "notify",
      parameters: {
        message: "Account updated"
      }
    };

    expect(parseDSL(dsl)).toEqual(expected);
  });
});
