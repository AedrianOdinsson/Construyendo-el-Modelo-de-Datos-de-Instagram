from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()
followers = Table(
    "followers"
    db.metadata,
)
    
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(40), nullable=False)
    firstname: Mapped[str] = mapped_column(String(40)nullable=False)
    lastanem: Mapped[str] = mapped_column(String(40), nullable=False)

    posts: Mapped[List["Post"]]= relationship ("User") 

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "lastname": self.lastname,
            "firstname": self.firstname,
        }

class Post(db.Model):
    __tablename__="post"

    id: Mapped [int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]= mapped_column(ForeingKey=("user.id"), nullable=False)
    description: Mapped [str]= mapped_column(String(255),back_populates="post")


class Media(db.Model):
     __tablename__="media"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str]= mapped_column(String(260), nullable=False)
    type: Mapped[str]= mapped_column(String(50), nullable=False)
    post_id:Mapped[int] = mapped_column(ForeingKey=("post.id"), nullable=False)
    
    post: Mapped["Post"] = relationship("Post", backpopulates="media")