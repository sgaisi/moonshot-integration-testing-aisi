import { test } from '@playwright/test';
import {expect} from "@playwright/test";

export async function create_endpoint_steps(page, name, uri, token, connectorType, maxCallPerSec, maxConcurr, otherParams, uriSkipCheck?: boolean) {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill(name);
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: connectorType, exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill(uri);
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill(token);
    await page.getByText('More Configs').click();
    if (maxCallPerSec != '') {
        await page.locator('.aiv__input-container').first().click();
        await page.getByRole('option', {name: maxCallPerSec}).click();
    }
    if (maxConcurr != '') {
        await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
        await page.getByRole('option', {name: maxConcurr}).click();
    }
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill(otherParams);
    await page.getByRole('button', {name: 'OK'}).click();
    await page.getByRole('button', {name: 'Save'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));
    //Verify Endpoint Created Successfully
    await page.getByRole('link', {name: name}).click();
    await expect(page.locator('h3')).toHaveText(name, {timeout: 600000})
    if (uriSkipCheck == false) {
        if (uri != '') {
            await expect(page.getByText('uri', {exact: true})).toBeVisible();
        } else {
            await expect(page.getByText('Not set').first()).toBeVisible();
        }
    }

    if (maxCallPerSec != '') {
        await page.getByText(maxCallPerSec, {exact: true}).isVisible();
    } else {
        await expect(page.getByText('10', {exact: true})).toBeVisible();
    }
    if (maxConcurr != '') {
        await expect(page.getByText(maxConcurr, {exact: true})).toBeVisible();
    } else {
        await expect(page.getByText('1', {exact: true})).toBeVisible()
    }
    await expect(page.getByText(otherParams)).toBeVisible()
}
test('test_create_endpoint_with_same_name_not_exist', async ({page}) => {
    await create_endpoint_steps(page, 'name_azure-openai-connector', 'uri', 'token123', 'openai-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_name_eq_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token123');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').press('ArrowDown');
    await page.getByPlaceholder('Additional parameters').press('ArrowLeft');
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }');
    await page.getByRole('button', {name: 'OK'}).click();
    // Select the Save button
    const saveBtn = page.getByRole('button', {name: 'Save'});
    // Check if the Save button is disabled
    await expect(saveBtn).toBeDisabled();
    //Check for Name error message display
    await expect(page.getByText('Name is required')).toBeVisible()
});

test('test_create_endpoint_with_same_name_exist', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_azure-openai-connector', 'uri', 'token123', 'openai-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 1,\n      "model": "123"\n  }')
    await page.waitForTimeout(5000);
    //Attempt to create same name but different configuration endpoint
    await create_endpoint_steps(page, 'name_azure-openai-connector', 'uri', 'token123', 'openai-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 1,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_together_connector', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_together-connector', 'uri', 'token123', 'together-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});
test('test_create_endpoint_with_connectorType_claude2_connector', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_claude2-connector', 'uri', 'token123', 'claude2-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});
test('test_create_endpoint_with_connectorType_huggingface_connector', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_huggingface-connector', 'uri', 'token123', 'huggingface-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_flageval_connector', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_flageval-connector', 'uri', 'token123', 'flageval-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')
});

test('test_create_endpoint_with_connectorType_azure_openai_connector', async ({page}) => {
    //Set the viewport size
    await page.setViewportSize({"width": 1024, "height": 768})
    //Create new endpoints
    await create_endpoint_steps(page, 'name_azure-openai-connector', 'uri', 'token123', 'azure-openai-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')

});


test('test_create_endpoint_without_uri&token', async ({page}) => {
    await page.goto('http://127.0.0.1:3000/endpoints');
    await page.getByRole('link', {name: 'model endpoints'}).click();
    await page.getByRole('button', {name: 'Create New Endpoint'}).click();
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('test');
    await page.locator('div').filter({hasText: /^Select the connector type$/}).nth(2).click();
    await page.getByRole('option', {name: 'openai-connector', exact: true}).click();
    // Select the Save button
    const saveBtn = page.getByRole('button', {name: 'Save'});
    // Check if the Save button is disabled
    await expect(saveBtn).toBeDisabled();
});
test('test_create_endpoint_with_uri_empty', async ({page}) => {
    //Create new endpoints
    await create_endpoint_steps(page, 'name_azure-openai-connector', '', 'token123', 'azure-openai-connector', '3', '2', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')

});
test('test_create_endpoint_with_token_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill("test_token_empty");
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('');
    // Select the Save button
    const saveBtn = page.getByRole('button', {name: 'Save'});
    // Check if the Save button is disabled
    await expect(saveBtn).toBeDisabled();

});

