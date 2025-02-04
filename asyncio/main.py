import asyncio

async def fecth_data():
    print("データを取得します...")
    await asyncio.sleep(4)
    print("データが取得されました!!!「data:xyz」")

async def perform_calculation():
    print("計算を開始します...")
    await asyncio.sleep(2)
    print("計算が完了しました!!! 答え「12345」")
    
async def main():
    print("データ取得と計算を開始する前")
    await asyncio.gather(fecth_data(), perform_calculation())
    print("すべてのタスクが完了しました")
    
asyncio.run(main())