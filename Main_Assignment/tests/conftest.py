import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup_browser(request):
    global driver

    driver = webdriver.Chrome(executable_path="/Users/vidmisra/PycharmProjects/Selenium/Main_Assignment/chromedriver")

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    pass

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)