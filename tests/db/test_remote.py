import pytest

from chairdb import HTTPDatabase, Document
from chairdb.utils import async_iter

DOCS = [
    Document('mytest', 1, ('x',), {'Hello': 'World!'}),
    Document('mytest', 2, ('y', 'x'), body=None)
]


@pytest.mark.asyncio
async def test_remote():  # noqa: C901
    url = 'http://localhost:5984/test'
    async with HTTPDatabase(url, credentials=('marten', 'test')) as db:
        try:
            assert await db.create()
            assert not await db.create()

            assert await db.update_seq
            # query some unexisting rev
            query = [('unexisting', [(1, 'x'), (2, 'y')]), ('abc', [(1, 'a')])]
            async for change in db.revs_diff(async_iter(query)):
                print(change)
            async for result in db.write(async_iter(DOCS)):
                print(result)  # succesful writes don't return anything
            req = [
                # three different ways...
                ('mytest', {'revs': 'all'}),
                ('mytest', {}),
                ('mytest', {'revs': [(2, 'y')]}),
            ]
            async for result in db.read(async_iter(req)):
                print(result)
            async for change in db.changes():
                print(change)
                break

            assert 'remote' in await db.id
        finally:
            # clean up
            print(await db.destroy())
