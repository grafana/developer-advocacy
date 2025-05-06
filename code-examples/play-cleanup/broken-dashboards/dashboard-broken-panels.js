import { check, sleep } from 'k6';
import { browser } from 'k6/browser';
import { Gauge } from 'k6/metrics';
import exec from 'k6/execution';
import http from 'k6/http';

export const options = {
  scenarios: {
    browser: {
      executor: 'shared-iterations',
      exec: 'checkForBrokenPanels',
      options: {
        browser: {
          type: 'chromium',
        },
      },
      vus: 10,
      iterations: 500,
    },
  },
};

export async function setup() {
  const dashboards = await http.get('https://play.grafana.org/api/search?type=dash-db&limit=5000');
  const urls = dashboards.json().filter(d => {
    // Exclude dashboards in folders that are used to replicate github issues
    // These tend to naturally break after the issue is fixed, but teams have requirements
    // to keep them around to prevent them from littering github issues with broken links.
    return (!(d.folderTitle === 'Bug reports reproduction') &&
      !(d.folderTitle === 'Replicating issues'))
  }).map(dashboard => ({
    url: `https://play.grafana.org/d/${dashboard.uid}`,
    title: dashboard.title,
    folderTitle: dashboard.folderTitle,
    uid: dashboard.uid,
  }))

  console.log("A total of", urls.length, "dashboards will be checked")
  return { dashboards: urls };
}

const brokenPanelsGauge = new Gauge('broken_panels');

export async function checkForBrokenPanels({ dashboards }) {
  const page = await browser.newPage();

  // See https://grafana.com/docs/k6/latest/javascript-api/k6-execution/#scenario
  if (exec.scenario.iterationInTest >= dashboards.length) {
    console.log("No more dashboards to check")
    return
  }

  const dashboard = dashboards[exec.scenario.iterationInTest];
  const url = dashboard.url;

  try {
    await page.goto(url);

    // Wait for time picker to confirm page load
    await page.waitForSelector('[aria-controls="TimePickerContent"]');

    sleep(2)
    const brokenPanels = await page.evaluate(() => {
      const brokenPanels = document.querySelectorAll('button[data-testid="data-testid Panel status error"]');
      return brokenPanels.length;
    });

    console.log(`ResultMeasurement,${dashboard.title},${dashboard.folderTitle},${dashboard.uid},${url},${brokenPanels}`)
    brokenPanelsGauge.add(brokenPanels, { url: url });

    check(brokenPanels, {
      'Dashboard contains no broken panels': count => count === 0
    });
  } catch (error) {
    console.error("Error:", error.message);
    console.error(error.stack);
  } finally {
    await page.close();
  }
}