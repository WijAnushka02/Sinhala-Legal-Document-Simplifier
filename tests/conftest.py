"""
Pytest fixtures for the Sinhala Legal Document Simplifier test suite.
"""
import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from main import app
from database import Base, get_db

# In-memory test database
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def test_db():
    """Create a fresh in-memory database for each test."""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    TestSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with TestSessionLocal() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def client(test_db: AsyncSession):
    """AsyncClient with DB dependency overridden to use test DB."""
    async def override_get_db():
        yield test_db

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest.fixture
def sample_sinhala_legal_text() -> str:
    return "නියමිත කාල සීමාව තුළ අයදුම්පත ඉදිරිපත් කිරීමට අපොහොසත් වන අයදුම්කරුවෙකුට අදාළ සේවාව ලබා ගැනීම සඳහා නැවත අයදුම් කිරීමට සිදුවේ."


@pytest.fixture
def sample_simplified_text() -> str:
    return "අයදුම්පත නියමිත කාලය තුළ ලබා නොදුන්නොත්, නැවත අයදුම් කිරීමට සිදුවේ."
