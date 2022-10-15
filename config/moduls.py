from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    created_at = Column(String, default=datetime.now())
    updated_at = Column(String, default=datetime.now(), onupdate=datetime.now())
    posts = relationship("Post", back_populates="creator")
    roles = relationship("UserRoles", back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    image = Column(String)
    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="posts")
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(String, default=datetime.now())
    updated_at = Column(String, default=datetime.now(), onupdate=datetime.now())
    permissions = relationship("RolePermissions", back_populates="role")
    users = relationship("UserRoles", back_populates="role")

class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(String, default=datetime.now())
    updated_at = Column(String, default=datetime.now(), onupdate=datetime.now())
    roles = relationship("RolePermissions", back_populates="permission")
    

class UserRoles(Base):
    __tablename__ = "user_roles"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")

class RolePermissions(Base):
    __tablename__ = "role_permissions"
    role_id = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permissions.id"), primary_key=True)
    role = relationship("Role", back_populates="permissions")
    permission = relationship("Permission", back_populates="roles")
    
