import vkbottle
from config import TOKEN_VK
import asyncio

owner_id = -216438878
api = vkbottle.API('vk1.a.B9wrGPmkHqK-MPAb889GHwHSZhgBtYXtSJoR4boGpKcECUM2RPFFDp767U1ZkNFi4Ed0wBrsR_Bqygo26Ihu534lQiajLyKQcR-iyjefAIis54drp7Ro5q6WvKFSdDYb_9EHKDanmFWlPeb9TDVlVc-7--4AP870ffd3d2PCBRZpOPDokNRbWv3go8kjUzA4nV0Qbm0ZBbtSRXtmL0f_tA')


async def get_wall():
    wall = await api.wall.get(owner_id=owner_id)
    for i in wall:
        print(i)

asyncio.run(get_wall())