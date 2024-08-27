import { test, expect } from '../fixtures/base-test';

async function create_endpoint_steps(page,name,uri,token,connectorType,maxCallPerSec,maxConcurr,otherParams) {
  await page.goto('http://localhost:3000/endpoints/new');
  await page.getByPlaceholder('Name of the model').click();
  await page.getByPlaceholder('Name of the model').fill(name);
  await page.locator('.aiv__input-container').click();
  await page.getByRole('option', { name: connectorType, exact: true }).click();
  await page.getByPlaceholder('URI of the remote model').click();
  await page.getByPlaceholder('URI of the remote model').fill(uri);
  await page.getByPlaceholder('Access token for the remote').click();
  await page.getByPlaceholder('Access token for the remote').fill(token);
  await page.getByText('More Configs').click();
  await page.locator('.aiv__input-container').first().click();
  await page.getByRole('option', { name: maxCallPerSec}).click();
  await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
  await page.getByRole('option', { name: maxConcurr }).click();
  await page.getByPlaceholder('Additional parameters').click();
  await page.getByPlaceholder('Additional parameters').fill(otherParams);
  await page.getByRole('button', { name: 'OK' }).click();
  await page.getByRole('button', { name: 'Save' }).click();

  //Verify Expected redirection
  await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));
  //Verify Endpoint Created Successfully
  await await page.getByRole('link', { name: 'name Type openai-connector' }).click();
  await page.locator('div').filter({ hasText: /^test$/ }).isVisible();
  await page.getByText(uri, { exact: true }).isVisible();
  await page.getByText('********').isVisible();
  await page.getByText('3', { exact: true }).isVisible();
  await page.getByText('2', { exact: true }).isVisible();
  await page.getByText('{ "model": "123", "').isVisible();
}

test('test_create_endpoint_with_same_name_not_exist', async ({ page }) => {
 await create_endpoint_steps(page,'name','uri','token123','openai-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_name_eq_empty', async ({ page }) => {
  await page.goto('http://localhost:3000/endpoints/new');
  await page.getByPlaceholder('Name of the model').click();
  await page.locator('.aiv__input-container').click();
  await page.getByRole('option', { name: 'openai-connector', exact: true }).click();
  await page.getByPlaceholder('URI of the remote model').click();
  await page.getByPlaceholder('URI of the remote model').fill('uri');
  await page.getByPlaceholder('Access token for the remote').click();
  await page.getByPlaceholder('Access token for the remote').fill('token123');
  await page.getByText('More Configs').click();
  await page.locator('.aiv__input-container').first().click();
  await page.getByRole('option', { name: '3' }).click();
  await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
  await page.getByRole('option', { name: '2' }).click();
  await page.getByPlaceholder('Additional parameters').click();
  await page.getByPlaceholder('Additional parameters').click();
  await page.getByPlaceholder('Additional parameters').press('ArrowDown');
  await page.getByPlaceholder('Additional parameters').press('ArrowLeft');
  await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }');
  await page.getByRole('button', { name: 'OK' }).click();
  // Select the Save button
  const saveBtn = page.getByRole('button', { name: 'Save' });
  // Check if the Save button is disabled
  await expect(saveBtn).toBeDisabled();
  //Check for Name error message display
  await page.getByText('Name is required').isVisible()
});

test('test_create_endpoint_with_same_name_exist', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name','uri','token123','openai-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
  //Attempt to create same name but different configuration endpoint
  await create_endpoint_steps(page,'name','uri123','token123','openai-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_together_connector', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name_together-connector','uri','token123','together-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});
test('test_create_endpoint_with_connectorType_claude2_connector', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name_claude2-connector','uri','token123','claude2-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});
test('test_create_endpoint_with_connectorType_huggingface_connector', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name_huggingface-connector','uri','token123','huggingface-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_flageval_connector', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name_flageval-connector','uri','token123','flageval-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_azure_openai_connector', async ({ page }) => {
  //Set the viewport size
  await page.setViewportSize({"width": 1024, "height": 768})
  //Create new endpoints
  await create_endpoint_steps(page,'name_azure-openai-connector','uri','token123','azure-openai-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')

});


test('test_create_endpoint_without_uri&token', async ({ page }) => {
  await page.goto('http://127.0.0.1:3000/endpoints');
  await page.getByRole('link', { name: 'model endpoints' }).click();
  await page.getByRole('button', { name: 'Create New Endpoint' }).click();
  await page.getByPlaceholder('Name of the model').click();
  await page.getByPlaceholder('Name of the model').fill('test');
  await page.locator('div').filter({ hasText: /^Select the connector type$/ }).nth(2).click();
  await page.getByRole('option', { name: 'openai-connector', exact: true }).click();
  // Select the Save button
  const saveBtn = page.getByRole('button', { name: 'Save' });
  // Check if the Save button is disabled
  await expect(saveBtn).toBeDisabled();
});
test('test_create_endpoint_with_uri_empty', async ({ page }) => {
  //Create new endpoints
  await create_endpoint_steps(page,'name_azure-openai-connector','','token123','azure-openai-connector','3','2','{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')

});
test.only('test_create_endpoint_with_token_empty', async ({ page }) => {
  await page.goto('http://localhost:3000/endpoints/new');
  await page.getByPlaceholder('Name of the model').click();
  await page.getByPlaceholder('Name of the model').fill("test_token_empty");
  await page.locator('.aiv__input-container').click();
  await page.getByRole('option', { name: 'azure-openai-connector', exact: true }).click();
  await page.getByPlaceholder('URI of the remote model').click();
  await page.getByPlaceholder('URI of the remote model').fill('uri');
  await page.getByPlaceholder('Access token for the remote').click();
  await page.getByPlaceholder('Access token for the remote').fill('');
  // Select the Save button
  const saveBtn = page.getByRole('button', { name: 'Save' });
  // Check if the Save button is disabled
  await expect(saveBtn).toBeDisabled();

});