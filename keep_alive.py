# ファイル名: keep_alive.py

import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # ヘッドレスモードでブラウザ起動
        page = await browser.new_page()

        # ① アプリのURLを開く
        await page.goto('https://word2vec-yyfpltniu5iob544pq9rcx.streamlit.app/')

        # ② 「実行」という名前のボタンを探す
        run_button = page.get_by_role('button', name='実行')

        # ③ ボタンが見つかったらクリック！
        await run_button.click()

        # ④ アプリが動くのを少し待つ（5秒くらい）
        await page.wait_for_timeout(5000)

        # ⑤ ブラウザを閉じる
        await browser.close()

asyncio.run(run())
