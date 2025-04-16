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


test('test_benchmarking_one_endpoint_run_with_percentage_check', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    // Locate the element
    const locator = page.locator('p.text-white.text-\\[1\\.1rem\\].w-\\[90\\%\\]');

    // Poll for the text content to change from "0%" to "100%"
    let currentText = await locator.textContent();

    // Loop until the text becomes "100%"
    while (currentText !== '100%') {
        console.log(`Current percentage: ${currentText}`); // Log progress (optional)

        // Wait for a short time before checking again (e.g., 500ms)
        await page.waitForTimeout(500);

        // Get the updated text content
        currentText = await locator.textContent();
    }

    // Once it reaches "100%", execute some action
    console.log('Reached 100%, executing action...');
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

test('test_benchmarking_one_endpoint_slider_percentage', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    //Start Benchmarking
     // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    // await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    // Locate the slider handle
    const sliderHandle = page.locator('.Slider_handle__AaqrC'); // Update with the actual selector of your slider handle

    // Locate the slider track or an end position element if needed
    const sliderTrack = page.locator('.Slider_slider__3olqj'); // Update with the slider's track selector

    // Get the bounding box of the slider track
    const sliderBox = await sliderTrack.boundingBox();
    if (!sliderBox) {
        throw new Error('Could not retrieve slider bounding box.');
    }

    // Drag the slider handle by simulating mouse events
    const targetX = sliderBox.x + sliderBox.width * 0.5; // Move to the middle of the slider
    const targetY = sliderBox.y + sliderBox.height / 2; // Center vertically

    await sliderHandle.dragTo(sliderHandle, {
        force: true,
        targetPosition: {
            x: 15,
            y: targetY,
        },
    });

    await page.getByRole('button', {name: 'Run'}).click();
    //////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:4')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});
test('test_benchmarking_one_endpoint', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
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
test('test_benchmarking_one_endpoint_cookbook_common-risk-easy', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Common Risk Easy " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select common-risk-easy').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:942')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_singapore-context', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Facts About Singapore " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
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
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
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

test('test_benchmarking_one_endpoint_cookbook_medical-llm-leaderboard', async ({browserName, page}) => {
    test.setTimeout(3000000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Medical " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select medical-llm-leaderboard').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 2100000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1947')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_leaderboard-cookbook', async ({browserName, page}) => {
    test.setTimeout(2100000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Leaderboard " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select leaderboard-cookbook').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 1800000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1256')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_tamil-language-cookbook', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Tamil " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select tamil-language-cookbook').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:49')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_legal-summarisation', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Legal Summarization " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select legal-summarisation').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:664')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_mlc-ai-safety', async ({browserName, page}) => {
    test.setTimeout(4000000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test MLC " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select mlc-ai-safety').check();
    await page.getByLabel('Next View').click();
    //Edit Endpoint
    // const TOGETHER_ENDPOINT_NAME: string = "Together Llama Guard 7B Assistant";
    // await page.locator('li').filter({hasText: TOGETHER_ENDPOINT_NAME + "Added"}).getByRole('button').click();
    await page.getByRole('button', { name: 'Configure' }).click();
    await page.getByPlaceholder('Access token for the remote').fill(process.env.TOGETHER_TOKEN);
    await page.getByRole('button', {name: 'Save'}).click();
    //////////////////////////////////////////////////
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 3500000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:426')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_common-risk-hard', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Hard CookBook " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select common-risk-hard').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    //Check Detailss
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:942')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});

test('test_benchmarking_one_endpoint_cookbook_chinese-safety-cookbook', async ({browserName, page}) => {
    test.setTimeout(1800000);
    // Check if the browser is WebKit
    test.skip(browserName === 'webkit', 'This test is skipped on WebKit');
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test Clcc " + Math.floor(Math.random() * 1000000000);
    ////////////////////////////////////////////////////////////////////////////
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, process.env.URI, process.env.TOKEN, 'openai-connector', '2', '', 'gpt-4o', '{\n "timeout": 300,\n "max_attempts": 3,\n "temperature": 0.5\n}', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByRole('button', {name: 'Trust & Safety'}).click();
    await page.getByLabel('Select chinese-safety-cookbook').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    await page.getByRole('button', {name: 'Run'}).click();
    ////////////////////////////////////////////////////////////////////////////
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 1200000})
    //Check Details
    await page.getByRole('button', {name: 'See Details'}).click();
    await expect(page.getByText("Name:" + RUNNER_NAME)).toBeVisible();
    await expect(page.getByText('Description:')).toBeVisible();
    await expect(page.getByText('Number of prompts to run:1127')).toBeVisible();
    await page.getByRole('main').getByRole('img').nth(1).click();
    // await download_validation_steps (page)
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});


test('test_benchmarking_with_invalid_endpoint', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    // Benchmarking
    console.log('Benchmarking')
    await create_endpoint_steps(page, ENDPOINT_NAME, "uri", "token123", 'openai-connector', '2', '', 'gpt-4o', '{\n      "timeout": 300,\n   "max_attempts": 1,\n      "temperature": 0.5\n  }', true)
    await page.getByRole('listitem').nth(1).click();
    await page.getByRole('button', {name: 'Start New Run'}).click();
    await page.getByLabel('Select ' + ENDPOINT_NAME).check();
    await page.getByLabel('Next View').click();
    await page.getByLabel('Select singapore-context').check();
    await page.getByLabel('Next View').click();
    await page.getByPlaceholder('Give this session a unique').click();
    await page.getByPlaceholder('Give this session a unique').fill('Test ' + Math.floor(Math.random() * 1000000000));
    await page.getByRole('button', {name: 'Run'}).click();
    // Assert Error Running Benchmarking
    await expect(page.getByRole('button', {name: 'View Errors'})).toBeVisible({timeout: 600000});
    await expect(page.getByText('% (with error)')).toBeVisible();
    await page.getByRole('button', {name: 'View Errors'}).click();
    await expect(page.getByRole('heading', {name: 'Errors'})).toBeVisible();
    await page.getByRole('button', {name: 'Close'}).click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_runner_name_exist', async ({browserName, page}) => {
    test.setTimeout(1200000);
    // Check if the browser is WebKit
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const ENDPOINT_NAME2: string = "Azure OpenAI2 " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    // Run again
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME2, RUNNER_NAME)
    await expect(page.getByText('Unable to create and execute')).toBeVisible();
    await expect(page.getByText('Errors')).toBeVisible();
    await page.getByRole('button', {name: 'Close'}).click();
});

test('test_benchmarking_runner_name_input_integer', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "" + Math.floor(Math.random() * 1000000000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_runner_name_input_decimal', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = Math.floor(Math.random() * 100000) + "." + Math.floor(Math.random() * 100000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});

test('test_benchmarking_runner_name_input_special_char', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "@" + Math.floor(Math.random() * 100000);
    await create_single_endpoint_benchmark_steps(page, ENDPOINT_NAME, RUNNER_NAME)
    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()
});
test('test_benchmarking_runner_name_input_empty', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = ""
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
    // await page.getByPlaceholder('Give this session a unique').fill(RUNNER_NAME);
    // await expect(page.getByText('Name is required')).toBeVisible();
    // Select the Run button
    const runBtn = page.getByRole('button', {name: 'Run'});
    // Check if the Save button is disabled
    await expect(runBtn).toBeDisabled();

});

test('test_benchmarking_runner_description_input_!empty', async ({browserName, page}) => {
    test.setTimeout(1200000);
    const ENDPOINT_NAME: string = "Azure OpenAI " + Math.floor(Math.random() * 1000000000);
    const RUNNER_NAME: string = "Test " + Math.floor(Math.random() * 1000000000);
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
    await page.getByPlaceholder('Description of this benchmark').fill('test');
    await page.getByRole('button', {name: 'Run'}).click();

    await expect(page.getByRole('button', {name: 'View Report'})).toBeVisible({timeout: 600000})
    await page.getByRole('button', {name: 'View Report'}).click();
    await page.locator('main').filter({hasText: 'Showing results forazure-'}).getByRole('link').first().click();
    await page.getByText(/back to home/i).click()

});