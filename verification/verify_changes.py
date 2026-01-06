from playwright.sync_api import sync_playwright, expect

def verify_performance_changes(page):
    # Go to the local server
    page.goto("http://localhost:8000")

    # 1. Verify Font Awesome is loaded
    # We check if the moon icon is visible, which depends on Font Awesome
    # The icon is <i class="fas fa-moon"></i>
    theme_toggle_icon = page.locator("#theme-toggle i")
    expect(theme_toggle_icon).to_be_visible()

    # 2. Verify Dark Mode Toggle works (Scripts loaded correctly)
    # This verifies that js/script.js is loaded and running
    theme_toggle = page.locator("#theme-toggle")
    theme_toggle.click()

    # Check if body has dark-mode class
    body = page.locator("body")
    expect(body).to_have_class(re.compile(r"dark-mode"))

    # 3. Verify Mobile Menu works (Inline script moved correctly)
    # We need to set viewport to mobile
    page.set_viewport_size({"width": 375, "height": 667})

    mobile_menu = page.locator("#mobile-menu")
    expect(mobile_menu).to_be_visible()
    mobile_menu.click()

    # Check if nav is active
    nav = page.locator(".nav")
    expect(nav).to_have_class(re.compile(r"active"))

    # Take screenshot of open menu
    page.screenshot(path="verification/mobile_menu.png")

    print("Verification passed!")

import re

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        verify_performance_changes(page)
        browser.close()