test('test_create_endpoint_check_default_maxCallPerSec&maxConcurr', async ({page}) => {
    await create_endpoint_steps(page, 'name_azure-openai-connector', 'uri', 'token123', 'azure-openai-connector', '', '', '{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n  }')

});

test('test_create_endpoint_more_config_other_params_empty_json', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{}');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('Parameter "Model" is required')).toBeVisible()
    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_model_params_integer', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": 1\n  }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('model must be a `string` type')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_model_params_decimal', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": 1.1\n  }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('model must be a `string` type')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_model_params_special_character', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": -1\n  }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('model must be a `string` type')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_model_params_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": ""\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('Parameter "Model" is required')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});
test('test_create_endpoint_more_config_timeout_params_string', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": "300",\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('timeout must be a `number` type, but the final value was: `"300"`.\n')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_timeout_params_decimal', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 1.1,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_timeout_params_special_char', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": -300,\n      "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('Timeout must be a positive number\n')).toBeVisible()

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_timeout_params_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n "allow_retries": true,\n      "num_of_retries": 3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected to remain on the same page
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_numOfRetries_params_string', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": "3",\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('num_of_retries must be a `number` type, but the final value was: `"3"`.\n')).toBeVisible()

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_numOfRetries_params_decimal', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": 3.3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_numOfRetries_params_special_char', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n      "num_of_retries": @3,\n      "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    // Use getByText to locate the element by its text
    const expectedErrorMsg1 = page.getByText('Unexpected token \'@\', ..."retries": @3, "... is not valid JSON\n')
    const expectedErrorMsg2 = page.getByText('JSON.parse: unexpected character at line 4 column 25 of the JSON data\n')
    const expectedErrorMsg3 = page.getByText('JSON Parse error: Unrecognized token \'@\'\n')

    if (await expectedErrorMsg1.count() > 0) {
        // Error message is found
        console.log("Error message found.");
        await expect(page.getByText('Unexpected token \'@\', ..."retries": @3, "... is not valid JSON\n')).toBeVisible()

    } else if (await expectedErrorMsg2.count() > 0) {
        // Error message is found
        console.log("Error message found.");
        await expect(page.getByText('JSON.parse: unexpected character at line 4 column 25 of the JSON data\n')).toBeVisible()

    } else if (await expectedErrorMsg3.count() > 0) {
        // Element is found
        console.log("Error message found.");
        await expect(page.getByText('JSON Parse error: Unrecognized token \'@\'\n')).toBeVisible()

    } else {
        console.log("Error message Not found.");
        //Explicitly Fail
        await page.waitForSelector('text=Error message not found', {state: 'visible', timeout: 5000});
    }

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));


});

test('test_create_endpoint_more_config_numOfRetries_params_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n      "allow_retries": true,\n     "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_allowRetries_params_false', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": false,\n     "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_allowRetries_params_!bool', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": 1.1,\n     "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('allow_retries must be a `boolean` type, but the final value was: `1.1`.\n')).toBeVisible()

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_allowRetries_params_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_temperature_params_string', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": true,\n     "temperature": "0.5",\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();
    await expect(page.getByText('temperature must be a `number` type, but the final value was: `"0.5"`.\n')).toBeVisible()

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints/new'));

});

test('test_create_endpoint_more_config_temperature_params_decimal', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": true,\n     "temperature": 0.5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_temperature_params_special_char', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": true,\n     "temperature": -5,\n      "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});

test('test_create_endpoint_more_config_temperature_params_empty', async ({page}) => {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill('name_azure-openai-connector');
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: 'azure-openai-connector', exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill('uri');
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill('token');
    await page.getByText('More Configs').click();
    await page.locator('.aiv__input-container').first().click();
    await page.getByRole('option', {name: '3'}).click();
    await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container').click();
    await page.getByRole('option', {name: '2'}).click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n      "timeout": 300,\n     "num_of_retries": 3,\n  "allow_retries": true,\n   "model": "123"\n }');
    await page.getByRole('button', {name: 'OK'}).click();

    //Verify Expected redirection
    await expect.soft(page).toHaveURL(new RegExp('^http://localhost:3000/endpoints'));

});