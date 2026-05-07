import pytest
from playwright.sync_api import sync_playwright

def test_heroku_login():
    """UI自动化：测试 Heroku 标准登录页面"""
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 打开标准测试登录页面
        page.goto("https://the-internet.herokuapp.com/login")

        # =============================================
        # 自动化步骤：输入用户名 + 密码 + 点击登录
        # =============================================
        page.fill("#username", "tomsmith")          # 输入用户名
        page.fill("#password", "SuperSecretPassword!")  # 输入密码
        page.click('button[type="submit"]')         # 点击登录按钮

        # 等待登录后跳转
        page.wait_for_timeout(2000)

        # 断言登录成功（出现成功提示）
        assert "You logged into a secure area!" in page.text_content("#flash")

        # 退出登录
        page.click("a[href='/logout']")

        # 断言退出成功
        assert "You logged out" in page.text_content("#flash")

        # 关闭资源
        context.close()
        browser.close()