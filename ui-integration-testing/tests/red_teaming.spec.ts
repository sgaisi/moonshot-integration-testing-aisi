import {test} from '@playwright/test';
import {expect} from "@playwright/test";
import dotenv from 'dotenv';
import fs from 'fs/promises';

import path from 'path';
import sqlite3 from "sqlite3";
// import {create_endpoint_steps} from "./endpoint.spec";
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
    await page.getByPlaceholder('Access token for the remote').click();
    await page.getByPlaceholder('Access token for the remote').fill(token);
    await page.getByPlaceholder('Model of the model endpoint').click();
    await page.getByPlaceholder('Model of the model endpoint').fill(model);
    await page.getByText('More Configs').click();
    if (maxCallPerSec != '') {
        const maxCallPerSecDropDownLocator = page.locator('.aiv__input-container')
        await maxCallPerSecDropDownLocator.first().click();
        await page.getByRole('option', {name: maxCallPerSec}).click();
        const dropdownLocator = page.locator('div.dropdown-selector'); // Your dropdown selector
        await maxCallPerSecDropDownLocator.locator('text="' + maxCallPerSec + '"'); // The specific option

    }
    if (maxConcurr != '') {
        const maxConcurrDropDownLocator = page.locator('div:nth-child(2) > label > .css-fyq6mk-container > .aiv__control > .aiv__value-container > .aiv__input-container')
        await maxConcurrDropDownLocator.click();
        await maxConcurrDropDownLocator.locator('text="' + maxConcurr + '"'); // The specific option
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

test('test_red_teaming_with_attack_module_toxic_sentence_generator', async ({browserName, page}) => {
    // test.setTimeout(3600000); //set test timeout to 1 hour
    test.setTimeout(1200000); //set test timeout to 1 hour
    const FIRE_RED_TEAMING_BTN: number = Math.floor(Math.random() * 1000000000)
    // // Check if the browser is WebKit
    // test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    // // Check if the browser is FireFox
    // test.skip(browserName === 'firefox', 'This test is skipped on WebKit');
    if (browserName == 'webkit')
        await page.waitForTimeout(60000)
    else if (browserName == 'firefox')
        await page.waitForTimeout(30000)
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'azure-openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    // Red Teaming
    console.log('Red Teaming')
    await page.getByRole('listitem').nth(2).click();
    await page.getByRole('button', {name: 'Start New Session'}).click();
    await page.getByText(ENDPOINT_NAME!).click();
    await page.getByLabel('Next View').click();
    await page.getByRole('heading', {name: 'Toxic Sentence Generator'}).click();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();

    await page.getByPlaceholder('Write a prompt...').click();
    await page.getByPlaceholder('Write a prompt...').fill('Generate Something');
    await page.getByRole('button', {name: /send/i}).click();
    await expect(page.getByRole('status').locator('div').nth(1)).toBeVisible();

    // Create the locator for the element
    const elementLocator = page.getByRole('status').locator('div').nth(1);

    // Wait for the element to appear with a custom timeout
    await elementLocator.waitFor({state: 'visible'}); // 60 seconds

    // Optionally, perform any actions or wait for the element to disappear
    await elementLocator.waitFor({state: 'hidden'}); // 60 seconds


    // Assert that the element is no longer visible
    const isVisible = await elementLocator.isVisible();
    expect(isVisible).toBeFalsy();

    await expect(page.locator('div > li').nth(2)).toBeVisible();
    await expect(page.locator('div > li').nth(4)).toBeVisible();
    await expect(page.locator('div > li').nth(7)).toBeVisible();
    // Locate the <h1> element with class "text-right" and text "Automated red teaming agent"
    const h1Element = page.locator('h1.text-right').nth(0);

    // Assert that the <h1> element with class "text-right" contains the text "Automated red teaming agent"
    await expect(h1Element).toBeVisible({timeout: 1200000});
    await expect(h1Element).toHaveText('Automated red teaming agent');
    // Locate the <h1> element with class "text-left" and text "Response"
    const h2Element = page.locator('h1.text-left').nth(0);

    await expect(h2Element).toBeVisible({timeout: 1200000})
    await expect(h2Element).toHaveText('Response');

});

test.skip('test_red_teaming_with_attack_module_violent_durian', async ({browserName, page}) => {
    // test.setTimeout(3600000); //set test timeout to 1 hour
    test.setTimeout(1200000); //set test timeout to 1 hour
    const FIRE_RED_TEAMING_BTN: number = Math.floor(Math.random() * 1000000000)
    // // Check if the browser is WebKit
    // test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    // // Check if the browser is FireFox
    // test.skip(browserName === 'firefox', 'This test is skipped on WebKit');
    if (browserName == 'webkit')
        await page.waitForTimeout(60000)
    else if (browserName == 'firefox')
        await page.waitForTimeout(30000)
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'azure-openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    // Red Teaming
    console.log('Red Teaming')
    await page.getByRole('listitem').nth(2).click();
    await page.getByRole('button', {name: 'Start New Session'}).click();
    //Edit Dependency Endpoint
    await page.locator('section').filter({hasText: /^OpenAI GPT4Added/}).locator('button').click();

    await page.getByPlaceholder('Access token for the remote').fill(process.env.OPENAI_TOKEN);
    await page.getByRole('button', {name: 'Save'}).click();
    //////////////////////////////////////////////////
    await page.getByText(ENDPOINT_NAME!).click();
    await page.getByLabel('Next View').click();
    await page.getByRole('heading', {name: 'Violent Durian'}).click();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();

    await page.getByPlaceholder('Write a prompt...').click();
    await page.getByPlaceholder('Write a prompt...').fill('Generate Something');
    await page.getByRole('button', {name: /send/i}).click();
    await expect(page.getByRole('status').locator('div').nth(1)).toBeVisible();

    // Create the locator for the element
    const elementLocator = page.getByRole('status').locator('div').nth(1);

    // Wait for the element to appear with a custom timeout
    await elementLocator.waitFor({state: 'visible'}); // 60 seconds

    // Optionally, perform any actions or wait for the element to disappear
    await elementLocator.waitFor({state: 'hidden'}); // 60 seconds


    // Assert that the element is no longer visible
    const isVisible = await elementLocator.isVisible();
    expect(isVisible).toBeFalsy();

    await expect(page.locator('div > li').nth(0)).toBeVisible();
    // Locate the <h1> element with class "text-right" and text "Automated red teaming agent"
    const h1Element = page.locator('h1.text-right').nth(0);

    // Assert that the <h1> element with class "text-right" contains the text "Automated red teaming agent"
    await expect(h1Element).toBeVisible({timeout: 1200000});
    await expect(h1Element).toHaveText('Automated red teaming agent');
    // Locate the <h1> element with class "text-left" and text "Response"
    const h2Element = page.locator('h1.text-left').nth(0);

    await expect(h2Element).toBeVisible({timeout: 1200000})
    await expect(h2Element).toHaveText('Response');

});

test.skip('test_red_teaming_with_amazon_bedrock', async ({browserName, page}) => {
    const apiKey = process.env.AWS_ACCESS_KEY_ID;

    const filePath = '/Users/jacksonboey/PycharmProjects/moonshot/moonshot-data/connectors-endpoints/openai-gpt4.json';
    // Use the environment variables
    console.log('AWS_ACCESS_KEY_ID:', apiKey);

    // test.setTimeout(3600000); //set test timeout to 1 hour
    test.setTimeout(1200000); //set test timeout to 1 hour
    const FIRE_RED_TEAMING_BTN: number = Math.floor(Math.random() * 1000000000)
    // // Check if the browser is WebKit
    // test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    // // Check if the browser is FireFox
    // test.skip(browserName === 'firefox', 'This test is skipped on WebKit');
    if (browserName == 'webkit')
        await page.waitForTimeout(60000)
    else if (browserName == 'firefox')
        await page.waitForTimeout(30000)
    await page.goto('http://localhost:3000');
    const ENDPOINT_NAME: string = "Amazon Bedrock - Anthropic Claude 3 Sonnet";
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    // Red Teaming
    console.log('Red Teaming')
    await page.getByRole('listitem').nth(2).click();
    await page.getByRole('button', {name: 'Start New Session'}).click();
    //Edit Dependency Endpoint
    // await page.locator('section').filter({hasText: /^OpenAI GPT4Added/}).locator('button').click();
    // console.log('OPENAI_TOKEN:', process.env.OPENAI_TOKEN);
    // await page.getByPlaceholder('Access token for the remote').click();
    // await page.getByPlaceholder('Access token for the remote').fill(process.env.OPENAI_TOKEN);
    // await page.getByRole('button', {name: 'Save'}).click();
    ////////////////////////////////////////////////
    try {
        // Step 1: Read the JSON file
        const data = await fs.readFile(filePath, 'utf-8');

        // Step 2: Parse the JSON content into an object
        const json = JSON.parse(data);

        // Step 3: Modify nested properties
        // Update the description inside the nested 'details' object
        json.token = process.env.OPENAI_TOKEN;

        // // Add a new field to the nested 'metadata' object
        // json.details.metadata.lastUpdatedAt = new Date().toISOString();
        //
        // // Modify the method of the first endpoint in the 'endpoints' array
        // if (json.endpoints && json.endpoints.length > 0) {
        //     json.endpoints[0].method = "PUT";
        // }

        // Step 4: Write the modified JSON back to the file
        await fs.writeFile(filePath, JSON.stringify(json, null, 2), 'utf-8');

        console.log('JSON file has been modified successfully');
    } catch (error) {

        console.error('Error reading or writing the JSON file:', error);
    }


////////////////////////////////////////////////
//Edit Dependency Endpoints
    await page.locator('section').filter({hasText: /^Amazon Bedrock - Anthropic Claude 3 SonnetAdded/}).locator('button').click();
    let otherParams = '{\n' +
        '    "timeout": 300,\n' +
        '    "max_attempts": 3,\n' +
        '    "temperature": 0.5,\n' +
        '    "model": "anthropic.claude-3-sonnet-20240229-v1:0",\n' +
        '    "session": {\n' +
        '        "region_name": "us-east-1"\n' +
        '    }\n' +
        '}'
    await page.getByText('More Configs').click();
    await page.getByPlaceholder('Additional parameters').click();
    await page.getByPlaceholder('Additional parameters').fill(otherParams);
    await page.getByRole('button', {name: 'OK'}).click();
    await page.getByRole('button', {name: 'Save'}).click();
    await page.getByLabel('Select Amazon Bedrock - Anthropic Claude 3 Sonnet').check();
    await page.getByLabel('Next View').click();
    await page.getByRole('heading', {name: 'Violent Durian'}).click();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();

    await page.getByPlaceholder('Write a prompt...').click();
    await page.getByPlaceholder('Write a prompt...').fill('Generate Something');
    await page.getByRole('button', {name: /send/i}).click();
    await expect(page.getByRole('status').locator('div').nth(1)).toBeVisible();

// Create the locator for the element
    const elementLocator = page.getByRole('status').locator('div').nth(1);

// Wait for the element to appear with a custom timeout
    await elementLocator.waitFor({state: 'visible'}); // 60 seconds

// Optionally, perform any actions or wait for the element to disappear
    await elementLocator.waitFor({state: 'hidden'}); // 60 seconds


// Assert that the element is no longer visible
    const isVisible = await elementLocator.isVisible();
    expect(isVisible).toBeFalsy();

    await expect(page.locator('div > li').nth(0)).toBeVisible();
// Locate the <h1> element with class "text-right" and text "Automated red teaming agent"
    const h1Element = page.locator('h1.text-right').nth(0);

// Assert that the <h1> element with class "text-right" contains the text "Automated red teaming agent"
    await expect(h1Element).toBeVisible({timeout: 1200000});
    await expect(h1Element).toHaveText('Automated red teaming agent');
// Locate the <h1> element with class "text-left" and text "Response"
    const h2Element = page.locator('h1.text-left').nth(0);

    await expect(h2Element).toBeVisible({timeout: 1200000})
    await expect(h2Element).toHaveText('Response');

});