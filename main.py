from waifulabs import Waifulab
import asyncio
client = Waifulab()
async def main():
    test = await client.second_image()
    #1枚目取得(10枚まである)
    key="1"
    #Base64の画像データが出力される
    print("".join(test[f"{key}"].keys()))
    
    
asyncio.run(main())