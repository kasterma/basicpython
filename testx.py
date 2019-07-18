# seeing how testing in async context could work

from asynctest import mock, CoroutineMock
import asyncio

with mock.patch("x.X", autospec=True) as patchx:
    from x import X
    xx = X()
    print(xx)
    print(xx.f)
    print(xx.g)

    async def cg():
        await xx.g(4)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(cg())

    CoroutineMock()

    xx.g.assert_awaited()

