from app.backend.db import Base
from app.models.user import User
from fastapi import APIRouter
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey

router = APIRouter(prefix="/task", tags=["task"])


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates='tasks')


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))


@router.get("/")
async def all_tasks():
    pass


@router.get("/task_id")
async def task_by_id():
    pass


@router.post("/create")
async def create_task():
    pass


@router.put("/update")
async def update_task():
    pass


@router.delete("/delete")
async def delete_task():
    pass