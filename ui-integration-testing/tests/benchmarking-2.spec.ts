import {Page, test} from '@playwright/test';
import {expect} from "@playwright/test";
// import {create_endpoint_steps} from './endpoint.spec';
import dotenv from 'dotenv';
import path from 'path';
import fs from "fs/promises";
// Read from ".env" file.
const __dirname: string = '.'
dotenv.config({path: path.resolve(__dirname, '.env')});

export async function create_endpoint_steps(page, name, uri, token, connectorType, maxCallPerSec, maxConcurr, model, otherParams, uriSkipCheck?: boolean) {
    await page.goto('http://localhost:3000/endpoints/new');
    await page.getByPlaceholder('Name of the model').click();
    await page.getByPlaceholder('Name of the model').fill(name);
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: connectorType, exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill(uri);
    await page.getByPlaceholder('Model of the model endpoint').click();
    await page.getByPlaceholder('Model of the model endpoint').fill(model);
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill(token);
    await page.getByText('More Configs').click();
    if (maxCallPerSec != '') {
        await page.locator('.aiv__input-container').first().click();
        await page.getByRole('option', {name: maxCallPerSec}).click();
    }
    if (maxConcurr != '') {
        await page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container')
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
    // Check for display of addtional parameters @ http://localhost:3000/endpoints page
    await expect(page.locator('pre')).toContainText(otherParams);

}

export async function create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME) {
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
}


export async function download_validation_steps(page) {
    // Benchmarking
    console.log('Download Validation')
    const downloadPromise = page.waitForEvent('download');
    await page.getByRole('button', {name: 'Download Report'}).click();
    const download = await downloadPromise;
}

test('test_benchmarking_two_endpoint', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const ENDPOINT_NAME_2: string = "Azure OpenAI 2" + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await create_endpoint_steps(page, ENDPOINT_NAME_2, process.env.URI2, process.env.TOKEN2, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Select ' + ENDPOINT_NAME_2).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill('Test ' + Math.floor(Math.random() * 1000000000));
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    await page.getByRole('button', {name: 'View Report'}).click();

    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_two_endpoint_invalid', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const ENDPOINT_NAME_2: string = "Azure OpenAI 2" + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, "URI", "Token123", 'openai-connector', '2', '', '123', '{\n      "timeout": 300,\n "max_attempts": 3,\n      "temperature": 0.5\n  }', true)
    await create_endpoint_steps(page, ENDPOINT_NAME_2, "URI", "Token123", 'openai-connector', '2', '', '123', '{\n      "timeout": 300,\n    "max_attempts": 3,\n      "temperature": 0.5\n  }', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Select ' + ENDPOINT_NAME_2).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();

    // Assert Error Running Benchmarking
    await expect(page.getByRole('button', {name: 'View Errors'})).toBeVisible({timeout: 600000});
    await expect(page.getByText('% (with error)')).toBeVisible();
    await page.getByRole('button', {name: 'View Errors'}).click();
    await expect(page.getByRole('heading', {name: 'Errors'})).toBeVisible();
    await page.getByRole('button', {name: 'Close'}).click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_two_endpoint_mixed_valid&invalid', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const ENDPOINT_NAME_2: string = "Azure OpenAI 2" + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await create_endpoint_steps(page, ENDPOINT_NAME_2, "URI", "Token123", 'openai-connector', '2', '', '123', '{\n      "timeout": 300,\n    "max_attempts": 3,\n      "temperature": 0.5\n }', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Select ' + ENDPOINT_NAME_2).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();

    // Assert Error Running Benchmarking
    await expect(page.getByRole('button', {name: 'View Errors'})).toBeVisible({timeout: 600000});
    await expect(page.getByText('% (with error)')).toBeVisible();
    await page.getByRole('button', {name: 'View Errors'}).click();
    await expect(page.getByRole('heading', {name: 'Errors'})).toBeVisible();
    await page.getByRole('button', {name: 'Close'}).click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_zero_endpoint_selected', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();

    await expect(page.getByRole('heading', {name: 'Select the Endpoint(s) to be'})).toBeVisible();

});

