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

        # 「処理を選択してください」のラジオボタンから「類似語を調べる」を選ぶ
        await page.get_by_role("radio", name="類似語を調べる").click()
        
        # 「実行」ボタンが現れるまで最大60秒待つ
        run_button = page.get_by_role('button', name='実行')
        await run_button.wait_for(state="visible", timeout=60000)

        # ③ ボタンが見つかったらクリック！
        await run_button.click()

        # ④ アプリが動くのを少し待つ（5秒くらい）
        await page.wait_for_timeout(5000)

        # ⑤ ブラウザを閉じる
        await browser.close()

asyncio.run(run())
