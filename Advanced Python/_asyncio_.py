import asyncio

async def task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)  # Simulate a task taking some time
    print(f"Task {name} finished")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())