test('test_benchmarking_edit_endpoint_step', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, "URI", process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    //Edit Endpoint
    await page.locator('li').filter({hasText: ENDPOINT_NAME + "Added"}).getByRole('button').click();
    await page.getByPlaceholder('URI of the remote model').fill(process.env.URI);
    await page.getByRole('button', {name: 'Save'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    //////////////////////////////////////////////////
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_create_new_endpoint_step', async ({browserName, page}) => {
    test.setTimeout(600_000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    const CONNECTORTYPE: string = 'openai-connector';
    const TOKEN: string = process.env.TOKEN;
    const URI: string = process.env.URI;
    // Benchmarking
    console.log('Benchmarking')
    await page.goto('http://localhost:3000/');
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    //Create Endpoint
    await page.getByRole('button', {name: 'Create New Endpoint'}).click();
    await page.getByPlaceholder('Name of the model').fill(ENDPOINT_NAME);
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: CONNECTORTYPE, exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill(URI);
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill(TOKEN);
    await page.getByPlaceholder('Model of the model endpoint').click();
    await page.getByPlaceholder('Model of the model endpoint').fill('gpt-4o');
    await page.getByText('More Configs').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}');
    await page.getByRole('button', {name: 'OK'}).click();
    await page.getByRole('button', {name: 'Save'}).click();
    console.log('Select ' + ENDPOINT_NAME)
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    //////////////////////////////////////////////////
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600_000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_create_endpoint_entry_point_2', async ({browserName, page}) => {
    test.setTimeout(600_000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    const CONNECTORTYPE: string = 'openai-connector';
    const TOKEN: string = process.env.TOKEN;
    const URI: string = process.env.URI;
    // Benchmarking
    console.log('Benchmarking')
    await page.goto('http://localhost:3000/');
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    //Create Endpoint via another entry point
    await page.locator('li').filter({hasText: 'Testing a new Endpoint?Create'}).click();
    await page.getByPlaceholder('Name of the model').fill(ENDPOINT_NAME);
    await page.locator('.aiv__input-container').click();
    await page.getByRole('option', {name: CONNECTORTYPE, exact: true}).click();
    await page.getByPlaceholder('URI of the remote model').click();
    await page.getByPlaceholder('URI of the remote model').fill(URI);
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill(TOKEN);
    await page.getByPlaceholder('Model of the model endpoint').click();
    await page.getByPlaceholder('Model of the model endpoint').fill('gpt-4o');
    await page.getByText('More Configs').click();
    await page.getByPlaceholder('Additional parameters').fill('{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}');
    await page.getByRole('button', {name: 'OK'}).click();
    await page.getByRole('button', {name: 'Save'}).click();
    //////////////////////////////////////////////////
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();

    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600_000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});
// test('test_benchmarking_modification_add_cookbook_step', async ({browserName, page}) => {
//     const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
//     const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
//     // Benchmarking
//     console.log('Benchmarking')
//     await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'azure-openai-connector', '2', '','gpt-4o', '{\n timeout": 300,\n max_attempts":300,\n temperature": 0.5\n ', true)
//     await page.getByRole('listitem').nth(1).click();
//     await page.getByRole('button', {name: 'Start New Run'}).click();
//     await page.getByRole('button', {name: 'Hard test sets for Common'}).click();
//     await page.getByRole('button', {name: 'MLCommons AI Safety'}).click();
//     await page.getByLabel('Next View').click();
//     await page.getByText('these cookbooks').click();
//     await page.getByText('Facts about SingaporeThis').click();
//     await page.getByRole('button', {name: 'OK'}).click();
//
//     await page.getByRole('main').getByRole('img').nth(2).click();
//     await page.getByText(ENDPOINT_NAME!).click();
//     await page.locator('div:nth-child(3) > .flex > svg').click();
//     await page.getByPlaceholder('Give this session a unique').click();
//     await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
//
//
//     await page.getByRole('button', {name: 'Run'}).click();
//
//
//     await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
//     //Check Details
//     await page.getByRole('button', {name: 'See Details'}).click();
//     await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
//     await expect(page.getByText('Description:')).toBeVisible();
//     await expect(page.getByText('Number of prompts to run:1')).toBeVisible();
//     await page.getByRole('main').getByRole('img').nth(1).click();
//     // await download_validation_steps (page)
//     await page.getByRole('button', {name: 'View Report'}).click();
//     await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
//     await page.getByText(/back to home/i).click()
// });

test('test_benchmarking_run_with_two_cookbook_standard', async ({browserName, page}) => {
    test.setTimeout(2100_000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await page.goto('http://localhost:3000/');
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME, {exact: true}).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select common-risk-easy').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 1800_000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:943')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});
test('test_benchmarking_run_with_two_cookbook_standard_with_mlc_type', async ({browserName, page}) => {
    test.setTimeout(4600000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    // Check if the browser is WebKit
    test.skip(browserName === 'firefox', 'This test is skipped on WebKit');
    // const TOGETHER_ENDPOINT_NAME: string = "Together Llama Guard 3 8B Assistant";
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await page.goto('http://localhost:3000/');
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME, {exact: true}).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select mlc-ai-safety').check();

    await page.getByLabel('Next View').click();

    //Edit Llama Guard Evaluator Endpoint
    // await page.locator('li').filter({hasText: TOGETHER_ENDPOINT_NAME + "Added"}).getByRole('button').click();
    await page.getByRole('button', { name: 'Configure' }).click();
    await page.getByPlaceholder('Access token for the remote').fill(process.env.TOGETHER_TOKEN);
    await page.getByRole('button', {name: 'Save'}).click();
    // //////////////////////////////////////////////////

    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 4100000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:427')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_run_with_zero_cookbook_step', async ({browserName, page}) => {
    test.setTimeout(300_000);
    const ENDPOINT_NAME: string = "Azure OpenAI GPT4o";
    await page.goto('http://localhost:3000/');
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
     //Edit Endpoint
    await page.locator('li').filter({hasText: ENDPOINT_NAME + "Added"}).getByRole('button').click();
    await page.getByPlaceholder('URI of the remote model').fill(process.env.URI);
    await page.getByPlaceholder('Access token for the remote').fill(process.env.TOKEN);
    await page.getByRole('button', {name: 'Save'}).click();
    //////////////////////////////////////////////////
    await page.getByLabel('Select ' + ENDPOINT_NAME, {exact: true}).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Select singapore-context').uncheck();
    await expect(page.getByLabel('Next View')).toBeDisabled();
});
