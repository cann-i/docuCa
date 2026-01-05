
from playwright.sync_api import sync_playwright

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the file directly
        import os
        cwd = os.getcwd()
        page.goto(f'file://{cwd}/index.html')

        # Check if the preload link is present
        preload_link = page.query_selector('link[rel="preload"][as="image"]')
        if preload_link:
            print('SUCCESS: Preload link found.')
            href = preload_link.get_attribute('href')
            print(f'Preload href: {href}')
        else:
            print('FAILURE: Preload link NOT found.')

        # Check for js-enabled class on html
        html_class = page.eval_on_selector('html', 'el => el.className')
        print(f'HTML classes: {html_class}')
        if 'js-enabled' in html_class:
             print('SUCCESS: js-enabled class present on html.')
        else:
             print('FAILURE: js-enabled class missing from html.')

        # Check for theme script execution (no errors)
        # We can check if dark mode works by setting localStorage

        page.reload()
        # Set dark mode
        page.evaluate("localStorage.setItem('theme', 'dark')")
        page.reload()

        # Check if dark-mode class is applied to body
        body_class = page.eval_on_selector('body', 'el => el.className')
        print(f'Body classes with dark theme: {body_class}')
        if 'dark-mode' in body_class:
             print('SUCCESS: dark-mode applied correctly.')
        else:
             print('FAILURE: dark-mode NOT applied.')

        # Take screenshot
        page.screenshot(path='verification/verification.png')
        browser.close()

if __name__ == '__main__':
    verify_site()
