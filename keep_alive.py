import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto('https://word2vec-yyfpltniu5iob544pq9rcx.streamlit.app/')
        await page.wait_for_load_state('networkidle')

        # ラジオボタンの選択
        radio_button = page.get_by_text("類似語を調べる", exact=True)
        await radio_button.wait_for(state="visible", timeout=60000)
        await radio_button.click()

        # モデルロード中の表示が消えるのを待つ
        try:
            await page.locator("text=日本語学習済みモデル(800MB)をロード中...しばらくお待ちください。").wait_for(state="detached", timeout=600000)
        except Exception:
            print("ロード待機スキップ（ロード中メッセージが出なかった）")

        # 実行ボタンを押す
        run_button = page.get_by_role('button', name='実行')
        await run_button.wait_for(state="visible", timeout=60000)
        await run_button.click()

        await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(run())
