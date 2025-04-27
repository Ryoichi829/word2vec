# ファイル名: keep_alive.py

import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # ヘッドレスモードでブラウザ起動
        page = await browser.new_page()

        # アプリのURLを開く
        await page.goto('https://word2vec-yyfpltniu5iob544pq9rcx.streamlit.app/')

        # ページが完全にロードされるまで最大60秒待つ
        await page.wait_for_load_state('networkidle')

        # 「類似語を調べる」のテキストを持つ要素を探してクリック
        # await page.get_by_text("類似語を調べる", exact=True).click()

        # それからラジオボタンクリック
        # await radio_button.click()
        
        # 「実行」ボタンが現れるまで最大60秒待つ
        run_button = page.get_by_role('button', name='実行')
        await run_button.wait_for(state="visible", timeout=60000)

        # ボタンが見つかったらクリック！
        await run_button.click()

        # アプリが動くのを少し待つ（10秒くらい）
        await page.wait_for_timeout(1000 * 10)

        # ブラウザを閉じる
        await browser.close()

asyncio.run(run())
